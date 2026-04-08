# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types.x import (
    MediaUploadResponse,
    MediaDownloadResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMedia:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_download(self, client: XTwitterScraper) -> None:
        media = client.x.media.download()
        assert_matches_type(MediaDownloadResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_download_with_all_params(self, client: XTwitterScraper) -> None:
        media = client.x.media.download(
            tweet_ids=["1234567890", "1234567891"],
            tweet_input="https://x.com/elonmusk/status/1234567890",
        )
        assert_matches_type(MediaDownloadResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_download(self, client: XTwitterScraper) -> None:
        response = client.x.media.with_raw_response.download()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert_matches_type(MediaDownloadResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_download(self, client: XTwitterScraper) -> None:
        with client.x.media.with_streaming_response.download() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert_matches_type(MediaDownloadResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload(self, client: XTwitterScraper) -> None:
        media = client.x.media.upload(
            account="@elonmusk",
            file=b"Example data",
        )
        assert_matches_type(MediaUploadResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload_with_all_params(self, client: XTwitterScraper) -> None:
        media = client.x.media.upload(
            account="@elonmusk",
            file=b"Example data",
            is_long_video=True,
        )
        assert_matches_type(MediaUploadResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: XTwitterScraper) -> None:
        response = client.x.media.with_raw_response.upload(
            account="@elonmusk",
            file=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert_matches_type(MediaUploadResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: XTwitterScraper) -> None:
        with client.x.media.with_streaming_response.upload(
            account="@elonmusk",
            file=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert_matches_type(MediaUploadResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMedia:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_download(self, async_client: AsyncXTwitterScraper) -> None:
        media = await async_client.x.media.download()
        assert_matches_type(MediaDownloadResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_download_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        media = await async_client.x.media.download(
            tweet_ids=["1234567890", "1234567891"],
            tweet_input="https://x.com/elonmusk/status/1234567890",
        )
        assert_matches_type(MediaDownloadResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_download(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.media.with_raw_response.download()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert_matches_type(MediaDownloadResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_download(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.media.with_streaming_response.download() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert_matches_type(MediaDownloadResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncXTwitterScraper) -> None:
        media = await async_client.x.media.upload(
            account="@elonmusk",
            file=b"Example data",
        )
        assert_matches_type(MediaUploadResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        media = await async_client.x.media.upload(
            account="@elonmusk",
            file=b"Example data",
            is_long_video=True,
        )
        assert_matches_type(MediaUploadResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.media.with_raw_response.upload(
            account="@elonmusk",
            file=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert_matches_type(MediaUploadResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.media.with_streaming_response.upload(
            account="@elonmusk",
            file=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert_matches_type(MediaUploadResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True
