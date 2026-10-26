# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
import hashlib
import subprocess
from pathlib import Path

import pytest

from scripts.verify_release import verify_files
from x_twitter_scraper._utils import is_dict, is_list
from x_twitter_scraper._utils._json import json_loads


@pytest.fixture()
def release(tmp_path: Path) -> tuple[dict[str, object], Path]:
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


def test_verified_artifacts(release: tuple[dict[str, object], Path]) -> None:
    report, directory = release
    verify_files(report, directory, "0.12.0")
    (directory / "extra.whl").touch()
    with pytest.raises(ValueError, match="exactly"):
        verify_files(report, directory, "0.12.0")


def test_ignores_the_gitignore_that_uv_build_writes(release: tuple[dict[str, object], Path]) -> None:
    report, directory = release
    (directory / ".gitignore").write_text("*")
    verify_files(report, directory, "0.12.0")
    (directory / ".env").touch()
    with pytest.raises(ValueError, match="exactly"):
        verify_files(report, directory, "0.12.0")


@pytest.mark.parametrize("report", [None, [], {}, {"info": {"version": "old"}}, {"info": {"version": "0.12.0"}}])
def test_invalid_release_metadata(report: object, tmp_path: Path) -> None:
    with pytest.raises(ValueError):
        verify_files(report, tmp_path, "0.12.0")


@pytest.mark.parametrize(
    "change", ["partial", "hash", "yanked", "invalid-file", "missing-name", "missing-digests", "extra", "duplicate"]
)
def test_rejects_unsafe_publication(release: tuple[dict[str, object], Path], change: str) -> None:
    report, directory = release
    urls = report["urls"]
    assert is_list(urls)
    first = urls[0]
    assert is_dict(first)
    if change == "partial":
        urls.pop()
    elif change == "hash":
        digests = first["digests"]
        assert is_dict(digests)
        digests["sha256"] = "wrong"
    elif change == "yanked":
        first["yanked"] = True
    elif change == "invalid-file":
        urls[0] = None
    elif change == "extra":
        urls.append({"filename": "unexpected.whl", "digests": {"sha256": "other"}})
    elif change == "duplicate":
        urls.append(first)
    elif change == "missing-name":
        del first["filename"]
    else:
        del first["digests"]
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
    assert json_loads(result.stdout) == {"status": "failed", "exitCode": result.returncode}
