# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types.x import (
    XAccountDetail,
    AccountListResponse,
    AccountCreateResponse,
    AccountDeleteResponse,
    AccountReauthResponse,
    AccountBulkRetryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: XTwitterScraper) -> None:
        account = client.x.accounts.create(
            email="user@example.com",
            password="s3cur3Pa$$w0rd",
            username="elonmusk",
        )
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: XTwitterScraper) -> None:
        account = client.x.accounts.create(
            email="user@example.com",
            password="s3cur3Pa$$w0rd",
            username="elonmusk",
            proxy_country="US",
            totp_secret="JBSWY3DPEHPK3PXP",
        )
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: XTwitterScraper) -> None:
        response = client.x.accounts.with_raw_response.create(
            email="user@example.com",
            password="s3cur3Pa$$w0rd",
            username="elonmusk",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: XTwitterScraper) -> None:
        with client.x.accounts.with_streaming_response.create(
            email="user@example.com",
            password="s3cur3Pa$$w0rd",
            username="elonmusk",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountCreateResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: XTwitterScraper) -> None:
        account = client.x.accounts.retrieve(
            "id",
        )
        assert_matches_type(XAccountDetail, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: XTwitterScraper) -> None:
        response = client.x.accounts.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(XAccountDetail, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: XTwitterScraper) -> None:
        with client.x.accounts.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(XAccountDetail, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.accounts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: XTwitterScraper) -> None:
        account = client.x.accounts.list()
        assert_matches_type(AccountListResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: XTwitterScraper) -> None:
        response = client.x.accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountListResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: XTwitterScraper) -> None:
        with client.x.accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountListResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: XTwitterScraper) -> None:
        account = client.x.accounts.delete(
            "id",
        )
        assert_matches_type(AccountDeleteResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: XTwitterScraper) -> None:
        response = client.x.accounts.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountDeleteResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: XTwitterScraper) -> None:
        with client.x.accounts.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountDeleteResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.accounts.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_bulk_retry(self, client: XTwitterScraper) -> None:
        account = client.x.accounts.bulk_retry()
        assert_matches_type(AccountBulkRetryResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_bulk_retry(self, client: XTwitterScraper) -> None:
        response = client.x.accounts.with_raw_response.bulk_retry()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountBulkRetryResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_bulk_retry(self, client: XTwitterScraper) -> None:
        with client.x.accounts.with_streaming_response.bulk_retry() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountBulkRetryResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reauth(self, client: XTwitterScraper) -> None:
        account = client.x.accounts.reauth(
            id="id",
            password="password_value",
        )
        assert_matches_type(AccountReauthResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reauth_with_all_params(self, client: XTwitterScraper) -> None:
        account = client.x.accounts.reauth(
            id="id",
            password="password_value",
            email="user@example.com",
            proxy_country="US",
            totp_secret="totp_secret_value",
        )
        assert_matches_type(AccountReauthResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_reauth(self, client: XTwitterScraper) -> None:
        response = client.x.accounts.with_raw_response.reauth(
            id="id",
            password="password_value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountReauthResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_reauth(self, client: XTwitterScraper) -> None:
        with client.x.accounts.with_streaming_response.reauth(
            id="id",
            password="password_value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountReauthResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_reauth(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.accounts.with_raw_response.reauth(
                id="",
                password="password_value",
            )


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncXTwitterScraper) -> None:
        account = await async_client.x.accounts.create(
            email="user@example.com",
            password="s3cur3Pa$$w0rd",
            username="elonmusk",
        )
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        account = await async_client.x.accounts.create(
            email="user@example.com",
            password="s3cur3Pa$$w0rd",
            username="elonmusk",
            proxy_country="US",
            totp_secret="JBSWY3DPEHPK3PXP",
        )
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.accounts.with_raw_response.create(
            email="user@example.com",
            password="s3cur3Pa$$w0rd",
            username="elonmusk",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountCreateResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.accounts.with_streaming_response.create(
            email="user@example.com",
            password="s3cur3Pa$$w0rd",
            username="elonmusk",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountCreateResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        account = await async_client.x.accounts.retrieve(
            "id",
        )
        assert_matches_type(XAccountDetail, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.accounts.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(XAccountDetail, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.accounts.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(XAccountDetail, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.accounts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncXTwitterScraper) -> None:
        account = await async_client.x.accounts.list()
        assert_matches_type(AccountListResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountListResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountListResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncXTwitterScraper) -> None:
        account = await async_client.x.accounts.delete(
            "id",
        )
        assert_matches_type(AccountDeleteResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.accounts.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountDeleteResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.accounts.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountDeleteResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.accounts.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_bulk_retry(self, async_client: AsyncXTwitterScraper) -> None:
        account = await async_client.x.accounts.bulk_retry()
        assert_matches_type(AccountBulkRetryResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_bulk_retry(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.accounts.with_raw_response.bulk_retry()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountBulkRetryResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_bulk_retry(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.accounts.with_streaming_response.bulk_retry() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountBulkRetryResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reauth(self, async_client: AsyncXTwitterScraper) -> None:
        account = await async_client.x.accounts.reauth(
            id="id",
            password="password_value",
        )
        assert_matches_type(AccountReauthResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reauth_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        account = await async_client.x.accounts.reauth(
            id="id",
            password="password_value",
            email="user@example.com",
            proxy_country="US",
            totp_secret="totp_secret_value",
        )
        assert_matches_type(AccountReauthResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_reauth(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.accounts.with_raw_response.reauth(
            id="id",
            password="password_value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountReauthResponse, account, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_reauth(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.accounts.with_streaming_response.reauth(
            id="id",
            password="password_value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountReauthResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_reauth(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.accounts.with_raw_response.reauth(
                id="",
                password="password_value",
            )
