# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types.x import BookmarkRetrieveFoldersResponse
from x_twitter_scraper.pagination import SyncCursorPage, AsyncCursorPage
from x_twitter_scraper.types.shared import PaginatedTweets

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBookmarks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: XTwitterScraper) -> None:
        bookmark = client.x.bookmarks.list()
        assert_matches_type(SyncCursorPage[PaginatedTweets], bookmark, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: XTwitterScraper) -> None:
        bookmark = client.x.bookmarks.list(
            cursor="folders_value",
            folder_id="folderId",
        )
        assert_matches_type(SyncCursorPage[PaginatedTweets], bookmark, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: XTwitterScraper) -> None:
        response = client.x.bookmarks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookmark = response.parse()
        assert_matches_type(SyncCursorPage[PaginatedTweets], bookmark, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: XTwitterScraper) -> None:
        with client.x.bookmarks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookmark = response.parse()
            assert_matches_type(SyncCursorPage[PaginatedTweets], bookmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_folders(self, client: XTwitterScraper) -> None:
        bookmark = client.x.bookmarks.retrieve_folders()
        assert_matches_type(BookmarkRetrieveFoldersResponse, bookmark, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_folders(self, client: XTwitterScraper) -> None:
        response = client.x.bookmarks.with_raw_response.retrieve_folders()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookmark = response.parse()
        assert_matches_type(BookmarkRetrieveFoldersResponse, bookmark, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_folders(self, client: XTwitterScraper) -> None:
        with client.x.bookmarks.with_streaming_response.retrieve_folders() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookmark = response.parse()
            assert_matches_type(BookmarkRetrieveFoldersResponse, bookmark, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBookmarks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncXTwitterScraper) -> None:
        bookmark = await async_client.x.bookmarks.list()
        assert_matches_type(AsyncCursorPage[PaginatedTweets], bookmark, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        bookmark = await async_client.x.bookmarks.list(
            cursor="folders_value",
            folder_id="folderId",
        )
        assert_matches_type(AsyncCursorPage[PaginatedTweets], bookmark, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.bookmarks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookmark = await response.parse()
        assert_matches_type(AsyncCursorPage[PaginatedTweets], bookmark, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.bookmarks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookmark = await response.parse()
            assert_matches_type(AsyncCursorPage[PaginatedTweets], bookmark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_folders(self, async_client: AsyncXTwitterScraper) -> None:
        bookmark = await async_client.x.bookmarks.retrieve_folders()
        assert_matches_type(BookmarkRetrieveFoldersResponse, bookmark, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_folders(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.bookmarks.with_raw_response.retrieve_folders()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bookmark = await response.parse()
        assert_matches_type(BookmarkRetrieveFoldersResponse, bookmark, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_folders(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.bookmarks.with_streaming_response.retrieve_folders() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bookmark = await response.parse()
            assert_matches_type(BookmarkRetrieveFoldersResponse, bookmark, path=["response"])

        assert cast(Any, response.is_closed) is True
