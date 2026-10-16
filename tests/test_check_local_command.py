# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]
CHECK = r"""#!/usr/bin/env bash
name=$(basename "$0")
if [ "${1:-}" = --version ]; then [ "$CHECK_CASE" != no-codeql ] || exit 1; echo 2.27.2; exit; fi
printf '%s\n' "$name" >> "$CHECK_EVENTS"
case "$name" in
 test) printf '%s\n' '==> Running tests' '===== 3029 passed in 10.00s =====' '===== 3016 passed in 9.00s =====';;
 coverage-parent) printf 'report=%s\nrevision=%s\n' parent.json abc123 >> "$COVERAGE_PARENT_OUTPUT";;
 audit) [ "$CHECK_CASE" != changed ] || touch "$CHECK_DIRTY";;
esac
[ "$CHECK_CASE" != "$name" ]
"""
STUB = r"""git() {
 case "$1 $2" in
  'rev-parse --quiet') :;;
  'rev-parse HEAD') echo abc123;;
  'status --porcelain') if [ "$CHECK_CASE" = dirty ] || [ -e "$CHECK_DIRTY" ]; then echo ' M README.md'; fi;;
  *) exit 99;;
 esac
}
gh() {
 [ "$1 $2" = 'api --silent' ] || exit 99
 case "$3" in
  repos/Xquik-dev/x-twitter-scraper-python/commits/abc123) [ "$CHECK_CASE" != unpushed ];;
  repos/Xquik-dev/x-twitter-scraper-python/statuses/abc123)
   [ "$4 $6 $7 $8" = '-f -f context=xquik-local-checks -f' ] && [ "$#" = 9 ] || exit 99
   printf '%s: %s\n' "${5#state=}" "${9#description=}" >> "$CHECK_STATUSES";;
  *) exit 99;;
 esac
}
uv() {
 case "$1 $2" in
  'run --locked')
   case "$3 $4 $5 $6" in
    '--all-extras python -m scripts.check_api_coverage') printf 'api-coverage\n' >> "$CHECK_EVENTS"; [ "$CHECK_CASE" != api-coverage ];;
    '--all-extras python -m scripts.check_api_fields') printf 'api-fields\n' >> "$CHECK_EVENTS"; [ "$CHECK_CASE" != api-fields ];;
   esac;;
  'python find'|'sync --locked'|'build --out-dir') :;;
  'tool run') [ "$3 $4 $5 $6" = '--from reuse==6.2.0 reuse lint' ] || exit 99; printf 'reuse\n' >> "$CHECK_EVENTS";;
  *) exit 99;;
 esac
}
export -f git gh uv
runner=$1; shift
bash "$runner" "$@"
"""
CHECKS = [
    "api-coverage",
    "api-fields",
    "lint",
    "reuse",
    "check-reproducible",
    "test",
    "coverage-parent",
    "coverage",
    "audit",
    "codeql-security",
]
PENDING = "pending: Running API coverage & fields, lint, licensing, build, tests, coverage, audit & CodeQL."
PASSED = (
    "API coverage, API fields, lint & types, REUSE, reproducible build, metadata, 6045 tests in 2 runs, coverage, "
    "audit, CodeQL 2.27.2."
)


def run_checks(tmp_path: Path, case: str, *arguments: str) -> tuple[int, list[str], list[str], list[str]]:
    project = tmp_path / "project"
    for folder in ("bin", "scripts"):
        (project / folder).mkdir(parents=True)
    runner = project / "bin/check-local"
    runner.write_bytes((ROOT / "bin/check-local").read_bytes())
    (project / "scripts/cleanup.sh").write_bytes((ROOT / "scripts/cleanup.sh").read_bytes())
    for name in CHECKS:
        (project / "scripts" / name).write_text(CHECK)
    events, statuses = tmp_path / "events", tmp_path / "statuses"
    events.touch()
    statuses.touch()
    result = subprocess.run(
        ["bash", "-c", STUB, "check-local-test", str(runner), *arguments],
        env={
            **os.environ,
            "CHECK_CASE": case,
            "CHECK_EVENTS": str(events),
            "CHECK_STATUSES": str(statuses),
            "CHECK_DIRTY": str(tmp_path / "dirty"),
        },
        capture_output=True,
        text=True,
        check=False,
    )
    output = (result.stdout + result.stderr).splitlines()
    return result.returncode, events.read_text().splitlines(), statuses.read_text().splitlines(), output


def test_success_status_lists_the_checks_that_passed(tmp_path: Path) -> None:
    status, events, statuses, output = run_checks(tmp_path, "ready")
    assert status == 0, output
    assert events == CHECKS
    assert statuses == [PENDING, f"success: Passed {PASSED}"]
    assert output[-1] == f"All local checks passed. They were {PASSED}"


@pytest.mark.parametrize(
    "case,ran,failed",
    [
        ("api-coverage", CHECKS[:1], "API coverage: compare the SDK operations with the API spec"),
        ("api-fields", CHECKS[:2], "API fields: compare the SDK fields with the API spec"),
        ("lint", CHECKS[:3], "Lint: Ruff, Pyright, Mypy, and package import"),
        ("test", CHECKS[:6], "Tests: Python 3.10.22 and 3.14.8 with Pydantic 1 and 2"),
        ("audit", CHECKS[:9], "Dependency security: pip-audit and audit-exceptions.json"),
        ("codeql-security", CHECKS, "Static analysis: CodeQL 2.27.2 security-extended queries"),
        ("changed", CHECKS, "Final tree check"),
    ],
)
def test_failed_check_posts_failure_and_stops(tmp_path: Path, case: str, ran: list[str], failed: str) -> None:
    status, events, statuses, _ = run_checks(tmp_path, case)
    assert status != 0
    assert events == ran
    assert statuses == [PENDING, f"failure: Failed at {failed}."]


def test_unusable_codeql_fails_before_any_check(tmp_path: Path) -> None:
    status, events, statuses, _ = run_checks(tmp_path, "no-codeql")
    assert status == 1
    assert events == []
    assert statuses == [PENDING, "failure: Failed at CodeQL CLI."]


@pytest.mark.parametrize(
    "case,arguments,reason",
    [
        ("ready", ["--no-status"], "--no-status was passed."),
        ("dirty", [], "the tree has uncommitted changes."),
        ("unpushed", [], "GitHub does not have HEAD, or gh is signed out. Push first."),
    ],
)
def test_status_is_posted_only_for_a_clean_pushed_commit(
    tmp_path: Path, case: str, arguments: list[str], reason: str
) -> None:
    status, events, statuses, output = run_checks(tmp_path, case, *arguments)
    assert status == 0, output
    assert events == CHECKS
    assert statuses == []
    assert output[0] == f"==> Commit status not posted because {reason}"
