# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import sys
import json
import subprocess
from typing import TypedDict
from pathlib import Path


class SourceSnapshot(TypedDict):
    revision: str
    sources: dict[str, str]


def git(root: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=root, encoding="utf-8")


def snapshot(root: Path) -> SourceSnapshot:
    paths = sorted(
        set(git(root, "ls-files", "-z", "--cached", "--others", "--exclude-standard", "--", "*.py").split("\0")) - {""}
    )
    paths = [path for path in paths if (root / path).is_file()]
    hashes = git(root, "hash-object", "--", *paths).splitlines() if paths else []
    return {"revision": git(root, "rev-parse", "HEAD").strip(), "sources": dict(zip(paths, hashes, strict=True))}


def committed_sources(root: Path, revision: str) -> SourceSnapshot:
    commit = git(root, "rev-parse", "--verify", f"{revision}^{{commit}}").strip()
    sources: dict[str, str] = {}
    for entry in git(root, "ls-tree", "-rz", "--full-tree", commit).split("\0"):
        if entry:
            metadata, path = entry.split("\t", 1)
            if path.endswith(".py"):
                sources[path] = metadata.split()[2]
    return {"revision": commit, "sources": sources}


def attach(report_path: Path, before_path: Path, root: Path) -> None:
    before = json.loads(before_path.read_text())
    if before != snapshot(root):
        raise ValueError("Sources changed during coverage. Rerun coverage.")
    report = json.loads(report_path.read_text())
    if set(report["files"]) != set(before["sources"]):
        raise ValueError("Coverage omitted Python files. Measure every tracked and new Python file.")
    report["xquik_sources"] = before
    report_path.write_text(json.dumps(report))


def verify_parent(report_path: Path, root: Path, revision: str) -> None:
    report = json.loads(report_path.read_text())
    if report.get("xquik_sources") != committed_sources(root, revision):
        raise ValueError("Parent coverage does not match the Git revision. Regenerate its baseline.")


if __name__ == "__main__":
    action, *args = sys.argv[1:]
    if action == "snapshot":
        Path(args[0]).write_text(json.dumps(snapshot(Path.cwd())))
    elif action == "attach":
        attach(Path(args[0]), Path(args[1]), Path.cwd())
    elif action == "verify-parent":
        verify_parent(Path(args[0]), Path.cwd(), args[1])
    else:
        raise SystemExit("Use snapshot, attach, or verify-parent.")
