# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
import json
import hashlib
import subprocess
from typing import Any
from pathlib import Path

import pytest

from scripts.verify_release import verify_files


@pytest.fixture
def release(tmp_path: Path) -> tuple[dict[str, Any], Path]:
    names = ["x_twitter_scraper-0.12.0-py3-none-any.whl", "x_twitter_scraper-0.12.0.tar.gz"]
    for name in names:
        (tmp_path / name).write_bytes(name.encode())
    return {
        "info": {"version": "0.12.0"},
        "urls": [
            {"filename": name, "yanked": False, "digests": {"sha256": hashlib.sha256(name.encode()).hexdigest()}}
            for name in names
        ],
    }, tmp_path


def test_verified_artifacts(release: tuple[dict[str, Any], Path]) -> None:
    report, directory = release
    assert verify_files(report, directory, "0.12.0") is None
    (directory / "extra.whl").touch()
    with pytest.raises(ValueError, match="exactly"):
        verify_files(report, directory, "0.12.0")


@pytest.mark.parametrize("report", [None, [], {}, {"info": {"version": "old"}}, {"info": {"version": "0.12.0"}}])
def test_invalid_release_metadata(report: object, tmp_path: Path) -> None:
    with pytest.raises(ValueError):
        verify_files(report, tmp_path, "0.12.0")


@pytest.mark.parametrize(
    "change", ["partial", "hash", "yanked", "invalid-file", "missing-name", "missing-digests", "extra", "duplicate"]
)
def test_rejects_unsafe_publication(release: tuple[dict[str, Any], Path], change: str) -> None:
    report, directory = release
    if change == "partial":
        report["urls"].pop()
    elif change == "hash":
        report["urls"][0]["digests"]["sha256"] = "wrong"
    elif change == "yanked":
        report["urls"][0]["yanked"] = True
    elif change == "invalid-file":
        report["urls"][0] = None
    elif change == "extra":
        report["urls"].append({"filename": "unexpected.whl", "digests": {"sha256": "other"}})
    elif change == "duplicate":
        report["urls"].append(report["urls"][0])
    elif change == "missing-name":
        del report["urls"][0]["filename"]
    else:
        del report["urls"][0]["digests"]
    with pytest.raises(ValueError):
        verify_files(report, directory, "0.12.0")


@pytest.mark.parametrize("mode", ["prepare", "publish", "verify", "invalid"])
def test_release_command_rejects_dirty_sources(tmp_path: Path, mode: str) -> None:
    scripts = tmp_path / "scripts"
    scripts.mkdir()
    runner = scripts / "release"
    runner.write_bytes((Path(__file__).parents[1] / "scripts/release").read_bytes())
    binaries = tmp_path / "bin"
    binaries.mkdir()
    for name, body in {
        "git": 'case "$1" in rev-parse) echo abc;; status) echo " M source.py";; *) exit 99;; esac',
        "uv": 'test "$1" = version || exit 99; echo 0.12.0',
        "bun": "exit 99",
    }.items():
        executable = binaries / name
        executable.write_text("#!/bin/sh\n" + body + "\n")
        executable.chmod(0o755)
    result = subprocess.run(
        ["bash", str(runner), mode],
        env={**os.environ, "PATH": f"{binaries}:{os.environ['PATH']}"},
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == (2 if mode == "invalid" else 1)
    assert json.loads(result.stdout) == {"status": "failed", "exitCode": result.returncode}
