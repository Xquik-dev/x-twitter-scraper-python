# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import httpx
import pytest
from respx import MockRouter

from tests.conftest import base_url
from x_twitter_scraper import XTwitterScraper


@pytest.mark.respx(base_url=base_url)
def test_readme_quickstart_search(respx_mock: MockRouter) -> None:
    route = respx_mock.get("/x/tweets/search").mock(
        return_value=httpx.Response(
            200,
            json={
                "has_next_page": False,
                "next_cursor": "",
                "tweets": [
                    {
                        "id": "1",
                        "bookmarkCount": 0,
                        "likeCount": 42,
                        "quoteCount": 1,
                        "replyCount": 2,
                        "retweetCount": 3,
                        "text": "Hello from Elon",
                        "viewCount": 100,
                    }
                ],
            },
        )
    )

    with XTwitterScraper(
        base_url=base_url,
        api_key="My API Key",
        bearer_token="My Bearer Token",
    ) as client:
        result = client.x.tweets.search(
            q="from:elonmusk",
            limit=10,
        )

    assert route.called

    request = route.calls.last.request

    assert request.method == "GET"
    assert request.url.path == "/x/tweets/search"
    assert request.url.params["q"] == "from:elonmusk"
    assert request.url.params["limit"] == "10"

    assert result.has_next_page is False
    assert len(result.tweets) == 1
    assert result.tweets[0].text == "Hello from Elon"
