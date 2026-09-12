# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import Any, cast
from decimal import Decimal
from datetime import date
from functools import partial
from urllib.parse import unquote

import pytest

from x_twitter_scraper._qs import Querystring, parse, stringify
from x_twitter_scraper._types import ArrayFormat


def test_empty() -> None:
    assert stringify({}) == ""
    assert stringify({"a": {}}) == ""
    assert stringify({"a": {"b": {"c": {}}}}) == ""


def test_basic() -> None:
    assert stringify({"a": 1}) == "a=1"
    assert stringify({"a": "b"}) == "a=b"
    assert stringify({"a": True}) == "a=true"
    assert stringify({"a": False}) == "a=false"
    assert stringify({"a": 1.23456}) == "a=1.23456"
    assert stringify({"a": None}) == ""


def test_query_preserves_stringifiable_values() -> None:
    assert unquote(stringify({"date": date(2026, 9, 12), "nested": {"amount": Decimal("1.20")}})) == (
        "date=2026-09-12&nested[amount]=1.20"
    )


@pytest.mark.parametrize("method", ["class", "function"])
def test_nested_dotted(method: str) -> None:
    if method == "class":
        serialise = Querystring(nested_format="dots").stringify
    else:
        serialise = partial(stringify, nested_format="dots")

    assert unquote(serialise({"a": {"b": "c"}})) == "a.b=c"
    assert unquote(serialise({"a": {"b": "c", "d": "e", "f": "g"}})) == "a.b=c&a.d=e&a.f=g"
    assert unquote(serialise({"a": {"b": {"c": {"d": "e"}}}})) == "a.b.c.d=e"
    assert unquote(serialise({"a": {"b": True}})) == "a.b=true"


def test_nested_brackets() -> None:
    assert unquote(stringify({"a": {"b": "c"}})) == "a[b]=c"
    assert unquote(stringify({"a": {"b": "c", "d": "e", "f": "g"}})) == "a[b]=c&a[d]=e&a[f]=g"
    assert unquote(stringify({"a": {"b": {"c": {"d": "e"}}}})) == "a[b][c][d]=e"
    assert unquote(stringify({"a": {"b": True}})) == "a[b]=true"


@pytest.mark.parametrize("method", ["class", "function"])
@pytest.mark.parametrize(
    "array_format,flat,nested,nullable",
    [
        ("comma", "in=foo,bar", "a[b]=true,false", "a[b]=true,false,true"),
        ("repeat", "in=foo&in=bar", "a[b]=true&a[b]=false", "a[b]=true&a[b]=false&a[b]=true"),
        ("brackets", "in[]=foo&in[]=bar", "a[b][]=true&a[b][]=false", "a[b][]=true&a[b][]=false&a[b][]=true"),
        ("indices", "in[0]=foo&in[1]=bar", "a[b][0]=true&a[b][1]=false", "a[b][0]=true&a[b][1]=false&a[b][3]=true"),
    ],
)
def test_array_formats(method: str, array_format: ArrayFormat, flat: str, nested: str, nullable: str) -> None:
    if method == "class":
        serialise = Querystring(array_format=array_format).stringify
    else:
        serialise = partial(stringify, array_format=array_format)

    assert unquote(serialise({"in": ["foo", "bar"]})) == flat
    assert unquote(serialise({"in": ("foo", "bar")})) == flat
    assert unquote(serialise({"a": {"b": [True, False]}})) == nested
    assert unquote(serialise({"a": {"b": (True, False)}})) == nested
    assert unquote(serialise({"a": {"b": [True, False, None, True]}})) == nullable


def test_array_repeat_defaults() -> None:
    assert unquote(stringify({"in": ["foo", "bar"]})) == "in=foo&in=bar"
    assert unquote(stringify({"a": {"b": [True, False]}})) == "a[b]=true&a[b]=false"
    assert unquote(stringify({"a": {"b": [True, False, None, True]}})) == "a[b]=true&a[b]=false&a[b]=true"
    assert unquote(stringify({"in": ["foo", {"b": {"c": ["d", "e"]}}]})) == "in=foo&in[b][c]=d&in[b][c]=e"


def test_unknown_array_format() -> None:
    with pytest.raises(NotImplementedError, match="Unknown array_format value: foo, choose from comma, repeat"):
        stringify({"a": ["foo", "bar"]}, array_format=cast(Any, "foo"))


def test_array_indices() -> None:
    assert unquote(stringify({"items": ["foo", "bar"]}, array_format="indices")) == "items[0]=foo&items[1]=bar"


def test_parse() -> None:
    assert parse("item=foo&item=bar") == {"item": ["foo", "bar"]}
