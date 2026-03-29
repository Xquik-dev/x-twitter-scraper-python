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
    ExtractionRunResponse,
    ExtractionListResponse,
    ExtractionRetrieveResponse,
    ExtractionEstimateCostResponse,
)
from x_twitter_scraper._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExtractions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: XTwitterScraper) -> None:
        extraction = client.extractions.retrieve(
            id="id",
        )
        assert_matches_type(ExtractionRetrieveResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: XTwitterScraper) -> None:
        extraction = client.extractions.retrieve(
            id="id",
            after="after",
            limit=1,
        )
        assert_matches_type(ExtractionRetrieveResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: XTwitterScraper) -> None:
        response = client.extractions.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction = response.parse()
        assert_matches_type(ExtractionRetrieveResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: XTwitterScraper) -> None:
        with client.extractions.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction = response.parse()
            assert_matches_type(ExtractionRetrieveResponse, extraction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.extractions.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: XTwitterScraper) -> None:
        extraction = client.extractions.list()
        assert_matches_type(ExtractionListResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: XTwitterScraper) -> None:
        extraction = client.extractions.list(
            after="after",
            limit=1,
            status="running",
            tool_type="article_extractor",
        )
        assert_matches_type(ExtractionListResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: XTwitterScraper) -> None:
        response = client.extractions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction = response.parse()
        assert_matches_type(ExtractionListResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: XTwitterScraper) -> None:
        with client.extractions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction = response.parse()
            assert_matches_type(ExtractionListResponse, extraction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_estimate_cost(self, client: XTwitterScraper) -> None:
        extraction = client.extractions.estimate_cost(
            tool_type="article_extractor",
        )
        assert_matches_type(ExtractionEstimateCostResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_estimate_cost_with_all_params(self, client: XTwitterScraper) -> None:
        extraction = client.extractions.estimate_cost(
            tool_type="article_extractor",
            advanced_query="advancedQuery",
            exact_phrase="exactPhrase",
            exclude_words="excludeWords",
            search_query="searchQuery",
            target_community_id="targetCommunityId",
            target_list_id="targetListId",
            target_space_id="targetSpaceId",
            target_tweet_id="targetTweetId",
            target_username="targetUsername",
        )
        assert_matches_type(ExtractionEstimateCostResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_estimate_cost(self, client: XTwitterScraper) -> None:
        response = client.extractions.with_raw_response.estimate_cost(
            tool_type="article_extractor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction = response.parse()
        assert_matches_type(ExtractionEstimateCostResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_estimate_cost(self, client: XTwitterScraper) -> None:
        with client.extractions.with_streaming_response.estimate_cost(
            tool_type="article_extractor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction = response.parse()
            assert_matches_type(ExtractionEstimateCostResponse, extraction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_results(self, client: XTwitterScraper, respx_mock: MockRouter) -> None:
        respx_mock.get("/extractions/id/export").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        extraction = client.extractions.export_results(
            id="id",
        )
        assert extraction.is_closed
        assert extraction.json() == {"foo": "bar"}
        assert cast(Any, extraction.is_closed) is True
        assert isinstance(extraction, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_results_with_all_params(self, client: XTwitterScraper, respx_mock: MockRouter) -> None:
        respx_mock.get("/extractions/id/export").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        extraction = client.extractions.export_results(
            id="id",
            format="csv",
        )
        assert extraction.is_closed
        assert extraction.json() == {"foo": "bar"}
        assert cast(Any, extraction.is_closed) is True
        assert isinstance(extraction, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_export_results(self, client: XTwitterScraper, respx_mock: MockRouter) -> None:
        respx_mock.get("/extractions/id/export").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        extraction = client.extractions.with_raw_response.export_results(
            id="id",
        )

        assert extraction.is_closed is True
        assert extraction.http_request.headers.get("X-Stainless-Lang") == "python"
        assert extraction.json() == {"foo": "bar"}
        assert isinstance(extraction, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_export_results(self, client: XTwitterScraper, respx_mock: MockRouter) -> None:
        respx_mock.get("/extractions/id/export").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.extractions.with_streaming_response.export_results(
            id="id",
        ) as extraction:
            assert not extraction.is_closed
            assert extraction.http_request.headers.get("X-Stainless-Lang") == "python"

            assert extraction.json() == {"foo": "bar"}
            assert cast(Any, extraction.is_closed) is True
            assert isinstance(extraction, StreamedBinaryAPIResponse)

        assert cast(Any, extraction.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_export_results(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.extractions.with_raw_response.export_results(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run(self, client: XTwitterScraper) -> None:
        extraction = client.extractions.run(
            tool_type="article_extractor",
        )
        assert_matches_type(ExtractionRunResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_with_all_params(self, client: XTwitterScraper) -> None:
        extraction = client.extractions.run(
            tool_type="article_extractor",
            advanced_query="advancedQuery",
            exact_phrase="exactPhrase",
            exclude_words="excludeWords",
            search_query="searchQuery",
            target_community_id="targetCommunityId",
            target_list_id="targetListId",
            target_space_id="targetSpaceId",
            target_tweet_id="targetTweetId",
            target_username="targetUsername",
        )
        assert_matches_type(ExtractionRunResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run(self, client: XTwitterScraper) -> None:
        response = client.extractions.with_raw_response.run(
            tool_type="article_extractor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction = response.parse()
        assert_matches_type(ExtractionRunResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run(self, client: XTwitterScraper) -> None:
        with client.extractions.with_streaming_response.run(
            tool_type="article_extractor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction = response.parse()
            assert_matches_type(ExtractionRunResponse, extraction, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExtractions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        extraction = await async_client.extractions.retrieve(
            id="id",
        )
        assert_matches_type(ExtractionRetrieveResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        extraction = await async_client.extractions.retrieve(
            id="id",
            after="after",
            limit=1,
        )
        assert_matches_type(ExtractionRetrieveResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.extractions.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction = await response.parse()
        assert_matches_type(ExtractionRetrieveResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.extractions.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction = await response.parse()
            assert_matches_type(ExtractionRetrieveResponse, extraction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.extractions.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncXTwitterScraper) -> None:
        extraction = await async_client.extractions.list()
        assert_matches_type(ExtractionListResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        extraction = await async_client.extractions.list(
            after="after",
            limit=1,
            status="running",
            tool_type="article_extractor",
        )
        assert_matches_type(ExtractionListResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.extractions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction = await response.parse()
        assert_matches_type(ExtractionListResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.extractions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction = await response.parse()
            assert_matches_type(ExtractionListResponse, extraction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_estimate_cost(self, async_client: AsyncXTwitterScraper) -> None:
        extraction = await async_client.extractions.estimate_cost(
            tool_type="article_extractor",
        )
        assert_matches_type(ExtractionEstimateCostResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_estimate_cost_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        extraction = await async_client.extractions.estimate_cost(
            tool_type="article_extractor",
            advanced_query="advancedQuery",
            exact_phrase="exactPhrase",
            exclude_words="excludeWords",
            search_query="searchQuery",
            target_community_id="targetCommunityId",
            target_list_id="targetListId",
            target_space_id="targetSpaceId",
            target_tweet_id="targetTweetId",
            target_username="targetUsername",
        )
        assert_matches_type(ExtractionEstimateCostResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_estimate_cost(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.extractions.with_raw_response.estimate_cost(
            tool_type="article_extractor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction = await response.parse()
        assert_matches_type(ExtractionEstimateCostResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_estimate_cost(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.extractions.with_streaming_response.estimate_cost(
            tool_type="article_extractor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction = await response.parse()
            assert_matches_type(ExtractionEstimateCostResponse, extraction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_results(self, async_client: AsyncXTwitterScraper, respx_mock: MockRouter) -> None:
        respx_mock.get("/extractions/id/export").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        extraction = await async_client.extractions.export_results(
            id="id",
        )
        assert extraction.is_closed
        assert await extraction.json() == {"foo": "bar"}
        assert cast(Any, extraction.is_closed) is True
        assert isinstance(extraction, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_results_with_all_params(
        self, async_client: AsyncXTwitterScraper, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/extractions/id/export").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        extraction = await async_client.extractions.export_results(
            id="id",
            format="csv",
        )
        assert extraction.is_closed
        assert await extraction.json() == {"foo": "bar"}
        assert cast(Any, extraction.is_closed) is True
        assert isinstance(extraction, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_export_results(
        self, async_client: AsyncXTwitterScraper, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/extractions/id/export").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        extraction = await async_client.extractions.with_raw_response.export_results(
            id="id",
        )

        assert extraction.is_closed is True
        assert extraction.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await extraction.json() == {"foo": "bar"}
        assert isinstance(extraction, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_export_results(
        self, async_client: AsyncXTwitterScraper, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/extractions/id/export").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.extractions.with_streaming_response.export_results(
            id="id",
        ) as extraction:
            assert not extraction.is_closed
            assert extraction.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await extraction.json() == {"foo": "bar"}
            assert cast(Any, extraction.is_closed) is True
            assert isinstance(extraction, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, extraction.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_export_results(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.extractions.with_raw_response.export_results(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run(self, async_client: AsyncXTwitterScraper) -> None:
        extraction = await async_client.extractions.run(
            tool_type="article_extractor",
        )
        assert_matches_type(ExtractionRunResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        extraction = await async_client.extractions.run(
            tool_type="article_extractor",
            advanced_query="advancedQuery",
            exact_phrase="exactPhrase",
            exclude_words="excludeWords",
            search_query="searchQuery",
            target_community_id="targetCommunityId",
            target_list_id="targetListId",
            target_space_id="targetSpaceId",
            target_tweet_id="targetTweetId",
            target_username="targetUsername",
        )
        assert_matches_type(ExtractionRunResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.extractions.with_raw_response.run(
            tool_type="article_extractor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extraction = await response.parse()
        assert_matches_type(ExtractionRunResponse, extraction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.extractions.with_streaming_response.run(
            tool_type="article_extractor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extraction = await response.parse()
            assert_matches_type(ExtractionRunResponse, extraction, path=["response"])

        assert cast(Any, response.is_closed) is True
