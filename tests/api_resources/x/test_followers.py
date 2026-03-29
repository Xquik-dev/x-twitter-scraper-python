# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types.x import FollowerRetrieveCheckResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFollowers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_check(self, client: XTwitterScraper) -> None:
        follower = client.x.followers.retrieve_check(
            source="source",
            target="target",
        )
        assert_matches_type(FollowerRetrieveCheckResponse, follower, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_check(self, client: XTwitterScraper) -> None:
        response = client.x.followers.with_raw_response.retrieve_check(
            source="source",
            target="target",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        follower = response.parse()
        assert_matches_type(FollowerRetrieveCheckResponse, follower, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_check(self, client: XTwitterScraper) -> None:
        with client.x.followers.with_streaming_response.retrieve_check(
            source="source",
            target="target",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            follower = response.parse()
            assert_matches_type(FollowerRetrieveCheckResponse, follower, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFollowers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_check(self, async_client: AsyncXTwitterScraper) -> None:
        follower = await async_client.x.followers.retrieve_check(
            source="source",
            target="target",
        )
        assert_matches_type(FollowerRetrieveCheckResponse, follower, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_check(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.followers.with_raw_response.retrieve_check(
            source="source",
            target="target",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        follower = await response.parse()
        assert_matches_type(FollowerRetrieveCheckResponse, follower, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_check(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.followers.with_streaming_response.retrieve_check(
            source="source",
            target="target",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            follower = await response.parse()
            assert_matches_type(FollowerRetrieveCheckResponse, follower, path=["response"])

        assert cast(Any, response.is_closed) is True
