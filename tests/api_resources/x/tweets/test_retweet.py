# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types.x.tweets import (
    RetweetCreateResponse,
    RetweetDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRetweet:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: XTwitterScraper) -> None:
        retweet = client.x.tweets.retweet.create(
            tweet_id="tweetId",
            account="account",
        )
        assert_matches_type(RetweetCreateResponse, retweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.retweet.with_raw_response.create(
            tweet_id="tweetId",
            account="account",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retweet = response.parse()
        assert_matches_type(RetweetCreateResponse, retweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: XTwitterScraper) -> None:
        with client.x.tweets.retweet.with_streaming_response.create(
            tweet_id="tweetId",
            account="account",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retweet = response.parse()
            assert_matches_type(RetweetCreateResponse, retweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tweet_id` but received ''"):
            client.x.tweets.retweet.with_raw_response.create(
                tweet_id="",
                account="account",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: XTwitterScraper) -> None:
        retweet = client.x.tweets.retweet.delete(
            tweet_id="tweetId",
            account="account",
        )
        assert_matches_type(RetweetDeleteResponse, retweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.retweet.with_raw_response.delete(
            tweet_id="tweetId",
            account="account",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retweet = response.parse()
        assert_matches_type(RetweetDeleteResponse, retweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: XTwitterScraper) -> None:
        with client.x.tweets.retweet.with_streaming_response.delete(
            tweet_id="tweetId",
            account="account",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retweet = response.parse()
            assert_matches_type(RetweetDeleteResponse, retweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tweet_id` but received ''"):
            client.x.tweets.retweet.with_raw_response.delete(
                tweet_id="",
                account="account",
            )


class TestAsyncRetweet:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncXTwitterScraper) -> None:
        retweet = await async_client.x.tweets.retweet.create(
            tweet_id="tweetId",
            account="account",
        )
        assert_matches_type(RetweetCreateResponse, retweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.retweet.with_raw_response.create(
            tweet_id="tweetId",
            account="account",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retweet = await response.parse()
        assert_matches_type(RetweetCreateResponse, retweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.retweet.with_streaming_response.create(
            tweet_id="tweetId",
            account="account",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retweet = await response.parse()
            assert_matches_type(RetweetCreateResponse, retweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tweet_id` but received ''"):
            await async_client.x.tweets.retweet.with_raw_response.create(
                tweet_id="",
                account="account",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncXTwitterScraper) -> None:
        retweet = await async_client.x.tweets.retweet.delete(
            tweet_id="tweetId",
            account="account",
        )
        assert_matches_type(RetweetDeleteResponse, retweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.retweet.with_raw_response.delete(
            tweet_id="tweetId",
            account="account",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retweet = await response.parse()
        assert_matches_type(RetweetDeleteResponse, retweet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.retweet.with_streaming_response.delete(
            tweet_id="tweetId",
            account="account",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retweet = await response.parse()
            assert_matches_type(RetweetDeleteResponse, retweet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tweet_id` but received ''"):
            await async_client.x.tweets.retweet.with_raw_response.delete(
                tweet_id="",
                account="account",
            )
