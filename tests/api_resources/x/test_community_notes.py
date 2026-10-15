# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types.x import (
    CommunityNoteRetrieveContributorResponse,
    CommunityNoteListContributorNotesResponse,
    CommunityNoteListContributorDeletedNotesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCommunityNotes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_contributor_deleted_notes(self, client: XTwitterScraper) -> None:
        community_note = client.x.community_notes.list_contributor_deleted_notes(
            alias="alias",
        )
        assert_matches_type(CommunityNoteListContributorDeletedNotesResponse, community_note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_contributor_deleted_notes_with_all_params(self, client: XTwitterScraper) -> None:
        community_note = client.x.community_notes.list_contributor_deleted_notes(
            alias="alias",
            cursor="cursor",
            fields="id,text,author.username",
            omit="entities,media",
            page_size=1,
        )
        assert_matches_type(CommunityNoteListContributorDeletedNotesResponse, community_note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_contributor_deleted_notes(self, client: XTwitterScraper) -> None:
        response = client.x.community_notes.with_raw_response.list_contributor_deleted_notes(
            alias="alias",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community_note = response.parse()
        assert_matches_type(CommunityNoteListContributorDeletedNotesResponse, community_note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_contributor_deleted_notes(self, client: XTwitterScraper) -> None:
        with client.x.community_notes.with_streaming_response.list_contributor_deleted_notes(
            alias="alias",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community_note = response.parse()
            assert_matches_type(CommunityNoteListContributorDeletedNotesResponse, community_note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_contributor_deleted_notes(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `alias` but received ''"):
            client.x.community_notes.with_raw_response.list_contributor_deleted_notes(
                alias="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_contributor_notes(self, client: XTwitterScraper) -> None:
        community_note = client.x.community_notes.list_contributor_notes(
            alias="alias",
        )
        assert_matches_type(CommunityNoteListContributorNotesResponse, community_note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_contributor_notes_with_all_params(self, client: XTwitterScraper) -> None:
        community_note = client.x.community_notes.list_contributor_notes(
            alias="alias",
            cursor="cursor",
            fields="id,text,author.username",
            omit="entities,media",
            page_size=1,
        )
        assert_matches_type(CommunityNoteListContributorNotesResponse, community_note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_contributor_notes(self, client: XTwitterScraper) -> None:
        response = client.x.community_notes.with_raw_response.list_contributor_notes(
            alias="alias",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community_note = response.parse()
        assert_matches_type(CommunityNoteListContributorNotesResponse, community_note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_contributor_notes(self, client: XTwitterScraper) -> None:
        with client.x.community_notes.with_streaming_response.list_contributor_notes(
            alias="alias",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community_note = response.parse()
            assert_matches_type(CommunityNoteListContributorNotesResponse, community_note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_contributor_notes(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `alias` but received ''"):
            client.x.community_notes.with_raw_response.list_contributor_notes(
                alias="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_contributor(self, client: XTwitterScraper) -> None:
        community_note = client.x.community_notes.retrieve_contributor(
            alias="alias",
        )
        assert_matches_type(CommunityNoteRetrieveContributorResponse, community_note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_contributor_with_all_params(self, client: XTwitterScraper) -> None:
        community_note = client.x.community_notes.retrieve_contributor(
            alias="alias",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(CommunityNoteRetrieveContributorResponse, community_note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_contributor(self, client: XTwitterScraper) -> None:
        response = client.x.community_notes.with_raw_response.retrieve_contributor(
            alias="alias",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community_note = response.parse()
        assert_matches_type(CommunityNoteRetrieveContributorResponse, community_note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_contributor(self, client: XTwitterScraper) -> None:
        with client.x.community_notes.with_streaming_response.retrieve_contributor(
            alias="alias",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community_note = response.parse()
            assert_matches_type(CommunityNoteRetrieveContributorResponse, community_note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_contributor(self, client: XTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `alias` but received ''"):
            client.x.community_notes.with_raw_response.retrieve_contributor(
                alias="",
            )


class TestAsyncCommunityNotes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_contributor_deleted_notes(self, async_client: AsyncXTwitterScraper) -> None:
        community_note = await async_client.x.community_notes.list_contributor_deleted_notes(
            alias="alias",
        )
        assert_matches_type(CommunityNoteListContributorDeletedNotesResponse, community_note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_contributor_deleted_notes_with_all_params(
        self, async_client: AsyncXTwitterScraper
    ) -> None:
        community_note = await async_client.x.community_notes.list_contributor_deleted_notes(
            alias="alias",
            cursor="cursor",
            fields="id,text,author.username",
            omit="entities,media",
            page_size=1,
        )
        assert_matches_type(CommunityNoteListContributorDeletedNotesResponse, community_note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_contributor_deleted_notes(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.community_notes.with_raw_response.list_contributor_deleted_notes(
            alias="alias",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community_note = await response.parse()
        assert_matches_type(CommunityNoteListContributorDeletedNotesResponse, community_note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_contributor_deleted_notes(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.community_notes.with_streaming_response.list_contributor_deleted_notes(
            alias="alias",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community_note = await response.parse()
            assert_matches_type(CommunityNoteListContributorDeletedNotesResponse, community_note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_contributor_deleted_notes(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `alias` but received ''"):
            await async_client.x.community_notes.with_raw_response.list_contributor_deleted_notes(
                alias="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_contributor_notes(self, async_client: AsyncXTwitterScraper) -> None:
        community_note = await async_client.x.community_notes.list_contributor_notes(
            alias="alias",
        )
        assert_matches_type(CommunityNoteListContributorNotesResponse, community_note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_contributor_notes_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        community_note = await async_client.x.community_notes.list_contributor_notes(
            alias="alias",
            cursor="cursor",
            fields="id,text,author.username",
            omit="entities,media",
            page_size=1,
        )
        assert_matches_type(CommunityNoteListContributorNotesResponse, community_note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_contributor_notes(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.community_notes.with_raw_response.list_contributor_notes(
            alias="alias",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community_note = await response.parse()
        assert_matches_type(CommunityNoteListContributorNotesResponse, community_note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_contributor_notes(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.community_notes.with_streaming_response.list_contributor_notes(
            alias="alias",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community_note = await response.parse()
            assert_matches_type(CommunityNoteListContributorNotesResponse, community_note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_contributor_notes(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `alias` but received ''"):
            await async_client.x.community_notes.with_raw_response.list_contributor_notes(
                alias="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_contributor(self, async_client: AsyncXTwitterScraper) -> None:
        community_note = await async_client.x.community_notes.retrieve_contributor(
            alias="alias",
        )
        assert_matches_type(CommunityNoteRetrieveContributorResponse, community_note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_contributor_with_all_params(self, async_client: AsyncXTwitterScraper) -> None:
        community_note = await async_client.x.community_notes.retrieve_contributor(
            alias="alias",
            fields="id,text,author.username",
            omit="entities,media",
        )
        assert_matches_type(CommunityNoteRetrieveContributorResponse, community_note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_contributor(self, async_client: AsyncXTwitterScraper) -> None:
        response = await async_client.x.community_notes.with_raw_response.retrieve_contributor(
            alias="alias",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        community_note = await response.parse()
        assert_matches_type(CommunityNoteRetrieveContributorResponse, community_note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_contributor(self, async_client: AsyncXTwitterScraper) -> None:
        async with async_client.x.community_notes.with_streaming_response.retrieve_contributor(
            alias="alias",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            community_note = await response.parse()
            assert_matches_type(CommunityNoteRetrieveContributorResponse, community_note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_contributor(self, async_client: AsyncXTwitterScraper) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `alias` but received ''"):
            await async_client.x.community_notes.with_raw_response.retrieve_contributor(
                alias="",
            )
