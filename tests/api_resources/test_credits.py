# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types import (
    CreditTopupBalanceResponse,
    CreditRetrieveBalanceResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCredits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_balance(self, client: XTwitterScraper) -> None:
        credit = client.credits.retrieve_balance()
        assert_matches_type(CreditRetrieveBalanceResponse, credit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_balance(self, client: XTwitterScraper) -> None:
        response = client.credits.with_raw_response.retrieve_balance()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = response.parse()
        assert_matches_type(CreditRetrieveBalanceResponse, credit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_balance(self, client: XTwitterScraper) -> None:
        with client.credits.with_streaming_response.retrieve_balance() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = response.parse()
            assert_matches_type(CreditRetrieveBalanceResponse, credit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_topup_balance(self, client: XTwitterScraper) -> None:
        credit = client.credits.topup_balance(
            amount=0,
        )
        assert_matches_type(CreditTopupBalanceResponse, credit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_topup_balance(self, client: XTwitterScraper) -> None:
        response = client.credits.with_raw_response.topup_balance(
            amount=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = response.parse()
        assert_matches_type(CreditTopupBalanceResponse, credit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_topup_balance(self, client: XTwitterScraper) -> None:
        with client.credits.with_streaming_response.topup_balance(
            amount=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = response.parse()
            assert_matches_type(CreditTopupBalanceResponse, credit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCredits:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_balance(self, async_client: AsyncXTwitterScraper) -> None:
        credit = await async_client.credits.retrieve_balance()
        assert_matches_type(CreditRetrieveBalanceResponse, credit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_balance(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.credits.with_raw_response.retrieve_balance()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = await response.parse()
        assert_matches_type(CreditRetrieveBalanceResponse, credit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_balance(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.credits.with_streaming_response.retrieve_balance() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = await response.parse()
            assert_matches_type(CreditRetrieveBalanceResponse, credit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_topup_balance(self, async_client: AsyncXTwitterScraper) -> None:
        credit = await async_client.credits.topup_balance(
            amount=0,
        )
        assert_matches_type(CreditTopupBalanceResponse, credit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_topup_balance(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.credits.with_raw_response.topup_balance(
            amount=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = await response.parse()
        assert_matches_type(CreditTopupBalanceResponse, credit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_topup_balance(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.credits.with_streaming_response.topup_balance(
            amount=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = await response.parse()
            assert_matches_type(CreditTopupBalanceResponse, credit, path=["response"])

        assert cast(Any, response.is_closed) is True
