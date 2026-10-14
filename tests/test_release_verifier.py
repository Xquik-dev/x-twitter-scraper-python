# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import hashlib
from typing import TypedDict
from pathlib import Path

import pytest

from scripts.verify_release import verify_files


class ReleaseFile(TypedDict):
    filename: str
    yanked: bool
    digests: dict[str, str]


class ReleaseReport(TypedDict):
    info: dict[str, str]
    urls: list[ReleaseFile]


@pytest.fixture
def release(tmp_path: Path) -> tuple[ReleaseReport, Path]:
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


def test_verified_artifacts(release: tuple[ReleaseReport, Path]) -> None:
    report, directory = release
    assert verify_files(report, directory, "0.12.0") is None


def test_rejects_extra_local_artifacts(release: tuple[ReleaseReport, Path]) -> None:
    report, directory = release
    (directory / "extra.whl").touch()
    with pytest.raises(ValueError, match="exactly"):
        verify_files(report, directory, "0.12.0")


@pytest.mark.parametrize("report", [None, [], {}, {"info": {"version": "old"}}, {"info": {"version": "0.12.0"}}])
def test_invalid_release_metadata(report: object, tmp_path: Path) -> None:
    with pytest.raises(ValueError):
        verify_files(report, tmp_path, "0.12.0")


@pytest.mark.parametrize(
    "change",
    ["version", "partial", "hash", "yanked", "invalid-file", "missing-name", "missing-digests", "extra", "duplicate"],
)
def test_rejects_unsafe_publication(release: tuple[ReleaseReport, Path], change: str) -> None:
    original, directory = release
    first: dict[str, object] = dict(original["urls"][0])
    files: list[object] = [first, original["urls"][1]]
    report: dict[str, object] = {"info": original["info"], "urls": files}
    if change == "version":
        report["info"] = {"version": "old"}
    elif change == "partial":
        files.pop()
    elif change == "hash":
        first["digests"] = {"sha256": "wrong"}
    elif change == "yanked":
        first["yanked"] = True
    elif change == "invalid-file":
        files[0] = None
    elif change == "extra":
        files.append({"filename": "unexpected.whl", "digests": {"sha256": "other"}})
    elif change == "duplicate":
        files.append(first)
    elif change == "missing-name":
        del first["filename"]
    else:
        del first["digests"]
    with pytest.raises(ValueError):
        verify_files(report, directory, "0.12.0")
