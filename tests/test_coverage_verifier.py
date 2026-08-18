# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import json
from pathlib import Path

import pytest

from scripts.verify_coverage import verify_coverage


def write_report(path: Path, *, lines: tuple[int, int], branches: tuple[int, int]) -> None:
    path.write_text(
        json.dumps(
            {
                "totals": {
                    "covered_lines": lines[0],
                    "num_statements": lines[1],
                    "covered_branches": branches[0],
                    "num_branches": branches[1],
                }
            }
        ),
        encoding="utf-8",
    )


@pytest.mark.parametrize(("branches", "expected"), [((80, 100), True), ((79, 100), False)])
def test_verify_coverage_enforces_thresholds(tmp_path: Path, branches: tuple[int, int], expected: bool) -> None:
    report_path = tmp_path / "coverage.json"
    write_report(report_path, lines=(90, 100), branches=branches)
    assert verify_coverage(report_path) is expected


def test_verify_coverage_rejects_invalid_reports(tmp_path: Path) -> None:
    report_path = tmp_path / "coverage.json"
    report_path.write_text('{"totals": {"covered_lines": true}}', encoding="utf-8")
    with pytest.raises(ValueError, match="must be an integer"):
        verify_coverage(report_path)
