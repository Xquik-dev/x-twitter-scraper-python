# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types import (
    XGetTrendsResponse,
    XGetArticleResponse,
    XGetHashflagsResponse,
    XSearchPlacesResponse,
    XGetNotificationsResponse,
    XGetTrendsHistoryResponse,
    XGetTrendLocationsResponse,
    XAutocompleteSearchResponse,
    XGetNewsStoryVersionsResponse,
)
from x_twitter_scraper.types.shared import PaginatedTweets

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestX:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_autocomplete_search(self, client: XTwitterScraper) -> None:
        x = client.x.autocomplete_search(
            q="nasa",
        )
        assert_matches_type(XAutocompleteSearchResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_autocomplete_search_with_all_params(self, client: XTwitterScraper) -> None:
        x = client.x.autocomplete_search(
            q="nasa",
            fields="id,text,author.username",
            limit=1,
            omit="entities,media",
            types="users,topics",
        )
        assert_matches_type(XAutocompleteSearchResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_autocomplete_search(self, client: XTwitterScraper) -> None:
        response = client.x.with_raw_response.autocomplete_search(
            q="nasa",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        x = response.parse()
        assert_matches_type(XAutocompleteSearchResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_autocomplete_search(self, client: XTwitterScraper) -> None:
        with client.x.with_streaming_response.autocomplete_search(
            q="nasa",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            x = response.parse()
            assert_matches_type(XAutocompleteSearchResponse, x, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_article(self, client: XTwitterScraper) -> None:
        x = client.x.get_article(
            tweet_id="tweetId",
        )
        assert_matches_type(XGetArticleResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_article_with_all_params(self, client: XTwitterScraper) -> None:
        x = client.x.get_article(
            tweet_id="tweetId",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(XGetArticleResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_article(self, client: XTwitterScraper) -> None:
        response = client.x.with_raw_response.get_article(
            tweet_id="tweetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        x = response.parse()
        assert_matches_type(XGetArticleResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_article(self, client: XTwitterScraper) -> None:
        with client.x.with_streaming_response.get_article(
            tweet_id="tweetId",
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
                tweet_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_hashflags(self, client: XTwitterScraper) -> None:
        x = client.x.get_hashflags()
        assert_matches_type(XGetHashflagsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_hashflags_with_all_params(self, client: XTwitterScraper) -> None:
        x = client.x.get_hashflags(
            active_only=True,
            fields="id,text,author.username",
            limit=1,
            omit="entities,media",
            q="q",
        )
        assert_matches_type(XGetHashflagsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_hashflags(self, client: XTwitterScraper) -> None:
        response = client.x.with_raw_response.get_hashflags()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        x = response.parse()
        assert_matches_type(XGetHashflagsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_hashflags(self, client: XTwitterScraper) -> None:
        with client.x.with_streaming_response.get_hashflags() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            x = response.parse()
            assert_matches_type(XGetHashflagsResponse, x, path=["response"])

        assert cast(Any, response.is_closed) is True

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
    def test_method_get_news_story_versions(self, client: XTwitterScraper) -> None:
        x = client.x.get_news_story_versions(
            id="id",
        )
        assert_matches_type(XGetNewsStoryVersionsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_news_story_versions_with_all_params(self, client: XTwitterScraper) -> None:
        x = client.x.get_news_story_versions(
            id="id",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(XGetNewsStoryVersionsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_news_story_versions(self, client: XTwitterScraper) -> None:
        response = client.x.with_raw_response.get_news_story_versions(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        x = response.parse()
        assert_matches_type(XGetNewsStoryVersionsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_news_story_versions(self, client: XTwitterScraper) -> None:
        with client.x.with_streaming_response.get_news_story_versions(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            x = response.parse()
            assert_matches_type(XGetNewsStoryVersionsResponse, x, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_news_story_versions(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.with_raw_response.get_news_story_versions(
                id="",
            )

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
    def test_method_get_trend_locations(self, client: XTwitterScraper) -> None:
        x = client.x.get_trend_locations()
        assert_matches_type(XGetTrendLocationsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_trend_locations_with_all_params(self, client: XTwitterScraper) -> None:
        x = client.x.get_trend_locations(
            country="country",
            fields="id,text,author.username",
            limit=1,
            omit="entities,media",
            place_type="country",
            q="q",
        )
        assert_matches_type(XGetTrendLocationsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_trend_locations(self, client: XTwitterScraper) -> None:
        response = client.x.with_raw_response.get_trend_locations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        x = response.parse()
        assert_matches_type(XGetTrendLocationsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_trend_locations(self, client: XTwitterScraper) -> None:
        with client.x.with_streaming_response.get_trend_locations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            x = response.parse()
            assert_matches_type(XGetTrendLocationsResponse, x, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_trends(self, client: XTwitterScraper) -> None:
        x = client.x.get_trends()
        assert_matches_type(XGetTrendsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_trends_with_all_params(self, client: XTwitterScraper) -> None:
        x = client.x.get_trends(
            at="2026-10-13T14:00:00Z",
            count=1,
            country="country",
            fields="id,text,author.username",
            location="location",
            omit="entities,media",
            woeid=1,
        )
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_trends_history(self, client: XTwitterScraper) -> None:
        x = client.x.get_trends_history()
        assert_matches_type(XGetTrendsHistoryResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_trends_history_with_all_params(self, client: XTwitterScraper) -> None:
        x = client.x.get_trends_history(
            count=1,
            country="country",
            cursor="2026-10-14T00:00:00.000Z~1791979200000",
            every="1h",
            fields="id,text,author.username",
            from_="2026-10-13",
            limit=1,
            location="location",
            omit="entities,media",
            to="2026-10-14",
            woeid=1,
        )
        assert_matches_type(XGetTrendsHistoryResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_trends_history(self, client: XTwitterScraper) -> None:
        response = client.x.with_raw_response.get_trends_history()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        x = response.parse()
        assert_matches_type(XGetTrendsHistoryResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_trends_history(self, client: XTwitterScraper) -> None:
        with client.x.with_streaming_response.get_trends_history() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            x = response.parse()
            assert_matches_type(XGetTrendsHistoryResponse, x, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_places(self, client: XTwitterScraper) -> None:
        x = client.x.search_places(
            q="q",
        )
        assert_matches_type(XSearchPlacesResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_places_with_all_params(self, client: XTwitterScraper) -> None:
        x = client.x.search_places(
            q="q",
            fields="id,text,author.username",
            limit=1,
            omit="entities,media",
        )
        assert_matches_type(XSearchPlacesResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search_places(self, client: XTwitterScraper) -> None:
        response = client.x.with_raw_response.search_places(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        x = response.parse()
        assert_matches_type(XSearchPlacesResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search_places(self, client: XTwitterScraper) -> None:
        with client.x.with_streaming_response.search_places(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            x = response.parse()
            assert_matches_type(XSearchPlacesResponse, x, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncX:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_autocomplete_search(self, async_client: AsyncXTwitterScraper) -> None:
        x = await async_client.x.autocomplete_search(
            q="nasa",
        )
        assert_matches_type(XAutocompleteSearchResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_autocomplete_search_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        x = await async_client.x.autocomplete_search(
            q="nasa",
            fields="id,text,author.username",
            limit=1,
            omit="entities,media",
            types="users,topics",
        )
        assert_matches_type(XAutocompleteSearchResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_autocomplete_search(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.with_raw_response.autocomplete_search(
            q="nasa",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        x = await response.parse()
        assert_matches_type(XAutocompleteSearchResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_autocomplete_search(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.with_streaming_response.autocomplete_search(
            q="nasa",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            x = await response.parse()
            assert_matches_type(XAutocompleteSearchResponse, x, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_article(self, async_client: AsyncXTwitterScraper) -> None:
        x = await async_client.x.get_article(
            tweet_id="tweetId",
        )
        assert_matches_type(XGetArticleResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_article_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        x = await async_client.x.get_article(
            tweet_id="tweetId",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(XGetArticleResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_article(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.with_raw_response.get_article(
            tweet_id="tweetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        x = await response.parse()
        assert_matches_type(XGetArticleResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_article(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.with_streaming_response.get_article(
            tweet_id="tweetId",
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
                tweet_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_hashflags(self, async_client: AsyncXTwitterScraper) -> None:
        x = await async_client.x.get_hashflags()
        assert_matches_type(XGetHashflagsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_hashflags_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        x = await async_client.x.get_hashflags(
            active_only=True,
            fields="id,text,author.username",
            limit=1,
            omit="entities,media",
            q="q",
        )
        assert_matches_type(XGetHashflagsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_hashflags(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.with_raw_response.get_hashflags()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        x = await response.parse()
        assert_matches_type(XGetHashflagsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_hashflags(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.with_streaming_response.get_hashflags() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            x = await response.parse()
            assert_matches_type(XGetHashflagsResponse, x, path=["response"])

        assert cast(Any, response.is_closed) is True

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
    async def test_method_get_news_story_versions(self, async_client: AsyncXTwitterScraper) -> None:
        x = await async_client.x.get_news_story_versions(
            id="id",
        )
        assert_matches_type(XGetNewsStoryVersionsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_news_story_versions_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        x = await async_client.x.get_news_story_versions(
            id="id",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(XGetNewsStoryVersionsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_news_story_versions(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.with_raw_response.get_news_story_versions(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        x = await response.parse()
        assert_matches_type(XGetNewsStoryVersionsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_news_story_versions(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.with_streaming_response.get_news_story_versions(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            x = await response.parse()
            assert_matches_type(XGetNewsStoryVersionsResponse, x, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_news_story_versions(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.with_raw_response.get_news_story_versions(
                id="",
            )

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
    async def test_method_get_trend_locations(self, async_client: AsyncXTwitterScraper) -> None:
        x = await async_client.x.get_trend_locations()
        assert_matches_type(XGetTrendLocationsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_trend_locations_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        x = await async_client.x.get_trend_locations(
            country="country",
            fields="id,text,author.username",
            limit=1,
            omit="entities,media",
            place_type="country",
            q="q",
        )
        assert_matches_type(XGetTrendLocationsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_trend_locations(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.with_raw_response.get_trend_locations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        x = await response.parse()
        assert_matches_type(XGetTrendLocationsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_trend_locations(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.with_streaming_response.get_trend_locations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            x = await response.parse()
            assert_matches_type(XGetTrendLocationsResponse, x, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_trends(self, async_client: AsyncXTwitterScraper) -> None:
        x = await async_client.x.get_trends()
        assert_matches_type(XGetTrendsResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_trends_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        x = await async_client.x.get_trends(
            at="2026-10-13T14:00:00Z",
            count=1,
            country="country",
            fields="id,text,author.username",
            location="location",
            omit="entities,media",
            woeid=1,
        )
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_trends_history(self, async_client: AsyncXTwitterScraper) -> None:
        x = await async_client.x.get_trends_history()
        assert_matches_type(XGetTrendsHistoryResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_trends_history_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        x = await async_client.x.get_trends_history(
            count=1,
            country="country",
            cursor="2026-10-14T00:00:00.000Z~1791979200000",
            every="1h",
            fields="id,text,author.username",
            from_="2026-10-13",
            limit=1,
            location="location",
            omit="entities,media",
            to="2026-10-14",
            woeid=1,
        )
        assert_matches_type(XGetTrendsHistoryResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_trends_history(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.with_raw_response.get_trends_history()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        x = await response.parse()
        assert_matches_type(XGetTrendsHistoryResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_trends_history(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.with_streaming_response.get_trends_history() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            x = await response.parse()
            assert_matches_type(XGetTrendsHistoryResponse, x, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_places(self, async_client: AsyncXTwitterScraper) -> None:
        x = await async_client.x.search_places(
            q="q",
        )
        assert_matches_type(XSearchPlacesResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_places_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        x = await async_client.x.search_places(
            q="q",
            fields="id,text,author.username",
            limit=1,
            omit="entities,media",
        )
        assert_matches_type(XSearchPlacesResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search_places(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.with_raw_response.search_places(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        x = await response.parse()
        assert_matches_type(XSearchPlacesResponse, x, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search_places(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.with_streaming_response.search_places(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            x = await response.parse()
            assert_matches_type(XSearchPlacesResponse, x, path=["response"])

        assert cast(Any, response.is_closed) is True
