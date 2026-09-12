# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import sys
import json
import hashlib
import urllib.request
from typing import cast
from pathlib import Path
from collections.abc import Mapping


def verify_files(report: object, artifacts: Path, version: str) -> None:
    if not isinstance(report, Mapping):
        raise ValueError("PyPI returned invalid release metadata.")
    data = cast(Mapping[str, object], report)
    info = data.get("info")
    if not isinstance(info, Mapping) or cast(Mapping[str, object], info).get("version") != version:
        raise ValueError("PyPI release version does not match.")
    urls = data.get("urls")
    if not isinstance(urls, list):
        raise ValueError("PyPI file metadata is missing.")
    expected = {
        f"x_twitter_scraper-{version}-py3-none-any.whl",
        f"x_twitter_scraper-{version}.tar.gz",
    }
    local = {file.name: file for file in artifacts.iterdir() if file.is_file()}
    if set(local) != expected:
        raise ValueError("Expected exactly the release wheel and source archive.")
    matched: set[str] = set()
    for item in cast(list[object], urls):
        if not isinstance(item, Mapping):
            raise ValueError("PyPI file metadata is invalid.")
        entry = cast(Mapping[str, object], item)
        name, digests = entry.get("filename"), entry.get("digests")
        if not isinstance(name, str) or not isinstance(digests, Mapping):
            raise ValueError("PyPI file identity is missing.")
        if name not in local or name in matched:
            raise ValueError("PyPI returned unexpected or duplicate release artifacts.")
        digest = hashlib.sha256(local[name].read_bytes()).hexdigest()
        if entry.get("yanked") is not False or cast(Mapping[str, object], digests).get("sha256") != digest:
            raise ValueError("Published artifact differs or was yanked. Do not overwrite this version.")
        matched.add(name)
    if matched != expected:
        raise ValueError("Publication is incomplete. Retry the same publish command.")


if __name__ == "__main__":
    version, directory = sys.argv[1:]
    with urllib.request.urlopen(f"https://pypi.org/pypi/x-twitter-scraper/{version}/json", timeout=20) as response:
        verify_files(json.load(response), Path(directory), version)
