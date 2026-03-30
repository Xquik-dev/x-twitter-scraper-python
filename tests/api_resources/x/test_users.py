# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types.x import (
    UserProfile,
)
from x_twitter_scraper.types.shared import PaginatedUsers, PaginatedTweets

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve(
            "username",
        )
        assert_matches_type(UserProfile, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve(
            "username",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserProfile, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve(
            "username",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserProfile, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `username` but received ''"):
            client.x.users.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_batch(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_batch(
            ids="ids",
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_batch(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_batch(
            ids="ids",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_batch(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_batch(
            ids="ids",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_followers(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_followers(
            id="id",
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_followers_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_followers(
            id="id",
            cursor="cursor",
            page_size=0,
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_followers(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_followers(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_followers(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_followers(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

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
            cursor="cursor",
        )
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_followers_you_know(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_followers_you_know(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_followers_you_know(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_followers_you_know(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(PaginatedUsers, user, path=["response"])

        assert cast(Any, response.is_closed) is True

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
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_following_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_following(
            id="id",
            cursor="cursor",
            page_size=0,
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_following(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_following(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_following(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_following(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_following(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.users.with_raw_response.retrieve_following(
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
            cursor="cursor",
        )
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_likes(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_likes(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_likes(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_likes(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(PaginatedTweets, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_likes(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.users.with_raw_response.retrieve_likes(
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
            cursor="cursor",
        )
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_media(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_media(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_media(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_media(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(PaginatedTweets, user, path=["response"])

        assert cast(Any, response.is_closed) is True

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
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_mentions_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_mentions(
            id="id",
            cursor="cursor",
            since_time="sinceTime",
            until_time="untilTime",
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_mentions(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_mentions(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_mentions(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_mentions(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_mentions(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.users.with_raw_response.retrieve_mentions(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_search(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_search(
            q="q",
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_search_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_search(
            q="q",
            cursor="cursor",
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_search(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_search(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

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
            cursor="cursor",
            include_parent_tweet=True,
            include_replies=True,
        )
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_tweets(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_tweets(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_tweets(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_tweets(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(PaginatedTweets, user, path=["response"])

        assert cast(Any, response.is_closed) is True

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
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_verified_followers_with_all_params(self, client: XTwitterScraper) -> None:
        user = client.x.users.retrieve_verified_followers(
            id="id",
            cursor="cursor",
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_verified_followers(self, client: XTwitterScraper) -> None:
        response = client.x.users.with_raw_response.retrieve_verified_followers(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_verified_followers(self, client: XTwitterScraper) -> None:
        with client.x.users.with_streaming_response.retrieve_verified_followers(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_verified_followers(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.users.with_raw_response.retrieve_verified_followers(
                id="",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve(
            "username",
        )
        assert_matches_type(UserProfile, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve(
            "username",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserProfile, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve(
            "username",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserProfile, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `username` but received ''"):
            await async_client.x.users.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_batch(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_batch(
            ids="ids",
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_batch(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_batch(
            ids="ids",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_batch(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_batch(
            ids="ids",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_followers(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_followers(
            id="id",
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_followers_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_followers(
            id="id",
            cursor="cursor",
            page_size=0,
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_followers(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_followers(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_followers(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_followers(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

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
            cursor="cursor",
        )
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_followers_you_know(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_followers_you_know(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(PaginatedUsers, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_followers_you_know(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_followers_you_know(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(PaginatedUsers, user, path=["response"])

        assert cast(Any, response.is_closed) is True

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
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_following_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_following(
            id="id",
            cursor="cursor",
            page_size=0,
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_following(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_following(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_following(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_following(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_following(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.users.with_raw_response.retrieve_following(
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
            cursor="cursor",
        )
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_likes(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_likes(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_likes(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_likes(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(PaginatedTweets, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_likes(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.users.with_raw_response.retrieve_likes(
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
            cursor="cursor",
        )
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_media(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_media(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_media(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_media(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(PaginatedTweets, user, path=["response"])

        assert cast(Any, response.is_closed) is True

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
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_mentions_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_mentions(
            id="id",
            cursor="cursor",
            since_time="sinceTime",
            until_time="untilTime",
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_mentions(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_mentions(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_mentions(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_mentions(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_mentions(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.users.with_raw_response.retrieve_mentions(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_search(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_search(
            q="q",
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_search_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_search(
            q="q",
            cursor="cursor",
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_search(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_search(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

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
            cursor="cursor",
            include_parent_tweet=True,
            include_replies=True,
        )
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_tweets(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_tweets(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(PaginatedTweets, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_tweets(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_tweets(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(PaginatedTweets, user, path=["response"])

        assert cast(Any, response.is_closed) is True

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
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_verified_followers_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        user = await async_client.x.users.retrieve_verified_followers(
            id="id",
            cursor="cursor",
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_verified_followers(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.with_raw_response.retrieve_verified_followers(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_verified_followers(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.with_streaming_response.retrieve_verified_followers(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_verified_followers(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.users.with_raw_response.retrieve_verified_followers(
                id="",
            )
