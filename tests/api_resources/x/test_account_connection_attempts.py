# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types.x import AccountConnectionAttemptRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccountConnectionAttempts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: XTwitterScraper) -> None:
        account_connection_attempt = client.x.account_connection_attempts.retrieve(
            "xatt_0123456789abcdef0123456789abcdef",
        )
        assert_matches_type(AccountConnectionAttemptRetrieveResponse, account_connection_attempt, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: XTwitterScraper) -> None:
        response = client.x.account_connection_attempts.with_raw_response.retrieve(
            "xatt_0123456789abcdef0123456789abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_connection_attempt = response.parse()
        assert_matches_type(AccountConnectionAttemptRetrieveResponse, account_connection_attempt, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: XTwitterScraper) -> None:
        with client.x.account_connection_attempts.with_streaming_response.retrieve(
            "xatt_0123456789abcdef0123456789abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_connection_attempt = response.parse()
            assert_matches_type(AccountConnectionAttemptRetrieveResponse, account_connection_attempt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.account_connection_attempts.with_raw_response.retrieve(
                "",
            )


class TestAsyncAccountConnectionAttempts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        account_connection_attempt = await async_client.x.account_connection_attempts.retrieve(
            "xatt_0123456789abcdef0123456789abcdef",
        )
        assert_matches_type(AccountConnectionAttemptRetrieveResponse, account_connection_attempt, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.account_connection_attempts.with_raw_response.retrieve(
            "xatt_0123456789abcdef0123456789abcdef",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_connection_attempt = await response.parse()
        assert_matches_type(AccountConnectionAttemptRetrieveResponse, account_connection_attempt, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.account_connection_attempts.with_streaming_response.retrieve(
            "xatt_0123456789abcdef0123456789abcdef",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_connection_attempt = await response.parse()
            assert_matches_type(AccountConnectionAttemptRetrieveResponse, account_connection_attempt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.account_connection_attempts.with_raw_response.retrieve(
                "",
            )
