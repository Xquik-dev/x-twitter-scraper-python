#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import sys
import json
from typing import cast
from pathlib import Path
from collections.abc import Mapping

THRESHOLDS = (
    ("Statement", "covered_lines", "num_statements", 90),
    ("Branch", "covered_branches", "num_branches", 80),
)


def _integer(mapping: Mapping[str, object], key: str) -> int:
    value = mapping.get(key)
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"Coverage report field {key!r} must be an integer. Regenerate coverage.")
    return value


def verify_coverage(report_path: Path) -> bool:
    payload = cast(object, json.loads(report_path.read_text(encoding="utf-8")))
    if not isinstance(payload, Mapping):
        raise ValueError("Coverage report root must be an object. Regenerate coverage.")
    report = cast(Mapping[str, object], payload)
    totals_value = report.get("totals")
    if not isinstance(totals_value, Mapping):
        raise ValueError("Coverage report lacks totals. Regenerate coverage.")
    totals = cast(Mapping[str, object], totals_value)

    passed = True
    for label, covered_key, total_key, minimum in THRESHOLDS:
        covered = _integer(totals, covered_key)
        total = _integer(totals, total_key)
        if total <= 0:
            raise ValueError("Coverage report has no measurable items. Regenerate coverage.")
        percent = covered * 100 / total
        print(f"{label} coverage: {covered}/{total} ({percent:.2f}%); minimum {minimum:.2f}%")
        passed = covered * 100 >= total * minimum and passed
    return passed


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: verify_coverage.py COVERAGE_JSON", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(0 if verify_coverage(Path(sys.argv[1])) else 1)
