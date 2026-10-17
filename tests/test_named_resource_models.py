# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import importlib

import pytest

from tests.utils import send_with_mock_transport
from x_twitter_scraper.types import Broadcast as ExportedBroadcast
from x_twitter_scraper.types.x import (
    Job,
    Space,
    SpaceParticipant,
    PaginatedCommunityNotes,
    CommunityNotesContributor,
    CommunityNotesRatingOutcome,
)
from x_twitter_scraper.types.x.job import Account, Company
from x_twitter_scraper.types.shared import Broadcast, Community
from x_twitter_scraper.types.x.space import Sharing
from x_twitter_scraper.types.shared.broadcast import PeriscopeUser
from x_twitter_scraper.types.x.space_participant import AffiliatesHighlightedLabel
from x_twitter_scraper.types.x.paginated_community_notes import Note, NoteEntity, NoteEntityRef, NotePostUnavailable
from x_twitter_scraper.types.x.community_notes_contributor import NotesCount, RatingsCount
from x_twitter_scraper.types.x.community_retrieve_info_response import CommunityRetrieveInfoResponse

JOB = {
    "job": {
        "id": "1899202395210649861",
        "title": "Engineer",
        "url": "https://x.com/i/jobs/1899202395210649861",
        "applyUrl": "https://xquik.com/example",
        "location": "United States",
        "locationType": "remote",
        "employmentType": "full_time",
        "seniorityLevel": "lead",
        "jobFunction": "software_engineering",
        "formattedSalary": "Starting at $225K",
        "salaryMin": 225000,
        "salaryCurrencyCode": "USD",
        "salaryInterval": "annually",
        "featured": True,
        "shortDescription": "Commonware is hiring founding engineers.",
        "description": "What is Commonware? We build open primitives.",
        "descriptionMarkdown": "# What is Commonware?",
        "account": {
            "id": "1812126202804711425",
            "username": "commonwarexyz",
            "name": "commonware",
            "verified": True,
            "verifiedType": "Business",
        },
    }
}

JOBS = {
    "jobs": [
        {
            "id": "1899202395210649861",
            "title": "Engineer",
            "url": "https://x.com/i/jobs/1899202395210649861",
            "applyUrl": "https://xquik.com/example",
            "location": "United States",
            "formattedSalary": "Starting at $225K",
            "salaryMin": 225000,
            "salaryCurrencyCode": "USD",
            "salaryInterval": "annually",
            "account": {
                "id": "1812126202804711425",
                "username": "commonwarexyz",
                "name": "commonware",
                "verified": True,
                "verifiedType": "Business",
            },
        }
    ],
    "has_next_page": True,
    "next_cursor": "DAACCgACGRElMJcAAA",
}


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_job_operations_return_the_same_model(asynchronous: bool) -> None:
    _, retrieved = await send_with_mock_transport(
        lambda client: client.x.jobs.retrieve("1899202395210649861"),
        lambda client: client.x.jobs.retrieve("1899202395210649861"),
        JOB,
        asynchronous,
    )
    _, searched = await send_with_mock_transport(
        lambda client: client.x.jobs.search(q="engineer"),
        lambda client: client.x.jobs.search(q="engineer"),
        JOBS,
        asynchronous,
    )

    jobs: list[Job] = [retrieved.job, searched.jobs[0]]
    assert type(jobs[0]) is type(jobs[1]) is Job
    assert jobs[0].id == jobs[1].id == "1899202395210649861"
    assert type(jobs[0].account) is type(jobs[1].account) is Account
    assert jobs[0].description == "What is Commonware? We build open primitives."
    assert jobs[1].description is None
    assert jobs[0].salary_min == jobs[1].salary_min == 225000


@pytest.mark.parametrize("module", ["job_retrieve_response", "job_search_response"])
def test_job_nested_names_remain_aliases(module: str) -> None:
    response = importlib.import_module("x_twitter_scraper.types.x." + module)
    assert response.Job is Job
    assert response.JobAccount is Account
    assert response.JobCompany is Company


@pytest.mark.parametrize("module", ["space_retrieve_response", "space_search_response"])
def test_space_nested_names_remain_aliases(module: str) -> None:
    response = importlib.import_module("x_twitter_scraper.types.x." + module)
    assert response.Space is Space
    assert response.SpaceSharing is Sharing
    for role in ["Admin", "Listener", "Speaker"]:
        assert getattr(response, "Space" + role) is SpaceParticipant
        assert getattr(response, "Space" + role + "AffiliatesHighlightedLabel") is AffiliatesHighlightedLabel


@pytest.mark.parametrize("module", ["broadcast_retrieve_response", "user_retrieve_live_response"])
def test_broadcast_nested_names_remain_aliases(module: str) -> None:
    response = importlib.import_module("x_twitter_scraper.types.x." + module)
    assert response.Broadcast is Broadcast is ExportedBroadcast
    assert response.BroadcastPeriscopeUser is PeriscopeUser


@pytest.mark.parametrize(
    ("module", "prefix"),
    [
        ("community_note_retrieve_contributor_response", "Contributor"),
        ("community_note_list_contributor_notes_response", "NoteContributor"),
        ("community_note_list_contributor_deleted_notes_response", "NoteContributor"),
    ],
)
def test_contributor_nested_names_remain_aliases(module: str, prefix: str) -> None:
    response = importlib.import_module("x_twitter_scraper.types.x." + module)
    assert getattr(response, prefix) is CommunityNotesContributor
    assert getattr(response, prefix + "NotesCount") is NotesCount
    assert getattr(response, prefix + "RatingsCount") is RatingsCount
    assert getattr(response, prefix + "RatingsCountSuccessful") is CommunityNotesRatingOutcome
    assert getattr(response, prefix + "RatingsCountUnsuccessful") is CommunityNotesRatingOutcome


@pytest.mark.parametrize(
    ("module", "name"),
    [
        ("community_note_list_contributor_notes_response", "CommunityNoteListContributorNotesResponse"),
        ("community_note_list_contributor_deleted_notes_response", "CommunityNoteListContributorDeletedNotesResponse"),
    ],
)
def test_notes_page_names_remain_aliases(module: str, name: str) -> None:
    response = importlib.import_module("x_twitter_scraper.types.x." + module)
    assert getattr(response, name) is PaginatedCommunityNotes
    assert response.Note is Note
    assert response.NoteEntity is NoteEntity
    assert response.NoteEntityRef is NoteEntityRef
    assert response.NotePostUnavailable is NotePostUnavailable


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_broadcast_operations_return_the_same_model(asynchronous: bool) -> None:
    _, retrieved = await send_with_mock_transport(
        lambda client: client.x.broadcasts.retrieve("1DxLdZyVPMMxm"),
        lambda client: client.x.broadcasts.retrieve("1DxLdZyVPMMxm"),
        {
            "broadcast": {
                "id": "1DxLdZyVPMMxm",
                "title": "NASA's SpaceX Crew-12 Re-Entry & Splashdown",
                "state": "Ended",
            }
        },
        asynchronous,
    )
    _, live = await send_with_mock_transport(
        lambda client: client.x.users.retrieve_live("NASA"),
        lambda client: client.x.users.retrieve_live("NASA"),
        {
            "live": False,
            "userId": "11348282",
            "userName": "NASA",
            "broadcast": {
                "id": "1DxLdZyVPMMxm",
                "title": "NASA's SpaceX Crew-12 Re-Entry & Splashdown",
                "state": "Ended",
            },
        },
        asynchronous,
    )

    assert type(retrieved.broadcast) is type(live.broadcast) is Broadcast


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_community_info_returns_the_shared_community(asynchronous: bool) -> None:
    _, response = await send_with_mock_transport(
        lambda client: client.x.communities.retrieve_info("1500000000000000000"),
        lambda client: client.x.communities.retrieve_info("1500000000000000000"),
        {
            "community": {
                "id": "1500000000000000000",
                "name": "Tesla Fans",
                "description": "A community for Tesla enthusiasts",
                "banner_url": "https://xquik.com/example",
                "created_at": "2025-01-15T12:00:00Z",
                "join_policy": "open",
                "member_count": 10000,
                "moderator_count": 5,
                "is_nsfw": False,
            }
        },
        asynchronous,
    )

    assert type(response) is CommunityRetrieveInfoResponse
    assert type(response.community) is Community
