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
    UserRetrieveLiveResponse,
    UserTranslateBioResponse,
    UserRetrieveBatchResponse,
    UserRetrieveListsResponse,
    UserRemoveFollowerResponse,
    UserRetrieveInsightsResponse,
    UserRetrieveFollowersResponse,
    UserRetrieveFollowingResponse,
    UserRetrieveBatchTweetsResponse,
    UserRetrieveFollowerIdsResponse,
    UserRetrieveFollowingIdsResponse,
    UserRetrieveListMembershipsResponse,
    UserRetrieveVerifiedFollowersResponse,
)
from x_twitter_scraper.types.shared import UserProfile, PaginatedUsers, PaginatedTweets

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve(
            id="id",
        )
        assert_matches_type(UserProfile, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve(
            id="id",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(UserProfile, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = response.parse()
        assert_matches_type(UserProfile, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = response.parse()
            assert_matches_type(UserProfile, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.users.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove_follower(self, client: XTwitterScraper) -> None:
        user = client.x.users.remove_follower(
            id="id",
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(UserRemoveFollowerResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove_follower(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.remove_follower(
            id="id",
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = response.parse()
        assert_matches_type(UserRemoveFollowerResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove_follower(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.remove_follower(
            id="id",
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = response.parse()
            assert_matches_type(UserRemoveFollowerResponse, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove_follower(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.users.with_raw_response.remove_follower(
                id="",
                account="@elonmusk",
                idempotency_key="Idempotency-Key",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_affiliates(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_affiliates(
            id="id",
        )
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_affiliates_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_affiliates(
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
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_affiliates(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_affiliates(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = response.parse()
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_affiliates(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_affiliates(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = response.parse()
            assert_matches_type(PaginatedUsers, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_affiliates(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.users.with_raw_response.retrieve_affiliates(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_articles(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_articles(
            id="id",
        )
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_articles_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_articles(
            id="id",
            any_words="anyWords",
            blue_verified_only=True,
            cashtags="cashtags",
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
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_articles(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_articles(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = response.parse()
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_articles(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_articles(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = response.parse()
            assert_matches_type(PaginatedTweets, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_articles(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.users.with_raw_response.retrieve_articles(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_batch(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_batch()
        assert_matches_type(UserRetrieveBatchResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_batch_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_batch(
            bio_contains="bioContains",
            blue_verified_only=True,
            business_email_only=True,
            email_domains="acme.com,stanford.edu",
            fields="id,text,author.username",
            has_email=True,
            has_location=True,
            has_website=True,
            ids="ids",
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
            usernames="nasa,@OpenAI,x.com/verge",
            verified_only=True,
            verified_type="verifiedType",
        )
        assert_matches_type(UserRetrieveBatchResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_batch(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_batch()

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = response.parse()
        assert_matches_type(UserRetrieveBatchResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_batch(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_batch() as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = response.parse()
            assert_matches_type(UserRetrieveBatchResponse, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_batch_tweets(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_batch_tweets()
        assert_matches_type(UserRetrieveBatchTweetsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_batch_tweets_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_batch_tweets(
            fields="id,text,author.username",
            ids="ids",
            omit="entities,media",
            page_size=1,
            usernames="nasa,@OpenAI,x.com/verge",
        )
        assert_matches_type(UserRetrieveBatchTweetsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_batch_tweets(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_batch_tweets()

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = response.parse()
        assert_matches_type(UserRetrieveBatchTweetsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_batch_tweets(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_batch_tweets() as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = response.parse()
            assert_matches_type(UserRetrieveBatchTweetsResponse, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_follower_ids(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_follower_ids(
            id="id",
        )
        assert_matches_type(UserRetrieveFollowerIdsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_follower_ids_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_follower_ids(
            id="id",
            cursor="cursor",
            page_size=1,
        )
        assert_matches_type(UserRetrieveFollowerIdsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_follower_ids(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_follower_ids(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = response.parse()
        assert_matches_type(UserRetrieveFollowerIdsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_follower_ids(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_follower_ids(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = response.parse()
            assert_matches_type(UserRetrieveFollowerIdsResponse, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_follower_ids(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.users.with_raw_response.retrieve_follower_ids(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_followers(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_followers(
            id="id",
        )
        assert_matches_type(UserRetrieveFollowersResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_followers_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_followers(
            id="id",
            after="after",
            bio_contains="bioContains",
            blue_verified_only=True,
            business_email_only=True,
            cursor="cursor",
            email_domains="acme.com,stanford.edu",
            enrich_profiles=True,
            fields="id,text,author.username",
            has_email=True,
            has_location=True,
            has_website=True,
            limit=1,
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
        assert_matches_type(UserRetrieveFollowersResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_followers(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_followers(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = response.parse()
        assert_matches_type(UserRetrieveFollowersResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_followers(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_followers(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = response.parse()
            assert_matches_type(UserRetrieveFollowersResponse, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_followers(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.users.with_raw_response.retrieve_followers(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_followers_you_know(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_followers_you_know(
            id="id",
        )
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_followers_you_know_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_followers_you_know(
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
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_followers_you_know(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_followers_you_know(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = response.parse()
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_followers_you_know(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_followers_you_know(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = response.parse()
            assert_matches_type(PaginatedUsers, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_followers_you_know(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.users.with_raw_response.retrieve_followers_you_know(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_following(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_following(
            id="id",
        )
        assert_matches_type(UserRetrieveFollowingResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_following_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_following(
            id="id",
            after="after",
            bio_contains="bioContains",
            blue_verified_only=True,
            business_email_only=True,
            cursor="cursor",
            email_domains="acme.com,stanford.edu",
            enrich_profiles=True,
            fields="id,text,author.username",
            has_email=True,
            has_location=True,
            has_website=True,
            limit=1,
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
        assert_matches_type(UserRetrieveFollowingResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_following(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_following(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = response.parse()
        assert_matches_type(UserRetrieveFollowingResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_following(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_following(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = response.parse()
            assert_matches_type(UserRetrieveFollowingResponse, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_following(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.users.with_raw_response.retrieve_following(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_following_ids(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_following_ids(
            id="id",
        )
        assert_matches_type(UserRetrieveFollowingIdsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_following_ids_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_following_ids(
            id="id",
            cursor="cursor",
            page_size=1,
        )
        assert_matches_type(UserRetrieveFollowingIdsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_following_ids(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_following_ids(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = response.parse()
        assert_matches_type(UserRetrieveFollowingIdsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_following_ids(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_following_ids(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = response.parse()
            assert_matches_type(UserRetrieveFollowingIdsResponse, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_following_ids(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.users.with_raw_response.retrieve_following_ids(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_highlights(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_highlights(
            id="id",
        )
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_highlights_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_highlights(
            id="id",
            any_words="anyWords",
            blue_verified_only=True,
            cashtags="cashtags",
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
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_highlights(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_highlights(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = response.parse()
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_highlights(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_highlights(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = response.parse()
            assert_matches_type(PaginatedTweets, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_highlights(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.users.with_raw_response.retrieve_highlights(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_insights(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_insights(
            id="id",
        )
        assert_matches_type(UserRetrieveInsightsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_insights_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_insights(
            id="id",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(UserRetrieveInsightsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_insights(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_insights(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = response.parse()
        assert_matches_type(UserRetrieveInsightsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_insights(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_insights(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = response.parse()
            assert_matches_type(UserRetrieveInsightsResponse, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_insights(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.users.with_raw_response.retrieve_insights(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_likes(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_likes(
            id="id",
        )
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_likes_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_likes(
            id="id",
            any_words="anyWords",
            blue_verified_only=True,
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
            near="near",
            news=True,
            omit="entities,media",
            page_size=1,
            quotes="include",
            quotes_of_tweet_id="quotesOfTweetId",
            replies="include",
            retweets="include",
            retweets_of_tweet_id="retweetsOfTweetId",
            safe=True,
            since_date=parse_date("2019-12-27"),
            since_id="sinceId",
            source="source",
            to_user="toUser",
            until_date=parse_date("2019-12-27"),
            url="url",
            verified_only=True,
            within="within",
            within_time="7d",
        )
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_likes(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_likes(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = response.parse()
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_likes(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_likes(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = response.parse()
            assert_matches_type(PaginatedTweets, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_likes(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.users.with_raw_response.retrieve_likes(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_list_memberships(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_list_memberships(
            id="id",
        )
        assert_matches_type(UserRetrieveListMembershipsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_list_memberships_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_list_memberships(
            id="id",
            cursor="cursor",
            fields="id,text,author.username",
            omit="entities,media",
            page_size=1,
        )
        assert_matches_type(UserRetrieveListMembershipsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_list_memberships(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_list_memberships(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = response.parse()
        assert_matches_type(UserRetrieveListMembershipsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_list_memberships(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_list_memberships(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = response.parse()
            assert_matches_type(UserRetrieveListMembershipsResponse, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_list_memberships(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.users.with_raw_response.retrieve_list_memberships(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_lists(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_lists(
            id="id",
        )
        assert_matches_type(UserRetrieveListsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_lists_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_lists(
            id="id",
            cursor="cursor",
            fields="id,text,author.username",
            omit="entities,media",
            page_size=1,
        )
        assert_matches_type(UserRetrieveListsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_lists(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_lists(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = response.parse()
        assert_matches_type(UserRetrieveListsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_lists(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_lists(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = response.parse()
            assert_matches_type(UserRetrieveListsResponse, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_lists(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.users.with_raw_response.retrieve_lists(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_live(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_live(
            id="id",
        )
        assert_matches_type(UserRetrieveLiveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_live_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_live(
            id="id",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(UserRetrieveLiveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_live(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_live(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = response.parse()
        assert_matches_type(UserRetrieveLiveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_live(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_live(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = response.parse()
            assert_matches_type(UserRetrieveLiveResponse, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_live(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.users.with_raw_response.retrieve_live(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_media(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_media(
            id="id",
        )
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_media_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_media(
            id="id",
            any_words="anyWords",
            blue_verified_only=True,
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
            near="near",
            news=True,
            omit="entities,media",
            page_size=1,
            quotes="include",
            quotes_of_tweet_id="quotesOfTweetId",
            replies="include",
            retweets="include",
            retweets_of_tweet_id="retweetsOfTweetId",
            safe=True,
            since_date=parse_date("2019-12-27"),
            since_id="sinceId",
            source="source",
            to_user="toUser",
            until_date=parse_date("2019-12-27"),
            url="url",
            verified_only=True,
            within="within",
            within_time="7d",
        )
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_media(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_media(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = response.parse()
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_media(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_media(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = response.parse()
            assert_matches_type(PaginatedTweets, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_media(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.users.with_raw_response.retrieve_media(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_mentions(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_mentions(
            id="id",
        )
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_mentions_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_mentions(
            id="id",
            any_words="anyWords",
            blue_verified_only=True,
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
            near="near",
            news=True,
            omit="entities,media",
            page_size=1,
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
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_mentions(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_mentions(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = response.parse()
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_mentions(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_mentions(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = response.parse()
            assert_matches_type(PaginatedTweets, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_mentions(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.users.with_raw_response.retrieve_mentions(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_replies(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_replies(
            id="id",
        )
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_replies_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_replies(
            id="id",
            advanced_query="advancedQuery",
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
            include_parent_tweet=True,
            in_reply_to_tweet_id="inReplyToTweetId",
            keywords="keywords",
            language="language",
            list_id="listId",
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
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_replies(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_replies(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = response.parse()
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_replies(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_replies(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = response.parse()
            assert_matches_type(PaginatedTweets, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_replies(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.users.with_raw_response.retrieve_replies(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_search(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_search(
            q="q",
        )
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_search_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_search(
            q="q",
            bio_contains="bioContains",
            blue_verified_only=True,
            business_email_only=True,
            cursor="cursor",
            email_domains="acme.com,stanford.edu",
            enrich_profiles=True,
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
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_search(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = response.parse()
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_search(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = response.parse()
            assert_matches_type(PaginatedUsers, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_similar(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_similar(
            id="id",
        )
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_similar_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_similar(
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
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_similar(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_similar(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = response.parse()
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_similar(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_similar(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = response.parse()
            assert_matches_type(PaginatedUsers, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_similar(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.users.with_raw_response.retrieve_similar(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_subscriptions(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_subscriptions(
            id="id",
        )
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_subscriptions_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_subscriptions(
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
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_subscriptions(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_subscriptions(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = response.parse()
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_subscriptions(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_subscriptions(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = response.parse()
            assert_matches_type(PaginatedUsers, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_subscriptions(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.users.with_raw_response.retrieve_subscriptions(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_tweets(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_tweets(
            id="id",
        )
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_tweets_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_tweets(
            id="id",
            advanced_query="advancedQuery",
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
            include_parent_tweet=True,
            include_replies=True,
            in_reply_to_tweet_id="inReplyToTweetId",
            keywords="keywords",
            language="language",
            list_id="listId",
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
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_tweets(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_tweets(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = response.parse()
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_tweets(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_tweets(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = response.parse()
            assert_matches_type(PaginatedTweets, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_tweets(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.users.with_raw_response.retrieve_tweets(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_verified_followers(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_verified_followers(
            id="id",
        )
        assert_matches_type(UserRetrieveVerifiedFollowersResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_verified_followers_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_verified_followers(
            id="id",
            after="after",
            bio_contains="bioContains",
            blue_verified_only=True,
            business_email_only=True,
            cursor="cursor",
            email_domains="acme.com,stanford.edu",
            enrich_profiles=True,
            fields="id,text,author.username",
            has_email=True,
            has_location=True,
            has_website=True,
            limit=1,
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
        assert_matches_type(UserRetrieveVerifiedFollowersResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_verified_followers(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_verified_followers(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = response.parse()
        assert_matches_type(UserRetrieveVerifiedFollowersResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_verified_followers(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_verified_followers(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = response.parse()
            assert_matches_type(UserRetrieveVerifiedFollowersResponse, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_verified_followers(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.users.with_raw_response.retrieve_verified_followers(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_translate_bio(self, client: XTwitterScraper) -> None:
        user = client.x.users.translate_bio(
            id="id",
            language="es",
        )
        assert_matches_type(UserTranslateBioResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_translate_bio_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.translate_bio(
            id="id",
            language="es",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(UserTranslateBioResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_translate_bio(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.translate_bio(
            id="id",
            language="es",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = response.parse()
        assert_matches_type(UserTranslateBioResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_translate_bio(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.translate_bio(
            id="id",
            language="es",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = response.parse()
            assert_matches_type(UserTranslateBioResponse, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_translate_bio(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.users.with_raw_response.translate_bio(
                id="",
                language="es",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve(
            id="id",
        )
        assert_matches_type(UserProfile, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve(
            id="id",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(UserProfile, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = await response.parse()
        assert_matches_type(UserProfile, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = await response.parse()
            assert_matches_type(UserProfile, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.users.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove_follower(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.remove_follower(
            id="id",
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(UserRemoveFollowerResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove_follower(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.remove_follower(
            id="id",
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = await response.parse()
        assert_matches_type(UserRemoveFollowerResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove_follower(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.remove_follower(
            id="id",
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = await response.parse()
            assert_matches_type(UserRemoveFollowerResponse, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove_follower(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.users.with_raw_response.remove_follower(
                id="",
                account="@elonmusk",
                idempotency_key="Idempotency-Key",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_affiliates(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_affiliates(
            id="id",
        )
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_affiliates_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_affiliates(
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
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_affiliates(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_affiliates(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = await response.parse()
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_affiliates(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_affiliates(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = await response.parse()
            assert_matches_type(PaginatedUsers, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_affiliates(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.users.with_raw_response.retrieve_affiliates(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_articles(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_articles(
            id="id",
        )
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_articles_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_articles(
            id="id",
            any_words="anyWords",
            blue_verified_only=True,
            cashtags="cashtags",
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
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_articles(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_articles(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = await response.parse()
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_articles(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_articles(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = await response.parse()
            assert_matches_type(PaginatedTweets, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_articles(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.users.with_raw_response.retrieve_articles(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_batch(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_batch()
        assert_matches_type(UserRetrieveBatchResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_batch_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_batch(
            bio_contains="bioContains",
            blue_verified_only=True,
            business_email_only=True,
            email_domains="acme.com,stanford.edu",
            fields="id,text,author.username",
            has_email=True,
            has_location=True,
            has_website=True,
            ids="ids",
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
            usernames="nasa,@OpenAI,x.com/verge",
            verified_only=True,
            verified_type="verifiedType",
        )
        assert_matches_type(UserRetrieveBatchResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_batch(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_batch()

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = await response.parse()
        assert_matches_type(UserRetrieveBatchResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_batch(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_batch() as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = await response.parse()
            assert_matches_type(UserRetrieveBatchResponse, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_batch_tweets(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_batch_tweets()
        assert_matches_type(UserRetrieveBatchTweetsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_batch_tweets_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_batch_tweets(
            fields="id,text,author.username",
            ids="ids",
            omit="entities,media",
            page_size=1,
            usernames="nasa,@OpenAI,x.com/verge",
        )
        assert_matches_type(UserRetrieveBatchTweetsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_batch_tweets(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_batch_tweets()

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = await response.parse()
        assert_matches_type(UserRetrieveBatchTweetsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_batch_tweets(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_batch_tweets() as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = await response.parse()
            assert_matches_type(UserRetrieveBatchTweetsResponse, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_follower_ids(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_follower_ids(
            id="id",
        )
        assert_matches_type(UserRetrieveFollowerIdsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_follower_ids_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_follower_ids(
            id="id",
            cursor="cursor",
            page_size=1,
        )
        assert_matches_type(UserRetrieveFollowerIdsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_follower_ids(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_follower_ids(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = await response.parse()
        assert_matches_type(UserRetrieveFollowerIdsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_follower_ids(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_follower_ids(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = await response.parse()
            assert_matches_type(UserRetrieveFollowerIdsResponse, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_follower_ids(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.users.with_raw_response.retrieve_follower_ids(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_followers(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_followers(
            id="id",
        )
        assert_matches_type(UserRetrieveFollowersResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_followers_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_followers(
            id="id",
            after="after",
            bio_contains="bioContains",
            blue_verified_only=True,
            business_email_only=True,
            cursor="cursor",
            email_domains="acme.com,stanford.edu",
            enrich_profiles=True,
            fields="id,text,author.username",
            has_email=True,
            has_location=True,
            has_website=True,
            limit=1,
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
        assert_matches_type(UserRetrieveFollowersResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_followers(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_followers(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = await response.parse()
        assert_matches_type(UserRetrieveFollowersResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_followers(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_followers(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = await response.parse()
            assert_matches_type(UserRetrieveFollowersResponse, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_followers(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.users.with_raw_response.retrieve_followers(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_followers_you_know(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_followers_you_know(
            id="id",
        )
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_followers_you_know_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_followers_you_know(
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
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_followers_you_know(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_followers_you_know(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = await response.parse()
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_followers_you_know(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_followers_you_know(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = await response.parse()
            assert_matches_type(PaginatedUsers, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_followers_you_know(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.users.with_raw_response.retrieve_followers_you_know(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_following(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_following(
            id="id",
        )
        assert_matches_type(UserRetrieveFollowingResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_following_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_following(
            id="id",
            after="after",
            bio_contains="bioContains",
            blue_verified_only=True,
            business_email_only=True,
            cursor="cursor",
            email_domains="acme.com,stanford.edu",
            enrich_profiles=True,
            fields="id,text,author.username",
            has_email=True,
            has_location=True,
            has_website=True,
            limit=1,
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
        assert_matches_type(UserRetrieveFollowingResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_following(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_following(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = await response.parse()
        assert_matches_type(UserRetrieveFollowingResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_following(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_following(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = await response.parse()
            assert_matches_type(UserRetrieveFollowingResponse, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_following(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.users.with_raw_response.retrieve_following(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_following_ids(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_following_ids(
            id="id",
        )
        assert_matches_type(UserRetrieveFollowingIdsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_following_ids_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_following_ids(
            id="id",
            cursor="cursor",
            page_size=1,
        )
        assert_matches_type(UserRetrieveFollowingIdsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_following_ids(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_following_ids(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = await response.parse()
        assert_matches_type(UserRetrieveFollowingIdsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_following_ids(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_following_ids(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = await response.parse()
            assert_matches_type(UserRetrieveFollowingIdsResponse, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_following_ids(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.users.with_raw_response.retrieve_following_ids(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_highlights(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_highlights(
            id="id",
        )
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_highlights_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_highlights(
            id="id",
            any_words="anyWords",
            blue_verified_only=True,
            cashtags="cashtags",
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
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_highlights(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_highlights(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = await response.parse()
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_highlights(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_highlights(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = await response.parse()
            assert_matches_type(PaginatedTweets, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_highlights(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.users.with_raw_response.retrieve_highlights(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_insights(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_insights(
            id="id",
        )
        assert_matches_type(UserRetrieveInsightsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_insights_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_insights(
            id="id",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(UserRetrieveInsightsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_insights(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_insights(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = await response.parse()
        assert_matches_type(UserRetrieveInsightsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_insights(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_insights(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = await response.parse()
            assert_matches_type(UserRetrieveInsightsResponse, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_insights(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.users.with_raw_response.retrieve_insights(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_likes(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_likes(
            id="id",
        )
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_likes_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_likes(
            id="id",
            any_words="anyWords",
            blue_verified_only=True,
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
            near="near",
            news=True,
            omit="entities,media",
            page_size=1,
            quotes="include",
            quotes_of_tweet_id="quotesOfTweetId",
            replies="include",
            retweets="include",
            retweets_of_tweet_id="retweetsOfTweetId",
            safe=True,
            since_date=parse_date("2019-12-27"),
            since_id="sinceId",
            source="source",
            to_user="toUser",
            until_date=parse_date("2019-12-27"),
            url="url",
            verified_only=True,
            within="within",
            within_time="7d",
        )
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_likes(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_likes(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = await response.parse()
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_likes(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_likes(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = await response.parse()
            assert_matches_type(PaginatedTweets, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_likes(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.users.with_raw_response.retrieve_likes(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_list_memberships(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_list_memberships(
            id="id",
        )
        assert_matches_type(UserRetrieveListMembershipsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_list_memberships_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_list_memberships(
            id="id",
            cursor="cursor",
            fields="id,text,author.username",
            omit="entities,media",
            page_size=1,
        )
        assert_matches_type(UserRetrieveListMembershipsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_list_memberships(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_list_memberships(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = await response.parse()
        assert_matches_type(UserRetrieveListMembershipsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_list_memberships(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_list_memberships(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = await response.parse()
            assert_matches_type(UserRetrieveListMembershipsResponse, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_list_memberships(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.users.with_raw_response.retrieve_list_memberships(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_lists(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_lists(
            id="id",
        )
        assert_matches_type(UserRetrieveListsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_lists_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_lists(
            id="id",
            cursor="cursor",
            fields="id,text,author.username",
            omit="entities,media",
            page_size=1,
        )
        assert_matches_type(UserRetrieveListsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_lists(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_lists(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = await response.parse()
        assert_matches_type(UserRetrieveListsResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_lists(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_lists(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = await response.parse()
            assert_matches_type(UserRetrieveListsResponse, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_lists(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.users.with_raw_response.retrieve_lists(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_live(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_live(
            id="id",
        )
        assert_matches_type(UserRetrieveLiveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_live_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_live(
            id="id",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(UserRetrieveLiveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_live(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_live(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = await response.parse()
        assert_matches_type(UserRetrieveLiveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_live(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_live(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = await response.parse()
            assert_matches_type(UserRetrieveLiveResponse, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_live(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.users.with_raw_response.retrieve_live(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_media(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_media(
            id="id",
        )
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_media_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_media(
            id="id",
            any_words="anyWords",
            blue_verified_only=True,
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
            near="near",
            news=True,
            omit="entities,media",
            page_size=1,
            quotes="include",
            quotes_of_tweet_id="quotesOfTweetId",
            replies="include",
            retweets="include",
            retweets_of_tweet_id="retweetsOfTweetId",
            safe=True,
            since_date=parse_date("2019-12-27"),
            since_id="sinceId",
            source="source",
            to_user="toUser",
            until_date=parse_date("2019-12-27"),
            url="url",
            verified_only=True,
            within="within",
            within_time="7d",
        )
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_media(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_media(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = await response.parse()
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_media(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_media(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = await response.parse()
            assert_matches_type(PaginatedTweets, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_media(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.users.with_raw_response.retrieve_media(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_mentions(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_mentions(
            id="id",
        )
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_mentions_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_mentions(
            id="id",
            any_words="anyWords",
            blue_verified_only=True,
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
            near="near",
            news=True,
            omit="entities,media",
            page_size=1,
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
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_mentions(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_mentions(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = await response.parse()
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_mentions(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_mentions(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = await response.parse()
            assert_matches_type(PaginatedTweets, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_mentions(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.users.with_raw_response.retrieve_mentions(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_replies(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_replies(
            id="id",
        )
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_replies_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_replies(
            id="id",
            advanced_query="advancedQuery",
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
            include_parent_tweet=True,
            in_reply_to_tweet_id="inReplyToTweetId",
            keywords="keywords",
            language="language",
            list_id="listId",
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
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_replies(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_replies(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = await response.parse()
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_replies(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_replies(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = await response.parse()
            assert_matches_type(PaginatedTweets, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_replies(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.users.with_raw_response.retrieve_replies(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_search(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_search(
            q="q",
        )
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_search_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_search(
            q="q",
            bio_contains="bioContains",
            blue_verified_only=True,
            business_email_only=True,
            cursor="cursor",
            email_domains="acme.com,stanford.edu",
            enrich_profiles=True,
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
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_search(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = await response.parse()
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_search(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = await response.parse()
            assert_matches_type(PaginatedUsers, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_similar(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_similar(
            id="id",
        )
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_similar_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_similar(
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
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_similar(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_similar(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = await response.parse()
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_similar(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_similar(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = await response.parse()
            assert_matches_type(PaginatedUsers, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_similar(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.users.with_raw_response.retrieve_similar(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_subscriptions(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_subscriptions(
            id="id",
        )
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_subscriptions_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_subscriptions(
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
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_subscriptions(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_subscriptions(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = await response.parse()
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_subscriptions(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_subscriptions(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = await response.parse()
            assert_matches_type(PaginatedUsers, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_subscriptions(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.users.with_raw_response.retrieve_subscriptions(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_tweets(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_tweets(
            id="id",
        )
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_tweets_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_tweets(
            id="id",
            advanced_query="advancedQuery",
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
            include_parent_tweet=True,
            include_replies=True,
            in_reply_to_tweet_id="inReplyToTweetId",
            keywords="keywords",
            language="language",
            list_id="listId",
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
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_tweets(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_tweets(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = await response.parse()
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_tweets(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_tweets(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = await response.parse()
            assert_matches_type(PaginatedTweets, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_tweets(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.users.with_raw_response.retrieve_tweets(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_verified_followers(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_verified_followers(
            id="id",
        )
        assert_matches_type(UserRetrieveVerifiedFollowersResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_verified_followers_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_verified_followers(
            id="id",
            after="after",
            bio_contains="bioContains",
            blue_verified_only=True,
            business_email_only=True,
            cursor="cursor",
            email_domains="acme.com,stanford.edu",
            enrich_profiles=True,
            fields="id,text,author.username",
            has_email=True,
            has_location=True,
            has_website=True,
            limit=1,
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
        assert_matches_type(UserRetrieveVerifiedFollowersResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_verified_followers(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_verified_followers(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = await response.parse()
        assert_matches_type(UserRetrieveVerifiedFollowersResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_verified_followers(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_verified_followers(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = await response.parse()
            assert_matches_type(UserRetrieveVerifiedFollowersResponse, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_verified_followers(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.users.with_raw_response.retrieve_verified_followers(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_translate_bio(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.translate_bio(
            id="id",
            language="es",
        )
        assert_matches_type(UserTranslateBioResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_translate_bio_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.translate_bio(
            id="id",
            language="es",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(UserTranslateBioResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_translate_bio(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.translate_bio(
            id="id",
            language="es",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        user = await response.parse()
        assert_matches_type(UserTranslateBioResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_translate_bio(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.translate_bio(
            id="id",
            language="es",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            user = await response.parse()
            assert_matches_type(UserTranslateBioResponse, user, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_translate_bio(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.users.with_raw_response.translate_bio(
                id="",
                language="es",
            )
