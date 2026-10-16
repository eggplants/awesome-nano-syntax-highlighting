"""Shared helpers for fetching *.nanorc files from upstream repositories."""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from functools import cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPOS_MD = ROOT / "README.md"

SAVANNAH_NANO = "savannah:nano"
SAVANNAH_GIT_URL = "https://git.savannah.gnu.org/git/nano.git"
SAVANNAH_CGIT_URL = "https://git.savannah.gnu.org/cgit/nano.git"
CACHE_DIR = ROOT / ".cache"


@cache
def github_token() -> str | None:
    if token := os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN"):
        return token
    if shutil.which("gh"):
        res = subprocess.run(
            ["gh", "auth", "token"], capture_output=True, text=True, check=False
        )
        if res.returncode == 0 and res.stdout.strip():
            return res.stdout.strip()
    return None


def http_get(url: str, *, accept: str | None = None, retries: int = 3) -> bytes:
    headers = {"User-Agent": "nanorc-collector"}
    if accept:
        headers["Accept"] = accept
    if url.startswith("https://api.github.com/") and (token := github_token()):
        headers["Authorization"] = f"Bearer {token}"
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(
                urllib.request.Request(url, headers=headers), timeout=60
            ) as res:
                return res.read()
        except urllib.error.HTTPError as e:
            if e.code in {404, 451}:
                raise
            if attempt == retries - 1:
                raise
        except urllib.error.URLError:
            if attempt == retries - 1:
                raise
        time.sleep(2**attempt)
    raise AssertionError("unreachable")


def http_json(url: str) -> object:
    return json.loads(http_get(url, accept="application/json"))


@dataclass(frozen=True)
class Repo:
    """A repository identified by `host:owner/name` (e.g. `github:scopatz/nanorc`)."""

    key: str

    @property
    def host(self) -> str:
        return self.key.split(":", 1)[0]

    @property
    def slug(self) -> str:
        return self.key.split(":", 1)[1]

    @property
    def web_url(self) -> str:
        if self.key == SAVANNAH_NANO:
            return SAVANNAH_CGIT_URL
        return f"https://{self.host}.{'com' if self.host == 'github' else 'org'}/{self.slug}"


@dataclass(frozen=True)
class RepoInfo:
    repo: Repo
    sha: str
    license: str | None
    archived: bool


def _quote_path(path: str) -> str:
    return urllib.parse.quote(path, safe="/")


@cache
def savannah_checkout() -> Path:
    dest = CACHE_DIR / "nano.git"
    if dest.exists():
        subprocess.run(
            ["git", "-C", str(dest), "fetch", "-q", "--depth=1", "origin", "HEAD"],
            check=True,
        )
        subprocess.run(
            ["git", "-C", str(dest), "reset", "-q", "--hard", "FETCH_HEAD"], check=True
        )
    else:
        dest.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            ["git", "clone", "-q", "--depth=1", SAVANNAH_GIT_URL, str(dest)], check=True
        )
    return dest


def repo_info(repo: Repo) -> RepoInfo:
    if repo.key == SAVANNAH_NANO:
        dest = savannah_checkout()
        sha = subprocess.run(
            ["git", "-C", str(dest), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()
        return RepoInfo(repo, sha, "GPL-3.0-or-later", archived=False)
    if repo.host == "github":
        meta = http_json(f"https://api.github.com/repos/{repo.slug}")
        assert isinstance(meta, dict)
        branch = meta["default_branch"]
        commit = http_json(
            f"https://api.github.com/repos/{repo.slug}/commits/{urllib.parse.quote(branch)}"
        )
        assert isinstance(commit, dict)
        lic = (meta.get("license") or {}).get("spdx_id")
        return RepoInfo(
            repo,
            commit["sha"],
            None if lic in {None, "NOASSERTION"} else lic,
            bool(meta.get("archived")),
        )
    if repo.host == "codeberg":
        api = f"https://codeberg.org/api/v1/repos/{repo.slug}"
        meta = http_json(api)
        assert isinstance(meta, dict)
        branch = http_json(f"{api}/branches/{urllib.parse.quote(meta['default_branch'])}")
        assert isinstance(branch, dict)
        lics = meta.get("licenses") or []
        return RepoInfo(
            repo,
            branch["commit"]["id"],
            " AND ".join(lics) or None,
            bool(meta.get("archived")),
        )
    raise ValueError(f"unsupported host: {repo.key}")


def list_files(info: RepoInfo) -> list[str]:
    repo = info.repo
    if repo.key == SAVANNAH_NANO:
        out = subprocess.run(
            ["git", "-C", str(savannah_checkout()), "ls-files", "-s"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout
        return [
            line.split("\t", 1)[1]
            for line in out.splitlines()
            if not line.startswith("120000 ")
        ]
    if repo.host == "github":
        tree = http_json(
            f"https://api.github.com/repos/{repo.slug}/git/trees/{info.sha}?recursive=1"
        )
        assert isinstance(tree, dict)
        # mode 120000 = symlink (an alias of another file); skip it
        return [
            e["path"]
            for e in tree["tree"]
            if e["type"] == "blob" and e["mode"] != "120000"
        ]
    if repo.host == "codeberg":
        tree = http_json(
            f"https://codeberg.org/api/v1/repos/{repo.slug}/git/trees/{info.sha}?recursive=true&per_page=10000"
        )
        assert isinstance(tree, dict)
        return [
            e["path"]
            for e in tree["tree"]
            if e["type"] == "blob" and e["mode"] != "120000"
        ]
    raise ValueError(f"unsupported host: {repo.key}")


def fetch_file(info: RepoInfo, path: str) -> bytes:
    repo = info.repo
    if repo.key == SAVANNAH_NANO:
        return (savannah_checkout() / path).read_bytes()
    if repo.host == "github":
        return http_get(
            f"https://raw.githubusercontent.com/{repo.slug}/{info.sha}/{_quote_path(path)}"
        )
    if repo.host == "codeberg":
        return http_get(
            f"https://codeberg.org/{repo.slug}/raw/commit/{info.sha}/{_quote_path(path)}"
        )
    raise ValueError(f"unsupported host: {repo.key}")


def blob_url(info: RepoInfo, path: str) -> str:
    repo = info.repo
    if repo.key == SAVANNAH_NANO:
        return f"{SAVANNAH_CGIT_URL}/tree/{_quote_path(path)}?id={info.sha}"
    if repo.host == "github":
        return f"https://github.com/{repo.slug}/blob/{info.sha}/{_quote_path(path)}"
    if repo.host == "codeberg":
        return f"https://codeberg.org/{repo.slug}/src/commit/{info.sha}/{_quote_path(path)}"
    raise ValueError(f"unsupported host: {repo.key}")


def last_commit_date(info: RepoInfo, path: str) -> str | None:
    """Return the ISO date of the last commit touching `path` (GitHub/Codeberg only)."""
    repo = info.repo
    q = urllib.parse.quote(path, safe="")
    try:
        if repo.host == "github":
            data = http_json(
                f"https://api.github.com/repos/{repo.slug}/commits?path={q}&sha={info.sha}&per_page=1"
            )
        elif repo.host == "codeberg":
            data = http_json(
                f"https://codeberg.org/api/v1/repos/{repo.slug}/commits?path={q}&sha={info.sha}&limit=1&stat=false&files=false"
            )
        else:
            return None
    except urllib.error.HTTPError:
        return None
    assert isinstance(data, list)
    if not data:
        return None
    return data[0]["commit"]["committer"]["date"][:10]


_REPO_LINK = re.compile(r"\]\(https://(github\.com|codeberg\.org)/([^/\s)]+/[^/\s)]+)")
_LISTS_HEADING = re.compile(r"^## Lists[ \t]*$", re.M)
_REMOVED_HEADING = re.compile(r"^#+ Removed[ \t]*$", re.M)


def repos_from_markdown(path: Path = REPOS_MD) -> list[Repo]:
    """Extract repositories listed in the "Lists" section of README.md (excluding "Removed")."""
    repos = [Repo(SAVANNAH_NANO)]
    text = path.read_text()
    if m := _LISTS_HEADING.search(text):
        text = text[m.end() :]
    if m := _REMOVED_HEADING.search(text):
        text = text[: m.start()]
    for host, slug in _REPO_LINK.findall(text):
        key = f"{host.split('.')[0]}:{slug}"
        if key == "github:madnight/nano":  # mirror of the official repository
            continue
        if Repo(key) not in repos:
            repos.append(Repo(key))
    return repos
