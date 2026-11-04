# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
import sys
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]
RECORD_BASE_URL = """
import os


def test_record_base_url() -> None:
    with open(os.environ["MOCK_API_BASE_URLS"], "a") as base_urls:
        base_urls.write(os.environ["TEST_API_BASE_URL"] + "\\n")
"""


@pytest.mark.parametrize(
    ("options", "processes"),
    [(["-n", "2", "--dist", "each"], 2), (["-n", "0"], 1)],
    ids=["2 xdist workers", "no xdist"],
)
def test_each_test_process_calls_its_own_mock_api_server(tmp_path: Path, options: list[str], processes: int) -> None:
    (tmp_path / "pytest.ini").write_text("[pytest]\n")
    (tmp_path / "test_record.py").write_text(RECORD_BASE_URL)
    base_urls = tmp_path / "base-urls"
    env = {
        name: value
        for name, value in os.environ.items()
        if name != "TEST_API_BASE_URL" and not name.startswith("PYTEST_")
    }
    env["MOCK_API_BASE_URLS"] = str(base_urls)

    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-c", str(tmp_path / "pytest.ini"), "-p", "tests.conftest"]
        + ["-p", "no:cacheprovider", *options, str(tmp_path / "test_record.py")],
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
        timeout=120,
        check=False,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    recorded = base_urls.read_text().splitlines()
    assert len(recorded) == processes
    assert len(set(recorded)) == processes, f"{processes} test processes shared {recorded}"
    assert all(url.startswith("http://127.0.0.1:") for url in recorded)
