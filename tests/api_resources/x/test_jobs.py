# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types.x import (
    JobSearchResponse,
    JobRetrieveResponse,
    JobListLocationsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: XTwitterScraper) -> None:
        job = client.x.jobs.retrieve(
            id="1899202395210649861",
        )
        assert_matches_type(JobRetrieveResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: XTwitterScraper) -> None:
        job = client.x.jobs.retrieve(
            id="1899202395210649861",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(JobRetrieveResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: XTwitterScraper) -> None:
        response = client.x.jobs.with_raw_response.retrieve(
            id="1899202395210649861",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        job = response.parse()
        assert_matches_type(JobRetrieveResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: XTwitterScraper) -> None:
        with client.x.jobs.with_streaming_response.retrieve(
            id="1899202395210649861",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            job = response.parse()
            assert_matches_type(JobRetrieveResponse, job, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.jobs.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_locations(self, client: XTwitterScraper) -> None:
        job = client.x.jobs.list_locations(
            q="new york",
        )
        assert_matches_type(JobListLocationsResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_locations_with_all_params(self, client: XTwitterScraper) -> None:
        job = client.x.jobs.list_locations(
            q="new york",
            fields="id,text,author.username",
            limit=5,
            omit="entities,media",
        )
        assert_matches_type(JobListLocationsResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_locations(self, client: XTwitterScraper) -> None:
        response = client.x.jobs.with_raw_response.list_locations(
            q="new york",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        job = response.parse()
        assert_matches_type(JobListLocationsResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_locations(self, client: XTwitterScraper) -> None:
        with client.x.jobs.with_streaming_response.list_locations(
            q="new york",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            job = response.parse()
            assert_matches_type(JobListLocationsResponse, job, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: XTwitterScraper) -> None:
        job = client.x.jobs.search(
            q="engineer",
        )
        assert_matches_type(JobSearchResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: XTwitterScraper) -> None:
        job = client.x.jobs.search(
            q="engineer",
            company="SpaceX",
            cursor="cursor",
            employment_type="full_time",
            fields="id,text,author.username",
            location="Berlin",
            location_id="1720462281849397612",
            location_type="remote,hybrid",
            omit="entities,media",
            page_size=1,
            seniority="senior,lead",
        )
        assert_matches_type(JobSearchResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: XTwitterScraper) -> None:
        response = client.x.jobs.with_raw_response.search(
            q="engineer",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        job = response.parse()
        assert_matches_type(JobSearchResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: XTwitterScraper) -> None:
        with client.x.jobs.with_streaming_response.search(
            q="engineer",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            job = response.parse()
            assert_matches_type(JobSearchResponse, job, path=["response"])

        assert response.is_closed is True


class TestAsyncJobs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        job = await async_client.x.jobs.retrieve(
            id="1899202395210649861",
        )
        assert_matches_type(JobRetrieveResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        job = await async_client.x.jobs.retrieve(
            id="1899202395210649861",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(JobRetrieveResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.jobs.with_raw_response.retrieve(
            id="1899202395210649861",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        job = await response.parse()
        assert_matches_type(JobRetrieveResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.jobs.with_streaming_response.retrieve(
            id="1899202395210649861",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            job = await response.parse()
            assert_matches_type(JobRetrieveResponse, job, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.jobs.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_locations(self, async_client: AsyncXTwitterScraper) -> None:
        job = await async_client.x.jobs.list_locations(
            q="new york",
        )
        assert_matches_type(JobListLocationsResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_locations_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        job = await async_client.x.jobs.list_locations(
            q="new york",
            fields="id,text,author.username",
            limit=5,
            omit="entities,media",
        )
        assert_matches_type(JobListLocationsResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_locations(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.jobs.with_raw_response.list_locations(
            q="new york",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        job = await response.parse()
        assert_matches_type(JobListLocationsResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_locations(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.jobs.with_streaming_response.list_locations(
            q="new york",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            job = await response.parse()
            assert_matches_type(JobListLocationsResponse, job, path=["response"])

        assert response.is_closed is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncXTwitterScraper) -> None:
        job = await async_client.x.jobs.search(
            q="engineer",
        )
        assert_matches_type(JobSearchResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        job = await async_client.x.jobs.search(
            q="engineer",
            company="SpaceX",
            cursor="cursor",
            employment_type="full_time",
            fields="id,text,author.username",
            location="Berlin",
            location_id="1720462281849397612",
            location_type="remote,hybrid",
            omit="entities,media",
            page_size=1,
            seniority="senior,lead",
        )
        assert_matches_type(JobSearchResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.jobs.with_raw_response.search(
            q="engineer",
        )

        assert response.is_closed is True
        assert response.http_request.headers["X-Stainless-Lang"] == "python"
        job = await response.parse()
        assert_matches_type(JobSearchResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.jobs.with_streaming_response.search(
            q="engineer",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers["X-Stainless-Lang"] == "python"

            job = await response.parse()
            assert_matches_type(JobSearchResponse, job, path=["response"])

        assert response.is_closed is True
