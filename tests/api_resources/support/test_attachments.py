# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

import pytest

from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)


class TestAttachments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_download(self, client: XTwitterScraper) -> None:
        attachment = client.support.attachments.download(
            id="att_a1b2c3d4e5f6a1b2c3d4e5f6",
        )
        assert attachment.http_request.url.path == "/support/attachments/att_a1b2c3d4e5f6a1b2c3d4e5f6"
        assert attachment.is_closed
        assert attachment.json() == {"foo": "bar"}
        assert cast(Any, attachment.is_closed) is True
        assert isinstance(attachment, BinaryAPIResponse)

    @parametrize
    def test_method_download_with_all_params(self, client: XTwitterScraper) -> None:
        attachment = client.support.attachments.download(
            id="att_a1b2c3d4e5f6a1b2c3d4e5f6",
            range="bytes=0-1048575",
        )
        assert attachment.http_request.url.path == "/support/attachments/att_a1b2c3d4e5f6a1b2c3d4e5f6"
        assert attachment.is_closed
        assert attachment.json() == {"foo": "bar"}
        assert cast(Any, attachment.is_closed) is True
        assert isinstance(attachment, BinaryAPIResponse)

    @parametrize
    def test_raw_response_download(self, client: XTwitterScraper) -> None:

        attachment = client.support.attachments.with_raw_response.download(
            id="att_a1b2c3d4e5f6a1b2c3d4e5f6",
        )
        assert attachment.http_request.url.path == "/support/attachments/att_a1b2c3d4e5f6a1b2c3d4e5f6"

        assert attachment.is_closed is True
        assert attachment.http_request.headers.get("X-Stainless-Lang") == "python"
        assert attachment.json() == {"foo": "bar"}
        assert isinstance(attachment, BinaryAPIResponse)

    @parametrize
    def test_streaming_response_download(self, client: XTwitterScraper) -> None:
        with client.support.attachments.with_streaming_response.download(
            id="att_a1b2c3d4e5f6a1b2c3d4e5f6",
        ) as attachment:
            assert attachment.http_request.url.path == "/support/attachments/att_a1b2c3d4e5f6a1b2c3d4e5f6"
            assert not attachment.is_closed
            assert attachment.http_request.headers.get("X-Stainless-Lang") == "python"

            assert attachment.json() == {"foo": "bar"}
            assert cast(Any, attachment.is_closed) is True
            assert isinstance(attachment, StreamedBinaryAPIResponse)

        assert cast(Any, attachment.is_closed) is True

    @parametrize
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
    async def test_method_download(self, async_client: AsyncXTwitterScraper) -> None:
        attachment = await async_client.support.attachments.download(
            id="att_a1b2c3d4e5f6a1b2c3d4e5f6",
        )
        assert attachment.http_request.url.path == "/support/attachments/att_a1b2c3d4e5f6a1b2c3d4e5f6"
        assert attachment.is_closed
        assert await attachment.json() == {"foo": "bar"}
        assert cast(Any, attachment.is_closed) is True
        assert isinstance(attachment, AsyncBinaryAPIResponse)

    @parametrize
    async def test_method_download_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        attachment = await async_client.support.attachments.download(
            id="att_a1b2c3d4e5f6a1b2c3d4e5f6",
            range="bytes=0-1048575",
        )
        assert attachment.http_request.url.path == "/support/attachments/att_a1b2c3d4e5f6a1b2c3d4e5f6"
        assert attachment.is_closed
        assert await attachment.json() == {"foo": "bar"}
        assert cast(Any, attachment.is_closed) is True
        assert isinstance(attachment, AsyncBinaryAPIResponse)

    @parametrize
    async def test_raw_response_download(self, async_client: AsyncXTwitterScraper) -> None:

        attachment = await async_client.support.attachments.with_raw_response.download(
            id="att_a1b2c3d4e5f6a1b2c3d4e5f6",
        )
        assert attachment.http_request.url.path == "/support/attachments/att_a1b2c3d4e5f6a1b2c3d4e5f6"

        assert attachment.is_closed is True
        assert attachment.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await attachment.json() == {"foo": "bar"}
        assert isinstance(attachment, AsyncBinaryAPIResponse)

    @parametrize
    async def test_streaming_response_download(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.support.attachments.with_streaming_response.download(
            id="att_a1b2c3d4e5f6a1b2c3d4e5f6",
        ) as attachment:
            assert attachment.http_request.url.path == "/support/attachments/att_a1b2c3d4e5f6a1b2c3d4e5f6"
            assert not attachment.is_closed
            assert attachment.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await attachment.json() == {"foo": "bar"}
            assert cast(Any, attachment.is_closed) is True
            assert isinstance(attachment, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, attachment.is_closed) is True

    @parametrize
    async def test_path_params_download(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.support.attachments.with_raw_response.download(
                id="",
            )
