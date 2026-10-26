# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper._utils import parse_date
from x_twitter_scraper.types.x import (
    ListRetrieveResponse,
    ListRetrieveSearchResponse,
    ListRetrieveMembersResponse,
    ListRetrieveFollowersResponse,
)
from x_twitter_scraper.types.shared import PaginatedTweets

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLists:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: XTwitterScraper) -> None:
        list_ = client.x.lists.retrieve(
            id="id",
        )
        assert_matches_type(ListRetrieveResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: XTwitterScraper) -> None:
        list_ = client.x.lists.retrieve(
            id="id",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(ListRetrieveResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: XTwitterScraper) -> None:
        response = client.x.lists.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        list_ = response.parse()
        assert_matches_type(ListRetrieveResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: XTwitterScraper) -> None:
        with client.x.lists.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            list_ = response.parse()
            assert_matches_type(ListRetrieveResponse, list_, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.lists.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_followers(self, client: XTwitterScraper) -> None:
        list_ = client.x.lists.retrieve_followers(
            id="id",
        )
        assert_matches_type(ListRetrieveFollowersResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_followers_with_all_params(self, client: XTwitterScraper) -> None:
        list_ = client.x.lists.retrieve_followers(
            id="id",
            after="after",
            bio_contains="bioContains",
            blue_verified_only=True,
            business_email_only=True,
            cursor="cursor",
            email_domains="acme.com,stanford.edu",
            fields="id,text,author.username",
            has_email=True,
            has_location=True,
            has_website=True,
            location_contains="locationContains",
            max_followers=0,
            max_following=0,
            max_scan=10000,
            max_statuses=0,
            min_account_age_days=0,
            min_followers=0,
            min_following=0,
            min_statuses=0,
            mode="standard",
            omit="entities,media",
            page_size=1,
            username_contains="usernameContains",
            verified_only=True,
            verified_type="verifiedType",
        )
        assert_matches_type(ListRetrieveFollowersResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_followers(self, client: XTwitterScraper) -> None:
        response = client.x.lists.with_raw_response.retrieve_followers(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        list_ = response.parse()
        assert_matches_type(ListRetrieveFollowersResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_followers(self, client: XTwitterScraper) -> None:
        with client.x.lists.with_streaming_response.retrieve_followers(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            list_ = response.parse()
            assert_matches_type(ListRetrieveFollowersResponse, list_, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_followers(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.lists.with_raw_response.retrieve_followers(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_members(self, client: XTwitterScraper) -> None:
        list_ = client.x.lists.retrieve_members(
            id="id",
        )
        assert_matches_type(ListRetrieveMembersResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_members_with_all_params(self, client: XTwitterScraper) -> None:
        list_ = client.x.lists.retrieve_members(
            id="id",
            after="after",
            bio_contains="bioContains",
            blue_verified_only=True,
            business_email_only=True,
            cursor="cursor",
            email_domains="acme.com,stanford.edu",
            fields="id,text,author.username",
            has_email=True,
            has_location=True,
            has_website=True,
            location_contains="locationContains",
            max_followers=0,
            max_following=0,
            max_scan=10000,
            max_statuses=0,
            min_account_age_days=0,
            min_followers=0,
            min_following=0,
            min_statuses=0,
            mode="standard",
            omit="entities,media",
            page_size=1,
            username_contains="usernameContains",
            verified_only=True,
            verified_type="verifiedType",
        )
        assert_matches_type(ListRetrieveMembersResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_members(self, client: XTwitterScraper) -> None:
        response = client.x.lists.with_raw_response.retrieve_members(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        list_ = response.parse()
        assert_matches_type(ListRetrieveMembersResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_members(self, client: XTwitterScraper) -> None:
        with client.x.lists.with_streaming_response.retrieve_members(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            list_ = response.parse()
            assert_matches_type(ListRetrieveMembersResponse, list_, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_members(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.lists.with_raw_response.retrieve_members(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_search(self, client: XTwitterScraper) -> None:
        list_ = client.x.lists.retrieve_search(
            q="q",
        )
        assert_matches_type(ListRetrieveSearchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_search_with_all_params(self, client: XTwitterScraper) -> None:
        list_ = client.x.lists.retrieve_search(
            q="q",
            cursor="cursor",
            fields="id,text,author.username",
            omit="entities,media",
            page_size=1,
        )
        assert_matches_type(ListRetrieveSearchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_search(self, client: XTwitterScraper) -> None:
        response = client.x.lists.with_raw_response.retrieve_search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        list_ = response.parse()
        assert_matches_type(ListRetrieveSearchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_search(self, client: XTwitterScraper) -> None:
        with client.x.lists.with_streaming_response.retrieve_search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            list_ = response.parse()
            assert_matches_type(ListRetrieveSearchResponse, list_, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_tweets(self, client: XTwitterScraper) -> None:
        list_ = client.x.lists.retrieve_tweets(
            id="id",
        )
        assert_matches_type(PaginatedTweets, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_tweets_with_all_params(self, client: XTwitterScraper) -> None:
        list_ = client.x.lists.retrieve_tweets(
            id="id",
            advanced_query="advancedQuery",
            after="after",
            any_words="anyWords",
            blue_verified_only=True,
            bounding_box="boundingBox",
            card_name="cardName",
            cashtags="cashtags",
            conversation_id="conversationId",
            cursor="cursor",
            exact_phrase="exactPhrase",
            exclude_source="excludeSource",
            exclude_words="excludeWords",
            fields="id,text,author.username",
            from_user="fromUser",
            geocode="geocode",
            hashtags="hashtags",
            include_replies=True,
            in_reply_to_tweet_id="inReplyToTweetId",
            keywords="keywords",
            language="language",
            max_faves=0,
            max_id="maxId",
            max_quotes=0,
            max_replies=0,
            max_retweets=0,
            media_type="images",
            mentioning="mentioning",
            min_bookmarks=0,
            min_likes=0,
            min_quotes=0,
            min_replies=0,
            min_retweets=0,
            min_views=0,
            mode="standard",
            native_retweets=True,
            near="near",
            news=True,
            omit="entities,media",
            page_size=1,
            place="place",
            place_country="placeCountry",
            point_radius="pointRadius",
            quotes="include",
            quotes_of_tweet_id="quotesOfTweetId",
            replies="include",
            retweets="include",
            retweets_of_tweet_id="retweetsOfTweetId",
            safe=True,
            since_date=parse_date("2019-12-27"),
            since_id="sinceId",
            since_time="sinceTime",
            source="source",
            to_user="toUser",
            until_date=parse_date("2019-12-27"),
            until_time="untilTime",
            url="url",
            verified_only=True,
            within="within",
            within_time="7d",
        )
        assert_matches_type(PaginatedTweets, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_tweets(self, client: XTwitterScraper) -> None:
        response = client.x.lists.with_raw_response.retrieve_tweets(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        list_ = response.parse()
        assert_matches_type(PaginatedTweets, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_tweets(self, client: XTwitterScraper) -> None:
        with client.x.lists.with_streaming_response.retrieve_tweets(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            list_ = response.parse()
            assert_matches_type(PaginatedTweets, list_, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_tweets(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.lists.with_raw_response.retrieve_tweets(
                id="",
            )


class TestAsyncLists:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        list_ = await async_client.x.lists.retrieve(
            id="id",
        )
        assert_matches_type(ListRetrieveResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        list_ = await async_client.x.lists.retrieve(
            id="id",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(ListRetrieveResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.lists.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        list_ = await response.parse()
        assert_matches_type(ListRetrieveResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.lists.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            list_ = await response.parse()
            assert_matches_type(ListRetrieveResponse, list_, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.lists.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_followers(self, async_client: AsyncXTwitterScraper) -> None:
        list_ = await async_client.x.lists.retrieve_followers(
            id="id",
        )
        assert_matches_type(ListRetrieveFollowersResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_followers_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        list_ = await async_client.x.lists.retrieve_followers(
            id="id",
            after="after",
            bio_contains="bioContains",
            blue_verified_only=True,
            business_email_only=True,
            cursor="cursor",
            email_domains="acme.com,stanford.edu",
            fields="id,text,author.username",
            has_email=True,
            has_location=True,
            has_website=True,
            location_contains="locationContains",
            max_followers=0,
            max_following=0,
            max_scan=10000,
            max_statuses=0,
            min_account_age_days=0,
            min_followers=0,
            min_following=0,
            min_statuses=0,
            mode="standard",
            omit="entities,media",
            page_size=1,
            username_contains="usernameContains",
            verified_only=True,
            verified_type="verifiedType",
        )
        assert_matches_type(ListRetrieveFollowersResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_followers(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.lists.with_raw_response.retrieve_followers(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        list_ = await response.parse()
        assert_matches_type(ListRetrieveFollowersResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_followers(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.lists.with_streaming_response.retrieve_followers(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            list_ = await response.parse()
            assert_matches_type(ListRetrieveFollowersResponse, list_, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_followers(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.lists.with_raw_response.retrieve_followers(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_members(self, async_client: AsyncXTwitterScraper) -> None:
        list_ = await async_client.x.lists.retrieve_members(
            id="id",
        )
        assert_matches_type(ListRetrieveMembersResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_members_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        list_ = await async_client.x.lists.retrieve_members(
            id="id",
            after="after",
            bio_contains="bioContains",
            blue_verified_only=True,
            business_email_only=True,
            cursor="cursor",
            email_domains="acme.com,stanford.edu",
            fields="id,text,author.username",
            has_email=True,
            has_location=True,
            has_website=True,
            location_contains="locationContains",
            max_followers=0,
            max_following=0,
            max_scan=10000,
            max_statuses=0,
            min_account_age_days=0,
            min_followers=0,
            min_following=0,
            min_statuses=0,
            mode="standard",
            omit="entities,media",
            page_size=1,
            username_contains="usernameContains",
            verified_only=True,
            verified_type="verifiedType",
        )
        assert_matches_type(ListRetrieveMembersResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_members(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.lists.with_raw_response.retrieve_members(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        list_ = await response.parse()
        assert_matches_type(ListRetrieveMembersResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_members(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.lists.with_streaming_response.retrieve_members(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            list_ = await response.parse()
            assert_matches_type(ListRetrieveMembersResponse, list_, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_members(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.lists.with_raw_response.retrieve_members(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_search(self, async_client: AsyncXTwitterScraper) -> None:
        list_ = await async_client.x.lists.retrieve_search(
            q="q",
        )
        assert_matches_type(ListRetrieveSearchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_search_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        list_ = await async_client.x.lists.retrieve_search(
            q="q",
            cursor="cursor",
            fields="id,text,author.username",
            omit="entities,media",
            page_size=1,
        )
        assert_matches_type(ListRetrieveSearchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_search(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.lists.with_raw_response.retrieve_search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        list_ = await response.parse()
        assert_matches_type(ListRetrieveSearchResponse, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_search(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.lists.with_streaming_response.retrieve_search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            list_ = await response.parse()
            assert_matches_type(ListRetrieveSearchResponse, list_, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_tweets(self, async_client: AsyncXTwitterScraper) -> None:
        list_ = await async_client.x.lists.retrieve_tweets(
            id="id",
        )
        assert_matches_type(PaginatedTweets, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_tweets_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        list_ = await async_client.x.lists.retrieve_tweets(
            id="id",
            advanced_query="advancedQuery",
            after="after",
            any_words="anyWords",
            blue_verified_only=True,
            bounding_box="boundingBox",
            card_name="cardName",
            cashtags="cashtags",
            conversation_id="conversationId",
            cursor="cursor",
            exact_phrase="exactPhrase",
            exclude_source="excludeSource",
            exclude_words="excludeWords",
            fields="id,text,author.username",
            from_user="fromUser",
            geocode="geocode",
            hashtags="hashtags",
            include_replies=True,
            in_reply_to_tweet_id="inReplyToTweetId",
            keywords="keywords",
            language="language",
            max_faves=0,
            max_id="maxId",
            max_quotes=0,
            max_replies=0,
            max_retweets=0,
            media_type="images",
            mentioning="mentioning",
            min_bookmarks=0,
            min_likes=0,
            min_quotes=0,
            min_replies=0,
            min_retweets=0,
            min_views=0,
            mode="standard",
            native_retweets=True,
            near="near",
            news=True,
            omit="entities,media",
            page_size=1,
            place="place",
            place_country="placeCountry",
            point_radius="pointRadius",
            quotes="include",
            quotes_of_tweet_id="quotesOfTweetId",
            replies="include",
            retweets="include",
            retweets_of_tweet_id="retweetsOfTweetId",
            safe=True,
            since_date=parse_date("2019-12-27"),
            since_id="sinceId",
            since_time="sinceTime",
            source="source",
            to_user="toUser",
            until_date=parse_date("2019-12-27"),
            until_time="untilTime",
            url="url",
            verified_only=True,
            within="within",
            within_time="7d",
        )
        assert_matches_type(PaginatedTweets, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_tweets(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.lists.with_raw_response.retrieve_tweets(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        list_ = await response.parse()
        assert_matches_type(PaginatedTweets, list_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_tweets(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.lists.with_streaming_response.retrieve_tweets(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            list_ = await response.parse()
            assert_matches_type(PaginatedTweets, list_, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_tweets(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.lists.with_raw_response.retrieve_tweets(
                id="",
            )
