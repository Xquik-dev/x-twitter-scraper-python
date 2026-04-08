# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types import (
    XGetTrendsResponse,
    XGetArticleResponse,
    XGetNotificationsResponse,
)
from x_twitter_scraper.types.shared import PaginatedTweets

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestX:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_article(self, client: XTwitterScraper) -> None:
        x = client.x.get_article(
            "tweetId",
        )
        assert_matches_type(XGetArticleResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_article(self, client: XTwitterScraper) -> None:
        response = client.x.with_raw_response.get_article(
            "tweetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        x = response.parse()
        assert_matches_type(XGetArticleResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_article(self, client: XTwitterScraper) -> None:
        with client.x.with_streaming_response.get_article(
            "tweetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            x = response.parse()
            assert_matches_type(XGetArticleResponse, x, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_article(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tweet_id` but received ''"):
            client.x.with_raw_response.get_article(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_home_timeline(self, client: XTwitterScraper) -> None:
        x = client.x.get_home_timeline()
        assert_matches_type(PaginatedTweets, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_home_timeline_with_all_params(self, client: XTwitterScraper) -> None:
        x = client.x.get_home_timeline(
            cursor="cursor",
            seen_tweet_ids="seenTweetIds",
        )
        assert_matches_type(PaginatedTweets, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_home_timeline(self, client: XTwitterScraper) -> None:
        response = client.x.with_raw_response.get_home_timeline()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        x = response.parse()
        assert_matches_type(PaginatedTweets, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_home_timeline(self, client: XTwitterScraper) -> None:
        with client.x.with_streaming_response.get_home_timeline() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            x = response.parse()
            assert_matches_type(PaginatedTweets, x, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_notifications(self, client: XTwitterScraper) -> None:
        x = client.x.get_notifications()
        assert_matches_type(XGetNotificationsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_notifications_with_all_params(self, client: XTwitterScraper) -> None:
        x = client.x.get_notifications(
            cursor="cursor",
            type="All",
        )
        assert_matches_type(XGetNotificationsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_notifications(self, client: XTwitterScraper) -> None:
        response = client.x.with_raw_response.get_notifications()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        x = response.parse()
        assert_matches_type(XGetNotificationsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_notifications(self, client: XTwitterScraper) -> None:
        with client.x.with_streaming_response.get_notifications() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            x = response.parse()
            assert_matches_type(XGetNotificationsResponse, x, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_trends(self, client: XTwitterScraper) -> None:
        x = client.x.get_trends()
        assert_matches_type(XGetTrendsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_trends(self, client: XTwitterScraper) -> None:
        response = client.x.with_raw_response.get_trends()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        x = response.parse()
        assert_matches_type(XGetTrendsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_trends(self, client: XTwitterScraper) -> None:
        with client.x.with_streaming_response.get_trends() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            x = response.parse()
            assert_matches_type(XGetTrendsResponse, x, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncX:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_article(self, async_client: AsyncXTwitterScraper) -> None:
        x = await async_client.x.get_article(
            "tweetId",
        )
        assert_matches_type(XGetArticleResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_article(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.with_raw_response.get_article(
            "tweetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        x = await response.parse()
        assert_matches_type(XGetArticleResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_article(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.with_streaming_response.get_article(
            "tweetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            x = await response.parse()
            assert_matches_type(XGetArticleResponse, x, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_article(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tweet_id` but received ''"):
            await async_client.x.with_raw_response.get_article(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_home_timeline(self, async_client: AsyncXTwitterScraper) -> None:
        x = await async_client.x.get_home_timeline()
        assert_matches_type(PaginatedTweets, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_home_timeline_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        x = await async_client.x.get_home_timeline(
            cursor="cursor",
            seen_tweet_ids="seenTweetIds",
        )
        assert_matches_type(PaginatedTweets, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_home_timeline(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.with_raw_response.get_home_timeline()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        x = await response.parse()
        assert_matches_type(PaginatedTweets, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_home_timeline(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.with_streaming_response.get_home_timeline() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            x = await response.parse()
            assert_matches_type(PaginatedTweets, x, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_notifications(self, async_client: AsyncXTwitterScraper) -> None:
        x = await async_client.x.get_notifications()
        assert_matches_type(XGetNotificationsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_notifications_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        x = await async_client.x.get_notifications(
            cursor="cursor",
            type="All",
        )
        assert_matches_type(XGetNotificationsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_notifications(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.with_raw_response.get_notifications()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        x = await response.parse()
        assert_matches_type(XGetNotificationsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_notifications(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.with_streaming_response.get_notifications() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            x = await response.parse()
            assert_matches_type(XGetNotificationsResponse, x, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_trends(self, async_client: AsyncXTwitterScraper) -> None:
        x = await async_client.x.get_trends()
        assert_matches_type(XGetTrendsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_trends(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.with_raw_response.get_trends()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        x = await response.parse()
        assert_matches_type(XGetTrendsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_trends(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.with_streaming_response.get_trends() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            x = await response.parse()
            assert_matches_type(XGetTrendsResponse, x, path=["response"])

        assert cast(Any, response.is_closed) is True
