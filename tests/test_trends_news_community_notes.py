# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Tuple, Union
from datetime import datetime, timezone
from typing_extensions import Unpack

import httpx
import pytest

from tests.utils import send_with_mock_transport
from x_twitter_scraper.types import (
    XGetTrendsHistoryParams,
    XGetTrendsHistoryResponse,
    XGetNewsStoryVersionsParams,
    XGetNewsStoryVersionsResponse,
)
from x_twitter_scraper.types.x import (
    CommunityNoteRetrieveContributorParams,
    CommunityNoteListContributorNotesParams,
    CommunityNoteRetrieveContributorResponse,
    CommunityNoteListContributorNotesResponse,
    CommunityNoteListContributorDeletedNotesResponse,
)
from x_twitter_scraper.types.shared import SearchTweet

NotesPage = Union[CommunityNoteListContributorNotesResponse, CommunityNoteListContributorDeletedNotesResponse]

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

FULL_NOTE = {
    "id": "2026375778254868977",
    "createdAt": "2026-02-25T08:00:00.000Z",
    "language": "es",
    "classification": "NotMisleading",
    "text": "La foto es de 2019. #AI",
    "contributor": {
        "alias": "ardent-beach-friarbird",
        "deletedNotesCount": 3,
        "isApiContributor": True,
        "isTopWriter": True,
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
            "unsuccessful": {"helpfulCount": 15, "notHelpfulCount": 4, "total": 19},
            "updatedAt": "2026-10-12T22:50:13.228Z",
        },
    },
    "entities": [
        {
            "fromIndex": 20,
            "toIndex": 23,
            "ref": {
                "type": "Hashtag",
                "text": "AI",
                "screenName": "discord",
                "url": "https://x.com/hashtag/AI",
                "urlType": "ExternalUrl",
            },
        }
    ],
    "ratingStatus": "NeedsMoreRatings",
    "helpfulTags": ["GoodSources"],
    "notHelpfulTags": ["Outdated"],
    "decidedBy": "CoreModel (v1.1)",
    "fullyVisibleModel": False,
    "abovePcrhThreshold": True,
    "appealStatus": "Appealed",
    "deleted": False,
    "isApiAuthor": True,
    "isMediaNote": True,
    "mediaNoteMatchCount": 12,
    "isUrlNote": True,
    "displayUrl": "discord.com/blog",
    "isTranslatable": True,
    "timeToHelpfulFromNoteMs": 1000,
    "timeToHelpfulFromPostMs": 2000,
    "impressionCount": 45000,
    "postId": "2026359315657805940",
    "post": None,
    "postUnavailable": {"reason": "Suspended"},
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


async def list_notes(
    method: str,
    alias: str,
    payload: object,
    asynchronous: bool,
    **arguments: Unpack[CommunityNoteListContributorNotesParams],
) -> Tuple[httpx.Request, NotesPage]:
    if method == "notes":
        return await send_with_mock_transport(
            lambda client: client.x.community_notes.list_contributor_notes(alias, **arguments),
            lambda client: client.x.community_notes.list_contributor_notes(alias, **arguments),
            payload,
            asynchronous,
        )
    deleted_request, deleted_page = await send_with_mock_transport(
        lambda client: client.x.community_notes.list_contributor_deleted_notes(alias, **arguments),
        lambda client: client.x.community_notes.list_contributor_deleted_notes(alias, **arguments),
        payload,
        asynchronous,
    )
    return deleted_request, deleted_page


ALIASES = [
    pytest.param(
        "ardent-beach-friarbird", b"/api/v1/x/community-notes/contributors/ardent-beach-friarbird", id="alias"
    ),
    pytest.param(
        "x.com/i/communitynotes/u/ardent-beach-friarbird",
        b"/api/v1/x/community-notes/contributors/x.com%2Fi%2Fcommunitynotes%2Fu%2Fardent-beach-friarbird",
        id="url",
    ),
]
NOTE_LISTS = [pytest.param("notes", b"/notes", id="notes"), pytest.param("deleted", b"/deleted-notes", id="deleted")]


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_trends_history_sends_every_filter_and_reads_the_snapshots(asynchronous: bool) -> None:
    arguments: XGetTrendsHistoryParams = {
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
    }
    request, history = await send_with_mock_transport(
        lambda client: client.x.get_trends_history(**arguments),
        lambda client: client.x.get_trends_history(**arguments),
        TRENDS_HISTORY,
        asynchronous,
    )

    assert request.url.path == "/api/v1/x/trends/history"
    assert dict(request.url.params.items()) == {
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
    location = history.location
    assert location is not None
    assert (location.woeid, location.name, location.country, location.country_code) == (
        23424969,
        "Turkey",
        "Turkey",
        "TR",
    )
    assert (location.place_type, location.place_type_code, location.parent_woeid) == ("Country", 12, 1)
    assert location.url == "http://where.yahooapis.com/v1/place/23424969"


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_trends_history_without_filters_sends_no_query(asynchronous: bool) -> None:
    request, history = await send_with_mock_transport(
        lambda client: client.x.get_trends_history(),
        lambda client: client.x.get_trends_history(),
        TRENDS_HISTORY,
        asynchronous,
    )

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
    arguments: XGetNewsStoryVersionsParams = {"fields": "versions.headline", "omit": "versions.text"}
    request, story_versions = await send_with_mock_transport(
        lambda client: client.x.get_news_story_versions(story, **arguments),
        lambda client: client.x.get_news_story_versions(story, **arguments),
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
@pytest.mark.parametrize(("alias", "raw_path"), ALIASES)
async def test_contributor_reads_note_and_rating_counts(alias: str, raw_path: bytes, asynchronous: bool) -> None:
    arguments: CommunityNoteRetrieveContributorParams = {"fields": "alias,notesCount", "omit": "ratingsCount"}
    request, response = await send_with_mock_transport(
        lambda client: client.x.community_notes.retrieve_contributor(alias, **arguments),
        lambda client: client.x.community_notes.retrieve_contributor(alias, **arguments),
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
    notes_count = contributor.notes_count
    assert notes_count is not None
    assert (notes_count.awaiting_more_ratings, notes_count.currently_rated_helpful) == (18, 1)
    assert notes_count.currently_rated_not_helpful == 2
    assert notes_count.updated_at == datetime(2026, 10, 12, 22, 18, 40, 96000, tzinfo=timezone.utc)
    ratings = contributor.ratings_count
    assert ratings is not None
    assert (ratings.awaiting_more_ratings, ratings.rated_after_decision) == (703, 154)
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
@pytest.mark.parametrize(("alias", "raw_path"), ALIASES)
@pytest.mark.parametrize(("method", "suffix"), NOTE_LISTS)
async def test_contributor_note_lists_send_the_alias_and_paging(
    method: str, suffix: bytes, alias: str, raw_path: bytes, asynchronous: bool
) -> None:
    request, page = await list_notes(
        method,
        alias,
        CONTRIBUTOR_DELETED_NOTES,
        asynchronous,
        cursor="-1767098234260",
        page_size=10,
        fields="notes.text",
        omit="notes.post",
    )

    assert request.url.raw_path.partition(b"?")[0] == raw_path + suffix
    assert dict(request.url.params.items()) == {
        "cursor": "-1767098234260",
        "pageSize": "10",
        "fields": "notes.text",
        "omit": "notes.post",
    }
    assert page.notes[0].id == "2078950499982696756"


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize(("method", "suffix"), NOTE_LISTS)
async def test_contributor_note_lists_read_each_note_with_its_post(
    method: str, suffix: bytes, asynchronous: bool
) -> None:
    request, page = await list_notes(method, "ardent-beach-friarbird", CONTRIBUTOR_NOTES, asynchronous)

    assert request.url.raw_path == b"/api/v1/x/community-notes/contributors/ardent-beach-friarbird" + suffix
    assert page.has_next_page is True
    assert page.next_cursor == "-1767098234260"
    note = page.notes[0]
    assert note.id == "2026375778254868976"
    assert note.created_at == datetime(2026, 2, 24, 19, 16, 48, 435000, tzinfo=timezone.utc)
    assert note.language == "en"
    assert note.classification == "MisinformedOrPotentiallyMisleading"
    assert note.text == NOTE_TEXT
    contributor = note.contributor
    assert contributor is not None
    assert contributor.alias == "ardent-beach-friarbird"
    assert (contributor.deleted_notes_count, contributor.is_api_contributor, contributor.is_top_writer) == (
        None,
        None,
        None,
    )
    assert contributor.notes_count is not None
    assert contributor.notes_count.currently_rated_helpful == 1
    assert contributor.notes_count.currently_rated_not_helpful == 2
    assert contributor.notes_count.awaiting_more_ratings is None
    assert contributor.ratings_count is not None
    assert contributor.ratings_count.successful is not None
    assert contributor.ratings_count.successful.total == 49
    assert contributor.ratings_count.unsuccessful is not None
    assert contributor.ratings_count.unsuccessful.helpful_count == 15
    assert contributor.ratings_count.unsuccessful.not_helpful_count == 4
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
@pytest.mark.parametrize(("method", "suffix"), NOTE_LISTS)
async def test_contributor_note_lists_read_every_note_field(method: str, suffix: bytes, asynchronous: bool) -> None:
    payload = {"notes": [FULL_NOTE], "has_next_page": False, "next_cursor": ""}
    request, page = await list_notes(method, "ardent-beach-friarbird", payload, asynchronous)

    assert request.url.raw_path == b"/api/v1/x/community-notes/contributors/ardent-beach-friarbird" + suffix
    note = page.notes[0]
    assert (note.id, note.language, note.classification) == ("2026375778254868977", "es", "NotMisleading")
    assert note.created_at == datetime(2026, 2, 25, 8, 0, tzinfo=timezone.utc)
    assert note.text == "La foto es de 2019. #AI"
    contributor = note.contributor
    assert contributor is not None
    assert (contributor.alias, contributor.deleted_notes_count) == ("ardent-beach-friarbird", 3)
    assert (contributor.is_api_contributor, contributor.is_top_writer) == (True, True)
    notes_count = contributor.notes_count
    assert notes_count is not None
    assert (notes_count.awaiting_more_ratings, notes_count.currently_rated_helpful) == (18, 1)
    assert notes_count.currently_rated_not_helpful == 2
    assert notes_count.updated_at == datetime(2026, 10, 12, 22, 18, 40, 96000, tzinfo=timezone.utc)
    ratings = contributor.ratings_count
    assert ratings is not None
    assert (ratings.awaiting_more_ratings, ratings.rated_after_decision) == (703, 154)
    assert ratings.updated_at == datetime(2026, 10, 12, 22, 50, 13, 228000, tzinfo=timezone.utc)
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
    ) == (15, 4, 19)
    assert note.entities is not None
    entity = note.entities[0]
    assert (entity.from_index, entity.to_index) == (20, 23)
    ref = entity.ref
    assert ref is not None
    assert (ref.type, ref.text, ref.screen_name) == ("Hashtag", "AI", "discord")
    assert (ref.url, ref.url_type) == ("https://x.com/hashtag/AI", "ExternalUrl")
    assert note.rating_status == "NeedsMoreRatings"
    assert (note.helpful_tags, note.not_helpful_tags) == (["GoodSources"], ["Outdated"])
    assert (note.decided_by, note.fully_visible_model, note.above_pcrh_threshold) == ("CoreModel (v1.1)", False, True)
    assert (note.appeal_status, note.deleted, note.is_api_author) == ("Appealed", False, True)
    assert (note.is_media_note, note.media_note_match_count, note.is_url_note) == (True, 12, True)
    assert (note.display_url, note.is_translatable, note.impression_count) == ("discord.com/blog", True, 45000)
    assert (note.time_to_helpful_from_note_ms, note.time_to_helpful_from_post_ms) == (1000, 2000)
    assert (note.post_id, note.post) == ("2026359315657805940", None)
    assert note.post_unavailable is not None
    assert note.post_unavailable.reason == "Suspended"
    assert note.tombstone is None


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize(("method", "suffix"), NOTE_LISTS)
async def test_contributor_note_lists_read_the_tombstones(method: str, suffix: bytes, asynchronous: bool) -> None:
    request, page = await list_notes(method, "ardent-beach-friarbird", CONTRIBUTOR_DELETED_NOTES, asynchronous)

    assert request.url.raw_path == b"/api/v1/x/community-notes/contributors/ardent-beach-friarbird" + suffix
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
    assert (note.text, note.post, note.contributor) == (None, None, None)
