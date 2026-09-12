# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from pathlib import Path
from importlib import import_module

import pytest

formatter = import_module("scripts.utils.ruffen-docs")


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ("Plain text\n", "Plain text\n"),
        ("```python\nx=1\n```\n", "```python\nx = 1\n```\n"),
        ("  ```python\n  x=1\n  ```\n", "  ```python\n  x = 1\n  ```\n"),
        ("```pycon\n>>> x=1\n>>> x\n1\n```\n", "```pycon\n>>> x = 1\n>>> x\n1\n```\n"),
        ("```pycon\n>>> \n```\n", "```pycon\n>>> \n```\n"),
        ("```javascript\nx=1\n```\n", "```javascript\nx=1\n```\n"),
    ],
)
def test_document_formatting(source: str, expected: str) -> None:
    formatted, errors = formatter.format_str(source)
    assert (formatted, errors) == (expected, [])
    assert formatter.format_str(formatted) == (expected, [])


def test_invalid_blocks_prevent_partial_writes(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    source = "```python\nx=1\n```\n\n```python\ndef broken(\n```\n\n```pycon\n>>> if :\n```\n"
    path = tmp_path / "example.md"
    path.write_text(source)
    assert formatter.main([str(path)]) == 1
    assert path.read_text() == source
    output = capsys.readouterr().out
    assert f"{path}:5: code block parse error" in output
    assert f"{path}:9: code block parse error" in output
    assert formatter.main(["--skip-errors", str(path)]) == 0
    assert path.read_text() == source.replace("x=1", "x = 1")


def test_cli_options_reach_ruff(tmp_path: Path) -> None:
    path = tmp_path / "example.md"
    source = "```python\nvalue = call('first argument', 'second argument', 'third argument')\n```\n"
    path.write_text(source)
    assert formatter.main(["--line-length", "30", "--skip-string-normalization", str(path)]) == 0
    assert "call(\n" in path.read_text()
    assert "'first argument'" in path.read_text()
    assert formatter.main([str(path)]) == 0
    assert '"first argument"' in path.read_text()
    assert formatter.main([]) == 0


@pytest.mark.parametrize(
    "source, result",
    [("```python\nx=1\n```\n", 1), ("```python\nx = 1\n```\n", 0), ("```python\ndef broken(\n```\n", 1)],
)
def test_check_never_rewrites_documents(tmp_path: Path, source: str, result: int) -> None:
    path = tmp_path / "example.md"
    path.write_text(source)
    assert formatter.main(["--check", str(path)]) == result
    assert path.read_text() == source
