# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAttachments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download(self, client: XTwitterScraper, respx_mock: MockRouter) -> None:
        respx_mock.get("/support/attachments/att_a1b2c3d4e5f6a1b2c3d4e5f6").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        attachment = client.support.attachments.download(
            id="att_a1b2c3d4e5f6a1b2c3d4e5f6",
        )
        assert attachment.is_closed
        assert attachment.json() == {"foo": "bar"}
        assert cast(Any, attachment.is_closed) is True
        assert isinstance(attachment, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download_with_all_params(self, client: XTwitterScraper, respx_mock: MockRouter) -> None:
        respx_mock.get("/support/attachments/att_a1b2c3d4e5f6a1b2c3d4e5f6").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        attachment = client.support.attachments.download(
            id="att_a1b2c3d4e5f6a1b2c3d4e5f6",
            range="bytes=0-1048575",
        )
        assert attachment.is_closed
        assert attachment.json() == {"foo": "bar"}
        assert cast(Any, attachment.is_closed) is True
        assert isinstance(attachment, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download(self, client: XTwitterScraper, respx_mock: MockRouter) -> None:
        respx_mock.get("/support/attachments/att_a1b2c3d4e5f6a1b2c3d4e5f6").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        attachment = client.support.attachments.with_raw_response.download(
            id="att_a1b2c3d4e5f6a1b2c3d4e5f6",
        )

        assert attachment.is_closed is True
        assert attachment.http_request.headers.get("X-Stainless-Lang") == "python"
        assert attachment.json() == {"foo": "bar"}
        assert isinstance(attachment, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download(self, client: XTwitterScraper, respx_mock: MockRouter) -> None:
        respx_mock.get("/support/attachments/att_a1b2c3d4e5f6a1b2c3d4e5f6").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.support.attachments.with_streaming_response.download(
            id="att_a1b2c3d4e5f6a1b2c3d4e5f6",
        ) as attachment:
            assert not attachment.is_closed
            assert attachment.http_request.headers.get("X-Stainless-Lang") == "python"

            assert attachment.json() == {"foo": "bar"}
            assert cast(Any, attachment.is_closed) is True
            assert isinstance(attachment, StreamedBinaryAPIResponse)

        assert cast(Any, attachment.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.support.attachments.with_raw_response.download(
                id="",
            )


class TestAsyncAttachments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download(self, async_client: AsyncXTwitterScraper, respx_mock: MockRouter) -> None:
        respx_mock.get("/support/attachments/att_a1b2c3d4e5f6a1b2c3d4e5f6").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        attachment = await async_client.support.attachments.download(
            id="att_a1b2c3d4e5f6a1b2c3d4e5f6",
        )
        assert attachment.is_closed
        assert await attachment.json() == {"foo": "bar"}
        assert cast(Any, attachment.is_closed) is True
        assert isinstance(attachment, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download_with_all_params(
        self, async_client: AsyncXTwitterScraper, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/support/attachments/att_a1b2c3d4e5f6a1b2c3d4e5f6").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        attachment = await async_client.support.attachments.download(
            id="att_a1b2c3d4e5f6a1b2c3d4e5f6",
            range="bytes=0-1048575",
        )
        assert attachment.is_closed
        assert await attachment.json() == {"foo": "bar"}
        assert cast(Any, attachment.is_closed) is True
        assert isinstance(attachment, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download(self, async_client: AsyncXTwitterScraper, respx_mock: MockRouter) -> None:
        respx_mock.get("/support/attachments/att_a1b2c3d4e5f6a1b2c3d4e5f6").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        attachment = await async_client.support.attachments.with_raw_response.download(
            id="att_a1b2c3d4e5f6a1b2c3d4e5f6",
        )

        assert attachment.is_closed is True
        assert attachment.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await attachment.json() == {"foo": "bar"}
        assert isinstance(attachment, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download(
        self, async_client: AsyncXTwitterScraper, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/support/attachments/att_a1b2c3d4e5f6a1b2c3d4e5f6").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.support.attachments.with_streaming_response.download(
            id="att_a1b2c3d4e5f6a1b2c3d4e5f6",
        ) as attachment:
            assert not attachment.is_closed
            assert attachment.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await attachment.json() == {"foo": "bar"}
            assert cast(Any, attachment.is_closed) is True
            assert isinstance(attachment, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, attachment.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.support.attachments.with_raw_response.download(
                id="",
            )
