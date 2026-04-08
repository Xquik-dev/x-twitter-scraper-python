# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types.x import (
    DmSendResponse,
    DmRetrieveHistoryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDm:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send(self, client: XTwitterScraper) -> None:
        dm = client.x.dm.send(
            user_id="userId",
            account="@elonmusk",
            text="Example text content",
        )
        assert_matches_type(DmSendResponse, dm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_with_all_params(self, client: XTwitterScraper) -> None:
        dm = client.x.dm.send(
            user_id="userId",
            account="@elonmusk",
            text="Example text content",
            media_ids=["1234567890123456789"],
            reply_to_message_id="1234567890123456789",
        )
        assert_matches_type(DmSendResponse, dm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: XTwitterScraper) -> None:
        response = client.x.dm.with_raw_response.send(
            user_id="userId",
            account="@elonmusk",
            text="Example text content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dm = response.parse()
        assert_matches_type(DmSendResponse, dm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: XTwitterScraper) -> None:
        with client.x.dm.with_streaming_response.send(
            user_id="userId",
            account="@elonmusk",
            text="Example text content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dm = response.parse()
            assert_matches_type(DmSendResponse, dm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_send(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.x.dm.with_raw_response.send(
                user_id="",
                account="@elonmusk",
                text="Example text content",
            )


class TestAsyncDm:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncXTwitterScraper) -> None:
        dm = await async_client.x.dm.send(
            user_id="userId",
            account="@elonmusk",
            text="Example text content",
        )
        assert_matches_type(DmSendResponse, dm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        dm = await async_client.x.dm.send(
            user_id="userId",
            account="@elonmusk",
            text="Example text content",
            media_ids=["1234567890123456789"],
            reply_to_message_id="1234567890123456789",
        )
        assert_matches_type(DmSendResponse, dm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.dm.with_raw_response.send(
            user_id="userId",
            account="@elonmusk",
            text="Example text content",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dm = await response.parse()
        assert_matches_type(DmSendResponse, dm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.dm.with_streaming_response.send(
            user_id="userId",
            account="@elonmusk",
            text="Example text content",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dm = await response.parse()
            assert_matches_type(DmSendResponse, dm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_send(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.x.dm.with_raw_response.send(
                user_id="",
                account="@elonmusk",
                text="Example text content",
            )
