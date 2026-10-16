#!/usr/bin/env python3
"""Fetch the latest *.nanorc files listed in scripts/sources.toml into files/.

Each copied file is prefixed with a link to the exact upstream revision and
its license. Files in files/ that are no longer listed in the manifest are
removed.

Usage: scripts/update.py [-j JOBS]
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import tomllib
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from fnmatch import fnmatch
from pathlib import Path, PurePosixPath

from _common import (
    REPOS_MD,
    ROOT,
    Repo,
    RepoInfo,
    blob_url,
    fetch_file,
    list_files,
    repo_info,
    repos_from_markdown,
)

MANIFEST = ROOT / "scripts" / "sources.toml"
OUT_DIR = ROOT / "files"
EXTRAS = "_extras"

_FILE_LICENSE = re.compile(r"^[ \t]*#+[ \t]*License[ \t]*:[ \t]*(\S.*?)[ \t]*$", re.I | re.M)


def report(level: str, msg: str) -> None:
    """Print a warning/error, as an annotation when running on GitHub Actions."""
    if os.environ.get("GITHUB_ACTIONS") == "true":
        print(f"::{level}::{msg}")
    else:
        print(f"{level}: {msg}", file=sys.stderr if level == "error" else sys.stdout)


@dataclass
class Source:
    repo: Repo
    targets: dict[str, str]  # upstream path -> destination relative to OUT_DIR
    ignore: list[str]
    license: str | None
    skip: str | None


@dataclass
class Result:
    source: Source
    written: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    error: str | None = None


def load_manifest() -> list[Source]:
    data = tomllib.loads(MANIFEST.read_text())
    sources = []
    for entry in data["source"]:
        targets = {}
        for path in entry.get("files", []):
            targets[path] = PurePosixPath(path).name
        for path in entry.get("extras", []):
            targets[path] = f"{EXTRAS}/{PurePosixPath(path).name}"
        targets.update(entry.get("rename", {}))
        sources.append(
            Source(
                Repo(entry["repo"]),
                targets,
                entry.get("ignore", []),
                entry.get("license"),
                entry.get("skip"),
            )
        )
    return sources


def validate(sources: list[Source]) -> None:
    seen: dict[str, str] = {}
    for src in sources:
        for path, dest in src.targets.items():
            if not dest.endswith(".nanorc"):
                sys.exit(f"error: destination must end with .nanorc: {dest}")
            if dest.lower() in seen:
                sys.exit(
                    f"error: {dest} is provided by both {seen[dest.lower()]} and {src.repo.key}:{path}"
                )
            seen[dest.lower()] = f"{src.repo.key}:{path}"
    listed = {s.repo for s in sources}
    for repo in repos_from_markdown():
        if repo not in listed:
            report("warning", f"{repo.key} is in {REPOS_MD.name} but not in {MANIFEST.name}")


def to_spdx(text: str) -> str | None:
    """Best-effort mapping of a free-form license statement to an SPDX id."""
    t = text.lower()
    if m := re.search(r"\bgpl(?:v|\b.*?)(?<![\d.])([23])(?:\.0)?\b(.*)", t):
        suffix = "-or-later" if re.search(r"newer|later|\+", m.group(2)) else ""
        return f"GPL-{m.group(1)}.0{suffix}"
    for pattern, spdx in [
        (r"\bmit\b", "MIT"),
        (r"\bcc0\b", "CC0-1.0"),
        (r"\bunlicense\b", "Unlicense"),
    ]:
        if re.search(pattern, t):
            return spdx
    return None


def license_line(info: RepoInfo, src: Source, content: str) -> str:
    repo_license = src.license or info.license
    head = "\n".join(content.splitlines()[:40])
    if m := _FILE_LICENSE.search(head):
        stated = m.group(1).rstrip(".")
        spdx = to_spdx(stated)
        if spdx and repo_license and spdx.startswith(repo_license.removesuffix("-or-later")):
            # the statement agrees with the repository license; keep the more specific one
            return max(spdx, repo_license, key=len)
        if spdx:
            stated = spdx
        if repo_license and stated.lower() != repo_license.lower():
            return f"{stated} (stated in file; repository: {repo_license})"
        return f"{stated} (stated in file)"
    return repo_license or "NOASSERTION (no license found upstream)"


def render(info: RepoInfo, src: Source, path: str, raw: bytes) -> bytes:
    content = raw.decode("utf-8", errors="surrogateescape")
    newline = "\r\n" if "\r\n" in content else "\n"
    header = [
        f"# Source: {blob_url(info, path)}",
        f"# License: {license_line(info, src, content)}",
        "",
    ]
    if not content.endswith(("\n", "\r")):
        content += newline
    return (newline.join(header) + newline + content).encode(
        "utf-8", errors="surrogateescape"
    )


def process(src: Source) -> tuple[Result, dict[str, bytes]]:
    res = Result(src)
    outputs: dict[str, bytes] = {}
    try:
        info = repo_info(src.repo)
        upstream = set(list_files(info))
        if info.archived:
            res.warnings.append("repository is archived")
        for path in sorted(upstream):
            if not path.endswith(".nanorc") or path in src.targets:
                continue
            if not any(fnmatch(path, pat) for pat in src.ignore):
                res.warnings.append(f"new upstream file not in manifest: {path}")
        for path, dest in src.targets.items():
            if path not in upstream:
                res.warnings.append(f"missing upstream: {path} (keeping old {dest})")
                continue
            outputs[dest] = render(info, src, path, fetch_file(info, path))
            res.written.append(dest)
    except Exception as e:  # noqa: BLE001
        res.error = f"{type(e).__name__}: {e}"
    return res, outputs


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("-j", "--jobs", type=int, default=8)
    args = parser.parse_args()

    sources = load_manifest()
    validate(sources)

    active = [s for s in sources if not s.skip]
    with ThreadPoolExecutor(args.jobs) as pool:
        results = list(pool.map(process, active))

    expected = {dest for s in active for dest in s.targets.values()}
    failed = False
    changed = 0
    for res, outputs in results:
        for dest, data in outputs.items():
            out = OUT_DIR / dest
            if out.exists() and out.read_bytes() == data:
                continue
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(data)
            changed += 1
        for w in res.warnings:
            report("warning", f"{res.source.repo.key}: {w}")
        if res.error:
            failed = True
            report("error", f"{res.source.repo.key}: {res.error}")

    removed = 0
    for path in sorted(OUT_DIR.rglob("*.nanorc")):
        if path.relative_to(OUT_DIR).as_posix() not in expected:
            path.unlink()
            removed += 1

    total = sum(len(r.written) for r, _ in results)
    print(f"{total} files fetched, {changed} updated, {removed} removed")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
