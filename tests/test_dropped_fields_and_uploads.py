# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import json
from typing import Any, Dict, List, Type
from datetime import datetime, timezone

import httpx
import pytest

from tests.utils import send_with_mock_transport
from x_twitter_scraper import XTwitterScraper
from tests.mock_api_schema import model_payloads
from x_twitter_scraper.types import (
    Monitor,
    DraftCreateResponse,
    MonitorListResponse,
    MonitorCreateResponse,
    WebhookCreateResponse,
    AccountUpdateLocaleResponse,
)
from x_twitter_scraper._compat import PYDANTIC_V1
from x_twitter_scraper._models import BaseModel
from x_twitter_scraper.types.x import (
    MediaUploadResponse,
    SpaceRetrieveResponse,
    TweetGetRepliesResponse,
    ProfileUpdateAvatarResponse,
    ProfileUpdateBannerResponse,
)
from x_twitter_scraper.types.event import Event, DataMonitorFollow, DataMonitorLegacyPost, DataMonitorProfileChange
from x_twitter_scraper.types.shared import SearchTweet, UserProfile
from x_twitter_scraper.types.support import TicketReplyResponse, TicketCreateResponse
from x_twitter_scraper.types.monitors import KeywordListResponse
from x_twitter_scraper.types.compose_create_response import (
    ComposePrepareResult,
    ComposePrepareResultEngagementMultiplier,
)
from x_twitter_scraper.types.monitors.keyword_list_response import Monitor as KeywordMonitor
from x_twitter_scraper.types.x.user_retrieve_followers_response import UserListPage

AVATAR = "https://pbs.twimg.com/profile_images/example.jpg"
FILE = ("avatar.png", b"binary-content", "image/png")


def minimal(model: Type[BaseModel]) -> Dict[str, object]:
    payload: Dict[str, object] = json.loads(model_payloads({model})[model])
    return payload


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_user_profiles_keep_the_full_size_picture_and_redirect(asynchronous: bool) -> None:
    payload = {**minimal(UserProfile), "profilePictureOriginal": AVATAR, "redirectsToUsername": "spacexsi"}
    _, profile = await send_with_mock_transport(
        lambda client: client.x.users.retrieve("44196397"),
        lambda client: client.x.users.retrieve("44196397"),
        payload,
        asynchronous,
    )

    assert profile.profile_picture_original == AVATAR
    assert profile.redirects_to_username == "spacexsi"


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_tombstone_and_interstitial_entities_keep_their_text(asynchronous: bool) -> None:
    text = {
        "text": "This post is from a suspended account. Learn more",
        "entities": [
            {
                "fromIndex": 39,
                "toIndex": 49,
                "ref": {
                    "type": "TimelineUrl",
                    "url": "https://help.x.com",
                    "text": "Learn more",
                    "screenName": "XSupport",
                },
            }
        ],
    }
    tweet = {**minimal(SearchTweet), "tombstone": {"text": text}, "interstitial": {"text": text}}
    payload = {"tweets": [tweet], "has_next_page": False, "next_cursor": ""}
    _, page = await send_with_mock_transport(
        lambda client: client.x.users.retrieve_likes("44196397"),
        lambda client: client.x.users.retrieve_likes("44196397"),
        payload,
        asynchronous,
    )

    found = page.tweets[0]
    assert found.tombstone is not None and found.tombstone.text is not None
    assert found.tombstone.text.entities is not None
    tombstone_ref = found.tombstone.text.entities[0].ref
    assert tombstone_ref is not None
    assert (tombstone_ref.text, tombstone_ref.screen_name) == ("Learn more", "XSupport")
    assert found.interstitial is not None and found.interstitial.text is not None
    assert found.interstitial.text.entities is not None
    interstitial_ref = found.interstitial.text.entities[0].ref
    assert interstitial_ref is not None
    assert (interstitial_ref.text, interstitial_ref.screen_name) == ("Learn more", "XSupport")


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_follower_and_count_events_parse_with_their_data(asynchronous: bool) -> None:
    event: Dict[str, object] = {
        **minimal(Event),
        "id": "9001",
        "monitorId": "12",
        "monitorType": "account",
        "username": "elonmusk",
        "occurredAt": "2026-10-13T02:40:00.000Z",
        "createdAt": "2026-10-13T02:40:00.000Z",
    }
    events = [
        {
            **event,
            "type": "follower.added",
            "data": {
                "id": "2244994945",
                "followedAt": "2026-10-13T02:36:54.961Z",
                "followedAtExact": True,
                "username": "XDevelopers",
            },
        },
        {**event, "type": "follower.removed", "data": {"id": "2244994945", "reason": "unfollowed"}},
        {
            **event,
            "type": "profile.followers.changed",
            "data": {
                "field": "followers",
                "userId": "44196397",
                "username": "elonmusk",
                "change": -3,
                "previous": 100,
                "current": 97,
            },
        },
    ]
    request, page = await send_with_mock_transport(
        lambda client: client.events.list(event_type="follower.added"),
        lambda client: client.events.list(event_type="follower.added"),
        {"events": events, "hasMore": False},
        asynchronous,
    )

    assert dict(request.url.params) == {"eventType": "follower.added"}
    added, removed, changed = page.events
    assert (added.type, removed.type) == ("follower.added", "follower.removed")
    if PYDANTIC_V1:
        assert isinstance(added.data, DataMonitorLegacyPost)
        assert added.data.to_dict()["followedAt"] == "2026-10-13T02:36:54.961Z"
        assert isinstance(removed.data, DataMonitorLegacyPost)
        assert removed.data.to_dict()["reason"] == "unfollowed"
    else:
        assert isinstance(added.data, DataMonitorFollow)
        assert added.data.id == "2244994945"
        assert added.data.followed_at == datetime(2026, 10, 13, 2, 36, 54, 961000, tzinfo=timezone.utc)
        assert added.data.followed_at_exact is True
        assert isinstance(removed.data, DataMonitorFollow)
        assert removed.data.reason == "unfollowed"
    assert changed.type == "profile.followers.changed"
    assert isinstance(changed.data, DataMonitorProfileChange)
    assert changed.data.change == -3
    assert (changed.data.previous, changed.data.current) == (("100", "97") if PYDANTIC_V1 else (100, 97))


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_monitors_take_the_follower_event_types(asynchronous: bool) -> None:
    request, _ = await send_with_mock_transport(
        lambda client: client.monitors.create(
            event_types=[
                "follower.added",
                "follower.removed",
                "profile.followers.changed",
                "profile.following.changed",
            ],
            username="elonmusk",
        ),
        lambda client: client.monitors.create(
            event_types=[
                "follower.added",
                "follower.removed",
                "profile.followers.changed",
                "profile.following.changed",
            ],
            username="elonmusk",
        ),
        {
            **minimal(MonitorCreateResponse),
            "eventTypes": ["follower.added", "profile.following.changed"],
        },
        asynchronous,
        method="POST",
    )

    assert json.loads(request.content)["eventTypes"] == [
        "follower.added",
        "follower.removed",
        "profile.followers.changed",
        "profile.following.changed",
    ]


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_paused_monitors_say_why(asynchronous: bool) -> None:
    monitor = {
        **minimal(Monitor),
        "eventTypes": ["profile.followers.changed"],
        "pausedReason": "insufficient_credits",
    }
    _, page = await send_with_mock_transport(
        lambda client: client.monitors.list(),
        lambda client: client.monitors.list(),
        {**minimal(MonitorListResponse), "monitors": [monitor]},
        asynchronous,
    )
    assert page.monitors[0].paused_reason == "insufficient_credits"
    assert page.monitors[0].event_types == ["profile.followers.changed"]

    keyword_monitor = {
        **minimal(KeywordMonitor),
        "pausedAt": "2025-01-15T12:00:00Z",
        "pausedReason": "insufficient_credits",
    }
    _, keyword_page = await send_with_mock_transport(
        lambda client: client.monitors.keywords.list(),
        lambda client: client.monitors.keywords.list(),
        {**minimal(KeywordListResponse), "monitors": [keyword_monitor]},
        asynchronous,
    )
    assert keyword_page.monitors[0].paused_at == datetime(2025, 1, 15, 12, tzinfo=timezone.utc)
    assert keyword_page.monitors[0].paused_reason == "insufficient_credits"


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_writes_report_the_fields_they_ignored(asynchronous: bool) -> None:
    _, account = await send_with_mock_transport(
        lambda client: client.account.update_locale(locale="tr"),
        lambda client: client.account.update_locale(locale="tr"),
        {**minimal(AccountUpdateLocaleResponse), "ignoredFields": ["plan"]},
        asynchronous,
        method="PATCH",
    )
    assert account.ignored_fields == ["plan"]

    _, draft = await send_with_mock_transport(
        lambda client: client.drafts.create(text="Ship it"),
        lambda client: client.drafts.create(text="Ship it"),
        {**minimal(DraftCreateResponse), "ignoredFields": ["plan"]},
        asynchronous,
        method="POST",
    )
    assert isinstance(draft, DraftCreateResponse)
    assert draft.ignored_fields == ["plan"]

    _, webhook = await send_with_mock_transport(
        lambda client: client.webhooks.create(event_types=["follower.added"], url="https://example.com/hook"),
        lambda client: client.webhooks.create(event_types=["follower.added"], url="https://example.com/hook"),
        {**minimal(WebhookCreateResponse), "eventTypes": ["follower.added"], "ignoredFields": ["plan"]},
        asynchronous,
        method="POST",
    )
    assert webhook.ignored_fields == ["plan"]
    assert webhook.event_types == ["follower.added"]


def multipart_fields(request: httpx.Request) -> List[bytes]:
    boundary = request.headers["Content-Type"].split("boundary=", 1)[1].encode()
    parts = request.content.split(b"--" + boundary)[1:-1]
    return [part.strip(b"\r\n").split(b"\r\n\r\n", 1)[0] for part in parts]


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_media_and_profile_images_upload_as_files(asynchronous: bool) -> None:
    request, media = await send_with_mock_transport(
        lambda client: client.x.media.upload(
            account="@elonmusk", file=FILE, is_long_video=False, idempotency_key="upload-1"
        ),
        lambda client: client.x.media.upload(
            account="@elonmusk", file=FILE, is_long_video=False, idempotency_key="upload-1"
        ),
        minimal(MediaUploadResponse),
        asynchronous,
        method="POST",
    )
    assert isinstance(media, MediaUploadResponse)
    assert request.url.path == "/api/v1/x/media"
    assert request.headers["Content-Type"].startswith("multipart/form-data; boundary=")
    assert request.headers["Idempotency-Key"] == "upload-1"
    assert b"binary-content" in request.content
    assert multipart_fields(request) == [
        b'Content-Disposition: form-data; name="account"',
        b'Content-Disposition: form-data; name="is_long_video"',
        b'Content-Disposition: form-data; name="file"; filename="avatar.png"\r\nContent-Type: image/png',
    ]

    for path, response_type in [
        ("/api/v1/x/profile/avatar", ProfileUpdateAvatarResponse),
        ("/api/v1/x/profile/banner", ProfileUpdateBannerResponse),
    ]:
        if path.endswith("avatar"):
            request, image = await send_with_mock_transport(
                lambda client: client.x.profile.update_avatar(account="@elonmusk", file=FILE, idempotency_key="a"),
                lambda client: client.x.profile.update_avatar(account="@elonmusk", file=FILE, idempotency_key="a"),
                minimal(response_type),
                asynchronous,
                method="PATCH",
            )
        else:
            request, image = await send_with_mock_transport(
                lambda client: client.x.profile.update_banner(account="@elonmusk", file=FILE, idempotency_key="b"),
                lambda client: client.x.profile.update_banner(account="@elonmusk", file=FILE, idempotency_key="b"),
                minimal(response_type),
                asynchronous,
                method="PATCH",
            )
        assert isinstance(image, response_type)
        assert request.url.path == path
        assert request.headers["Content-Type"].startswith("multipart/form-data; boundary=")
        assert multipart_fields(request) == [
            b'Content-Disposition: form-data; name="account"',
            b'Content-Disposition: form-data; name="file"; filename="avatar.png"\r\nContent-Type: image/png',
        ]


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_url_uploads_still_send_json(asynchronous: bool) -> None:
    request, _ = await send_with_mock_transport(
        lambda client: client.x.media.upload(
            account="@elonmusk", url="https://example.com/image.png", idempotency_key="upload-2"
        ),
        lambda client: client.x.media.upload(
            account="@elonmusk", url="https://example.com/image.png", idempotency_key="upload-2"
        ),
        minimal(MediaUploadResponse),
        asynchronous,
        method="POST",
    )
    assert request.headers["Content-Type"] == "application/json"
    assert json.loads(request.content) == {"account": "@elonmusk", "url": "https://example.com/image.png"}


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_support_tickets_take_attachments(asynchronous: bool) -> None:
    request, ticket = await send_with_mock_transport(
        lambda client: client.support.tickets.create(subject="Billing", attachments=[FILE]),
        lambda client: client.support.tickets.create(subject="Billing", attachments=[FILE]),
        minimal(TicketCreateResponse),
        asynchronous,
        method="POST",
    )
    assert isinstance(ticket, TicketCreateResponse)
    assert request.headers["Content-Type"].startswith("multipart/form-data; boundary=")
    assert multipart_fields(request) == [
        b'Content-Disposition: form-data; name="subject"',
        b'Content-Disposition: form-data; name="attachments[]"; filename="avatar.png"\r\nContent-Type: image/png',
    ]

    request, reply = await send_with_mock_transport(
        lambda client: client.support.tickets.reply("7", content="Here is the receipt.", attachments=[FILE]),
        lambda client: client.support.tickets.reply("7", content="Here is the receipt.", attachments=[FILE]),
        minimal(TicketReplyResponse),
        asynchronous,
        method="POST",
    )
    assert isinstance(reply, TicketReplyResponse)
    assert request.url.path == "/api/v1/support/tickets/7/messages"
    assert multipart_fields(request) == [
        b'Content-Disposition: form-data; name="body"',
        b'Content-Disposition: form-data; name="attachments[]"; filename="avatar.png"\r\nContent-Type: image/png',
    ]


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_space_participants_keep_the_full_size_picture(asynchronous: bool) -> None:
    payload = minimal(SpaceRetrieveResponse)
    space = payload["space"]
    assert isinstance(space, dict)
    space["admins"] = [
        {"id": "951329744804392960", "username": "solana", "name": "Solana", "profilePictureOriginal": AVATAR}
    ]
    _, response = await send_with_mock_transport(
        lambda client: client.x.spaces.retrieve("1OGwblLjnQMKB"),
        lambda client: client.x.spaces.retrieve("1OGwblLjnQMKB"),
        payload,
        asynchronous,
    )

    assert response.space.admins[0].profile_picture_original == AVATAR


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_long_reads_say_where_they_stopped(asynchronous: bool) -> None:
    scan_limit = {
        "limit": 100000,
        "rowsRead": 100000,
        "message": "Stopped at the scan limit of 100,000 profiles. Read the list again with a higher maxScan to read further.",
    }
    _, followers = await send_with_mock_transport(
        lambda client: client.x.users.retrieve_followers("44196397", bio_contains="founder"),
        lambda client: client.x.users.retrieve_followers("44196397", bio_contains="founder"),
        {"users": [], "has_next_page": False, "next_cursor": "", "scanLimit": scan_limit},
        asynchronous,
    )
    assert isinstance(followers, UserListPage)
    assert followers.scan_limit is not None
    assert (followers.scan_limit.limit, followers.scan_limit.rows_read) == (100000, 100000)
    assert followers.scan_limit.message.startswith("Stopped at the scan limit of 100,000 profiles.")

    _, replies = await send_with_mock_transport(
        lambda client: client.x.tweets.get_replies("1"),
        lambda client: client.x.tweets.get_replies("1"),
        {**minimal(TweetGetRepliesResponse), "partialBefore": "2026-10-07T00:00:00.000Z"},
        asynchronous,
    )
    assert replies.partial_before == datetime(2026, 10, 7, tzinfo=timezone.utc)


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize(
    "multiplier", ["Source default. Production value can vary.", "Source default; production value can vary"]
)
async def test_compose_reads_both_multiplier_notes(multiplier: str, asynchronous: bool) -> None:
    payload = minimal(ComposePrepareResult)
    payload["engagementMultipliers"] = [{**minimal(ComposePrepareResultEngagementMultiplier), "multiplier": multiplier}]
    _, result = await send_with_mock_transport(
        lambda client: client.compose.create(step="compose", topic="Launch"),
        lambda client: client.compose.create(step="compose", topic="Launch"),
        payload,
        asynchronous,
        method="POST",
    )
    assert isinstance(result, ComposePrepareResult)
    assert result.engagement_multipliers[0].multiplier == multiplier


def test_an_upload_needs_a_url_or_a_file() -> None:
    client = XTwitterScraper(api_key="isolated-test")
    upload: Any = client.x.media.upload
    with pytest.raises(
        TypeError,
        match=r"Missing required arguments; Expected either \('account', 'idempotency_key' and 'url'\) or \('account', 'file' and 'idempotency_key'\) arguments to be given",
    ):
        upload(account="@elonmusk", idempotency_key="upload-3")
    reply: Any = client.support.tickets.reply
    with pytest.raises(TypeError, match=r"Expected either \('content'\) or \('attachments'\) arguments to be given"):
        reply("7")
