# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types.x import (
    SpaceSearchResponse,
    SpaceRetrieveResponse,
    SpaceRetrieveReplayResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpaces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: XTwitterScraper) -> None:
        space = client.x.spaces.retrieve(
            id="id",
        )
        assert_matches_type(SpaceRetrieveResponse, space, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: XTwitterScraper) -> None:
        space = client.x.spaces.retrieve(
            id="id",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(SpaceRetrieveResponse, space, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: XTwitterScraper) -> None:
        response = client.x.spaces.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = response.parse()
        assert_matches_type(SpaceRetrieveResponse, space, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: XTwitterScraper) -> None:
        with client.x.spaces.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = response.parse()
            assert_matches_type(SpaceRetrieveResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.spaces.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_replay(self, client: XTwitterScraper) -> None:
        space = client.x.spaces.retrieve_replay(
            id="id",
        )
        assert_matches_type(SpaceRetrieveReplayResponse, space, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_replay_with_all_params(self, client: XTwitterScraper) -> None:
        space = client.x.spaces.retrieve_replay(
            id="id",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(SpaceRetrieveReplayResponse, space, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_replay(self, client: XTwitterScraper) -> None:
        response = client.x.spaces.with_raw_response.retrieve_replay(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = response.parse()
        assert_matches_type(SpaceRetrieveReplayResponse, space, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_replay(self, client: XTwitterScraper) -> None:
        with client.x.spaces.with_streaming_response.retrieve_replay(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = response.parse()
            assert_matches_type(SpaceRetrieveReplayResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_replay(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.spaces.with_raw_response.retrieve_replay(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: XTwitterScraper) -> None:
        space = client.x.spaces.search(
            q="from:solana",
        )
        assert_matches_type(SpaceSearchResponse, space, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: XTwitterScraper) -> None:
        space = client.x.spaces.search(
            q="from:solana",
            cursor="cursor",
            fields="id,text,author.username",
            omit="entities,media",
            page_size=1,
            query_type="Latest",
        )
        assert_matches_type(SpaceSearchResponse, space, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: XTwitterScraper) -> None:
        response = client.x.spaces.with_raw_response.search(
            q="from:solana",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = response.parse()
        assert_matches_type(SpaceSearchResponse, space, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: XTwitterScraper) -> None:
        with client.x.spaces.with_streaming_response.search(
            q="from:solana",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = response.parse()
            assert_matches_type(SpaceSearchResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSpaces:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        space = await async_client.x.spaces.retrieve(
            id="id",
        )
        assert_matches_type(SpaceRetrieveResponse, space, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        space = await async_client.x.spaces.retrieve(
            id="id",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(SpaceRetrieveResponse, space, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.spaces.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = await response.parse()
        assert_matches_type(SpaceRetrieveResponse, space, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.spaces.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = await response.parse()
            assert_matches_type(SpaceRetrieveResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.spaces.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_replay(self, async_client: AsyncXTwitterScraper) -> None:
        space = await async_client.x.spaces.retrieve_replay(
            id="id",
        )
        assert_matches_type(SpaceRetrieveReplayResponse, space, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_replay_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        space = await async_client.x.spaces.retrieve_replay(
            id="id",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(SpaceRetrieveReplayResponse, space, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_replay(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.spaces.with_raw_response.retrieve_replay(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = await response.parse()
        assert_matches_type(SpaceRetrieveReplayResponse, space, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_replay(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.spaces.with_streaming_response.retrieve_replay(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = await response.parse()
            assert_matches_type(SpaceRetrieveReplayResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_replay(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.spaces.with_raw_response.retrieve_replay(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncXTwitterScraper) -> None:
        space = await async_client.x.spaces.search(
            q="from:solana",
        )
        assert_matches_type(SpaceSearchResponse, space, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        space = await async_client.x.spaces.search(
            q="from:solana",
            cursor="cursor",
            fields="id,text,author.username",
            omit="entities,media",
            page_size=1,
            query_type="Latest",
        )
        assert_matches_type(SpaceSearchResponse, space, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.spaces.with_raw_response.search(
            q="from:solana",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        space = await response.parse()
        assert_matches_type(SpaceSearchResponse, space, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.spaces.with_streaming_response.search(
            q="from:solana",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            space = await response.parse()
            assert_matches_type(SpaceSearchResponse, space, path=["response"])

        assert cast(Any, response.is_closed) is True
