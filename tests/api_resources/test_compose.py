# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types import ComposeCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompose:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: XTwitterScraper) -> None:
        compose = client.compose.create(
            step="compose",
            topic="PostgreSQL query planning",
        )
        assert_matches_type(ComposeCreateResponse, compose, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: XTwitterScraper) -> None:
        compose = client.compose.create(
            step="compose",
            topic="PostgreSQL query planning",
            goal="engagement",
            style_username="x",
        )
        assert_matches_type(ComposeCreateResponse, compose, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: XTwitterScraper) -> None:
        response = client.compose.with_raw_response.create(
            step="compose",
            topic="PostgreSQL query planning",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compose = response.parse()
        assert_matches_type(ComposeCreateResponse, compose, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: XTwitterScraper) -> None:
        with client.compose.with_streaming_response.create(
            step="compose",
            topic="PostgreSQL query planning",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compose = response.parse()
            assert_matches_type(ComposeCreateResponse, compose, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: XTwitterScraper) -> None:
        compose = client.compose.create(
            goal="engagement",
            step="refine",
            tone="professional",
            topic="x",
        )
        assert_matches_type(ComposeCreateResponse, compose, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: XTwitterScraper) -> None:
        compose = client.compose.create(
            goal="engagement",
            step="refine",
            tone="professional",
            topic="x",
            additional_context="x",
            call_to_action="x",
            media_type="photo",
        )
        assert_matches_type(ComposeCreateResponse, compose, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: XTwitterScraper) -> None:
        response = client.compose.with_raw_response.create(
            goal="engagement",
            step="refine",
            tone="professional",
            topic="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compose = response.parse()
        assert_matches_type(ComposeCreateResponse, compose, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: XTwitterScraper) -> None:
        with client.compose.with_streaming_response.create(
            goal="engagement",
            step="refine",
            tone="professional",
            topic="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compose = response.parse()
            assert_matches_type(ComposeCreateResponse, compose, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_3(self, client: XTwitterScraper) -> None:
        compose = client.compose.create(
            draft="x",
            step="score",
        )
        assert_matches_type(ComposeCreateResponse, compose, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: XTwitterScraper) -> None:
        compose = client.compose.create(
            draft="x",
            step="score",
            has_link=True,
            has_media=True,
        )
        assert_matches_type(ComposeCreateResponse, compose, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_3(self, client: XTwitterScraper) -> None:
        response = client.compose.with_raw_response.create(
            draft="x",
            step="score",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compose = response.parse()
        assert_matches_type(ComposeCreateResponse, compose, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_3(self, client: XTwitterScraper) -> None:
        with client.compose.with_streaming_response.create(
            draft="x",
            step="score",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compose = response.parse()
            assert_matches_type(ComposeCreateResponse, compose, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCompose:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncXTwitterScraper) -> None:
        compose = await async_client.compose.create(
            step="compose",
            topic="PostgreSQL query planning",
        )
        assert_matches_type(ComposeCreateResponse, compose, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncXTwitterScraper) -> None:
        compose = await async_client.compose.create(
            step="compose",
            topic="PostgreSQL query planning",
            goal="engagement",
            style_username="x",
        )
        assert_matches_type(ComposeCreateResponse, compose, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.compose.with_raw_response.create(
            step="compose",
            topic="PostgreSQL query planning",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compose = await response.parse()
        assert_matches_type(ComposeCreateResponse, compose, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.compose.with_streaming_response.create(
            step="compose",
            topic="PostgreSQL query planning",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compose = await response.parse()
            assert_matches_type(ComposeCreateResponse, compose, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncXTwitterScraper) -> None:
        compose = await async_client.compose.create(
            goal="engagement",
            step="refine",
            tone="professional",
            topic="x",
        )
        assert_matches_type(ComposeCreateResponse, compose, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncXTwitterScraper) -> None:
        compose = await async_client.compose.create(
            goal="engagement",
            step="refine",
            tone="professional",
            topic="x",
            additional_context="x",
            call_to_action="x",
            media_type="photo",
        )
        assert_matches_type(ComposeCreateResponse, compose, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.compose.with_raw_response.create(
            goal="engagement",
            step="refine",
            tone="professional",
            topic="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compose = await response.parse()
        assert_matches_type(ComposeCreateResponse, compose, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.compose.with_streaming_response.create(
            goal="engagement",
            step="refine",
            tone="professional",
            topic="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compose = await response.parse()
            assert_matches_type(ComposeCreateResponse, compose, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncXTwitterScraper) -> None:
        compose = await async_client.compose.create(
            draft="x",
            step="score",
        )
        assert_matches_type(ComposeCreateResponse, compose, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncXTwitterScraper) -> None:
        compose = await async_client.compose.create(
            draft="x",
            step="score",
            has_link=True,
            has_media=True,
        )
        assert_matches_type(ComposeCreateResponse, compose, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.compose.with_raw_response.create(
            draft="x",
            step="score",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        compose = await response.parse()
        assert_matches_type(ComposeCreateResponse, compose, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.compose.with_streaming_response.create(
            draft="x",
            step="score",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            compose = await response.parse()
            assert_matches_type(ComposeCreateResponse, compose, path=["response"])

        assert cast(Any, response.is_closed) is True
