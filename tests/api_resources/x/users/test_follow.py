# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types.x.users import (
    FollowCreateResponse,
    FollowDeleteAllResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFollow:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: XTwitterScraper) -> None:
        follow = client.x.users.follow.create(
            user_id="userId",
            account="account",
        )
        assert_matches_type(FollowCreateResponse, follow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: XTwitterScraper) -> None:
        response = client.x.users.follow.with_raw_response.create(
            user_id="userId",
            account="account",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        follow = response.parse()
        assert_matches_type(FollowCreateResponse, follow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: XTwitterScraper) -> None:
        with client.x.users.follow.with_streaming_response.create(
            user_id="userId",
            account="account",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            follow = response.parse()
            assert_matches_type(FollowCreateResponse, follow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.x.users.follow.with_raw_response.create(
                user_id="",
                account="account",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_all(self, client: XTwitterScraper) -> None:
        follow = client.x.users.follow.delete_all(
            user_id="userId",
            account="account",
        )
        assert_matches_type(FollowDeleteAllResponse, follow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_all(self, client: XTwitterScraper) -> None:
        response = client.x.users.follow.with_raw_response.delete_all(
            user_id="userId",
            account="account",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        follow = response.parse()
        assert_matches_type(FollowDeleteAllResponse, follow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_all(self, client: XTwitterScraper) -> None:
        with client.x.users.follow.with_streaming_response.delete_all(
            user_id="userId",
            account="account",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            follow = response.parse()
            assert_matches_type(FollowDeleteAllResponse, follow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_all(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.x.users.follow.with_raw_response.delete_all(
                user_id="",
                account="account",
            )


class TestAsyncFollow:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncXTwitterScraper) -> None:
        follow = await async_client.x.users.follow.create(
            user_id="userId",
            account="account",
        )
        assert_matches_type(FollowCreateResponse, follow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.follow.with_raw_response.create(
            user_id="userId",
            account="account",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        follow = await response.parse()
        assert_matches_type(FollowCreateResponse, follow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.follow.with_streaming_response.create(
            user_id="userId",
            account="account",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            follow = await response.parse()
            assert_matches_type(FollowCreateResponse, follow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.x.users.follow.with_raw_response.create(
                user_id="",
                account="account",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_all(self, async_client: AsyncXTwitterScraper) -> None:
        follow = await async_client.x.users.follow.delete_all(
            user_id="userId",
            account="account",
        )
        assert_matches_type(FollowDeleteAllResponse, follow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_all(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.users.follow.with_raw_response.delete_all(
            user_id="userId",
            account="account",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        follow = await response.parse()
        assert_matches_type(FollowDeleteAllResponse, follow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_all(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.users.follow.with_streaming_response.delete_all(
            user_id="userId",
            account="account",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            follow = await response.parse()
            assert_matches_type(FollowDeleteAllResponse, follow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_all(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.x.users.follow.with_raw_response.delete_all(
                user_id="",
                account="account",
            )
