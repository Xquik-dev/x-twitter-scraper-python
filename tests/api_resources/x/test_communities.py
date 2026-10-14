# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper._utils import parse_date
from x_twitter_scraper.types.x import (
    CommunityCreateResponse,
    CommunityDeleteResponse,
    CommunityListTopicsResponse,
    CommunityRetrieveInfoResponse,
    CommunityListSuggestedResponse,
)
from x_twitter_scraper.types.shared import (
    CommunityPage,
    PaginatedUsers,
    PaginatedTweets,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCommunities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: XTwitterScraper) -> None:
        community = client.x.communities.create(
            account="@elonmusk",
            name="Example Name",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(CommunityCreateResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: XTwitterScraper) -> None:
        community = client.x.communities.create(
            account="@elonmusk",
            name="Example Name",
            idempotency_key="Idempotency-Key",
            description="A community for Tesla enthusiasts",
        )
        assert_matches_type(CommunityCreateResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: XTwitterScraper) -> None:
        response = client.x.communities.with_raw_response.create(
            account="@elonmusk",
            name="Example Name",
            idempotency_key="Idempotency-Key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert_matches_type(CommunityCreateResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: XTwitterScraper) -> None:
        with client.x.communities.with_streaming_response.create(
            account="@elonmusk",
            name="Example Name",
            idempotency_key="Idempotency-Key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert_matches_type(CommunityCreateResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: XTwitterScraper) -> None:
        community = client.x.communities.delete(
            id="1500000000000000000",
            account="@elonmusk",
            community_name="Tesla Fans",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(CommunityDeleteResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: XTwitterScraper) -> None:
        response = client.x.communities.with_raw_response.delete(
            id="1500000000000000000",
            account="@elonmusk",
            community_name="Tesla Fans",
            idempotency_key="Idempotency-Key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert_matches_type(CommunityDeleteResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: XTwitterScraper) -> None:
        with client.x.communities.with_streaming_response.delete(
            id="1500000000000000000",
            account="@elonmusk",
            community_name="Tesla Fans",
            idempotency_key="Idempotency-Key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert_matches_type(CommunityDeleteResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.communities.with_raw_response.delete(
                id="",
                account="@elonmusk",
                community_name="Tesla Fans",
                idempotency_key="Idempotency-Key",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find(self, client: XTwitterScraper) -> None:
        community = client.x.communities.find(
            q="q",
        )
        assert_matches_type(CommunityPage, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_find_with_all_params(self, client: XTwitterScraper) -> None:
        community = client.x.communities.find(
            q="q",
            cursor="cursor",
            fields="id,text,author.username",
            omit="entities,media",
            page_size=1,
        )
        assert_matches_type(CommunityPage, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_find(self, client: XTwitterScraper) -> None:
        response = client.x.communities.with_raw_response.find(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert_matches_type(CommunityPage, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_find(self, client: XTwitterScraper) -> None:
        with client.x.communities.with_streaming_response.find(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert_matches_type(CommunityPage, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_popular(self, client: XTwitterScraper) -> None:
        community = client.x.communities.list_popular()
        assert_matches_type(CommunityPage, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_popular_with_all_params(self, client: XTwitterScraper) -> None:
        community = client.x.communities.list_popular(
            cursor="cursor",
            fields="id,text,author.username",
            omit="entities,media",
            page_size=1,
            topic="topic",
            topic_id="topicId",
        )
        assert_matches_type(CommunityPage, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_popular(self, client: XTwitterScraper) -> None:
        response = client.x.communities.with_raw_response.list_popular()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert_matches_type(CommunityPage, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_popular(self, client: XTwitterScraper) -> None:
        with client.x.communities.with_streaming_response.list_popular() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert_matches_type(CommunityPage, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_suggested(self, client: XTwitterScraper) -> None:
        community = client.x.communities.list_suggested()
        assert_matches_type(CommunityListSuggestedResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_suggested_with_all_params(self, client: XTwitterScraper) -> None:
        community = client.x.communities.list_suggested(
            fields="id,text,author.username",
            limit=1,
            omit="entities,media",
        )
        assert_matches_type(CommunityListSuggestedResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_suggested(self, client: XTwitterScraper) -> None:
        response = client.x.communities.with_raw_response.list_suggested()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert_matches_type(CommunityListSuggestedResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_suggested(self, client: XTwitterScraper) -> None:
        with client.x.communities.with_streaming_response.list_suggested() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert_matches_type(CommunityListSuggestedResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_topics(self, client: XTwitterScraper) -> None:
        community = client.x.communities.list_topics()
        assert_matches_type(CommunityListTopicsResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_topics_with_all_params(self, client: XTwitterScraper) -> None:
        community = client.x.communities.list_topics(
            fields="id,text,author.username",
            limit=1,
            omit="entities,media",
        )
        assert_matches_type(CommunityListTopicsResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_topics(self, client: XTwitterScraper) -> None:
        response = client.x.communities.with_raw_response.list_topics()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert_matches_type(CommunityListTopicsResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_topics(self, client: XTwitterScraper) -> None:
        with client.x.communities.with_streaming_response.list_topics() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert_matches_type(CommunityListTopicsResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_info(self, client: XTwitterScraper) -> None:
        community = client.x.communities.retrieve_info(
            id="id",
        )
        assert_matches_type(CommunityRetrieveInfoResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_info_with_all_params(self, client: XTwitterScraper) -> None:
        community = client.x.communities.retrieve_info(
            id="id",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(CommunityRetrieveInfoResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_info(self, client: XTwitterScraper) -> None:
        response = client.x.communities.with_raw_response.retrieve_info(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert_matches_type(CommunityRetrieveInfoResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_info(self, client: XTwitterScraper) -> None:
        with client.x.communities.with_streaming_response.retrieve_info(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert_matches_type(CommunityRetrieveInfoResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_info(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.communities.with_raw_response.retrieve_info(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_members(self, client: XTwitterScraper) -> None:
        community = client.x.communities.retrieve_members(
            id="id",
        )
        assert_matches_type(PaginatedUsers, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_members_with_all_params(self, client: XTwitterScraper) -> None:
        community = client.x.communities.retrieve_members(
            id="id",
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
            max_statuses=0,
            min_account_age_days=0,
            min_followers=0,
            min_following=0,
            min_statuses=0,
            omit="entities,media",
            page_size=1,
            username_contains="usernameContains",
            verified_only=True,
            verified_type="verifiedType",
        )
        assert_matches_type(PaginatedUsers, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_members(self, client: XTwitterScraper) -> None:
        response = client.x.communities.with_raw_response.retrieve_members(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert_matches_type(PaginatedUsers, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_members(self, client: XTwitterScraper) -> None:
        with client.x.communities.with_streaming_response.retrieve_members(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert_matches_type(PaginatedUsers, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_members(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.communities.with_raw_response.retrieve_members(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_moderators(self, client: XTwitterScraper) -> None:
        community = client.x.communities.retrieve_moderators(
            id="id",
        )
        assert_matches_type(PaginatedUsers, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_moderators_with_all_params(self, client: XTwitterScraper) -> None:
        community = client.x.communities.retrieve_moderators(
            id="id",
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
            max_statuses=0,
            min_account_age_days=0,
            min_followers=0,
            min_following=0,
            min_statuses=0,
            omit="entities,media",
            username_contains="usernameContains",
            verified_only=True,
            verified_type="verifiedType",
        )
        assert_matches_type(PaginatedUsers, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_moderators(self, client: XTwitterScraper) -> None:
        response = client.x.communities.with_raw_response.retrieve_moderators(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert_matches_type(PaginatedUsers, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_moderators(self, client: XTwitterScraper) -> None:
        with client.x.communities.with_streaming_response.retrieve_moderators(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert_matches_type(PaginatedUsers, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_moderators(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.communities.with_raw_response.retrieve_moderators(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_search(self, client: XTwitterScraper) -> None:
        community = client.x.communities.retrieve_search(
            q="q",
        )
        assert_matches_type(PaginatedTweets, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_search_with_all_params(self, client: XTwitterScraper) -> None:
        community = client.x.communities.retrieve_search(
            q="q",
            any_words="anyWords",
            blue_verified_only=True,
            cashtags="cashtags",
            community_id="1234567890",
            conversation_id="conversationId",
            cursor="cursor",
            exact_phrase="exactPhrase",
            exclude_words="excludeWords",
            fields="id,text,author.username",
            from_user="fromUser",
            hashtags="hashtags",
            in_reply_to_tweet_id="inReplyToTweetId",
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
            native_retweets=True,
            omit="entities,media",
            page_size=1,
            query_type="Latest",
            quotes="include",
            quotes_of_tweet_id="quotesOfTweetId",
            replies="include",
            retweets="include",
            retweets_of_tweet_id="retweetsOfTweetId",
            since_date=parse_date("2019-12-27"),
            since_id="sinceId",
            to_user="toUser",
            until_date=parse_date("2019-12-27"),
            url="url",
            verified_only=True,
            within_time="7d",
        )
        assert_matches_type(PaginatedTweets, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_search(self, client: XTwitterScraper) -> None:
        response = client.x.communities.with_raw_response.retrieve_search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert_matches_type(PaginatedTweets, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_search(self, client: XTwitterScraper) -> None:
        with client.x.communities.with_streaming_response.retrieve_search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert_matches_type(PaginatedTweets, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_members(self, client: XTwitterScraper) -> None:
        community = client.x.communities.search_members(
            id="id",
            q="q",
        )
        assert_matches_type(PaginatedUsers, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_members_with_all_params(self, client: XTwitterScraper) -> None:
        community = client.x.communities.search_members(
            id="id",
            q="q",
            bio_contains="bioContains",
            blue_verified_only=True,
            business_email_only=True,
            email_domains="acme.com,stanford.edu",
            fields="id,text,author.username",
            has_email=True,
            has_location=True,
            has_website=True,
            location_contains="locationContains",
            max_followers=0,
            max_following=0,
            max_statuses=0,
            min_account_age_days=0,
            min_followers=0,
            min_following=0,
            min_statuses=0,
            omit="entities,media",
            username_contains="usernameContains",
            verified_only=True,
            verified_type="verifiedType",
        )
        assert_matches_type(PaginatedUsers, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search_members(self, client: XTwitterScraper) -> None:
        response = client.x.communities.with_raw_response.search_members(
            id="id",
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert_matches_type(PaginatedUsers, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search_members(self, client: XTwitterScraper) -> None:
        with client.x.communities.with_streaming_response.search_members(
            id="id",
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert_matches_type(PaginatedUsers, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_search_members(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.communities.with_raw_response.search_members(
                id="",
                q="q",
            )


class TestAsyncCommunities:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.create(
            account="@elonmusk",
            name="Example Name",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(CommunityCreateResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.create(
            account="@elonmusk",
            name="Example Name",
            idempotency_key="Idempotency-Key",
            description="A community for Tesla enthusiasts",
        )
        assert_matches_type(CommunityCreateResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.communities.with_raw_response.create(
            account="@elonmusk",
            name="Example Name",
            idempotency_key="Idempotency-Key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert_matches_type(CommunityCreateResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.communities.with_streaming_response.create(
            account="@elonmusk",
            name="Example Name",
            idempotency_key="Idempotency-Key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert_matches_type(CommunityCreateResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.delete(
            id="1500000000000000000",
            account="@elonmusk",
            community_name="Tesla Fans",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(CommunityDeleteResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.communities.with_raw_response.delete(
            id="1500000000000000000",
            account="@elonmusk",
            community_name="Tesla Fans",
            idempotency_key="Idempotency-Key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert_matches_type(CommunityDeleteResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.communities.with_streaming_response.delete(
            id="1500000000000000000",
            account="@elonmusk",
            community_name="Tesla Fans",
            idempotency_key="Idempotency-Key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert_matches_type(CommunityDeleteResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.communities.with_raw_response.delete(
                id="",
                account="@elonmusk",
                community_name="Tesla Fans",
                idempotency_key="Idempotency-Key",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.find(
            q="q",
        )
        assert_matches_type(CommunityPage, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_find_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.find(
            q="q",
            cursor="cursor",
            fields="id,text,author.username",
            omit="entities,media",
            page_size=1,
        )
        assert_matches_type(CommunityPage, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_find(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.communities.with_raw_response.find(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert_matches_type(CommunityPage, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_find(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.communities.with_streaming_response.find(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert_matches_type(CommunityPage, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_popular(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.list_popular()
        assert_matches_type(CommunityPage, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_popular_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.list_popular(
            cursor="cursor",
            fields="id,text,author.username",
            omit="entities,media",
            page_size=1,
            topic="topic",
            topic_id="topicId",
        )
        assert_matches_type(CommunityPage, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_popular(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.communities.with_raw_response.list_popular()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert_matches_type(CommunityPage, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_popular(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.communities.with_streaming_response.list_popular() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert_matches_type(CommunityPage, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_suggested(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.list_suggested()
        assert_matches_type(CommunityListSuggestedResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_suggested_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.list_suggested(
            fields="id,text,author.username",
            limit=1,
            omit="entities,media",
        )
        assert_matches_type(CommunityListSuggestedResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_suggested(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.communities.with_raw_response.list_suggested()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert_matches_type(CommunityListSuggestedResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_suggested(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.communities.with_streaming_response.list_suggested() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert_matches_type(CommunityListSuggestedResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_topics(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.list_topics()
        assert_matches_type(CommunityListTopicsResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_topics_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.list_topics(
            fields="id,text,author.username",
            limit=1,
            omit="entities,media",
        )
        assert_matches_type(CommunityListTopicsResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_topics(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.communities.with_raw_response.list_topics()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert_matches_type(CommunityListTopicsResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_topics(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.communities.with_streaming_response.list_topics() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert_matches_type(CommunityListTopicsResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_info(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.retrieve_info(
            id="id",
        )
        assert_matches_type(CommunityRetrieveInfoResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_info_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.retrieve_info(
            id="id",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(CommunityRetrieveInfoResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_info(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.communities.with_raw_response.retrieve_info(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert_matches_type(CommunityRetrieveInfoResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_info(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.communities.with_streaming_response.retrieve_info(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert_matches_type(CommunityRetrieveInfoResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_info(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.communities.with_raw_response.retrieve_info(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_members(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.retrieve_members(
            id="id",
        )
        assert_matches_type(PaginatedUsers, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_members_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.retrieve_members(
            id="id",
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
            max_statuses=0,
            min_account_age_days=0,
            min_followers=0,
            min_following=0,
            min_statuses=0,
            omit="entities,media",
            page_size=1,
            username_contains="usernameContains",
            verified_only=True,
            verified_type="verifiedType",
        )
        assert_matches_type(PaginatedUsers, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_members(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.communities.with_raw_response.retrieve_members(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert_matches_type(PaginatedUsers, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_members(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.communities.with_streaming_response.retrieve_members(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert_matches_type(PaginatedUsers, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_members(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.communities.with_raw_response.retrieve_members(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_moderators(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.retrieve_moderators(
            id="id",
        )
        assert_matches_type(PaginatedUsers, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_moderators_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.retrieve_moderators(
            id="id",
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
            max_statuses=0,
            min_account_age_days=0,
            min_followers=0,
            min_following=0,
            min_statuses=0,
            omit="entities,media",
            username_contains="usernameContains",
            verified_only=True,
            verified_type="verifiedType",
        )
        assert_matches_type(PaginatedUsers, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_moderators(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.communities.with_raw_response.retrieve_moderators(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert_matches_type(PaginatedUsers, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_moderators(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.communities.with_streaming_response.retrieve_moderators(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert_matches_type(PaginatedUsers, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_moderators(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.communities.with_raw_response.retrieve_moderators(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_search(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.retrieve_search(
            q="q",
        )
        assert_matches_type(PaginatedTweets, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_search_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.retrieve_search(
            q="q",
            any_words="anyWords",
            blue_verified_only=True,
            cashtags="cashtags",
            community_id="1234567890",
            conversation_id="conversationId",
            cursor="cursor",
            exact_phrase="exactPhrase",
            exclude_words="excludeWords",
            fields="id,text,author.username",
            from_user="fromUser",
            hashtags="hashtags",
            in_reply_to_tweet_id="inReplyToTweetId",
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
            native_retweets=True,
            omit="entities,media",
            page_size=1,
            query_type="Latest",
            quotes="include",
            quotes_of_tweet_id="quotesOfTweetId",
            replies="include",
            retweets="include",
            retweets_of_tweet_id="retweetsOfTweetId",
            since_date=parse_date("2019-12-27"),
            since_id="sinceId",
            to_user="toUser",
            until_date=parse_date("2019-12-27"),
            url="url",
            verified_only=True,
            within_time="7d",
        )
        assert_matches_type(PaginatedTweets, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_search(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.communities.with_raw_response.retrieve_search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert_matches_type(PaginatedTweets, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_search(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.communities.with_streaming_response.retrieve_search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert_matches_type(PaginatedTweets, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_members(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.search_members(
            id="id",
            q="q",
        )
        assert_matches_type(PaginatedUsers, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_members_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.search_members(
            id="id",
            q="q",
            bio_contains="bioContains",
            blue_verified_only=True,
            business_email_only=True,
            email_domains="acme.com,stanford.edu",
            fields="id,text,author.username",
            has_email=True,
            has_location=True,
            has_website=True,
            location_contains="locationContains",
            max_followers=0,
            max_following=0,
            max_statuses=0,
            min_account_age_days=0,
            min_followers=0,
            min_following=0,
            min_statuses=0,
            omit="entities,media",
            username_contains="usernameContains",
            verified_only=True,
            verified_type="verifiedType",
        )
        assert_matches_type(PaginatedUsers, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search_members(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.communities.with_raw_response.search_members(
            id="id",
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert_matches_type(PaginatedUsers, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search_members(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.communities.with_streaming_response.search_members(
            id="id",
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert_matches_type(PaginatedUsers, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_search_members(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.communities.with_raw_response.search_members(
                id="",
                q="q",
            )
