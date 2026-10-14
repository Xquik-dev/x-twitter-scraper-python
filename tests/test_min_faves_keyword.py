# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Any, Dict

import httpx
import pytest

from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper

MESSAGE = r"min_faves is deprecated & goes away in a later minor version\. Use min_likes\."

CALLS = [
    pytest.param("tweets", "search", {"q": "xquik"}, "/api/v1/x/tweets/search", id="search"),
    pytest.param("tweets", "get_quotes", {"id": "123"}, "/api/v1/x/tweets/123/quotes", id="quotes"),
    pytest.param("tweets", "get_replies", {"id": "123"}, "/api/v1/x/tweets/123/replies", id="replies"),
    pytest.param("tweets", "get_thread", {"id": "123"}, "/api/v1/x/tweets/123/thread", id="thread"),
    pytest.param("users", "retrieve_likes", {"id": "44"}, "/api/v1/x/users/44/likes", id="likes"),
    pytest.param("users", "retrieve_media", {"id": "44"}, "/api/v1/x/users/44/media", id="media"),
    pytest.param("users", "retrieve_mentions", {"id": "44"}, "/api/v1/x/users/44/mentions", id="mentions"),
    pytest.param("users", "retrieve_replies", {"id": "44"}, "/api/v1/x/users/44/replies", id="user-replies"),
    pytest.param("users", "retrieve_tweets", {"id": "44"}, "/api/v1/x/users/44/tweets", id="tweets"),
]


async def send(
    resource: str, method: str, arguments: Dict[str, str], asynchronous: bool, **keywords: int
) -> httpx.Request:
    requests: list[httpx.Request] = []

    def respond(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json={"tweets": [], "has_next_page": False, "next_cursor": ""})

    transport = httpx.MockTransport(respond)
    if asynchronous:
        async with AsyncXTwitterScraper(
            api_key="isolated-test", http_client=httpx.AsyncClient(transport=transport)
        ) as client:
            call: Any = getattr(getattr(client.x, resource), method)
            await call(**arguments, **keywords)
    else:
        with XTwitterScraper(api_key="isolated-test", http_client=httpx.Client(transport=transport)) as sync_client:
            sync_call: Any = getattr(getattr(sync_client.x, resource), method)
            sync_call(**arguments, **keywords)
    assert len(requests) == 1
    return requests[0]


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize(("resource", "method", "arguments", "path"), CALLS)
async def test_min_faves_sends_what_min_likes_sends(
    resource: str, method: str, arguments: Dict[str, str], path: str, asynchronous: bool
) -> None:
    current = await send(resource, method, arguments, asynchronous, min_likes=25)
    with pytest.warns(DeprecationWarning, match=MESSAGE) as record:
        deprecated = await send(resource, method, arguments, asynchronous, min_faves=25)

    assert record[0].filename == __file__
    assert current.url.path == path
    assert current.url.params["minLikes"] == "25"
    assert deprecated.url == current.url
    assert deprecated.method == current.method


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize(("resource", "method", "arguments", "path"), CALLS)
async def test_min_likes_wins_over_min_faves(
    resource: str, method: str, arguments: Dict[str, str], path: str, asynchronous: bool
) -> None:
    with pytest.warns(DeprecationWarning, match=MESSAGE):
        request = await send(resource, method, arguments, asynchronous, min_likes=50, min_faves=25)

    assert request.url.path == path
    assert request.url.params.get_list("minLikes") == ["50"]
    assert "minFaves" not in request.url.params
