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
    TweetListResponse,
    TweetEmbedResponse,
    TweetCreateResponse,
    TweetDeleteResponse,
    TweetSearchResponse,
    TweetRetrieveResponse,
    TweetTranslateResponse,
    TweetGetRepliesResponse,
    TweetCheckRepostResponse,
    TweetGetInsightsResponse,
    TweetGetSubtitlesResponse,
    TweetResolveLinksResponse,
    TweetGetRetweeterIdsResponse,
)
from x_twitter_scraper.types.shared import PaginatedUsers, PaginatedTweets

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTweets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.create(
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(TweetCreateResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.create(
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
            community_id="1500000000000000000",
            is_note_tweet=False,
            media=["https://example.com/video.mp4"],
            reply_to_tweet_id="1880000000000000000",
            text="Just launched our new feature!",
        )
        assert_matches_type(TweetCreateResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.with_raw_response.create(
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = response.parse()
        assert_matches_type(TweetCreateResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: XTwitterScraper) -> None:
        with client.x.tweets.with_streaming_response.create(
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = response.parse()
            assert_matches_type(TweetCreateResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.retrieve(
            id="id",
        )
        assert_matches_type(TweetRetrieveResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.retrieve(
            id="id",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(TweetRetrieveResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = response.parse()
        assert_matches_type(TweetRetrieveResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: XTwitterScraper) -> None:
        with client.x.tweets.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = response.parse()
            assert_matches_type(TweetRetrieveResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.tweets.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.list(
            ids="ids",
        )
        assert_matches_type(TweetListResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.list(
            ids="ids",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(TweetListResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.with_raw_response.list(
            ids="ids",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = response.parse()
        assert_matches_type(TweetListResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: XTwitterScraper) -> None:
        with client.x.tweets.with_streaming_response.list(
            ids="ids",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = response.parse()
            assert_matches_type(TweetListResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.delete(
            id="id",
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(TweetDeleteResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.with_raw_response.delete(
            id="id",
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = response.parse()
        assert_matches_type(TweetDeleteResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: XTwitterScraper) -> None:
        with client.x.tweets.with_streaming_response.delete(
            id="id",
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = response.parse()
            assert_matches_type(TweetDeleteResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.tweets.with_raw_response.delete(
                id="",
                account="@elonmusk",
                idempotency_key="Idempotency-Key",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check_repost(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.check_repost(
            id="id",
            user="nasa",
        )
        assert_matches_type(TweetCheckRepostResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check_repost_with_all_params(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.check_repost(
            id="id",
            user="nasa",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(TweetCheckRepostResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_check_repost(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.with_raw_response.check_repost(
            id="id",
            user="nasa",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = response.parse()
        assert_matches_type(TweetCheckRepostResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_check_repost(self, client: XTwitterScraper) -> None:
        with client.x.tweets.with_streaming_response.check_repost(
            id="id",
            user="nasa",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = response.parse()
            assert_matches_type(TweetCheckRepostResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_check_repost(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.tweets.with_raw_response.check_repost(
                id="",
                user="nasa",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_embed(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.embed(
            id="id",
        )
        assert_matches_type(TweetEmbedResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_embed_with_all_params(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.embed(
            id="id",
            fields="id,text,author.username",
            hide_media=True,
            hide_thread=True,
            omit="entities,media",
            omit_script=True,
            theme="light",
        )
        assert_matches_type(TweetEmbedResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_embed(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.with_raw_response.embed(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = response.parse()
        assert_matches_type(TweetEmbedResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_embed(self, client: XTwitterScraper) -> None:
        with client.x.tweets.with_streaming_response.embed(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = response.parse()
            assert_matches_type(TweetEmbedResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_embed(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.tweets.with_raw_response.embed(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_favoriters(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.get_favoriters(
            id="id",
        )
        assert_matches_type(PaginatedUsers, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_favoriters_with_all_params(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.get_favoriters(
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
        assert_matches_type(PaginatedUsers, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_favoriters(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.with_raw_response.get_favoriters(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = response.parse()
        assert_matches_type(PaginatedUsers, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_favoriters(self, client: XTwitterScraper) -> None:
        with client.x.tweets.with_streaming_response.get_favoriters(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = response.parse()
            assert_matches_type(PaginatedUsers, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_favoriters(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.tweets.with_raw_response.get_favoriters(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_hidden_replies(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.get_hidden_replies(
            id="id",
        )
        assert_matches_type(PaginatedTweets, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_hidden_replies_with_all_params(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.get_hidden_replies(
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
        assert_matches_type(PaginatedTweets, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_hidden_replies(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.with_raw_response.get_hidden_replies(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = response.parse()
        assert_matches_type(PaginatedTweets, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_hidden_replies(self, client: XTwitterScraper) -> None:
        with client.x.tweets.with_streaming_response.get_hidden_replies(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = response.parse()
            assert_matches_type(PaginatedTweets, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_hidden_replies(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.tweets.with_raw_response.get_hidden_replies(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_insights(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.get_insights(
            id="id",
        )
        assert_matches_type(TweetGetInsightsResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_insights_with_all_params(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.get_insights(
            id="id",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(TweetGetInsightsResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_insights(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.with_raw_response.get_insights(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = response.parse()
        assert_matches_type(TweetGetInsightsResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_insights(self, client: XTwitterScraper) -> None:
        with client.x.tweets.with_streaming_response.get_insights(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = response.parse()
            assert_matches_type(TweetGetInsightsResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_insights(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.tweets.with_raw_response.get_insights(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_quotes(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.get_quotes(
            id="id",
        )
        assert_matches_type(PaginatedTweets, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_quotes_with_all_params(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.get_quotes(
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
            query_type="Latest",
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
        assert_matches_type(PaginatedTweets, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_quotes(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.with_raw_response.get_quotes(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = response.parse()
        assert_matches_type(PaginatedTweets, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_quotes(self, client: XTwitterScraper) -> None:
        with client.x.tweets.with_streaming_response.get_quotes(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = response.parse()
            assert_matches_type(PaginatedTweets, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_quotes(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.tweets.with_raw_response.get_quotes(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_replies(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.get_replies(
            id="id",
        )
        assert_matches_type(TweetGetRepliesResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_replies_with_all_params(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.get_replies(
            id="id",
            after="after",
            any_words="anyWords",
            blue_verified_only=True,
            card_name="cardName",
            cashtags="cashtags",
            conversation_id="conversationId",
            cursor="cursor",
            exact_phrase="exactPhrase",
            exclude_original_author=True,
            exclude_source="excludeSource",
            exclude_words="excludeWords",
            fields="id,text,author.username",
            from_user="fromUser",
            geocode="geocode",
            hashtags="hashtags",
            has_media_only=True,
            include_hidden=True,
            include_original_post=True,
            in_reply_to_tweet_id="inReplyToTweetId",
            language="language",
            limit=1,
            max_depth=1,
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
            quotes="include",
            quotes_of_tweet_id="quotesOfTweetId",
            replies="include",
            retweets="include",
            retweets_of_tweet_id="retweetsOfTweetId",
            safe=True,
            scope="all",
            since_date=parse_date("2019-12-27"),
            since_id="sinceId",
            since_time="sinceTime",
            sort="relevance",
            source="source",
            to_user="toUser",
            until_date=parse_date("2019-12-27"),
            until_time="untilTime",
            url="url",
            verified_only=True,
            within="within",
            within_time="7d",
        )
        assert_matches_type(TweetGetRepliesResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_replies(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.with_raw_response.get_replies(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = response.parse()
        assert_matches_type(TweetGetRepliesResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_replies(self, client: XTwitterScraper) -> None:
        with client.x.tweets.with_streaming_response.get_replies(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = response.parse()
            assert_matches_type(TweetGetRepliesResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_replies(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.tweets.with_raw_response.get_replies(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_retweeter_ids(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.get_retweeter_ids(
            id="id",
        )
        assert_matches_type(TweetGetRetweeterIdsResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_retweeter_ids_with_all_params(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.get_retweeter_ids(
            id="id",
            cursor="cursor",
            page_size=1,
        )
        assert_matches_type(TweetGetRetweeterIdsResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_retweeter_ids(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.with_raw_response.get_retweeter_ids(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = response.parse()
        assert_matches_type(TweetGetRetweeterIdsResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_retweeter_ids(self, client: XTwitterScraper) -> None:
        with client.x.tweets.with_streaming_response.get_retweeter_ids(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = response.parse()
            assert_matches_type(TweetGetRetweeterIdsResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_retweeter_ids(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.tweets.with_raw_response.get_retweeter_ids(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_retweeters(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.get_retweeters(
            id="id",
        )
        assert_matches_type(PaginatedUsers, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_retweeters_with_all_params(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.get_retweeters(
            id="id",
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
            include_retweet_timestamp=True,
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
        assert_matches_type(PaginatedUsers, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_retweeters(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.with_raw_response.get_retweeters(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = response.parse()
        assert_matches_type(PaginatedUsers, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_retweeters(self, client: XTwitterScraper) -> None:
        with client.x.tweets.with_streaming_response.get_retweeters(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = response.parse()
            assert_matches_type(PaginatedUsers, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_retweeters(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.tweets.with_raw_response.get_retweeters(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_subtitles(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.get_subtitles(
            id="id",
        )
        assert_matches_type(TweetGetSubtitlesResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_subtitles_with_all_params(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.get_subtitles(
            id="id",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(TweetGetSubtitlesResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_subtitles(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.with_raw_response.get_subtitles(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = response.parse()
        assert_matches_type(TweetGetSubtitlesResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_subtitles(self, client: XTwitterScraper) -> None:
        with client.x.tweets.with_streaming_response.get_subtitles(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = response.parse()
            assert_matches_type(TweetGetSubtitlesResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_subtitles(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.tweets.with_raw_response.get_subtitles(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_thread(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.get_thread(
            id="id",
        )
        assert_matches_type(PaginatedTweets, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_thread_with_all_params(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.get_thread(
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
        assert_matches_type(PaginatedTweets, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_thread(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.with_raw_response.get_thread(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = response.parse()
        assert_matches_type(PaginatedTweets, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_thread(self, client: XTwitterScraper) -> None:
        with client.x.tweets.with_streaming_response.get_thread(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = response.parse()
            assert_matches_type(PaginatedTweets, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_thread(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.tweets.with_raw_response.get_thread(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_top(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.list_top()
        assert_matches_type(PaginatedTweets, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_top_with_all_params(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.list_top(
            country="US",
            cursor="cursor",
            fields="id,text,author.username",
            language="en",
            metric="likes",
            omit="entities,media",
            page_size=1,
            window="day",
        )
        assert_matches_type(PaginatedTweets, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_top(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.with_raw_response.list_top()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = response.parse()
        assert_matches_type(PaginatedTweets, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_top(self, client: XTwitterScraper) -> None:
        with client.x.tweets.with_streaming_response.list_top() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = response.parse()
            assert_matches_type(PaginatedTweets, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_resolve_links(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.resolve_links(
            urls="https://t.co/Xe1nm2pkSX",
        )
        assert_matches_type(TweetResolveLinksResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_resolve_links_with_all_params(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.resolve_links(
            urls="https://t.co/Xe1nm2pkSX",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(TweetResolveLinksResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_resolve_links(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.with_raw_response.resolve_links(
            urls="https://t.co/Xe1nm2pkSX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = response.parse()
        assert_matches_type(TweetResolveLinksResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_resolve_links(self, client: XTwitterScraper) -> None:
        with client.x.tweets.with_streaming_response.resolve_links(
            urls="https://t.co/Xe1nm2pkSX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = response.parse()
            assert_matches_type(TweetResolveLinksResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.search(
            q="q",
        )
        assert_matches_type(TweetSearchResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.search(
            q="q",
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
            in_reply_to_tweet_id="inReplyToTweetId",
            keywords="keywords",
            language="language",
            limit=1,
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
            place="place",
            place_country="placeCountry",
            point_radius="pointRadius",
            query_type="queryType",
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
        assert_matches_type(TweetSearchResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.with_raw_response.search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = response.parse()
        assert_matches_type(TweetSearchResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: XTwitterScraper) -> None:
        with client.x.tweets.with_streaming_response.search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = response.parse()
            assert_matches_type(TweetSearchResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_translate(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.translate(
            id="id",
            language="tr",
        )
        assert_matches_type(TweetTranslateResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_translate_with_all_params(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.translate(
            id="id",
            language="tr",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(TweetTranslateResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_translate(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.with_raw_response.translate(
            id="id",
            language="tr",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = response.parse()
        assert_matches_type(TweetTranslateResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_translate(self, client: XTwitterScraper) -> None:
        with client.x.tweets.with_streaming_response.translate(
            id="id",
            language="tr",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = response.parse()
            assert_matches_type(TweetTranslateResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_translate(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.tweets.with_raw_response.translate(
                id="",
                language="tr",
            )


class TestAsyncTweets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.create(
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(TweetCreateResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.create(
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
            community_id="1500000000000000000",
            is_note_tweet=False,
            media=["https://example.com/video.mp4"],
            reply_to_tweet_id="1880000000000000000",
            text="Just launched our new feature!",
        )
        assert_matches_type(TweetCreateResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.with_raw_response.create(
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = await response.parse()
        assert_matches_type(TweetCreateResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.with_streaming_response.create(
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = await response.parse()
            assert_matches_type(TweetCreateResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.retrieve(
            id="id",
        )
        assert_matches_type(TweetRetrieveResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.retrieve(
            id="id",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(TweetRetrieveResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = await response.parse()
        assert_matches_type(TweetRetrieveResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = await response.parse()
            assert_matches_type(TweetRetrieveResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.tweets.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.list(
            ids="ids",
        )
        assert_matches_type(TweetListResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.list(
            ids="ids",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(TweetListResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.with_raw_response.list(
            ids="ids",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = await response.parse()
        assert_matches_type(TweetListResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.with_streaming_response.list(
            ids="ids",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = await response.parse()
            assert_matches_type(TweetListResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.delete(
            id="id",
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(TweetDeleteResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.with_raw_response.delete(
            id="id",
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = await response.parse()
        assert_matches_type(TweetDeleteResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.with_streaming_response.delete(
            id="id",
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = await response.parse()
            assert_matches_type(TweetDeleteResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.tweets.with_raw_response.delete(
                id="",
                account="@elonmusk",
                idempotency_key="Idempotency-Key",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check_repost(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.check_repost(
            id="id",
            user="nasa",
        )
        assert_matches_type(TweetCheckRepostResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check_repost_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.check_repost(
            id="id",
            user="nasa",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(TweetCheckRepostResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_check_repost(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.with_raw_response.check_repost(
            id="id",
            user="nasa",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = await response.parse()
        assert_matches_type(TweetCheckRepostResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_check_repost(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.with_streaming_response.check_repost(
            id="id",
            user="nasa",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = await response.parse()
            assert_matches_type(TweetCheckRepostResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_check_repost(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.tweets.with_raw_response.check_repost(
                id="",
                user="nasa",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_embed(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.embed(
            id="id",
        )
        assert_matches_type(TweetEmbedResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_embed_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.embed(
            id="id",
            fields="id,text,author.username",
            hide_media=True,
            hide_thread=True,
            omit="entities,media",
            omit_script=True,
            theme="light",
        )
        assert_matches_type(TweetEmbedResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_embed(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.with_raw_response.embed(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = await response.parse()
        assert_matches_type(TweetEmbedResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_embed(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.with_streaming_response.embed(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = await response.parse()
            assert_matches_type(TweetEmbedResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_embed(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.tweets.with_raw_response.embed(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_favoriters(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.get_favoriters(
            id="id",
        )
        assert_matches_type(PaginatedUsers, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_favoriters_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.get_favoriters(
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
        assert_matches_type(PaginatedUsers, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_favoriters(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.with_raw_response.get_favoriters(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = await response.parse()
        assert_matches_type(PaginatedUsers, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_favoriters(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.with_streaming_response.get_favoriters(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = await response.parse()
            assert_matches_type(PaginatedUsers, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_favoriters(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.tweets.with_raw_response.get_favoriters(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_hidden_replies(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.get_hidden_replies(
            id="id",
        )
        assert_matches_type(PaginatedTweets, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_hidden_replies_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.get_hidden_replies(
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
        assert_matches_type(PaginatedTweets, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_hidden_replies(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.with_raw_response.get_hidden_replies(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = await response.parse()
        assert_matches_type(PaginatedTweets, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_hidden_replies(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.with_streaming_response.get_hidden_replies(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = await response.parse()
            assert_matches_type(PaginatedTweets, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_hidden_replies(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.tweets.with_raw_response.get_hidden_replies(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_insights(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.get_insights(
            id="id",
        )
        assert_matches_type(TweetGetInsightsResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_insights_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.get_insights(
            id="id",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(TweetGetInsightsResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_insights(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.with_raw_response.get_insights(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = await response.parse()
        assert_matches_type(TweetGetInsightsResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_insights(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.with_streaming_response.get_insights(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = await response.parse()
            assert_matches_type(TweetGetInsightsResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_insights(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.tweets.with_raw_response.get_insights(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_quotes(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.get_quotes(
            id="id",
        )
        assert_matches_type(PaginatedTweets, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_quotes_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.get_quotes(
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
            query_type="Latest",
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
        assert_matches_type(PaginatedTweets, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_quotes(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.with_raw_response.get_quotes(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = await response.parse()
        assert_matches_type(PaginatedTweets, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_quotes(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.with_streaming_response.get_quotes(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = await response.parse()
            assert_matches_type(PaginatedTweets, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_quotes(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.tweets.with_raw_response.get_quotes(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_replies(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.get_replies(
            id="id",
        )
        assert_matches_type(TweetGetRepliesResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_replies_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.get_replies(
            id="id",
            after="after",
            any_words="anyWords",
            blue_verified_only=True,
            card_name="cardName",
            cashtags="cashtags",
            conversation_id="conversationId",
            cursor="cursor",
            exact_phrase="exactPhrase",
            exclude_original_author=True,
            exclude_source="excludeSource",
            exclude_words="excludeWords",
            fields="id,text,author.username",
            from_user="fromUser",
            geocode="geocode",
            hashtags="hashtags",
            has_media_only=True,
            include_hidden=True,
            include_original_post=True,
            in_reply_to_tweet_id="inReplyToTweetId",
            language="language",
            limit=1,
            max_depth=1,
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
            quotes="include",
            quotes_of_tweet_id="quotesOfTweetId",
            replies="include",
            retweets="include",
            retweets_of_tweet_id="retweetsOfTweetId",
            safe=True,
            scope="all",
            since_date=parse_date("2019-12-27"),
            since_id="sinceId",
            since_time="sinceTime",
            sort="relevance",
            source="source",
            to_user="toUser",
            until_date=parse_date("2019-12-27"),
            until_time="untilTime",
            url="url",
            verified_only=True,
            within="within",
            within_time="7d",
        )
        assert_matches_type(TweetGetRepliesResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_replies(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.with_raw_response.get_replies(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = await response.parse()
        assert_matches_type(TweetGetRepliesResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_replies(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.with_streaming_response.get_replies(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = await response.parse()
            assert_matches_type(TweetGetRepliesResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_replies(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.tweets.with_raw_response.get_replies(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_retweeter_ids(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.get_retweeter_ids(
            id="id",
        )
        assert_matches_type(TweetGetRetweeterIdsResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_retweeter_ids_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.get_retweeter_ids(
            id="id",
            cursor="cursor",
            page_size=1,
        )
        assert_matches_type(TweetGetRetweeterIdsResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_retweeter_ids(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.with_raw_response.get_retweeter_ids(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = await response.parse()
        assert_matches_type(TweetGetRetweeterIdsResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_retweeter_ids(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.with_streaming_response.get_retweeter_ids(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = await response.parse()
            assert_matches_type(TweetGetRetweeterIdsResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_retweeter_ids(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.tweets.with_raw_response.get_retweeter_ids(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_retweeters(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.get_retweeters(
            id="id",
        )
        assert_matches_type(PaginatedUsers, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_retweeters_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.get_retweeters(
            id="id",
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
            include_retweet_timestamp=True,
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
        assert_matches_type(PaginatedUsers, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_retweeters(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.with_raw_response.get_retweeters(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = await response.parse()
        assert_matches_type(PaginatedUsers, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_retweeters(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.with_streaming_response.get_retweeters(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = await response.parse()
            assert_matches_type(PaginatedUsers, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_retweeters(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.tweets.with_raw_response.get_retweeters(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_subtitles(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.get_subtitles(
            id="id",
        )
        assert_matches_type(TweetGetSubtitlesResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_subtitles_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.get_subtitles(
            id="id",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(TweetGetSubtitlesResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_subtitles(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.with_raw_response.get_subtitles(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = await response.parse()
        assert_matches_type(TweetGetSubtitlesResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_subtitles(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.with_streaming_response.get_subtitles(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = await response.parse()
            assert_matches_type(TweetGetSubtitlesResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_subtitles(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.tweets.with_raw_response.get_subtitles(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_thread(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.get_thread(
            id="id",
        )
        assert_matches_type(PaginatedTweets, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_thread_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.get_thread(
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
        assert_matches_type(PaginatedTweets, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_thread(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.with_raw_response.get_thread(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = await response.parse()
        assert_matches_type(PaginatedTweets, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_thread(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.with_streaming_response.get_thread(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = await response.parse()
            assert_matches_type(PaginatedTweets, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_thread(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.tweets.with_raw_response.get_thread(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_top(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.list_top()
        assert_matches_type(PaginatedTweets, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_top_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.list_top(
            country="US",
            cursor="cursor",
            fields="id,text,author.username",
            language="en",
            metric="likes",
            omit="entities,media",
            page_size=1,
            window="day",
        )
        assert_matches_type(PaginatedTweets, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_top(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.with_raw_response.list_top()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = await response.parse()
        assert_matches_type(PaginatedTweets, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_top(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.with_streaming_response.list_top() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = await response.parse()
            assert_matches_type(PaginatedTweets, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_resolve_links(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.resolve_links(
            urls="https://t.co/Xe1nm2pkSX",
        )
        assert_matches_type(TweetResolveLinksResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_resolve_links_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.resolve_links(
            urls="https://t.co/Xe1nm2pkSX",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(TweetResolveLinksResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_resolve_links(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.with_raw_response.resolve_links(
            urls="https://t.co/Xe1nm2pkSX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = await response.parse()
        assert_matches_type(TweetResolveLinksResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_resolve_links(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.with_streaming_response.resolve_links(
            urls="https://t.co/Xe1nm2pkSX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = await response.parse()
            assert_matches_type(TweetResolveLinksResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.search(
            q="q",
        )
        assert_matches_type(TweetSearchResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.search(
            q="q",
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
            in_reply_to_tweet_id="inReplyToTweetId",
            keywords="keywords",
            language="language",
            limit=1,
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
            place="place",
            place_country="placeCountry",
            point_radius="pointRadius",
            query_type="queryType",
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
        assert_matches_type(TweetSearchResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.with_raw_response.search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = await response.parse()
        assert_matches_type(TweetSearchResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.with_streaming_response.search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = await response.parse()
            assert_matches_type(TweetSearchResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_translate(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.translate(
            id="id",
            language="tr",
        )
        assert_matches_type(TweetTranslateResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_translate_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.translate(
            id="id",
            language="tr",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(TweetTranslateResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_translate(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.with_raw_response.translate(
            id="id",
            language="tr",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = await response.parse()
        assert_matches_type(TweetTranslateResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_translate(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.with_streaming_response.translate(
            id="id",
            language="tr",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = await response.parse()
            assert_matches_type(TweetTranslateResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_translate(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.tweets.with_raw_response.translate(
                id="",
                language="tr",
            )
