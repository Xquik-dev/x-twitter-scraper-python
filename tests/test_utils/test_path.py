# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Any

import pytest

from x_twitter_scraper._utils._path import path_template


@pytest.mark.parametrize(
    "template, kwargs, expected",
    [
        ("/v1/{id}", dict(id="abc"), "/v1/abc"),
        ("/v1/{a}/{b}", dict(a="x", b="y"), "/v1/x/y"),
        ("/v1/{a}{b}/path/{c}?val={d}#{e}", dict(a="x", b="y", c="z", d="u", e="v"), "/v1/xy/path/z?val=u#v"),
        ("/{w}/{w}", dict(w="echo"), "/echo/echo"),
        ("/v1/static", {}, "/v1/static"),
        ("", {}, ""),
        ("/v1/?q={n}&count=10", dict(n=42), "/v1/?q=42&count=10"),
        ("/v1/{v}", dict(v=None), "/v1/null"),
        ("/v1/{v}", dict(v=True), "/v1/true"),
        ("/v1/{v}", dict(v=False), "/v1/false"),
        ("/v1/{v}", dict(v=".hidden"), "/v1/.hidden"),
        ("/v1/{v}", dict(v="file.txt"), "/v1/file.txt"),
        ("/v1/{v}", dict(v="..."), "/v1/..."),
        ("/v1/{a}{b}", dict(a=".", b="txt"), "/v1/.txt"),
        ("/items?q={v}#{f}", dict(v=".", f=".."), "/items?q=.#.."),
        (
            "/v1/{a}?query={b}",
            dict(a="../../other/endpoint", b="a&bad=true"),
            "/v1/..%2F..%2Fother%2Fendpoint?query=a%26bad%3Dtrue",
        ),
        ("/v1/{val}", dict(val="a/b/c"), "/v1/a%2Fb%2Fc"),
        ("/v1/{val}", dict(val="a/b/c?query=value"), "/v1/a%2Fb%2Fc%3Fquery=value"),
        ("/v1/{val}", dict(val="a/b/c?query=value&bad=true"), "/v1/a%2Fb%2Fc%3Fquery=value&bad=true"),
        ("/v1/{val}", dict(val="%20"), "/v1/%2520"),
        ("/items?q={v}", dict(v="a/b"), "/items?q=a/b"),
        ("/items?q={v}", dict(v="a?b"), "/items?q=a?b"),
        ("/items?q={v}", dict(v="a#b"), "/items?q=a%23b"),
        ("/items?q={v}", dict(v="a b"), "/items?q=a%20b"),
        ("/docs#{v}", dict(v="a/b"), "/docs#a/b"),
        ("/docs#{v}", dict(v="a?b"), "/docs#a?b"),
        ("/v1/{v}", dict(v="a/b"), "/v1/a%2Fb"),
        ("/v1/{v}", dict(v="a?b"), "/v1/a%3Fb"),
        ("/v1/{v}", dict(v="a#b"), "/v1/a%23b"),
        (
            "/v1/{v}?q={v}#{v}",
            dict(v="a/b?c#d"),
            "/v1/a%2Fb%3Fc%23d?q=a/b?c%23d#a/b?c%23d",
        ),
        ("/v1/{val}", dict(val="x?admin=true"), "/v1/x%3Fadmin=true"),
        ("/v1/{val}", dict(val="x#admin"), "/v1/x%23admin"),
    ],
)
def test_interpolation(template: str, kwargs: dict[str, Any], expected: str) -> None:
    assert path_template(template, **kwargs) == expected


def test_missing_kwarg_raises_key_error() -> None:
    with pytest.raises(KeyError, match="org_id"):
        path_template("/v1/{org_id}")


@pytest.mark.parametrize(
    "template, kwargs",
    [
        ("{a}/path", dict(a=".")),
        ("{a}/path", dict(a="..")),
        ("/v1/{a}", dict(a=".")),
        ("/v1/{a}", dict(a="..")),
        ("/v1/{a}/path", dict(a=".")),
        ("/v1/{a}/path", dict(a="..")),
        ("/v1/{a}{b}", dict(a=".", b=".")),
        ("/v1/{a}.", dict(a=".")),
        ("/v1/{a}{b}", dict(a="", b=".")),
        ("/v1/%2e/{x}", dict(x="ok")),
        ("/v1/%2e./{x}", dict(x="ok")),
        ("/v1/.%2E/{x}", dict(x="ok")),
        ("/v1/{v}?q=1", dict(v="..")),
        ("/v1/{v}#frag", dict(v="..")),
    ],
)
def test_dot_segment_rejected(template: str, kwargs: dict[str, Any]) -> None:
    with pytest.raises(ValueError, match="dot-segment"):
        path_template(template, **kwargs)
