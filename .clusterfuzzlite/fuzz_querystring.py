# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import sys

import atheris

with atheris.instrument_imports():
    from x_twitter_scraper._qs import Querystring


_ARRAY_FORMATS = ("comma", "repeat", "indices", "brackets")
_NESTED_FORMATS = ("dots", "brackets")


def fuzz_querystring(data: bytes) -> None:
    if len(data) > 4096:
        return

    text = data.decode("utf-8", errors="replace")
    selector = data[0] if data else 0
    querystring = Querystring(
        array_format=_ARRAY_FORMATS[selector % len(_ARRAY_FORMATS)],
        nested_format=_NESTED_FORMATS[selector % len(_NESTED_FORMATS)],
    )
    params = {
        "raw": text,
        "items": [text, selector, bool(selector & 1), None],
        "nested": {"value": text},
    }

    querystring.parse(text)
    querystring.parse(querystring.stringify(params))


atheris.Setup(sys.argv, fuzz_querystring)
atheris.Fuzz()
