# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTweets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: XTwitterScraper) -> None:
        tweet = client.x.communities.tweets.list(
            q="q",
        )
        assert tweet is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: XTwitterScraper) -> None:
        tweet = client.x.communities.tweets.list(
            q="q",
            cursor="cursor",
            query_type="queryType",
        )
        assert tweet is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: XTwitterScraper) -> None:
        response = client.x.communities.tweets.with_raw_response.list(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = response.parse()
        assert tweet is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: XTwitterScraper) -> None:
        with client.x.communities.tweets.with_streaming_response.list(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = response.parse()
            assert tweet is None

        assert cast(Any, response.is_closed) is True


class TestAsyncTweets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.communities.tweets.list(
            q="q",
        )
        assert tweet is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.communities.tweets.list(
            q="q",
            cursor="cursor",
            query_type="queryType",
        )
        assert tweet is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.communities.tweets.with_raw_response.list(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = await response.parse()
        assert tweet is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.communities.tweets.with_streaming_response.list(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = await response.parse()
            assert tweet is None

        assert cast(Any, response.is_closed) is True
