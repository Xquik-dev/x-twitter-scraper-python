# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types import (
    StyleListResponse,
    StyleAnalyzeResponse,
    StyleCompareResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStyles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: XTwitterScraper) -> None:
        style = client.styles.list()
        assert_matches_type(StyleListResponse, style, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: XTwitterScraper) -> None:
        response = client.styles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        style = response.parse()
        assert_matches_type(StyleListResponse, style, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: XTwitterScraper) -> None:
        with client.styles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            style = response.parse()
            assert_matches_type(StyleListResponse, style, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_analyze(self, client: XTwitterScraper) -> None:
        style = client.styles.analyze(
            username="username",
        )
        assert_matches_type(StyleAnalyzeResponse, style, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_analyze(self, client: XTwitterScraper) -> None:
        response = client.styles.with_raw_response.analyze(
            username="username",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        style = response.parse()
        assert_matches_type(StyleAnalyzeResponse, style, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_analyze(self, client: XTwitterScraper) -> None:
        with client.styles.with_streaming_response.analyze(
            username="username",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            style = response.parse()
            assert_matches_type(StyleAnalyzeResponse, style, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_compare(self, client: XTwitterScraper) -> None:
        style = client.styles.compare(
            username1="username1",
            username2="username2",
        )
        assert_matches_type(StyleCompareResponse, style, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_compare(self, client: XTwitterScraper) -> None:
        response = client.styles.with_raw_response.compare(
            username1="username1",
            username2="username2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        style = response.parse()
        assert_matches_type(StyleCompareResponse, style, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_compare(self, client: XTwitterScraper) -> None:
        with client.styles.with_streaming_response.compare(
            username1="username1",
            username2="username2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            style = response.parse()
            assert_matches_type(StyleCompareResponse, style, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStyles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncXTwitterScraper) -> None:
        style = await async_client.styles.list()
        assert_matches_type(StyleListResponse, style, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.styles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        style = await response.parse()
        assert_matches_type(StyleListResponse, style, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.styles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            style = await response.parse()
            assert_matches_type(StyleListResponse, style, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_analyze(self, async_client: AsyncXTwitterScraper) -> None:
        style = await async_client.styles.analyze(
            username="username",
        )
        assert_matches_type(StyleAnalyzeResponse, style, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_analyze(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.styles.with_raw_response.analyze(
            username="username",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        style = await response.parse()
        assert_matches_type(StyleAnalyzeResponse, style, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_analyze(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.styles.with_streaming_response.analyze(
            username="username",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            style = await response.parse()
            assert_matches_type(StyleAnalyzeResponse, style, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_compare(self, async_client: AsyncXTwitterScraper) -> None:
        style = await async_client.styles.compare(
            username1="username1",
            username2="username2",
        )
        assert_matches_type(StyleCompareResponse, style, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_compare(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.styles.with_raw_response.compare(
            username1="username1",
            username2="username2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        style = await response.parse()
        assert_matches_type(StyleCompareResponse, style, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_compare(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.styles.with_streaming_response.compare(
            username1="username1",
            username2="username2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            style = await response.parse()
            assert_matches_type(StyleCompareResponse, style, path=["response"])

        assert cast(Any, response.is_closed) is True
