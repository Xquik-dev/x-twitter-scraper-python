# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types.x import (
    DmUpdateResponse,
    DmRetrieveHistoryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDm:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: XTwitterScraper) -> None:
        dm = client.x.dm.update(
            user_id="userId",
            account="account",
            text="text",
        )
        assert_matches_type(DmUpdateResponse, dm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: XTwitterScraper) -> None:
        dm = client.x.dm.update(
            user_id="userId",
            account="account",
            text="text",
            media_ids=["string"],
            reply_to_message_id="reply_to_message_id",
        )
        assert_matches_type(DmUpdateResponse, dm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: XTwitterScraper) -> None:
        response = client.x.dm.with_raw_response.update(
            user_id="userId",
            account="account",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dm = response.parse()
        assert_matches_type(DmUpdateResponse, dm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: XTwitterScraper) -> None:
        with client.x.dm.with_streaming_response.update(
            user_id="userId",
            account="account",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dm = response.parse()
            assert_matches_type(DmUpdateResponse, dm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.x.dm.with_raw_response.update(
                user_id="",
                account="account",
                text="text",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_history(self, client: XTwitterScraper) -> None:
        dm = client.x.dm.retrieve_history(
            user_id="userId",
        )
        assert_matches_type(DmRetrieveHistoryResponse, dm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_history_with_all_params(self, client: XTwitterScraper) -> None:
        dm = client.x.dm.retrieve_history(
            user_id="userId",
            cursor="cursor",
            max_id="maxId",
        )
        assert_matches_type(DmRetrieveHistoryResponse, dm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_history(self, client: XTwitterScraper) -> None:
        response = client.x.dm.with_raw_response.retrieve_history(
            user_id="userId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dm = response.parse()
        assert_matches_type(DmRetrieveHistoryResponse, dm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_history(self, client: XTwitterScraper) -> None:
        with client.x.dm.with_streaming_response.retrieve_history(
            user_id="userId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dm = response.parse()
            assert_matches_type(DmRetrieveHistoryResponse, dm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_history(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.x.dm.with_raw_response.retrieve_history(
                user_id="",
            )


class TestAsyncDm:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncXTwitterScraper) -> None:
        dm = await async_client.x.dm.update(
            user_id="userId",
            account="account",
            text="text",
        )
        assert_matches_type(DmUpdateResponse, dm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        dm = await async_client.x.dm.update(
            user_id="userId",
            account="account",
            text="text",
            media_ids=["string"],
            reply_to_message_id="reply_to_message_id",
        )
        assert_matches_type(DmUpdateResponse, dm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.dm.with_raw_response.update(
            user_id="userId",
            account="account",
            text="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dm = await response.parse()
        assert_matches_type(DmUpdateResponse, dm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.dm.with_streaming_response.update(
            user_id="userId",
            account="account",
            text="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dm = await response.parse()
            assert_matches_type(DmUpdateResponse, dm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.x.dm.with_raw_response.update(
                user_id="",
                account="account",
                text="text",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_history(self, async_client: AsyncXTwitterScraper) -> None:
        dm = await async_client.x.dm.retrieve_history(
            user_id="userId",
        )
        assert_matches_type(DmRetrieveHistoryResponse, dm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_history_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        dm = await async_client.x.dm.retrieve_history(
            user_id="userId",
            cursor="cursor",
            max_id="maxId",
        )
        assert_matches_type(DmRetrieveHistoryResponse, dm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_history(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.dm.with_raw_response.retrieve_history(
            user_id="userId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dm = await response.parse()
        assert_matches_type(DmRetrieveHistoryResponse, dm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_history(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.dm.with_streaming_response.retrieve_history(
            user_id="userId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dm = await response.parse()
            assert_matches_type(DmRetrieveHistoryResponse, dm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_history(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.x.dm.with_raw_response.retrieve_history(
                user_id="",
            )
