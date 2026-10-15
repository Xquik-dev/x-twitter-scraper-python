# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Any, Dict, Tuple
from datetime import datetime, timezone
from functools import reduce

import httpx
import pytest

from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper.types import XGetTrendsHistoryResponse, XGetNewsStoryVersionsResponse
from x_twitter_scraper.types.x import (
    CommunityNoteRetrieveContributorResponse,
    CommunityNoteListContributorNotesResponse,
    CommunityNoteListContributorDeletedNotesResponse,
)
from x_twitter_scraper.types.shared import SearchTweet

TRENDS_HISTORY = {
    "fromTime": "2026-10-13T00:00:00.000Z",
    "toTime": "2026-10-14T00:00:00.000Z",
    "snapshots": [
        {
            "capturedAt": "2026-10-13T14:00:26.000Z",
            "count": 1,
            "trends": [
                {
                    "name": "#AI",
                    "description": "Artificial intelligence discussions",
                    "promotedContent": None,
                    "query": "%23AI",
                    "rank": 1,
                    "tweetVolume": 250000,
                    "url": "https://x.com/search?q=%23AI",
                }
            ],
        }
    ],
    "count": 1,
    "woeid": 1,
    "location": {
        "woeid": 23424969,
        "name": "Turkey",
        "country": "Turkey",
        "countryCode": "TR",
        "placeType": "Country",
        "placeTypeCode": 12,
        "parentWoeid": 1,
        "url": "http://where.yahooapis.com/v1/place/23424969",
    },
    "has_next_page": False,
    "next_cursor": "",
}

STORY_HEADLINE = "Elon Musk Pushes Starlink for India's Remote Areas Amid Regulatory Hurdles"
STORY_TEXT = (
    "Musk has accused Reliance Industries' Mukesh Ambani of blocking Starlink's entry to protect local "
    "telecom giants like Jio, while India's government insists on equal treatment for all applicants, "
    "including ongoing security reviews. In Vietnam, Starlink already provides free internet to isolated "
    "spots for tourism and disaster response, highlighting its potential for hard-to-reach areas. Yet "
    "challengers note India's cheap mobile data from Jio and Airtel covers most needs, raising questions "
    "on pricing and national security as Starlink seeks final clearances."
)

NEWS_STORY_VERSIONS = {
    "id": "2110209733533598095",
    "count": 1,
    "versions": [
        {
            "id": "2110211669641105725",
            "createdAt": "2026-10-14T03:30:42.536Z",
            "headline": STORY_HEADLINE,
            "text": STORY_TEXT,
        }
    ],
}

CONTRIBUTOR = {
    "contributor": {
        "alias": "ardent-beach-friarbird",
        "deletedNotesCount": 0,
        "isApiContributor": False,
        "isTopWriter": False,
        "notesCount": {
            "awaitingMoreRatings": 18,
            "currentlyRatedHelpful": 1,
            "currentlyRatedNotHelpful": 2,
            "updatedAt": "2026-10-12T22:18:40.096Z",
        },
        "ratingsCount": {
            "awaitingMoreRatings": 703,
            "ratedAfterDecision": 154,
            "successful": {"helpfulCount": 27, "notHelpfulCount": 22, "total": 49},
            "unsuccessful": {"helpfulCount": 15, "notHelpfulCount": 4},
            "updatedAt": "2026-10-12T22:50:13.228Z",
        },
    }
}

NOTE_TEXT = (
    "Since this is a wall of text article and the headline doesn't say, this quick-to-read context is "
    "necessary:\n\nDiscord is STILL rolling out Age Verification methods, just delayed to the second half "
    "of 2026 per the very own article in this post.\n\n"
    "https://discord.com/blog/getting-global-age-assurance-right-what-we-got-wrong-and-whats-changing"
)
POST_TEXT = (
    "Getting Global Age Assurance Right: What We Got Wrong and What’s Changing. \n\n"
    "Read the update: https://t.co/h7aRGmN7xW"
)

CONTRIBUTOR_NOTES = {
    "notes": [
        {
            "id": "2026375778254868976",
            "createdAt": "2026-02-24T19:16:48.435Z",
            "language": "en",
            "classification": "MisinformedOrPotentiallyMisleading",
            "contributor": {
                "alias": "ardent-beach-friarbird",
                "notesCount": {"currentlyRatedHelpful": 1, "currentlyRatedNotHelpful": 2},
                "ratingsCount": {
                    "successful": {"total": 49},
                    "unsuccessful": {"helpfulCount": 15, "notHelpfulCount": 4},
                },
            },
            "text": NOTE_TEXT,
            "entities": [
                {
                    "fromIndex": 244,
                    "toIndex": 340,
                    "ref": {"type": "TimelineUrl", "url": "https://t.co/7fJbcLrO1k"},
                }
            ],
            "ratingStatus": "CurrentlyRatedHelpful",
            "helpfulTags": ["ImportantContext", "Clear"],
            "decidedBy": "CoreModel (v1.1)",
            "fullyVisibleModel": True,
            "abovePcrhThreshold": False,
            "appealStatus": "NotAppealed",
            "deleted": False,
            "isApiAuthor": False,
            "isMediaNote": False,
            "mediaNoteMatchCount": 0,
            "isUrlNote": False,
            "isTranslatable": False,
            "timeToHelpfulFromNoteMs": 132890587,
            "timeToHelpfulFromPostMs": 136815576,
            "postId": "2026359315657805939",
            "post": {
                "id": "2026359315657805939",
                "text": POST_TEXT,
                "createdAt": "Tue Feb 24 18:11:23 +0000 2026",
                "retweetCount": 542,
                "replyCount": 4197,
                "likeCount": 3990,
                "quoteCount": 1122,
                "viewCount": 7038435,
                "bookmarkCount": 1472,
                "lang": "en",
                "url": "https://x.com/discord/status/2026359315657805939",
                "author": {
                    "id": "3065618342",
                    "username": "discord",
                    "name": "Discord",
                    "verifiedType": "Business",
                },
            },
        }
    ],
    "has_next_page": True,
    "next_cursor": "-1767098234260",
}

CONTRIBUTOR_DELETED_NOTES = {
    "notes": [
        {
            "id": "2078950499982696756",
            "createdAt": "2026-07-19T21:09:58.885Z",
            "ratingStatus": "CurrentlyRatedNotHelpful",
            "notHelpfulTags": ["MissingKeyPoints", "Incorrect"],
            "decidedBy": "CoreModel (v1.1)",
            "fullyVisibleModel": True,
            "abovePcrhThreshold": False,
            "appealStatus": "NotAppealed",
            "deleted": True,
            "tombstone": "This note has been deleted",
            "isApiAuthor": False,
            "isMediaNote": False,
            "mediaNoteMatchCount": 0,
            "isUrlNote": False,
        }
    ],
    "has_next_page": False,
    "next_cursor": "",
}


async def send(
    method_path: Tuple[str, ...], arguments: Dict[str, object], payload: object, asynchronous: bool
) -> Tuple[httpx.Request, Any]:
    requests: list[httpx.Request] = []

    def respond(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json=payload)

    transport = httpx.MockTransport(respond)
    if asynchronous:
        async with AsyncXTwitterScraper(
            api_key="isolated-test",
            http_client=httpx.AsyncClient(transport=transport),
            _strict_response_validation=True,
        ) as client:
            call: Any = reduce(getattr, method_path, client)
            result = await call(**arguments)
    else:
        with XTwitterScraper(
            api_key="isolated-test",
            http_client=httpx.Client(transport=transport),
            _strict_response_validation=True,
        ) as sync_client:
            sync_call: Any = reduce(getattr, method_path, sync_client)
            result = sync_call(**arguments)
    assert len(requests) == 1
    assert requests[0].method == "GET"
    return requests[0], result


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_trends_history_sends_every_filter_and_reads_the_snapshots(asynchronous: bool) -> None:
    request, history = await send(
        ("x", "get_trends_history"),
        {
            "woeid": 23424969,
            "country": "Turkey",
            "location": "Istanbul",
            "from_": "7d",
            "to": "2026-10-14",
            "every": "15m",
            "count": 5,
            "limit": 100,
            "cursor": "2026-10-14T00:00:00.000Z~1791979200000",
            "fields": "snapshots,count",
            "omit": "location",
        },
        TRENDS_HISTORY,
        asynchronous,
    )

    assert request.url.path == "/api/v1/x/trends/history"
    assert dict(request.url.params) == {
        "woeid": "23424969",
        "country": "Turkey",
        "location": "Istanbul",
        "from": "7d",
        "to": "2026-10-14",
        "every": "15m",
        "count": "5",
        "limit": "100",
        "cursor": "2026-10-14T00:00:00.000Z~1791979200000",
        "fields": "snapshots,count",
        "omit": "location",
    }
    assert isinstance(history, XGetTrendsHistoryResponse)
    assert history.from_time == datetime(2026, 10, 13, tzinfo=timezone.utc)
    assert history.to_time == datetime(2026, 10, 14, tzinfo=timezone.utc)
    assert history.count == 1
    assert history.woeid == 1
    assert history.has_next_page is False
    assert history.next_cursor == ""
    snapshot = history.snapshots[0]
    assert snapshot.captured_at == datetime(2026, 10, 13, 14, 0, 26, tzinfo=timezone.utc)
    assert snapshot.count == 1
    trend = snapshot.trends[0]
    assert trend.name == "#AI"
    assert trend.description == "Artificial intelligence discussions"
    assert trend.promoted_content is None
    assert trend.query == "%23AI"
    assert trend.rank == 1
    assert trend.tweet_volume == 250000
    assert trend.url == "https://x.com/search?q=%23AI"
    assert history.location is not None
    assert history.location.woeid == 23424969
    assert history.location.name == "Turkey"
    assert history.location.country == "Turkey"
    assert history.location.country_code == "TR"
    assert history.location.place_type == "Country"
    assert history.location.place_type_code == 12
    assert history.location.parent_woeid == 1
    assert history.location.url == "http://where.yahooapis.com/v1/place/23424969"


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_trends_history_without_filters_sends_no_query(asynchronous: bool) -> None:
    request, history = await send(("x", "get_trends_history"), {}, TRENDS_HISTORY, asynchronous)

    assert request.url.path == "/api/v1/x/trends/history"
    assert request.url.query == b""
    assert history.snapshots[0].trends[0].name == "#AI"


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize(
    ("story", "raw_path"),
    [
        ("2110209733533598095", b"/api/v1/x/news/2110209733533598095/versions"),
        (
            "x.com/i/trending/2110209733533598095",
            b"/api/v1/x/news/x.com%2Fi%2Ftrending%2F2110209733533598095/versions",
        ),
    ],
)
async def test_news_story_versions_reads_each_version(story: str, raw_path: bytes, asynchronous: bool) -> None:
    request, story_versions = await send(
        ("x", "get_news_story_versions"),
        {"id": story, "fields": "versions.headline", "omit": "versions.text"},
        NEWS_STORY_VERSIONS,
        asynchronous,
    )

    assert request.url.raw_path == raw_path + b"?fields=versions.headline&omit=versions.text"
    assert isinstance(story_versions, XGetNewsStoryVersionsResponse)
    assert story_versions.id == "2110209733533598095"
    assert story_versions.count == 1
    version = story_versions.versions[0]
    assert version.id == "2110211669641105725"
    assert version.created_at == datetime(2026, 10, 14, 3, 30, 42, 536000, tzinfo=timezone.utc)
    assert version.headline == STORY_HEADLINE
    assert version.text == STORY_TEXT


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize(
    ("alias", "raw_path"),
    [
        ("ardent-beach-friarbird", b"/api/v1/x/community-notes/contributors/ardent-beach-friarbird"),
        (
            "x.com/i/communitynotes/u/ardent-beach-friarbird",
            b"/api/v1/x/community-notes/contributors/x.com%2Fi%2Fcommunitynotes%2Fu%2Fardent-beach-friarbird",
        ),
    ],
)
async def test_contributor_reads_note_and_rating_counts(alias: str, raw_path: bytes, asynchronous: bool) -> None:
    request, response = await send(
        ("x", "community_notes", "retrieve_contributor"),
        {"alias": alias, "fields": "alias,notesCount", "omit": "ratingsCount"},
        CONTRIBUTOR,
        asynchronous,
    )

    assert request.url.raw_path == raw_path + b"?fields=alias%2CnotesCount&omit=ratingsCount"
    assert isinstance(response, CommunityNoteRetrieveContributorResponse)
    contributor = response.contributor
    assert contributor.alias == "ardent-beach-friarbird"
    assert contributor.deleted_notes_count == 0
    assert contributor.is_api_contributor is False
    assert contributor.is_top_writer is False
    assert contributor.notes_count is not None
    assert contributor.notes_count.awaiting_more_ratings == 18
    assert contributor.notes_count.currently_rated_helpful == 1
    assert contributor.notes_count.currently_rated_not_helpful == 2
    assert contributor.notes_count.updated_at == datetime(2026, 10, 12, 22, 18, 40, 96000, tzinfo=timezone.utc)
    ratings = contributor.ratings_count
    assert ratings is not None
    assert ratings.awaiting_more_ratings == 703
    assert ratings.rated_after_decision == 154
    assert ratings.successful is not None
    assert (ratings.successful.helpful_count, ratings.successful.not_helpful_count, ratings.successful.total) == (
        27,
        22,
        49,
    )
    assert ratings.unsuccessful is not None
    assert (
        ratings.unsuccessful.helpful_count,
        ratings.unsuccessful.not_helpful_count,
        ratings.unsuccessful.total,
    ) == (15, 4, None)
    assert ratings.updated_at == datetime(2026, 10, 12, 22, 50, 13, 228000, tzinfo=timezone.utc)


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_contributor_notes_read_each_note_with_its_post(asynchronous: bool) -> None:
    request, page = await send(
        ("x", "community_notes", "list_contributor_notes"),
        {
            "alias": "ardent-beach-friarbird",
            "cursor": "-1767098234260",
            "page_size": 10,
            "fields": "notes.text",
            "omit": "notes.post",
        },
        CONTRIBUTOR_NOTES,
        asynchronous,
    )

    assert request.url.path == "/api/v1/x/community-notes/contributors/ardent-beach-friarbird/notes"
    assert dict(request.url.params) == {
        "cursor": "-1767098234260",
        "pageSize": "10",
        "fields": "notes.text",
        "omit": "notes.post",
    }
    assert isinstance(page, CommunityNoteListContributorNotesResponse)
    assert page.has_next_page is True
    assert page.next_cursor == "-1767098234260"
    note = page.notes[0]
    assert note.id == "2026375778254868976"
    assert note.created_at == datetime(2026, 2, 24, 19, 16, 48, 435000, tzinfo=timezone.utc)
    assert note.language == "en"
    assert note.classification == "MisinformedOrPotentiallyMisleading"
    assert note.text == NOTE_TEXT
    assert note.contributor is not None
    assert note.contributor.alias == "ardent-beach-friarbird"
    assert note.contributor.deleted_notes_count is None
    assert note.contributor.notes_count is not None
    assert note.contributor.notes_count.currently_rated_helpful == 1
    assert note.contributor.notes_count.currently_rated_not_helpful == 2
    assert note.contributor.notes_count.awaiting_more_ratings is None
    assert note.contributor.ratings_count is not None
    assert note.contributor.ratings_count.successful is not None
    assert note.contributor.ratings_count.successful.total == 49
    assert note.contributor.ratings_count.unsuccessful is not None
    assert note.contributor.ratings_count.unsuccessful.helpful_count == 15
    assert note.contributor.ratings_count.unsuccessful.not_helpful_count == 4
    assert note.entities is not None
    entity = note.entities[0]
    assert (entity.from_index, entity.to_index) == (244, 340)
    assert entity.ref is not None
    assert (entity.ref.type, entity.ref.url) == ("TimelineUrl", "https://t.co/7fJbcLrO1k")
    assert note.rating_status == "CurrentlyRatedHelpful"
    assert note.helpful_tags == ["ImportantContext", "Clear"]
    assert note.not_helpful_tags is None
    assert note.decided_by == "CoreModel (v1.1)"
    assert note.fully_visible_model is True
    assert note.above_pcrh_threshold is False
    assert note.appeal_status == "NotAppealed"
    assert note.deleted is False
    assert note.is_api_author is False
    assert note.is_media_note is False
    assert note.media_note_match_count == 0
    assert note.is_url_note is False
    assert note.is_translatable is False
    assert note.time_to_helpful_from_note_ms == 132890587
    assert note.time_to_helpful_from_post_ms == 136815576
    assert note.post_id == "2026359315657805939"
    assert isinstance(note.post, SearchTweet)
    assert note.post.id == "2026359315657805939"
    assert note.post.text == POST_TEXT
    assert note.post.created_at == "Tue Feb 24 18:11:23 +0000 2026"
    assert (note.post.retweet_count, note.post.reply_count, note.post.like_count) == (542, 4197, 3990)
    assert (note.post.quote_count, note.post.view_count, note.post.bookmark_count) == (1122, 7038435, 1472)
    assert note.post.author is not None
    assert note.post.author.username == "discord"
    assert note.post_unavailable is None


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_contributor_deleted_notes_read_the_tombstones(asynchronous: bool) -> None:
    request, page = await send(
        ("x", "community_notes", "list_contributor_deleted_notes"),
        {"alias": "ardent-beach-friarbird", "page_size": 5},
        CONTRIBUTOR_DELETED_NOTES,
        asynchronous,
    )

    assert request.url.path == "/api/v1/x/community-notes/contributors/ardent-beach-friarbird/deleted-notes"
    assert dict(request.url.params) == {"pageSize": "5"}
    assert isinstance(page, CommunityNoteListContributorDeletedNotesResponse)
    assert page.has_next_page is False
    assert page.next_cursor == ""
    note = page.notes[0]
    assert note.id == "2078950499982696756"
    assert note.created_at == datetime(2026, 7, 19, 21, 9, 58, 885000, tzinfo=timezone.utc)
    assert note.rating_status == "CurrentlyRatedNotHelpful"
    assert note.not_helpful_tags == ["MissingKeyPoints", "Incorrect"]
    assert note.decided_by == "CoreModel (v1.1)"
    assert note.fully_visible_model is True
    assert note.above_pcrh_threshold is False
    assert note.appeal_status == "NotAppealed"
    assert note.deleted is True
    assert note.tombstone == "This note has been deleted"
    assert note.is_api_author is False
    assert note.is_media_note is False
    assert note.media_note_match_count == 0
    assert note.is_url_note is False
    assert note.text is None
    assert note.post is None
