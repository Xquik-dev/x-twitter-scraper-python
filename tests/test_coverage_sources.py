# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

import json
from pathlib import Path

import pytest

from scripts.coverage_sources import git, attach, snapshot, verify_parent


def test_coverage_binds_to_committed_sources(tmp_path: Path) -> None:
    git(tmp_path, "init", "-q")
    source = tmp_path / "example.py"
    source.write_text("value = 1\n")
    git(tmp_path, "add", "example.py")
    git(tmp_path, "-c", "user.name=Test", "-c", "user.email=test@example.invalid", "commit", "-qm", "fixture")
    before, report = tmp_path / "before.json", tmp_path / "report.json"
    before.write_text(json.dumps(snapshot(tmp_path)))
    report.write_text(json.dumps({"files": {"example.py": {}}}))
    attach(report, before, tmp_path)
    assert verify_parent(report, tmp_path, "HEAD") is None
    source.write_text("value = 2\n")
    with pytest.raises(ValueError, match="Sources changed"):
        attach(report, before, tmp_path)
    before.write_text(json.dumps(snapshot(tmp_path)))
    attach(report, before, tmp_path)
    with pytest.raises(ValueError, match="does not match"):
        verify_parent(report, tmp_path, "HEAD")
    (tmp_path / "new.py").write_text("value = 3\n")
    before.write_text(json.dumps(snapshot(tmp_path)))
    with pytest.raises(ValueError, match="omitted Python files"):
        attach(report, before, tmp_path)
    source.unlink()
    assert set(snapshot(tmp_path)["sources"]) == {"new.py"}
