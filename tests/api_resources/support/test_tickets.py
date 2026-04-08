# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types.support import (
    TicketListResponse,
    TicketReplyResponse,
    TicketCreateResponse,
    TicketUpdateResponse,
    TicketRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTickets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: XTwitterScraper) -> None:
        ticket = client.support.tickets.create(
            body="I am unable to connect my X account. Please help.",
            subject="Cannot connect X account",
        )
        assert_matches_type(TicketCreateResponse, ticket, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: XTwitterScraper) -> None:
        response = client.support.tickets.with_raw_response.create(
            body="I am unable to connect my X account. Please help.",
            subject="Cannot connect X account",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(TicketCreateResponse, ticket, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: XTwitterScraper) -> None:
        with client.support.tickets.with_streaming_response.create(
            body="I am unable to connect my X account. Please help.",
            subject="Cannot connect X account",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = response.parse()
            assert_matches_type(TicketCreateResponse, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: XTwitterScraper) -> None:
        ticket = client.support.tickets.retrieve(
            "messages_value",
        )
        assert_matches_type(TicketRetrieveResponse, ticket, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: XTwitterScraper) -> None:
        response = client.support.tickets.with_raw_response.retrieve(
            "messages_value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(TicketRetrieveResponse, ticket, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: XTwitterScraper) -> None:
        with client.support.tickets.with_streaming_response.retrieve(
            "messages_value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = response.parse()
            assert_matches_type(TicketRetrieveResponse, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.support.tickets.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: XTwitterScraper) -> None:
        ticket = client.support.tickets.update(
            id="id",
            status="resolved",
        )
        assert_matches_type(TicketUpdateResponse, ticket, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: XTwitterScraper) -> None:
        response = client.support.tickets.with_raw_response.update(
            id="id",
            status="resolved",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(TicketUpdateResponse, ticket, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: XTwitterScraper) -> None:
        with client.support.tickets.with_streaming_response.update(
            id="id",
            status="resolved",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = response.parse()
            assert_matches_type(TicketUpdateResponse, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.support.tickets.with_raw_response.update(
                id="",
                status="resolved",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: XTwitterScraper) -> None:
        ticket = client.support.tickets.list()
        assert_matches_type(TicketListResponse, ticket, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: XTwitterScraper) -> None:
        response = client.support.tickets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(TicketListResponse, ticket, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: XTwitterScraper) -> None:
        with client.support.tickets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = response.parse()
            assert_matches_type(TicketListResponse, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reply(self, client: XTwitterScraper) -> None:
        ticket = client.support.tickets.reply(
            id="id",
            body="Thank you for the update.",
        )
        assert_matches_type(TicketReplyResponse, ticket, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_reply(self, client: XTwitterScraper) -> None:
        response = client.support.tickets.with_raw_response.reply(
            id="id",
            body="Thank you for the update.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = response.parse()
        assert_matches_type(TicketReplyResponse, ticket, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_reply(self, client: XTwitterScraper) -> None:
        with client.support.tickets.with_streaming_response.reply(
            id="id",
            body="Thank you for the update.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = response.parse()
            assert_matches_type(TicketReplyResponse, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_reply(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.support.tickets.with_raw_response.reply(
                id="",
                body="Thank you for the update.",
            )


class TestAsyncTickets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncXTwitterScraper) -> None:
        ticket = await async_client.support.tickets.create(
            body="I am unable to connect my X account. Please help.",
            subject="Cannot connect X account",
        )
        assert_matches_type(TicketCreateResponse, ticket, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.support.tickets.with_raw_response.create(
            body="I am unable to connect my X account. Please help.",
            subject="Cannot connect X account",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = await response.parse()
        assert_matches_type(TicketCreateResponse, ticket, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.support.tickets.with_streaming_response.create(
            body="I am unable to connect my X account. Please help.",
            subject="Cannot connect X account",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = await response.parse()
            assert_matches_type(TicketCreateResponse, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        ticket = await async_client.support.tickets.retrieve(
            "messages_value",
        )
        assert_matches_type(TicketRetrieveResponse, ticket, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.support.tickets.with_raw_response.retrieve(
            "messages_value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = await response.parse()
        assert_matches_type(TicketRetrieveResponse, ticket, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.support.tickets.with_streaming_response.retrieve(
            "messages_value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = await response.parse()
            assert_matches_type(TicketRetrieveResponse, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.support.tickets.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncXTwitterScraper) -> None:
        ticket = await async_client.support.tickets.update(
            id="id",
            status="resolved",
        )
        assert_matches_type(TicketUpdateResponse, ticket, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.support.tickets.with_raw_response.update(
            id="id",
            status="resolved",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = await response.parse()
        assert_matches_type(TicketUpdateResponse, ticket, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.support.tickets.with_streaming_response.update(
            id="id",
            status="resolved",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = await response.parse()
            assert_matches_type(TicketUpdateResponse, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.support.tickets.with_raw_response.update(
                id="",
                status="resolved",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncXTwitterScraper) -> None:
        ticket = await async_client.support.tickets.list()
        assert_matches_type(TicketListResponse, ticket, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.support.tickets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = await response.parse()
        assert_matches_type(TicketListResponse, ticket, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.support.tickets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = await response.parse()
            assert_matches_type(TicketListResponse, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reply(self, async_client: AsyncXTwitterScraper) -> None:
        ticket = await async_client.support.tickets.reply(
            id="id",
            body="Thank you for the update.",
        )
        assert_matches_type(TicketReplyResponse, ticket, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_reply(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.support.tickets.with_raw_response.reply(
            id="id",
            body="Thank you for the update.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ticket = await response.parse()
        assert_matches_type(TicketReplyResponse, ticket, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_reply(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.support.tickets.with_streaming_response.reply(
            id="id",
            body="Thank you for the update.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ticket = await response.parse()
            assert_matches_type(TicketReplyResponse, ticket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_reply(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.support.tickets.with_raw_response.reply(
                id="",
                body="Thank you for the update.",
            )
