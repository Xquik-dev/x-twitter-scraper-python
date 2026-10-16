# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
import sys
import json
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]
PINS = {
    "runtime": "anyio==4.14.2 \\\n    --hash=sha256:aa\n",
    "pydantic-v2": (
        "anyio==4.14.2 \\\n    --hash=sha256:aa\n"
        "colorama==0.4.6 ; sys_platform == 'win32' \\\n    --hash=sha256:bb\n    # via pytest\n"
        "pydantic==2.13.4 \\\n    --hash=sha256:cc\n"
    ),
    "pydantic-v1": "anyio==4.14.2 \\\n    --hash=sha256:aa\npydantic==1.10.26 \\\n    --hash=sha256:dd\n",
}
FAKE_PIP_AUDIT = r"""import os, re, sys, json
arguments = sys.argv[1:]
if not {"--strict", "--disable-pip", "--require-hashes"} <= set(arguments):
    sys.exit(99)
text = open(arguments[arguments.index("--requirement") + 1]).read()
open(os.environ["AUDIT_RECEIVED"], "a").write(text)
findings = json.loads(os.environ["AUDIT_FINDINGS"])
pins = [match.groups() for match in re.finditer(r"^([A-Za-z0-9._-]+)==(\S+) \\$", text, re.MULTILINE)]
dependencies = [{"name": name, "version": version, "vulns": findings.get(f"{name} {version}", [])} for name, version in pins]
json.dump({"dependencies": dependencies, "fixes": []}, open(arguments[arguments.index("--output") + 1], "w"))
sys.exit(any(dependency["vulns"] for dependency in dependencies))
"""
STUB = r"""uv() {
 case "$1" in
  export)
   local kind=""
   while [ "$1" != --output-file ]; do
    case "$1" in --no-dev) kind=runtime;; pydantic-v1|pydantic-v2) kind=$1;; esac
    shift
   done
   cp "$AUDIT_FIXTURES/$kind.txt" "$2";;
  tool) [ "$2 $3 $4 $5" = 'run --from pip-audit==2.10.1 pip-audit' ] || exit 99; shift 5; "$AUDIT_PYTHON" "$AUDIT_FIXTURES/pip_audit.py" "$@";;
  run) [ "$2 $3" = '--no-project python' ] || exit 99; shift 3; "$AUDIT_PYTHON" "$@";;
  *) exit 99;;
 esac
}
export -f uv
bash "$1"
"""


def run_audit(
    tmp_path: Path, findings: dict[str, list[dict[str, object]]]
) -> tuple[subprocess.CompletedProcess[str], str]:
    project, fixtures = tmp_path / "project", tmp_path / "fixtures"
    (project / "scripts").mkdir(parents=True)
    fixtures.mkdir()
    for name in ("scripts/audit", "scripts/cleanup.sh", "scripts/verify_audit.py", "audit-exceptions.json"):
        (project / name).write_bytes((ROOT / name).read_bytes())
    for name, text in PINS.items():
        (fixtures / f"{name}.txt").write_text(text)
    (fixtures / "pip_audit.py").write_text(FAKE_PIP_AUDIT)
    received = tmp_path / "received.txt"
    result = subprocess.run(
        ["bash", "-c", STUB, "audit-test", str(project / "scripts/audit")],
        env={
            **os.environ,
            "AUDIT_FIXTURES": str(fixtures),
            "AUDIT_PYTHON": sys.executable,
            "AUDIT_RECEIVED": str(received),
            "AUDIT_FINDINGS": json.dumps(findings),
        },
        capture_output=True,
        text=True,
        check=False,
    )
    return result, received.read_text()


def test_audit_checks_every_locked_pin_on_any_machine(tmp_path: Path) -> None:
    result, received = run_audit(tmp_path, {})
    assert result.returncode == 0, result.stderr
    assert result.stdout.splitlines()[-1] == "Dependency audit passed."
    assert "colorama==0.4.6 \\\n    --hash=sha256:bb\n" in received
    assert "pydantic==2.13.4 \\\n    --hash=sha256:cc\n" in received
    assert "pydantic==1.10.26 \\\n    --hash=sha256:dd\n" in received
    assert "sys_platform" not in received


@pytest.mark.parametrize(
    "pin,fixes,message",
    [
        ("colorama 0.4.6", ["0.4.7"], "colorama 0.4.6 GHSA-0000-0000-0001 is fixed in 0.4.7. Upgrade it in uv.lock."),
        (
            "pydantic 1.10.26",
            [],
            "pydantic 1.10.26 GHSA-0000-0000-0001 has no fix. Review it and list it in audit-exceptions.json.",
        ),
        (
            "anyio 4.14.2",
            [],
            "anyio 4.14.2 GHSA-0000-0000-0001 affects a shipped runtime dependency. Upgrade it in uv.lock.",
        ),
    ],
)
def test_audit_blocks_a_finding_in_any_locked_pin(tmp_path: Path, pin: str, fixes: list[str], message: str) -> None:
    result, _ = run_audit(tmp_path, {pin: [{"id": "GHSA-0000-0000-0001", "fix_versions": fixes, "aliases": []}]})
    assert result.returncode == 1
    assert result.stderr.splitlines() == [message]
    assert result.stdout.splitlines()[-1] != "Dependency audit passed."
