# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest

SCRIPT = Path(__file__).parents[1] / "scripts/codeql-security"
FAKE_CODEQL = "#!/usr/bin/env bash\n[ \"$*\" = 'version --format=terse' ] || exit 99\necho {version}\n"


def check_version(tmp_path: Path, version: str | None) -> subprocess.CompletedProcess[str]:
    codeql = tmp_path / "codeql"
    if version is not None:
        codeql.write_text(FAKE_CODEQL.format(version=version))
        codeql.chmod(0o755)
    return subprocess.run(
        ["bash", str(SCRIPT), "--version"],
        env={**os.environ, "XQUIK_CODEQL_BIN": str(codeql)},
        capture_output=True,
        text=True,
        check=False,
    )


@pytest.mark.parametrize("version", ["2.27.0", "2.27.2", "2.100.0", "3.0.0"])
def test_supported_codeql_prints_its_version_without_analyzing(tmp_path: Path, version: str) -> None:
    result = check_version(tmp_path, version)
    assert result.returncode == 0, result.stderr
    assert result.stdout == f"{version}\n"
    assert result.stderr == ""


@pytest.mark.parametrize(
    "version,message",
    [
        (None, "CodeQL CLI is missing. Install it with brew install --cask codeql, then rerun."),
        ("2.26.9", "CodeQL CLI 2.26.9 is older than 2.27.0. Run brew upgrade --cask codeql."),
    ],
)
def test_unusable_codeql_fails_with_the_next_step(tmp_path: Path, version: str | None, message: str) -> None:
    result = check_version(tmp_path, version)
    assert result.returncode == 1
    assert result.stderr == f"{message}\n"
    assert result.stdout == ""
