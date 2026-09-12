# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
import json
import subprocess
from pathlib import Path

import pytest

STUB = r"""record() { printf '%s\n' "$1" >> "$RELEASE_EVENTS"; }
name=$1; shift
case "$name" in
 git)
  case "$1" in
   rev-parse) case "$2" in v*) [ "$RELEASE_CASE" != tag ] || { echo wrong; exit; };; esac; echo abc;;
   merge-base) [ "$RELEASE_CASE" != ancestry ];;
   status|fetch) :;;
   *) exit 99;;
  esac;;
 bun) record "$2"; [ "$2:$RELEASE_CASE" != check:all:checks ];;
 security) [ "$*" = 'find-generic-password -s test-publisher -w' ] || exit 99; echo isolated-fixture-token;;
 uv)
  case "$1" in
   version) echo 0.12.0;;
   build)
    record artifacts
    while [ "$1" != --out-dir ]; do shift; done
    shift; mkdir -p "$1"
    for suffix in -py3-none-any.whl .tar.gz; do echo fixture > "$1/x_twitter_scraper-0.12.0$suffix"; done
    if [ "$RELEASE_CASE" = extra ]; then echo other > "$1/unexpected.whl"; fi;;
   publish)
    [ "$2" = --publish-url ] && [ "$3" = https://upload.pypi.org/legacy/ ] && [ "$4" = --check-url ] && [ "$5" = https://pypi.org/simple/ ] && [ "$#" = 7 ] || exit 99
    if [ "$RELEASE_CASE" = keychain ]; then [ "$UV_PUBLISH_TOKEN" = isolated-fixture-token ] || exit 99; fi
    record publish;;
   run)
    case " $* " in
     *' twine '*) record metadata;;
     *' scripts/verify_release.py '*) [ -z "${UV_PUBLISH_TOKEN:-}" ] || exit 99; record registry; [ "$RELEASE_CASE" != registry ];;
     *' --no-project '*) record install;;
     *) printf '%s\n' '{"status":"completed","action":"publish","version":"0.12.0","commit":"abc"}';;
    esac;;
   *) exit 99;;
  esac;;
 *) exit 99;;
esac
"""


@pytest.mark.parametrize("case", ["success", "keychain", "checks", "tag", "ancestry", "extra", "registry"])
def test_publish_sequence_stops_at_failed_guards(tmp_path: Path, case: str) -> None:
    scripts = tmp_path / "scripts"
    scripts.mkdir()
    runner = scripts / "release"
    runner.write_bytes((Path(__file__).parents[1] / "scripts/release").read_bytes())
    commands = "stub_command() {\n" + STUB + "\n}\n"
    for name in ("git", "bun", "uv", "security"):
        commands += f'{name}() {{ stub_command {name} "$@"; }}\nexport -f {name}\n'
    commands += 'export -f stub_command\nbash "$1" publish parent-coverage.json parent\n'
    events = tmp_path / "events"
    environment = {
        key: value
        for key, value in os.environ.items()
        if key not in ("UV_PUBLISH_TOKEN", "XQUIK_PYPI_KEYCHAIN_SERVICE")
    }
    environment.update(RELEASE_CASE=case, RELEASE_EVENTS=str(events))
    if case == "keychain":
        environment["XQUIK_PYPI_KEYCHAIN_SERVICE"] = "test-publisher"
    result = subprocess.run(
        ["bash", "-c", commands, "release-test", str(runner)],
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )
    observed = events.read_text().splitlines()
    assert "isolated-fixture-token" not in result.stdout + result.stderr
    if case in ("success", "keychain"):
        assert result.returncode == 0, result.stderr
        assert json.loads(result.stdout)["status"] == "completed"
        assert observed == ["check:all", "build", "artifacts", "metadata", "publish", "registry", "install"]
    else:
        assert result.returncode != 0
        assert json.loads(result.stdout)["status"] == "failed"
        assert ("publish" in observed) is (case == "registry")
        assert "install" not in observed
        if case == "checks":
            assert observed == ["check:all"]
