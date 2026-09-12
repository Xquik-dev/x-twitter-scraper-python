# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest


@pytest.mark.parametrize("host", ["-oProxyCommand=command", "host;command", "host\ncommand", "host $(command)"])
def test_fuzz_rejects_ssh_command_injection(host: str) -> None:
    script = Path(__file__).parents[1] / "scripts/fuzz"
    result = subprocess.run(
        ["bash", str(script)],
        env={**os.environ, "XQUIK_FUZZ_HOST": host},
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 2
    assert result.stderr.strip() == "Invalid SSH host."
    assert result.stdout == ""


def test_fuzz_requires_supported_runner() -> None:
    script = Path(__file__).parents[1] / "scripts/fuzz"
    result = subprocess.run(
        ["bash", "-c", 'uname() { echo Darwin; }; export -f uname; bash "$1"', "runner-test", str(script)],
        env={**os.environ, "XQUIK_FUZZ_HOST": ""},
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 1
    assert "Use Linux x86_64 or set XQUIK_FUZZ_HOST" in result.stderr
    assert result.stdout == ""
