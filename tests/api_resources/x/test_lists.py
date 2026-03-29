# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLists:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_followers(self, client: XTwitterScraper) -> None:
        list_ = client.x.lists.retrieve_followers(
            id="id",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_followers_with_all_params(self, client: XTwitterScraper) -> None:
        list_ = client.x.lists.retrieve_followers(
            id="id",
            cursor="cursor",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_followers(self, client: XTwitterScraper) -> None:
        response = client.x.lists.with_raw_response.retrieve_followers(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_followers(self, client: XTwitterScraper) -> None:
        with client.x.lists.with_streaming_response.retrieve_followers(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert list_ is None

        assert cast(Any, response.is_closed) is True

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
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_members_with_all_params(self, client: XTwitterScraper) -> None:
        list_ = client.x.lists.retrieve_members(
            id="id",
            cursor="cursor",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_members(self, client: XTwitterScraper) -> None:
        response = client.x.lists.with_raw_response.retrieve_members(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_members(self, client: XTwitterScraper) -> None:
        with client.x.lists.with_streaming_response.retrieve_members(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert list_ is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_members(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.lists.with_raw_response.retrieve_members(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_tweets(self, client: XTwitterScraper) -> None:
        list_ = client.x.lists.retrieve_tweets(
            id="id",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_tweets_with_all_params(self, client: XTwitterScraper) -> None:
        list_ = client.x.lists.retrieve_tweets(
            id="id",
            cursor="cursor",
            include_replies=True,
            since_time="sinceTime",
            until_time="untilTime",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_tweets(self, client: XTwitterScraper) -> None:
        response = client.x.lists.with_raw_response.retrieve_tweets(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_tweets(self, client: XTwitterScraper) -> None:
        with client.x.lists.with_streaming_response.retrieve_tweets(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert list_ is None

        assert cast(Any, response.is_closed) is True

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
    async def test_method_retrieve_followers(self, async_client: AsyncXTwitterScraper) -> None:
        list_ = await async_client.x.lists.retrieve_followers(
            id="id",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_followers_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        list_ = await async_client.x.lists.retrieve_followers(
            id="id",
            cursor="cursor",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_followers(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.lists.with_raw_response.retrieve_followers(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_followers(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.lists.with_streaming_response.retrieve_followers(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert list_ is None

        assert cast(Any, response.is_closed) is True

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
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_members_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        list_ = await async_client.x.lists.retrieve_members(
            id="id",
            cursor="cursor",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_members(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.lists.with_raw_response.retrieve_members(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_members(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.lists.with_streaming_response.retrieve_members(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert list_ is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_members(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.lists.with_raw_response.retrieve_members(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_tweets(self, async_client: AsyncXTwitterScraper) -> None:
        list_ = await async_client.x.lists.retrieve_tweets(
            id="id",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_tweets_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        list_ = await async_client.x.lists.retrieve_tweets(
            id="id",
            cursor="cursor",
            include_replies=True,
            since_time="sinceTime",
            until_time="untilTime",
        )
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_tweets(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.lists.with_raw_response.retrieve_tweets(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert list_ is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_tweets(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.lists.with_streaming_response.retrieve_tweets(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert list_ is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_tweets(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.lists.with_raw_response.retrieve_tweets(
                id="",
            )
