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
from x_twitter_scraper.types.monitors import (
    KeywordListResponse,
    KeywordCreateResponse,
    KeywordUpdateResponse,
    KeywordRetrieveResponse,
    KeywordDeactivateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKeywords:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: XTwitterScraper) -> None:
        keyword = client.monitors.keywords.create(
            event_types=["tweet.new"],
            query='xquik OR "x api"',
        )
        assert_matches_type(KeywordCreateResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: XTwitterScraper) -> None:
        response = client.monitors.keywords.with_raw_response.create(
            event_types=["tweet.new"],
            query='xquik OR "x api"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        keyword = response.parse()
        assert_matches_type(KeywordCreateResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: XTwitterScraper) -> None:
        with client.monitors.keywords.with_streaming_response.create(
            event_types=["tweet.new"],
            query='xquik OR "x api"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            keyword = response.parse()
            assert_matches_type(KeywordCreateResponse, keyword, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: XTwitterScraper) -> None:
        keyword = client.monitors.keywords.retrieve(
            "id",
        )
        assert_matches_type(KeywordRetrieveResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: XTwitterScraper) -> None:
        response = client.monitors.keywords.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        keyword = response.parse()
        assert_matches_type(KeywordRetrieveResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: XTwitterScraper) -> None:
        with client.monitors.keywords.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            keyword = response.parse()
            assert_matches_type(KeywordRetrieveResponse, keyword, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.monitors.keywords.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: XTwitterScraper) -> None:
        keyword = client.monitors.keywords.update(
            id="id",
        )
        assert_matches_type(KeywordUpdateResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: XTwitterScraper) -> None:
        keyword = client.monitors.keywords.update(
            id="id",
            event_types=["tweet.new"],
            is_active=True,
        )
        assert_matches_type(KeywordUpdateResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: XTwitterScraper) -> None:
        response = client.monitors.keywords.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        keyword = response.parse()
        assert_matches_type(KeywordUpdateResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: XTwitterScraper) -> None:
        with client.monitors.keywords.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            keyword = response.parse()
            assert_matches_type(KeywordUpdateResponse, keyword, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.monitors.keywords.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: XTwitterScraper) -> None:
        keyword = client.monitors.keywords.list()
        assert_matches_type(KeywordListResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: XTwitterScraper) -> None:
        response = client.monitors.keywords.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        keyword = response.parse()
        assert_matches_type(KeywordListResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: XTwitterScraper) -> None:
        with client.monitors.keywords.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            keyword = response.parse()
            assert_matches_type(KeywordListResponse, keyword, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_deactivate(self, client: XTwitterScraper) -> None:
        keyword = client.monitors.keywords.deactivate(
            "id",
        )
        assert_matches_type(KeywordDeactivateResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_deactivate(self, client: XTwitterScraper) -> None:
        response = client.monitors.keywords.with_raw_response.deactivate(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        keyword = response.parse()
        assert_matches_type(KeywordDeactivateResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_deactivate(self, client: XTwitterScraper) -> None:
        with client.monitors.keywords.with_streaming_response.deactivate(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            keyword = response.parse()
            assert_matches_type(KeywordDeactivateResponse, keyword, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_deactivate(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.monitors.keywords.with_raw_response.deactivate(
                "",
            )


class TestAsyncKeywords:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncXTwitterScraper) -> None:
        keyword = await async_client.monitors.keywords.create(
            event_types=["tweet.new"],
            query='xquik OR "x api"',
        )
        assert_matches_type(KeywordCreateResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.monitors.keywords.with_raw_response.create(
            event_types=["tweet.new"],
            query='xquik OR "x api"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        keyword = await response.parse()
        assert_matches_type(KeywordCreateResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.monitors.keywords.with_streaming_response.create(
            event_types=["tweet.new"],
            query='xquik OR "x api"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            keyword = await response.parse()
            assert_matches_type(KeywordCreateResponse, keyword, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        keyword = await async_client.monitors.keywords.retrieve(
            "id",
        )
        assert_matches_type(KeywordRetrieveResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.monitors.keywords.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        keyword = await response.parse()
        assert_matches_type(KeywordRetrieveResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.monitors.keywords.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            keyword = await response.parse()
            assert_matches_type(KeywordRetrieveResponse, keyword, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.monitors.keywords.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncXTwitterScraper) -> None:
        keyword = await async_client.monitors.keywords.update(
            id="id",
        )
        assert_matches_type(KeywordUpdateResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        keyword = await async_client.monitors.keywords.update(
            id="id",
            event_types=["tweet.new"],
            is_active=True,
        )
        assert_matches_type(KeywordUpdateResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.monitors.keywords.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        keyword = await response.parse()
        assert_matches_type(KeywordUpdateResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.monitors.keywords.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            keyword = await response.parse()
            assert_matches_type(KeywordUpdateResponse, keyword, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.monitors.keywords.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncXTwitterScraper) -> None:
        keyword = await async_client.monitors.keywords.list()
        assert_matches_type(KeywordListResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.monitors.keywords.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        keyword = await response.parse()
        assert_matches_type(KeywordListResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.monitors.keywords.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            keyword = await response.parse()
            assert_matches_type(KeywordListResponse, keyword, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_deactivate(self, async_client: AsyncXTwitterScraper) -> None:
        keyword = await async_client.monitors.keywords.deactivate(
            "id",
        )
        assert_matches_type(KeywordDeactivateResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_deactivate(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.monitors.keywords.with_raw_response.deactivate(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        keyword = await response.parse()
        assert_matches_type(KeywordDeactivateResponse, keyword, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_deactivate(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.monitors.keywords.with_streaming_response.deactivate(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            keyword = await response.parse()
            assert_matches_type(KeywordDeactivateResponse, keyword, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_deactivate(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.monitors.keywords.with_raw_response.deactivate(
                "",
            )
