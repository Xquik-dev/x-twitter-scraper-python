# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import re
import ast
import sys
import doctest
import argparse
import textwrap
import subprocess
from typing import Sequence, NamedTuple
from pathlib import Path

CODE_BLOCK = re.compile(
    r"^(?P<indent> *)```\s*(?P<language>python|pycon)\n(?P<code>.*?)^(?P=indent)```[^\n]*$",
    re.DOTALL | re.MULTILINE,
)


class CodeBlockError(NamedTuple):
    offset: int
    exc: Exception


def format_str(
    src: str, line_length: int | None = None, skip_string_normalization: bool = False
) -> tuple[str, Sequence[CodeBlockError]]:
    errors: list[CodeBlockError] = []
    for match in CODE_BLOCK.finditer(src):
        code = textwrap.dedent(match["code"])
        try:
            fragments = (
                [example.source for example in doctest.DocTestParser().get_examples(code)]
                if match["language"] == "pycon"
                else [code]
            )
            for fragment in fragments:
                ast.parse(fragment)
        except (SyntaxError, ValueError) as error:
            errors.append(CodeBlockError(match.start(), error))
    command = [sys.executable, "-m", "ruff", "format", "--stdin-filename=README.md"]
    if line_length is not None:
        command.append(f"--line-length={line_length}")
    if skip_string_normalization:
        command.extend(["--config", 'format.quote-style="preserve"'])
    return subprocess.check_output(command, encoding="utf-8", input=src), errors


def format_file(
    filename: str,
    skip_errors: bool,
    line_length: int | None = None,
    skip_string_normalization: bool = False,
    check: bool = False,
) -> int:
    path = Path(filename)
    contents = path.read_text(encoding="utf-8")
    new_contents, errors = format_str(contents, line_length, skip_string_normalization)
    for error in errors:
        lineno = contents[: error.offset].count("\n") + 1
        print(f"{filename}:{lineno}: code block parse error {error.exc}")
    if errors and not skip_errors:
        return 1
    if contents != new_contents:
        if check:
            print(f"{filename}: Needs formatting. Run scripts/format.")
            return 1
        print(f"{filename}: Rewriting...")
        path.write_text(new_contents, encoding="utf-8")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--line-length", type=int)
    parser.add_argument("-S", "--skip-string-normalization", action="store_true")
    parser.add_argument("-E", "--skip-errors", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args(argv)
    retv = 0
    for filename in args.filenames:
        retv |= format_file(filename, args.skip_errors, args.line_length, args.skip_string_normalization, args.check)
    return retv


if __name__ == "__main__":
    raise SystemExit(main())
