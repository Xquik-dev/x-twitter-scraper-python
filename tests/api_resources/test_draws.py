# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types import (
    DrawRunResponse,
    DrawListResponse,
    DrawRetrieveResponse,
)
from x_twitter_scraper._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDraws:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: XTwitterScraper) -> None:
        draw = client.draws.retrieve(
            "id",
        )
        assert_matches_type(DrawRetrieveResponse, draw, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: XTwitterScraper) -> None:
        response = client.draws.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draw = response.parse()
        assert_matches_type(DrawRetrieveResponse, draw, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: XTwitterScraper) -> None:
        with client.draws.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draw = response.parse()
            assert_matches_type(DrawRetrieveResponse, draw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.draws.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: XTwitterScraper) -> None:
        draw = client.draws.list()
        assert_matches_type(DrawListResponse, draw, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: XTwitterScraper) -> None:
        draw = client.draws.list(
            after="after",
            limit=1,
        )
        assert_matches_type(DrawListResponse, draw, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: XTwitterScraper) -> None:
        response = client.draws.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draw = response.parse()
        assert_matches_type(DrawListResponse, draw, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: XTwitterScraper) -> None:
        with client.draws.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draw = response.parse()
            assert_matches_type(DrawListResponse, draw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export(self, client: XTwitterScraper, respx_mock: MockRouter) -> None:
        respx_mock.get("/draws/id/export").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        draw = client.draws.export(
            id="id",
        )
        assert draw.is_closed
        assert draw.json() == {"foo": "bar"}
        assert cast(Any, draw.is_closed) is True
        assert isinstance(draw, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_with_all_params(self, client: XTwitterScraper, respx_mock: MockRouter) -> None:
        respx_mock.get("/draws/id/export").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        draw = client.draws.export(
            id="id",
            format="csv",
            type="winners",
        )
        assert draw.is_closed
        assert draw.json() == {"foo": "bar"}
        assert cast(Any, draw.is_closed) is True
        assert isinstance(draw, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_export(self, client: XTwitterScraper, respx_mock: MockRouter) -> None:
        respx_mock.get("/draws/id/export").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        draw = client.draws.with_raw_response.export(
            id="id",
        )

        assert draw.is_closed is True
        assert draw.http_request.headers.get("X-Stainless-Lang") == "python"
        assert draw.json() == {"foo": "bar"}
        assert isinstance(draw, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_export(self, client: XTwitterScraper, respx_mock: MockRouter) -> None:
        respx_mock.get("/draws/id/export").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.draws.with_streaming_response.export(
            id="id",
        ) as draw:
            assert not draw.is_closed
            assert draw.http_request.headers.get("X-Stainless-Lang") == "python"

            assert draw.json() == {"foo": "bar"}
            assert cast(Any, draw.is_closed) is True
            assert isinstance(draw, StreamedBinaryAPIResponse)

        assert cast(Any, draw.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_export(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.draws.with_raw_response.export(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run(self, client: XTwitterScraper) -> None:
        draw = client.draws.run(
            tweet_url="https://example.com",
        )
        assert_matches_type(DrawRunResponse, draw, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: XTwitterScraper) -> None:
        draw = client.draws.run(
            tweet_url="https://example.com",
            backup_count=0,
            filter_account_age_days=0,
            filter_language="filterLanguage",
            filter_min_followers=0,
            must_follow_username="mustFollowUsername",
            must_retweet=True,
            required_hashtags=["string"],
            required_keywords=["string"],
            required_mentions=["string"],
            unique_authors_only=True,
            winner_count=0,
        )
        assert_matches_type(DrawRunResponse, draw, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: XTwitterScraper) -> None:
        response = client.draws.with_raw_response.run(
            tweet_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draw = response.parse()
        assert_matches_type(DrawRunResponse, draw, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: XTwitterScraper) -> None:
        with client.draws.with_streaming_response.run(
            tweet_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draw = response.parse()
            assert_matches_type(DrawRunResponse, draw, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDraws:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        draw = await async_client.draws.retrieve(
            "id",
        )
        assert_matches_type(DrawRetrieveResponse, draw, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.draws.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draw = await response.parse()
        assert_matches_type(DrawRetrieveResponse, draw, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.draws.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draw = await response.parse()
            assert_matches_type(DrawRetrieveResponse, draw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.draws.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncXTwitterScraper) -> None:
        draw = await async_client.draws.list()
        assert_matches_type(DrawListResponse, draw, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        draw = await async_client.draws.list(
            after="after",
            limit=1,
        )
        assert_matches_type(DrawListResponse, draw, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.draws.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draw = await response.parse()
        assert_matches_type(DrawListResponse, draw, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.draws.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draw = await response.parse()
            assert_matches_type(DrawListResponse, draw, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export(self, async_client: AsyncXTwitterScraper, respx_mock: MockRouter) -> None:
        respx_mock.get("/draws/id/export").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        draw = await async_client.draws.export(
            id="id",
        )
        assert draw.is_closed
        assert await draw.json() == {"foo": "bar"}
        assert cast(Any, draw.is_closed) is True
        assert isinstance(draw, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_with_all_params(
        self, async_client: AsyncXTwitterScraper, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/draws/id/export").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        draw = await async_client.draws.export(
            id="id",
            format="csv",
            type="winners",
        )
        assert draw.is_closed
        assert await draw.json() == {"foo": "bar"}
        assert cast(Any, draw.is_closed) is True
        assert isinstance(draw, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_export(self, async_client: AsyncXTwitterScraper, respx_mock: MockRouter) -> None:
        respx_mock.get("/draws/id/export").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        draw = await async_client.draws.with_raw_response.export(
            id="id",
        )

        assert draw.is_closed is True
        assert draw.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await draw.json() == {"foo": "bar"}
        assert isinstance(draw, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_export(self, async_client: AsyncXTwitterScraper, respx_mock: MockRouter) -> None:
        respx_mock.get("/draws/id/export").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.draws.with_streaming_response.export(
            id="id",
        ) as draw:
            assert not draw.is_closed
            assert draw.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await draw.json() == {"foo": "bar"}
            assert cast(Any, draw.is_closed) is True
            assert isinstance(draw, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, draw.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_export(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.draws.with_raw_response.export(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncXTwitterScraper) -> None:
        draw = await async_client.draws.run(
            tweet_url="https://example.com",
        )
        assert_matches_type(DrawRunResponse, draw, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        draw = await async_client.draws.run(
            tweet_url="https://example.com",
            backup_count=0,
            filter_account_age_days=0,
            filter_language="filterLanguage",
            filter_min_followers=0,
            must_follow_username="mustFollowUsername",
            must_retweet=True,
            required_hashtags=["string"],
            required_keywords=["string"],
            required_mentions=["string"],
            unique_authors_only=True,
            winner_count=0,
        )
        assert_matches_type(DrawRunResponse, draw, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.draws.with_raw_response.run(
            tweet_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draw = await response.parse()
        assert_matches_type(DrawRunResponse, draw, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.draws.with_streaming_response.run(
            tweet_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draw = await response.parse()
            assert_matches_type(DrawRunResponse, draw, path=["response"])

        assert cast(Any, response.is_closed) is True
