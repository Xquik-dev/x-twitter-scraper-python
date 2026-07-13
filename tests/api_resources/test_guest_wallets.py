# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types import (
    GuestWalletTopupResponse,
    GuestWalletCreateResponse,
    GuestWalletRetrieveStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGuestWallets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: XTwitterScraper) -> None:
        guest_wallet = client.guest_wallets.create(
            amount_minor=1000,
            currency="usd",
            idempotency_key="e1cb97D8-dDF3-4AaA-ad0a-49E4A0d1CfAa",
        )
        assert_matches_type(GuestWalletCreateResponse, guest_wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: XTwitterScraper) -> None:
        response = client.guest_wallets.with_raw_response.create(
            amount_minor=1000,
            currency="usd",
            idempotency_key="e1cb97D8-dDF3-4AaA-ad0a-49E4A0d1CfAa",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guest_wallet = response.parse()
        assert_matches_type(GuestWalletCreateResponse, guest_wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: XTwitterScraper) -> None:
        with client.guest_wallets.with_streaming_response.create(
            amount_minor=1000,
            currency="usd",
            idempotency_key="e1cb97D8-dDF3-4AaA-ad0a-49E4A0d1CfAa",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guest_wallet = response.parse()
            assert_matches_type(GuestWalletCreateResponse, guest_wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_status(self, client: XTwitterScraper) -> None:
        guest_wallet = client.guest_wallets.retrieve_status()
        assert_matches_type(GuestWalletRetrieveStatusResponse, guest_wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_status(self, client: XTwitterScraper) -> None:
        response = client.guest_wallets.with_raw_response.retrieve_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guest_wallet = response.parse()
        assert_matches_type(GuestWalletRetrieveStatusResponse, guest_wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_status(self, client: XTwitterScraper) -> None:
        with client.guest_wallets.with_streaming_response.retrieve_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guest_wallet = response.parse()
            assert_matches_type(GuestWalletRetrieveStatusResponse, guest_wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_topup(self, client: XTwitterScraper) -> None:
        guest_wallet = client.guest_wallets.topup(
            amount_minor=1000,
            currency="usd",
            idempotency_key="e1cb97D8-dDF3-4AaA-ad0a-49E4A0d1CfAa",
        )
        assert_matches_type(GuestWalletTopupResponse, guest_wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_topup(self, client: XTwitterScraper) -> None:
        response = client.guest_wallets.with_raw_response.topup(
            amount_minor=1000,
            currency="usd",
            idempotency_key="e1cb97D8-dDF3-4AaA-ad0a-49E4A0d1CfAa",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guest_wallet = response.parse()
        assert_matches_type(GuestWalletTopupResponse, guest_wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_topup(self, client: XTwitterScraper) -> None:
        with client.guest_wallets.with_streaming_response.topup(
            amount_minor=1000,
            currency="usd",
            idempotency_key="e1cb97D8-dDF3-4AaA-ad0a-49E4A0d1CfAa",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guest_wallet = response.parse()
            assert_matches_type(GuestWalletTopupResponse, guest_wallet, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGuestWallets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncXTwitterScraper) -> None:
        guest_wallet = await async_client.guest_wallets.create(
            amount_minor=1000,
            currency="usd",
            idempotency_key="e1cb97D8-dDF3-4AaA-ad0a-49E4A0d1CfAa",
        )
        assert_matches_type(GuestWalletCreateResponse, guest_wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.guest_wallets.with_raw_response.create(
            amount_minor=1000,
            currency="usd",
            idempotency_key="e1cb97D8-dDF3-4AaA-ad0a-49E4A0d1CfAa",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guest_wallet = await response.parse()
        assert_matches_type(GuestWalletCreateResponse, guest_wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.guest_wallets.with_streaming_response.create(
            amount_minor=1000,
            currency="usd",
            idempotency_key="e1cb97D8-dDF3-4AaA-ad0a-49E4A0d1CfAa",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guest_wallet = await response.parse()
            assert_matches_type(GuestWalletCreateResponse, guest_wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_status(self, async_client: AsyncXTwitterScraper) -> None:
        guest_wallet = await async_client.guest_wallets.retrieve_status()
        assert_matches_type(GuestWalletRetrieveStatusResponse, guest_wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_status(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.guest_wallets.with_raw_response.retrieve_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guest_wallet = await response.parse()
        assert_matches_type(GuestWalletRetrieveStatusResponse, guest_wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_status(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.guest_wallets.with_streaming_response.retrieve_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guest_wallet = await response.parse()
            assert_matches_type(GuestWalletRetrieveStatusResponse, guest_wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_topup(self, async_client: AsyncXTwitterScraper) -> None:
        guest_wallet = await async_client.guest_wallets.topup(
            amount_minor=1000,
            currency="usd",
            idempotency_key="e1cb97D8-dDF3-4AaA-ad0a-49E4A0d1CfAa",
        )
        assert_matches_type(GuestWalletTopupResponse, guest_wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_topup(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.guest_wallets.with_raw_response.topup(
            amount_minor=1000,
            currency="usd",
            idempotency_key="e1cb97D8-dDF3-4AaA-ad0a-49E4A0d1CfAa",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guest_wallet = await response.parse()
        assert_matches_type(GuestWalletTopupResponse, guest_wallet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_topup(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.guest_wallets.with_streaming_response.topup(
            amount_minor=1000,
            currency="usd",
            idempotency_key="e1cb97D8-dDF3-4AaA-ad0a-49E4A0d1CfAa",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guest_wallet = await response.parse()
            assert_matches_type(GuestWalletTopupResponse, guest_wallet, path=["response"])

        assert cast(Any, response.is_closed) is True
