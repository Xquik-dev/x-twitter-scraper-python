# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types import RadarRetrieveTrendingTopicsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRadar:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_trending_topics(self, client: XTwitterScraper) -> None:
        radar = client.radar.retrieve_trending_topics()
        assert_matches_type(RadarRetrieveTrendingTopicsResponse, radar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_trending_topics_with_all_params(self, client: XTwitterScraper) -> None:
        radar = client.radar.retrieve_trending_topics(
            category="category",
            count=0,
            hours=0,
            region="region",
            source="github",
        )
        assert_matches_type(RadarRetrieveTrendingTopicsResponse, radar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_trending_topics(self, client: XTwitterScraper) -> None:
        response = client.radar.with_raw_response.retrieve_trending_topics()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        radar = response.parse()
        assert_matches_type(RadarRetrieveTrendingTopicsResponse, radar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_trending_topics(self, client: XTwitterScraper) -> None:
        with client.radar.with_streaming_response.retrieve_trending_topics() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            radar = response.parse()
            assert_matches_type(RadarRetrieveTrendingTopicsResponse, radar, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRadar:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_trending_topics(self, async_client: AsyncXTwitterScraper) -> None:
        radar = await async_client.radar.retrieve_trending_topics()
        assert_matches_type(RadarRetrieveTrendingTopicsResponse, radar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_trending_topics_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        radar = await async_client.radar.retrieve_trending_topics(
            category="category",
            count=0,
            hours=0,
            region="region",
            source="github",
        )
        assert_matches_type(RadarRetrieveTrendingTopicsResponse, radar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_trending_topics(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.radar.with_raw_response.retrieve_trending_topics()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        radar = await response.parse()
        assert_matches_type(RadarRetrieveTrendingTopicsResponse, radar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_trending_topics(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.radar.with_streaming_response.retrieve_trending_topics() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            radar = await response.parse()
            assert_matches_type(RadarRetrieveTrendingTopicsResponse, radar, path=["response"])

        assert cast(Any, response.is_closed) is True
