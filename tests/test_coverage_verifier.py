from __future__ import annotations

import json
from pathlib import Path

import pytest

from scripts.verify_coverage import coverage_passes, verify_coverage, coverage_percent


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


def test_coverage_thresholds_are_inclusive() -> None:
    assert coverage_percent(9, 10) == 90
    assert coverage_passes(9, 10, 90)
    assert coverage_passes(8, 10, 80)
    assert not coverage_passes(7, 10, 80)


def test_verify_coverage_accepts_gold_thresholds(tmp_path: Path) -> None:
    report_path = tmp_path / "coverage.json"
    write_report(report_path, lines=(90, 100), branches=(80, 100))
    assert verify_coverage(report_path)


def test_verify_coverage_rejects_low_branch_coverage(tmp_path: Path) -> None:
    report_path = tmp_path / "coverage.json"
    write_report(report_path, lines=(95, 100), branches=(79, 100))
    assert not verify_coverage(report_path)


def test_verify_coverage_rejects_invalid_reports(tmp_path: Path) -> None:
    report_path = tmp_path / "coverage.json"
    report_path.write_text('{"totals": {"covered_lines": true}}', encoding="utf-8")
    with pytest.raises(ValueError, match="must be an integer"):
        verify_coverage(report_path)
