# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types import BotTrackUsageResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBot:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_track_usage(self, client: XTwitterScraper) -> None:
        bot = client.bot.track_usage(
            input_tokens=0,
            output_tokens=0,
            platform_user_id="platformUserId",
        )
        assert_matches_type(BotTrackUsageResponse, bot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_track_usage(self, client: XTwitterScraper) -> None:
        response = client.bot.with_raw_response.track_usage(
            input_tokens=0,
            output_tokens=0,
            platform_user_id="platformUserId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = response.parse()
        assert_matches_type(BotTrackUsageResponse, bot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_track_usage(self, client: XTwitterScraper) -> None:
        with client.bot.with_streaming_response.track_usage(
            input_tokens=0,
            output_tokens=0,
            platform_user_id="platformUserId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = response.parse()
            assert_matches_type(BotTrackUsageResponse, bot, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBot:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_track_usage(self, async_client: AsyncXTwitterScraper) -> None:
        bot = await async_client.bot.track_usage(
            input_tokens=0,
            output_tokens=0,
            platform_user_id="platformUserId",
        )
        assert_matches_type(BotTrackUsageResponse, bot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_track_usage(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.bot.with_raw_response.track_usage(
            input_tokens=0,
            output_tokens=0,
            platform_user_id="platformUserId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bot = await response.parse()
        assert_matches_type(BotTrackUsageResponse, bot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_track_usage(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.bot.with_streaming_response.track_usage(
            input_tokens=0,
            output_tokens=0,
            platform_user_id="platformUserId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bot = await response.parse()
            assert_matches_type(BotTrackUsageResponse, bot, path=["response"])

        assert cast(Any, response.is_closed) is True
