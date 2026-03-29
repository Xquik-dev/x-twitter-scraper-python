# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types.x import (
    ProfilePatchAllResponse,
    ProfileUpdateAvatarResponse,
    ProfileUpdateBannerResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProfile:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_patch_all(self, client: XTwitterScraper) -> None:
        profile = client.x.profile.patch_all(
            account="account",
        )
        assert_matches_type(ProfilePatchAllResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_patch_all_with_all_params(self, client: XTwitterScraper) -> None:
        profile = client.x.profile.patch_all(
            account="account",
            description="description",
            location="location",
            name="name",
            url="url",
        )
        assert_matches_type(ProfilePatchAllResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_patch_all(self, client: XTwitterScraper) -> None:
        response = client.x.profile.with_raw_response.patch_all(
            account="account",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfilePatchAllResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_patch_all(self, client: XTwitterScraper) -> None:
        with client.x.profile.with_streaming_response.patch_all(
            account="account",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfilePatchAllResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_avatar(self, client: XTwitterScraper) -> None:
        profile = client.x.profile.update_avatar(
            account="account",
            file=b"Example data",
        )
        assert_matches_type(ProfileUpdateAvatarResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_avatar(self, client: XTwitterScraper) -> None:
        response = client.x.profile.with_raw_response.update_avatar(
            account="account",
            file=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileUpdateAvatarResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_avatar(self, client: XTwitterScraper) -> None:
        with client.x.profile.with_streaming_response.update_avatar(
            account="account",
            file=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileUpdateAvatarResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_banner(self, client: XTwitterScraper) -> None:
        profile = client.x.profile.update_banner(
            account="account",
            file=b"Example data",
        )
        assert_matches_type(ProfileUpdateBannerResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_banner(self, client: XTwitterScraper) -> None:
        response = client.x.profile.with_raw_response.update_banner(
            account="account",
            file=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileUpdateBannerResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_banner(self, client: XTwitterScraper) -> None:
        with client.x.profile.with_streaming_response.update_banner(
            account="account",
            file=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileUpdateBannerResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProfile:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_patch_all(self, async_client: AsyncXTwitterScraper) -> None:
        profile = await async_client.x.profile.patch_all(
            account="account",
        )
        assert_matches_type(ProfilePatchAllResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_patch_all_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        profile = await async_client.x.profile.patch_all(
            account="account",
            description="description",
            location="location",
            name="name",
            url="url",
        )
        assert_matches_type(ProfilePatchAllResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_patch_all(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.profile.with_raw_response.patch_all(
            account="account",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfilePatchAllResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_patch_all(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.profile.with_streaming_response.patch_all(
            account="account",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfilePatchAllResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_avatar(self, async_client: AsyncXTwitterScraper) -> None:
        profile = await async_client.x.profile.update_avatar(
            account="account",
            file=b"Example data",
        )
        assert_matches_type(ProfileUpdateAvatarResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_avatar(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.profile.with_raw_response.update_avatar(
            account="account",
            file=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileUpdateAvatarResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_avatar(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.profile.with_streaming_response.update_avatar(
            account="account",
            file=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileUpdateAvatarResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_banner(self, async_client: AsyncXTwitterScraper) -> None:
        profile = await async_client.x.profile.update_banner(
            account="account",
            file=b"Example data",
        )
        assert_matches_type(ProfileUpdateBannerResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_banner(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.profile.with_raw_response.update_banner(
            account="account",
            file=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileUpdateBannerResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_banner(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.profile.with_streaming_response.update_banner(
            account="account",
            file=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileUpdateBannerResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True
