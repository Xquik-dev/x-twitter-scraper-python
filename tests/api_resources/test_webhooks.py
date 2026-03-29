# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types import (
    WebhookListResponse,
    WebhookTestResponse,
    WebhookCreateResponse,
    WebhookUpdateResponse,
    WebhookDeactivateResponse,
    WebhookListDeliveriesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: XTwitterScraper) -> None:
        webhook = client.webhooks.create(
            event_types=["tweet.new"],
            url="https://example.com",
        )
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: XTwitterScraper) -> None:
        response = client.webhooks.with_raw_response.create(
            event_types=["tweet.new"],
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: XTwitterScraper) -> None:
        with client.webhooks.with_streaming_response.create(
            event_types=["tweet.new"],
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: XTwitterScraper) -> None:
        webhook = client.webhooks.update(
            id="id",
        )
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: XTwitterScraper) -> None:
        webhook = client.webhooks.update(
            id="id",
            event_types=["tweet.new"],
            is_active=True,
            url="https://example.com",
        )
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: XTwitterScraper) -> None:
        response = client.webhooks.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: XTwitterScraper) -> None:
        with client.webhooks.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: XTwitterScraper) -> None:
        webhook = client.webhooks.list()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: XTwitterScraper) -> None:
        response = client.webhooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: XTwitterScraper) -> None:
        with client.webhooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookListResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_deactivate(self, client: XTwitterScraper) -> None:
        webhook = client.webhooks.deactivate(
            "id",
        )
        assert_matches_type(WebhookDeactivateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_deactivate(self, client: XTwitterScraper) -> None:
        response = client.webhooks.with_raw_response.deactivate(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookDeactivateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_deactivate(self, client: XTwitterScraper) -> None:
        with client.webhooks.with_streaming_response.deactivate(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookDeactivateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_deactivate(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.with_raw_response.deactivate(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_deliveries(self, client: XTwitterScraper) -> None:
        webhook = client.webhooks.list_deliveries(
            "id",
        )
        assert_matches_type(WebhookListDeliveriesResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_deliveries(self, client: XTwitterScraper) -> None:
        response = client.webhooks.with_raw_response.list_deliveries(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookListDeliveriesResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_deliveries(self, client: XTwitterScraper) -> None:
        with client.webhooks.with_streaming_response.list_deliveries(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookListDeliveriesResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_deliveries(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.with_raw_response.list_deliveries(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_test(self, client: XTwitterScraper) -> None:
        webhook = client.webhooks.test(
            "id",
        )
        assert_matches_type(WebhookTestResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_test(self, client: XTwitterScraper) -> None:
        response = client.webhooks.with_raw_response.test(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookTestResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_test(self, client: XTwitterScraper) -> None:
        with client.webhooks.with_streaming_response.test(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookTestResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_test(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.with_raw_response.test(
                "",
            )


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncXTwitterScraper) -> None:
        webhook = await async_client.webhooks.create(
            event_types=["tweet.new"],
            url="https://example.com",
        )
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.webhooks.with_raw_response.create(
            event_types=["tweet.new"],
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.webhooks.with_streaming_response.create(
            event_types=["tweet.new"],
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncXTwitterScraper) -> None:
        webhook = await async_client.webhooks.update(
            id="id",
        )
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        webhook = await async_client.webhooks.update(
            id="id",
            event_types=["tweet.new"],
            is_active=True,
            url="https://example.com",
        )
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.webhooks.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.webhooks.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncXTwitterScraper) -> None:
        webhook = await async_client.webhooks.list()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.webhooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.webhooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookListResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_deactivate(self, async_client: AsyncXTwitterScraper) -> None:
        webhook = await async_client.webhooks.deactivate(
            "id",
        )
        assert_matches_type(WebhookDeactivateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_deactivate(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.webhooks.with_raw_response.deactivate(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookDeactivateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_deactivate(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.webhooks.with_streaming_response.deactivate(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookDeactivateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_deactivate(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.with_raw_response.deactivate(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_deliveries(self, async_client: AsyncXTwitterScraper) -> None:
        webhook = await async_client.webhooks.list_deliveries(
            "id",
        )
        assert_matches_type(WebhookListDeliveriesResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_deliveries(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.webhooks.with_raw_response.list_deliveries(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookListDeliveriesResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_deliveries(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.webhooks.with_streaming_response.list_deliveries(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookListDeliveriesResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_deliveries(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.with_raw_response.list_deliveries(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_test(self, async_client: AsyncXTwitterScraper) -> None:
        webhook = await async_client.webhooks.test(
            "id",
        )
        assert_matches_type(WebhookTestResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_test(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.webhooks.with_raw_response.test(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookTestResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_test(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.webhooks.with_streaming_response.test(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookTestResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_test(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.with_raw_response.test(
                "",
            )
