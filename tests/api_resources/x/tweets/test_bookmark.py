# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types.x.tweets import (
    BookmarkCreateResponse,
    BookmarkDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBookmark:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: XTwitterScraper) -> None:
        bookmark = client.x.tweets.bookmark.create(
            id="id",
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(BookmarkCreateResponse, bookmark, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.bookmark.with_raw_response.create(
            id="id",
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookmark = response.parse()
        assert_matches_type(BookmarkCreateResponse, bookmark, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: XTwitterScraper) -> None:
        with client.x.tweets.bookmark.with_streaming_response.create(
            id="id",
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookmark = response.parse()
            assert_matches_type(BookmarkCreateResponse, bookmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.tweets.bookmark.with_raw_response.create(
                id="",
                account="@elonmusk",
                idempotency_key="Idempotency-Key",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: XTwitterScraper) -> None:
        bookmark = client.x.tweets.bookmark.delete(
            id="id",
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(BookmarkDeleteResponse, bookmark, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: XTwitterScraper) -> None:
        response = client.x.tweets.bookmark.with_raw_response.delete(
            id="id",
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookmark = response.parse()
        assert_matches_type(BookmarkDeleteResponse, bookmark, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: XTwitterScraper) -> None:
        with client.x.tweets.bookmark.with_streaming_response.delete(
            id="id",
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookmark = response.parse()
            assert_matches_type(BookmarkDeleteResponse, bookmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.tweets.bookmark.with_raw_response.delete(
                id="",
                account="@elonmusk",
                idempotency_key="Idempotency-Key",
            )


class TestAsyncBookmark:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncXTwitterScraper) -> None:
        bookmark = await async_client.x.tweets.bookmark.create(
            id="id",
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(BookmarkCreateResponse, bookmark, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.bookmark.with_raw_response.create(
            id="id",
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookmark = await response.parse()
        assert_matches_type(BookmarkCreateResponse, bookmark, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.bookmark.with_streaming_response.create(
            id="id",
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookmark = await response.parse()
            assert_matches_type(BookmarkCreateResponse, bookmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.tweets.bookmark.with_raw_response.create(
                id="",
                account="@elonmusk",
                idempotency_key="Idempotency-Key",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncXTwitterScraper) -> None:
        bookmark = await async_client.x.tweets.bookmark.delete(
            id="id",
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(BookmarkDeleteResponse, bookmark, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.tweets.bookmark.with_raw_response.delete(
            id="id",
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookmark = await response.parse()
        assert_matches_type(BookmarkDeleteResponse, bookmark, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.tweets.bookmark.with_streaming_response.delete(
            id="id",
            account="@elonmusk",
            idempotency_key="Idempotency-Key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookmark = await response.parse()
            assert_matches_type(BookmarkDeleteResponse, bookmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.tweets.bookmark.with_raw_response.delete(
                id="",
                account="@elonmusk",
                idempotency_key="Idempotency-Key",
            )
