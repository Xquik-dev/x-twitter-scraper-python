# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
import json
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


FAKE_SCAN = """#!/usr/bin/env bash
case "$1 $2" in
  "version --format=terse") echo 2.27.2 ;;
  "pack install") ;;
  "database create") ;;
  "database analyze")
    for argument in "$@"; do
      case "$argument" in --output=*) cp "$FAKE_REPORT" "${argument#--output=}" ;; esac
    done ;;
  *) echo "unexpected codeql call $*" >&2; exit 97 ;;
esac
"""

EXTRACTED: dict[str, object] = {
    "locations": [{"physicalLocation": {"artifactLocation": {"uri": "src/x_twitter_scraper/_client.py"}}}],
    "message": {"text": ""},
    "level": "none",
    "descriptor": {"id": "py/diagnostics/successfully-extracted-files"},
}


def unread(file: str, line: int) -> list[dict[str, object]]:
    return [
        {
            "locations": [{"physicalLocation": {"artifactLocation": {"uri": file}, "region": {"startLine": line}}}],
            "message": {"text": f"Extraction failed in {file} with error Syntax Error"},
            "descriptor": {"id": "py/diagnostics/extraction-warnings"},
        },
        {
            "locations": [{"physicalLocation": {"artifactLocation": {"uri": file}}}],
            "message": {"text": f"A parse error occurred while processing `{file}`."},
            "descriptor": {"id": "py/diagnostics/syntax-error"},
        },
    ]


def report(notifications: list[dict[str, object]], diagnostics: list[str]) -> str:
    return json.dumps(
        {
            "version": "2.1.0",
            "runs": [
                {
                    "tool": {"driver": {"name": "CodeQL", "notifications": [{"id": d} for d in diagnostics]}},
                    "invocations": [{"toolExecutionNotifications": notifications, "executionSuccessful": True}],
                    "results": [],
                }
            ],
        }
    )


def scan(tmp_path: Path, sarif: str) -> subprocess.CompletedProcess[str]:
    codeql = tmp_path / "codeql"
    codeql.write_text(FAKE_SCAN)
    codeql.chmod(0o755)
    (tmp_path / "report.sarif").write_text(sarif)
    return subprocess.run(
        ["bash", str(SCRIPT)],
        env={
            **os.environ,
            "XQUIK_CODEQL_BIN": str(codeql),
            "FAKE_REPORT": str(tmp_path / "report.sarif"),
            "TMPDIR": str(tmp_path),
        },
        capture_output=True,
        text=True,
        check=False,
    )


def test_a_scan_that_read_every_file_passes(tmp_path: Path) -> None:
    result = scan(tmp_path, report([EXTRACTED], ["py/diagnostics/extraction-warnings"]))
    assert result.returncode == 0, result.stderr
    assert result.stdout.endswith("CodeQL completed without findings and extracted 1 Python entries.\n")


def test_a_file_that_codeql_could_not_parse_fails_the_scan_and_is_named(tmp_path: Path) -> None:
    notifications = [
        *unread("src/x_twitter_scraper/_client.py", 12),
        *unread("src/x_twitter_scraper/_files.py", 3),
        EXTRACTED,
    ]
    result = scan(tmp_path, report(notifications, ["py/diagnostics/extraction-warnings"]))
    assert result.returncode == 1
    assert result.stderr.endswith(
        "CodeQL could not parse src/x_twitter_scraper/_client.py at line 12 and src/x_twitter_scraper/_files.py "
        "at line 3, so the scan is incomplete. Rewrite that syntax so CodeQL parses it, then rerun bin/check-local.\n"
    )


def test_a_scan_without_the_extraction_diagnostic_fails(tmp_path: Path) -> None:
    result = scan(tmp_path, report([EXTRACTED], ["py/diagnostics/successfully-extracted-files"]))
    assert result.returncode == 1
    assert result.stderr.endswith(
        "The CodeQL scan lacks py/diagnostics/extraction-warnings, so it cannot show that it read every file. "
        "Make the suite in scripts/codeql-security run that diagnostic query.\n"
    )
