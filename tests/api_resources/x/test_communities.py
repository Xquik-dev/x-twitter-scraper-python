# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types.x import (
    CommunityCreateResponse,
    CommunityDeleteResponse,
    CommunityRetrieveInfoResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCommunities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: XTwitterScraper) -> None:
        community = client.x.communities.create(
            account="account",
            name="name",
        )
        assert_matches_type(CommunityCreateResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: XTwitterScraper) -> None:
        community = client.x.communities.create(
            account="account",
            name="name",
            description="description",
        )
        assert_matches_type(CommunityCreateResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: XTwitterScraper) -> None:
        response = client.x.communities.with_raw_response.create(
            account="account",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert_matches_type(CommunityCreateResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: XTwitterScraper) -> None:
        with client.x.communities.with_streaming_response.create(
            account="account",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert_matches_type(CommunityCreateResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: XTwitterScraper) -> None:
        community = client.x.communities.delete(
            id="id",
            account="account",
            community_name="community_name",
        )
        assert_matches_type(CommunityDeleteResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: XTwitterScraper) -> None:
        response = client.x.communities.with_raw_response.delete(
            id="id",
            account="account",
            community_name="community_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert_matches_type(CommunityDeleteResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: XTwitterScraper) -> None:
        with client.x.communities.with_streaming_response.delete(
            id="id",
            account="account",
            community_name="community_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert_matches_type(CommunityDeleteResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.communities.with_raw_response.delete(
                id="",
                account="account",
                community_name="community_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_info(self, client: XTwitterScraper) -> None:
        community = client.x.communities.retrieve_info(
            "id",
        )
        assert_matches_type(CommunityRetrieveInfoResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_info(self, client: XTwitterScraper) -> None:
        response = client.x.communities.with_raw_response.retrieve_info(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert_matches_type(CommunityRetrieveInfoResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_info(self, client: XTwitterScraper) -> None:
        with client.x.communities.with_streaming_response.retrieve_info(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert_matches_type(CommunityRetrieveInfoResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_info(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.communities.with_raw_response.retrieve_info(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_members(self, client: XTwitterScraper) -> None:
        community = client.x.communities.retrieve_members(
            id="id",
        )
        assert community is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_members_with_all_params(self, client: XTwitterScraper) -> None:
        community = client.x.communities.retrieve_members(
            id="id",
            cursor="cursor",
        )
        assert community is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_members(self, client: XTwitterScraper) -> None:
        response = client.x.communities.with_raw_response.retrieve_members(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert community is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_members(self, client: XTwitterScraper) -> None:
        with client.x.communities.with_streaming_response.retrieve_members(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert community is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_members(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.communities.with_raw_response.retrieve_members(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_moderators(self, client: XTwitterScraper) -> None:
        community = client.x.communities.retrieve_moderators(
            id="id",
        )
        assert community is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_moderators_with_all_params(self, client: XTwitterScraper) -> None:
        community = client.x.communities.retrieve_moderators(
            id="id",
            cursor="cursor",
        )
        assert community is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_moderators(self, client: XTwitterScraper) -> None:
        response = client.x.communities.with_raw_response.retrieve_moderators(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert community is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_moderators(self, client: XTwitterScraper) -> None:
        with client.x.communities.with_streaming_response.retrieve_moderators(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert community is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_moderators(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.x.communities.with_raw_response.retrieve_moderators(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_search(self, client: XTwitterScraper) -> None:
        community = client.x.communities.retrieve_search(
            q="q",
        )
        assert community is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_search_with_all_params(self, client: XTwitterScraper) -> None:
        community = client.x.communities.retrieve_search(
            q="q",
            cursor="cursor",
            query_type="queryType",
        )
        assert community is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_search(self, client: XTwitterScraper) -> None:
        response = client.x.communities.with_raw_response.retrieve_search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = response.parse()
        assert community is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_search(self, client: XTwitterScraper) -> None:
        with client.x.communities.with_streaming_response.retrieve_search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = response.parse()
            assert community is None

        assert cast(Any, response.is_closed) is True


class TestAsyncCommunities:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.create(
            account="account",
            name="name",
        )
        assert_matches_type(CommunityCreateResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.create(
            account="account",
            name="name",
            description="description",
        )
        assert_matches_type(CommunityCreateResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.communities.with_raw_response.create(
            account="account",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert_matches_type(CommunityCreateResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.communities.with_streaming_response.create(
            account="account",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert_matches_type(CommunityCreateResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.delete(
            id="id",
            account="account",
            community_name="community_name",
        )
        assert_matches_type(CommunityDeleteResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.communities.with_raw_response.delete(
            id="id",
            account="account",
            community_name="community_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert_matches_type(CommunityDeleteResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.communities.with_streaming_response.delete(
            id="id",
            account="account",
            community_name="community_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert_matches_type(CommunityDeleteResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.communities.with_raw_response.delete(
                id="",
                account="account",
                community_name="community_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_info(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.retrieve_info(
            "id",
        )
        assert_matches_type(CommunityRetrieveInfoResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_info(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.communities.with_raw_response.retrieve_info(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert_matches_type(CommunityRetrieveInfoResponse, community, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_info(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.communities.with_streaming_response.retrieve_info(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert_matches_type(CommunityRetrieveInfoResponse, community, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_info(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.communities.with_raw_response.retrieve_info(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_members(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.retrieve_members(
            id="id",
        )
        assert community is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_members_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.retrieve_members(
            id="id",
            cursor="cursor",
        )
        assert community is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_members(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.communities.with_raw_response.retrieve_members(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert community is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_members(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.communities.with_streaming_response.retrieve_members(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert community is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_members(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.communities.with_raw_response.retrieve_members(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_moderators(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.retrieve_moderators(
            id="id",
        )
        assert community is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_moderators_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.retrieve_moderators(
            id="id",
            cursor="cursor",
        )
        assert community is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_moderators(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.communities.with_raw_response.retrieve_moderators(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert community is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_moderators(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.communities.with_streaming_response.retrieve_moderators(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert community is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_moderators(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.x.communities.with_raw_response.retrieve_moderators(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_search(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.retrieve_search(
            q="q",
        )
        assert community is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_search_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        community = await async_client.x.communities.retrieve_search(
            q="q",
            cursor="cursor",
            query_type="queryType",
        )
        assert community is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_search(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.communities.with_raw_response.retrieve_search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community = await response.parse()
        assert community is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_search(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.communities.with_streaming_response.retrieve_search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community = await response.parse()
            assert community is None

        assert cast(Any, response.is_closed) is True
