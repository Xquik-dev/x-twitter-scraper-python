# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]
STUB = r"""record() { printf '%s\n' "$1" >> "$RELEASE_EVENTS"; }
git() {
 case "$1" in
  remote) echo git@github.com:Xquik-dev/x-twitter-scraper-python.git;;
  status) [ "$RELEASE_CASE" != dirty ] || echo ' M README.md';;
  symbolic-ref) case "$RELEASE_CASE" in detached) return 1;; branch) echo topic;; *) echo main;; esac;;
  fetch) :;;
  rev-parse)
   case "$*" in
    *refs/tags/*) return 1;;
    *origin/main*) if [ "$RELEASE_CASE" = behind ]; then echo def; else echo abc; fi;;
    *) echo abc;;
   esac;;
  ls-remote) [ "$RELEASE_CASE" = tagged ] || return 2;;
  tag) record "tag $3 $6";;
  push) record "push $3";;
  *) exit 99;;
 esac
}
uv() {
 case "$1" in
  version) echo 0.12.0;;
  build)
   [ "$2" = --no-sources ] || exit 99
   record build
   while [ "$1" != --out-dir ]; do shift; done
   mkdir -p "$2"
   for suffix in -py3-none-any.whl .tar.gz; do echo fixture > "$2/x_twitter_scraper-0.12.0$suffix"; done;;
  run) record metadata;;
  publish)
   [ "$UV_PUBLISH_TOKEN" = isolated-fixture-token ] && [ "$#" = 7 ] || exit 99
   [ "$2 $3 $4 $5" = '--publish-url https://upload.pypi.org/legacy/ --check-url https://pypi.org/simple/' ] || exit 99
   record publish;;
  *) exit 99;;
 esac
}
gh() {
 case "$1 $2" in
  'auth status') :;;
  'release create') record "release $3"; cat > "$RELEASE_NOTES";;
  *) exit 99;;
 esac
}
curl() {
 while [ "$#" -gt 1 ]; do shift; done
 [ "$1" = https://pypi.org/pypi/x-twitter-scraper/0.12.0/json ] || exit 99
 printf '%s' "$RELEASE_PYPI"
}
security() {
 [ "$1 $2 $3" = "find-generic-password -s $RELEASE_TOKEN_SERVICE" ] || exit 99
 [ "$RELEASE_CASE" != keychain ] || return 44
 [ "${4:-}" != -w ] || echo isolated-fixture-token
}
export -f record git uv gh curl security
runner=$1; shift
bash "$runner" "$@"
"""
CHECKED = ["checks", "audit", "build", "metadata"]
RELEASED = ["tag v0.12.0 abc", "push refs/tags/v0.12.0", "release v0.12.0"]
DRY_RUN_END = "Dry run finished for x-twitter-scraper 0.12.0. Nothing was uploaded, tagged, or released."


def run_release(tmp_path: Path, arguments: list[str], case: str, pypi: str) -> tuple[int, list[str], str, str]:
    project = tmp_path / "project"
    for folder in ("bin", "scripts", "src/x_twitter_scraper"):
        (project / folder).mkdir(parents=True)
    runner = project / "bin/release-local"
    runner.write_bytes((ROOT / "bin/release-local").read_bytes())
    for name, event in (("bin/check-local", "checks"), ("scripts/audit", "audit"), ("scripts/release", '"$1"')):
        (project / name).write_text(f"#!/usr/bin/env bash\nprintf '%s\\n' {event} >> \"$RELEASE_EVENTS\"\n")
        (project / name).chmod(0o755)
    (project / "src/x_twitter_scraper/_version.py").write_text('__version__ = "0.12.0"  # x-release-please-version\n')
    (project / "CHANGELOG.md").write_text("# Changelog\n\n## 0.12.0 (2026-09-30)\n\n- Added.\n\n## 0.11.2\n\n- Old.\n")
    events, notes = tmp_path / "events", tmp_path / "notes"
    events.touch()
    notes.touch()
    result = subprocess.run(
        ["bash", "-c", STUB, "release-local-test", str(runner), *arguments],
        env={
            **os.environ,
            "RELEASE_CASE": case,
            "RELEASE_PYPI": pypi,
            "RELEASE_EVENTS": str(events),
            "RELEASE_NOTES": str(notes),
            "RELEASE_TOKEN_SERVICE": "xquik-pypi-token",
        },
        capture_output=True,
        text=True,
        check=False,
    )
    assert "isolated-fixture-token" not in result.stdout + result.stderr
    return result.returncode, events.read_text().splitlines(), result.stdout + result.stderr, notes.read_text()


@pytest.mark.parametrize(
    "pypi,events",
    [("404", [*CHECKED, "publish", "verify", *RELEASED]), ("200", [*CHECKED, "verify", *RELEASED])],
)
def test_release_uploads_once_then_tags_and_releases(tmp_path: Path, pypi: str, events: list[str]) -> None:
    status, observed, output, notes = run_release(tmp_path, [], "ready", pypi)
    assert status == 0, output
    assert observed == events
    assert notes == "\n- Added.\n"
    assert output.splitlines()[-1] == "Released x-twitter-scraper 0.12.0 as v0.12.0."


@pytest.mark.parametrize(
    "case,pypi,events",
    [("ready", "404", CHECKED), ("ready", "200", [*CHECKED, "verify"]), ("detached", "404", CHECKED)],
)
def test_dry_run_uploads_tags_and_releases_nothing(tmp_path: Path, case: str, pypi: str, events: list[str]) -> None:
    status, observed, output, notes = run_release(tmp_path, ["--dry-run"], case, pypi)
    assert status == 0, output
    assert observed == events
    assert notes == ""
    assert output.splitlines()[-1] == DRY_RUN_END


@pytest.mark.parametrize(
    "arguments,case,pypi,status,message",
    [
        ([], "dirty", "404", 1, "release-local: Commit or remove local changes, then rerun."),
        ([], "detached", "404", 1, "release-local: Switch to main, then rerun."),
        (["--dry-run"], "branch", "404", 1, "release-local: Switch to main, then rerun."),
        (["--dry-run"], "behind", "404", 1, "release-local: Make main equal to origin/main, then rerun."),
        ([], "tagged", "404", 1, "release-local: Tag v0.12.0 already exists on origin. Bump the version, then rerun."),
        (
            ["--dry-run"],
            "keychain",
            "404",
            1,
            "release-local: Keychain has no xquik-pypi-token item. "
            "The owner must add the PyPI token as that service, then rerun.",
        ),
        ([], "ready", "503", 1, "release-local: PyPI returned HTTP 503. Retry later."),
        (["--publish"], "ready", "404", 2, "release-local: unknown option --publish. Use --dry-run or no option."),
    ],
)
def test_release_refuses_before_any_upload(
    tmp_path: Path, arguments: list[str], case: str, pypi: str, status: int, message: str
) -> None:
    observed_status, observed, output, notes = run_release(tmp_path, arguments, case, pypi)
    assert observed_status == status
    assert output.splitlines()[-1] == message
    assert not {"publish", "verify", *RELEASED} & set(observed)
    assert notes == ""
