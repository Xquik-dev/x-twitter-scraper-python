# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import sys
import json
import subprocess
from pathlib import Path
from fractions import Fraction

import pytest

from scripts.verify_coverage import verify_coverage, coverage_metrics, verify_non_regression


def write_report(
    path: Path,
    *,
    lines: tuple[int, int],
    branches: tuple[int, int],
    functions: tuple[int, int] = (1, 1),
    excluded_lines: int = 0,
) -> None:
    path.write_text(
        json.dumps(
            {
                "meta": {"format": 3, "version": "test", "branch_coverage": True},
                "totals": {
                    "covered_lines": lines[0],
                    "num_statements": lines[1],
                    "covered_branches": branches[0],
                    "num_branches": branches[1],
                    "excluded_lines": excluded_lines,
                },
                "files": {
                    "example.py": {
                        "functions": {
                            f"example_{index}": {
                                "summary": {"covered_lines": int(index < functions[0]), "num_statements": 1}
                            }
                            for index in range(functions[1])
                        }
                    }
                },
            }
        ),
        encoding="utf-8",
    )


@pytest.mark.parametrize(
    ("lines", "branches", "expected"),
    [
        ((90, 100), (80, 100), True),
        ((89, 100), (80, 100), True),
        ((90, 100), (79, 100), True),
        ((0, 100), (0, 100), True),
        ((100, 100), (100, 100), True),
    ],
)
def test_verify_coverage_accepts_valid_counts_without_absolute_floors(
    tmp_path: Path, lines: tuple[int, int], branches: tuple[int, int], expected: bool
) -> None:
    report_path = tmp_path / "coverage.json"
    write_report(report_path, lines=lines, branches=branches)
    assert verify_coverage(report_path) is expected


def test_verify_coverage_rejects_invalid_reports(tmp_path: Path) -> None:
    report_path = tmp_path / "coverage.json"
    report_path.write_text('{"totals": {"covered_lines": true}}', encoding="utf-8")
    with pytest.raises(ValueError, match="must be an integer"):
        verify_coverage(report_path)


@pytest.mark.parametrize("metric", ["lines", "branches"])
@pytest.mark.parametrize("counts", [(-1, 100), (101, 100), (0, 0), (0, -1)])
def test_verify_coverage_rejects_impossible_counts(tmp_path: Path, metric: str, counts: tuple[int, int]) -> None:
    report_path = tmp_path / "coverage.json"
    write_report(
        report_path,
        lines=counts if metric == "lines" else (90, 100),
        branches=counts if metric == "branches" else (80, 100),
    )
    with pytest.raises(ValueError, match="Regenerate coverage"):
        verify_coverage(report_path)


@pytest.mark.parametrize(
    "before, after, expected",
    [
        (8000, 8010, True),
        (8000, 8009, True),
        (8000, 8000, True),
        (8000, 7999, False),
        (9995, 10000, True),
        (10000, 9999, False),
        (10000, 10000, True),
    ],
)
def test_coverage_non_regression_is_exact(tmp_path: Path, before: int, after: int, expected: bool) -> None:
    parent, candidate = tmp_path / "parent.json", tmp_path / "candidate.json"
    write_report(parent, lines=(before, 10000), branches=(before, 10000))
    write_report(candidate, lines=(after, 10000), branches=(after, 10000))
    assert verify_coverage(candidate)
    assert verify_non_regression(candidate, parent) is expected


def test_missing_and_uncovered_functions_cannot_pass(tmp_path: Path) -> None:
    parent, candidate = tmp_path / "parent.json", tmp_path / "candidate.json"
    write_report(parent, lines=(100, 100), branches=(100, 100))
    report = json.loads(parent.read_text())
    report["files"]["example.py"]["functions"]["example_0"]["summary"]["covered_lines"] = 0
    candidate.write_text(json.dumps(report))
    assert not verify_non_regression(candidate, parent)
    report["files"] = {}
    candidate.write_text(json.dumps(report))
    with pytest.raises(ValueError, match="lacks files"):
        coverage_metrics(candidate)


def test_coverage_metrics_returns_exact_percentage_fractions(tmp_path: Path) -> None:
    report = tmp_path / "coverage.json"
    write_report(report, lines=(1, 3), branches=(2, 3), functions=(1, 2))
    assert coverage_metrics(report) == {
        "Statement": Fraction(100, 3),
        "Branch": Fraction(200, 3),
        "Function": Fraction(50, 1),
        "Line": Fraction(100, 3),
    }


@pytest.mark.parametrize("metric", ["lines", "branches", "functions"])
@pytest.mark.parametrize(
    "counts, expected",
    [((10, 20), True), ((3, 8), True), ((3, 7), True), ((2, 8), False)],
    ids=["preserved_ratio", "same_uncovered", "fewer_uncovered", "regression"],
)
def test_non_regression_preserves_ratio_or_uncovered_count(
    tmp_path: Path, metric: str, counts: tuple[int, int], expected: bool
) -> None:
    parent, candidate = tmp_path / "parent.json", tmp_path / "candidate.json"
    write_report(
        parent,
        lines=(5, 10) if metric == "lines" else (100, 100),
        branches=(5, 10) if metric == "branches" else (100, 100),
        functions=(5, 10) if metric == "functions" else (1, 1),
    )
    write_report(
        candidate,
        lines=counts if metric == "lines" else (100, 100),
        branches=counts if metric == "branches" else (100, 100),
        functions=counts if metric == "functions" else (1, 1),
    )
    assert verify_non_regression(candidate, parent) is expected


@pytest.mark.parametrize("boundary", ["report", "candidate_baseline", "parent_baseline"])
def test_coverage_rejects_excluded_lines(tmp_path: Path, boundary: str) -> None:
    parent, candidate = tmp_path / "parent.json", tmp_path / "candidate.json"
    write_report(parent, lines=(100, 100), branches=(100, 100), excluded_lines=int(boundary == "parent_baseline"))
    write_report(candidate, lines=(100, 100), branches=(100, 100), excluded_lines=int(boundary != "parent_baseline"))
    with pytest.raises(ValueError, match="Excluded lines"):
        if boundary == "report":
            verify_coverage(candidate)
        else:
            verify_non_regression(candidate, parent)


@pytest.mark.parametrize(
    "field, value", [("format", 2), ("branch_coverage", False), ("version", "other"), ("version", None)]
)
def test_incompatible_parent_report_is_rejected(tmp_path: Path, field: str, value: object) -> None:
    parent, candidate = tmp_path / "parent.json", tmp_path / "candidate.json"
    write_report(candidate, lines=(100, 100), branches=(100, 100))
    report = json.loads(candidate.read_text())
    report["meta"][field] = value
    parent.write_text(json.dumps(report))
    with pytest.raises(ValueError, match="Regenerate both reports"):
        verify_non_regression(candidate, parent)


@pytest.mark.parametrize("outcome", ["passed", "skipped", "xfailed", "xpassed", "deselected"])
def test_release_check_rejects_incomplete_tests(tmp_path: Path, outcome: str) -> None:
    test = tmp_path / "test_release.py"
    body = {"skipped": "pytest.skip('unavailable')", "xfailed": "pytest.xfail('known failure')"}.get(
        outcome, "assert True"
    )
    marker = "@pytest.mark.xfail\n" if outcome == "xpassed" else ""
    deselected = "\ndef test_omitted():\n    assert False\n" if outcome == "deselected" else ""
    test.write_text(f"import pytest\n{marker}def test_example():\n    {body}\n{deselected}")
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            "-p",
            "scripts.verify_coverage",
            "--noconftest",
            "-o",
            "addopts=",
            "-q",
            "-k",
            "test_example",
            str(test),
        ],
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
    )
    assert result.returncode == int(outcome != "passed"), result.stdout + result.stderr
    assert ("prevent release validation" in result.stdout) is (outcome != "passed")
