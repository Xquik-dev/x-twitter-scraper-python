from __future__ import annotations

import sys
from typing import NoReturn, Protocol, cast
from importlib import import_module
from contextlib import AbstractContextManager
from collections.abc import Callable, Sequence


class _Atheris(Protocol):
    def instrument_imports(self) -> AbstractContextManager[None]: ...

    def Setup(self, argv: Sequence[str], callback: Callable[[bytes], None]) -> None: ...

    def Fuzz(self) -> NoReturn: ...


atheris = cast(_Atheris, import_module("atheris"))

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
