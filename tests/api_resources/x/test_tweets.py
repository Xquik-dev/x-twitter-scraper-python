# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types.x import (
    TweetCreateResponse,
    TweetDeleteResponse,
    TweetSearchResponse,
    TweetRetrieveResponse,
    TweetGetQuotesResponse,
    TweetGetThreadResponse,
    TweetGetRepliesResponse,
    TweetGetFavoritersResponse,
    TweetGetRetweetersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTweets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.create(
            account="account",
            text="text",
        )
        assert_matches_type(TweetCreateResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.create(
            account="account",
            text="text",
            attachment_url="attachment_url",
            community_id="community_id",
            is_note_tweet=True,
            media_ids=["string"],
            reply_to_tweet_id="reply_to_tweet_id",
        )
        assert_matches_type(TweetCreateResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.with_raw_response.create(
            account="account",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = response.parse()
        assert_matches_type(TweetCreateResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: XTwitterScraper) -> None:
        with client.x.tweets.with_streaming_response.create(
            account="account",
            text="text",
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
            "tweetId",
        )
        assert_matches_type(TweetRetrieveResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.with_raw_response.retrieve(
            "tweetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = response.parse()
        assert_matches_type(TweetRetrieveResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: XTwitterScraper) -> None:
        with client.x.tweets.with_streaming_response.retrieve(
            "tweetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = response.parse()
            assert_matches_type(TweetRetrieveResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tweet_id` but received ''"):
            client.x.tweets.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.list(
            ids="ids",
        )
        assert tweet is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.with_raw_response.list(
            ids="ids",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = response.parse()
        assert tweet is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: XTwitterScraper) -> None:
        with client.x.tweets.with_streaming_response.list(
            ids="ids",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = response.parse()
            assert tweet is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.delete(
            tweet_id="tweetId",
            account="account",
        )
        assert_matches_type(TweetDeleteResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.with_raw_response.delete(
            tweet_id="tweetId",
            account="account",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = response.parse()
        assert_matches_type(TweetDeleteResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: XTwitterScraper) -> None:
        with client.x.tweets.with_streaming_response.delete(
            tweet_id="tweetId",
            account="account",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = response.parse()
            assert_matches_type(TweetDeleteResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tweet_id` but received ''"):
            client.x.tweets.with_raw_response.delete(
                tweet_id="",
                account="account",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_favoriters(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.get_favoriters(
            id="id",
        )
        assert_matches_type(TweetGetFavoritersResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_favoriters_with_all_params(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.get_favoriters(
            id="id",
            cursor="cursor",
        )
        assert_matches_type(TweetGetFavoritersResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_favoriters(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.with_raw_response.get_favoriters(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = response.parse()
        assert_matches_type(TweetGetFavoritersResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_favoriters(self, client: XTwitterScraper) -> None:
        with client.x.tweets.with_streaming_response.get_favoriters(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = response.parse()
            assert_matches_type(TweetGetFavoritersResponse, tweet, path=["response"])

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
    def test_method_get_quotes(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.get_quotes(
            id="id",
        )
        assert_matches_type(TweetGetQuotesResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_quotes_with_all_params(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.get_quotes(
            id="id",
            cursor="cursor",
            include_replies=True,
            since_time="sinceTime",
            until_time="untilTime",
        )
        assert_matches_type(TweetGetQuotesResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_quotes(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.with_raw_response.get_quotes(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = response.parse()
        assert_matches_type(TweetGetQuotesResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_quotes(self, client: XTwitterScraper) -> None:
        with client.x.tweets.with_streaming_response.get_quotes(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = response.parse()
            assert_matches_type(TweetGetQuotesResponse, tweet, path=["response"])

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
            cursor="cursor",
            since_time="sinceTime",
            until_time="untilTime",
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
    def test_method_get_retweeters(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.get_retweeters(
            id="id",
        )
        assert_matches_type(TweetGetRetweetersResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_retweeters_with_all_params(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.get_retweeters(
            id="id",
            cursor="cursor",
        )
        assert_matches_type(TweetGetRetweetersResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_retweeters(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.with_raw_response.get_retweeters(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = response.parse()
        assert_matches_type(TweetGetRetweetersResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_retweeters(self, client: XTwitterScraper) -> None:
        with client.x.tweets.with_streaming_response.get_retweeters(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = response.parse()
            assert_matches_type(TweetGetRetweetersResponse, tweet, path=["response"])

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
    def test_method_get_thread(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.get_thread(
            id="id",
        )
        assert_matches_type(TweetGetThreadResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_thread_with_all_params(self, client: XTwitterScraper) -> None:
        tweet = client.x.tweets.get_thread(
            id="id",
            cursor="cursor",
        )
        assert_matches_type(TweetGetThreadResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_thread(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.with_raw_response.get_thread(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = response.parse()
        assert_matches_type(TweetGetThreadResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_thread(self, client: XTwitterScraper) -> None:
        with client.x.tweets.with_streaming_response.get_thread(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = response.parse()
            assert_matches_type(TweetGetThreadResponse, tweet, path=["response"])

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
            cursor="cursor",
            limit=200,
            query_type="Latest",
            since_time="sinceTime",
            until_time="untilTime",
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


class TestAsyncTweets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.create(
            account="account",
            text="text",
        )
        assert_matches_type(TweetCreateResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.create(
            account="account",
            text="text",
            attachment_url="attachment_url",
            community_id="community_id",
            is_note_tweet=True,
            media_ids=["string"],
            reply_to_tweet_id="reply_to_tweet_id",
        )
        assert_matches_type(TweetCreateResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.with_raw_response.create(
            account="account",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = await response.parse()
        assert_matches_type(TweetCreateResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.with_streaming_response.create(
            account="account",
            text="text",
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
            "tweetId",
        )
        assert_matches_type(TweetRetrieveResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.with_raw_response.retrieve(
            "tweetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = await response.parse()
        assert_matches_type(TweetRetrieveResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.with_streaming_response.retrieve(
            "tweetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = await response.parse()
            assert_matches_type(TweetRetrieveResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tweet_id` but received ''"):
            await async_client.x.tweets.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.list(
            ids="ids",
        )
        assert tweet is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.with_raw_response.list(
            ids="ids",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = await response.parse()
        assert tweet is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.with_streaming_response.list(
            ids="ids",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = await response.parse()
            assert tweet is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.delete(
            tweet_id="tweetId",
            account="account",
        )
        assert_matches_type(TweetDeleteResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.with_raw_response.delete(
            tweet_id="tweetId",
            account="account",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = await response.parse()
        assert_matches_type(TweetDeleteResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.with_streaming_response.delete(
            tweet_id="tweetId",
            account="account",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = await response.parse()
            assert_matches_type(TweetDeleteResponse, tweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tweet_id` but received ''"):
            await async_client.x.tweets.with_raw_response.delete(
                tweet_id="",
                account="account",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_favoriters(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.get_favoriters(
            id="id",
        )
        assert_matches_type(TweetGetFavoritersResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_favoriters_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.get_favoriters(
            id="id",
            cursor="cursor",
        )
        assert_matches_type(TweetGetFavoritersResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_favoriters(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.with_raw_response.get_favoriters(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = await response.parse()
        assert_matches_type(TweetGetFavoritersResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_favoriters(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.with_streaming_response.get_favoriters(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = await response.parse()
            assert_matches_type(TweetGetFavoritersResponse, tweet, path=["response"])

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
    async def test_method_get_quotes(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.get_quotes(
            id="id",
        )
        assert_matches_type(TweetGetQuotesResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_quotes_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.get_quotes(
            id="id",
            cursor="cursor",
            include_replies=True,
            since_time="sinceTime",
            until_time="untilTime",
        )
        assert_matches_type(TweetGetQuotesResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_quotes(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.with_raw_response.get_quotes(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = await response.parse()
        assert_matches_type(TweetGetQuotesResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_quotes(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.with_streaming_response.get_quotes(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = await response.parse()
            assert_matches_type(TweetGetQuotesResponse, tweet, path=["response"])

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
            cursor="cursor",
            since_time="sinceTime",
            until_time="untilTime",
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
    async def test_method_get_retweeters(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.get_retweeters(
            id="id",
        )
        assert_matches_type(TweetGetRetweetersResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_retweeters_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.get_retweeters(
            id="id",
            cursor="cursor",
        )
        assert_matches_type(TweetGetRetweetersResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_retweeters(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.with_raw_response.get_retweeters(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = await response.parse()
        assert_matches_type(TweetGetRetweetersResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_retweeters(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.with_streaming_response.get_retweeters(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = await response.parse()
            assert_matches_type(TweetGetRetweetersResponse, tweet, path=["response"])

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
    async def test_method_get_thread(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.get_thread(
            id="id",
        )
        assert_matches_type(TweetGetThreadResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_thread_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        tweet = await async_client.x.tweets.get_thread(
            id="id",
            cursor="cursor",
        )
        assert_matches_type(TweetGetThreadResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_thread(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.with_raw_response.get_thread(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tweet = await response.parse()
        assert_matches_type(TweetGetThreadResponse, tweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_thread(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.with_streaming_response.get_thread(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tweet = await response.parse()
            assert_matches_type(TweetGetThreadResponse, tweet, path=["response"])

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
            cursor="cursor",
            limit=200,
            query_type="Latest",
            since_time="sinceTime",
            until_time="untilTime",
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
