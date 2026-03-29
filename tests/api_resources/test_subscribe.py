# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types import SubscribeCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscribe:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: XTwitterScraper) -> None:
        subscribe = client.subscribe.create()
        assert_matches_type(SubscribeCreateResponse, subscribe, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: XTwitterScraper) -> None:
        response = client.subscribe.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscribe = response.parse()
        assert_matches_type(SubscribeCreateResponse, subscribe, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: XTwitterScraper) -> None:
        with client.subscribe.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscribe = response.parse()
            assert_matches_type(SubscribeCreateResponse, subscribe, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSubscribe:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncXTwitterScraper) -> None:
        subscribe = await async_client.subscribe.create()
        assert_matches_type(SubscribeCreateResponse, subscribe, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.subscribe.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscribe = await response.parse()
        assert_matches_type(SubscribeCreateResponse, subscribe, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.subscribe.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscribe = await response.parse()
            assert_matches_type(SubscribeCreateResponse, subscribe, path=["response"])

        assert cast(Any, response.is_closed) is True
