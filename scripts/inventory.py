#!/usr/bin/env python3
"""List every *.nanorc found in the repositories listed in README.md.

The output (JSON lines) helps curating scripts/sources.toml: it shows, for each
file, the repository license, whether the repository is archived and the date
of the last commit touching the file.

Usage: scripts/inventory.py [--no-dates] > inventory.jsonl
"""

from __future__ import annotations

import argparse
import json
import sys
from concurrent.futures import ThreadPoolExecutor

from _common import last_commit_date, list_files, repo_info, repos_from_markdown


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--no-dates", action="store_true", help="skip per-file last commit lookups"
    )
    args = parser.parse_args()

    def scan(repo):
        try:
            info = repo_info(repo)
            paths = [p for p in list_files(info) if p.endswith(".nanorc")]
        except Exception as e:  # noqa: BLE001
            print(f"error: {repo.key}: {e}", file=sys.stderr)
            return []
        rows = []
        for path in paths:
            rows.append(
                {
                    "repo": repo.key,
                    "path": path,
                    "license": info.license,
                    "archived": info.archived,
                    "date": None if args.no_dates else last_commit_date(info, path),
                }
            )
        return rows

    with ThreadPoolExecutor(8) as pool:
        for rows in pool.map(scan, repos_from_markdown()):
            for row in rows:
                print(json.dumps(row), flush=True)


if __name__ == "__main__":
    main()
