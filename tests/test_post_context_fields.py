# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import List, Union, Callable, Awaitable

import pytest

from tests.utils import send_with_mock_transport
from x_twitter_scraper.types.x import TweetDetail
from x_twitter_scraper.types.event import DataMonitorPost as EventPost
from x_twitter_scraper.types.shared import SearchTweet, EmbeddedTweet
from x_twitter_scraper.types.event_detail import DataMonitorPost as EventDetailPost

AUXILIARY_LABEL = {
    "badgeUrl": "https://pbs.twimg.com/profile_images/1683325380441128960/yRsRRjGO_bigger.jpg",
    "description": "Automated by @NASA",
    "url": "https://x.com/NASA",
    "userLabelDisplayType": "Badge",
    "userLabelType": "AutomatedLabel",
}
AUTHOR = {
    "id": "11348282",
    "username": "NASA",
    "name": "NASA",
    "affiliatesHighlightedLabel": {"description": "NASA", "auxiliaryLabels": [AUXILIARY_LABEL]},
}
COUNTS = {"likeCount": 42, "retweetCount": 5, "replyCount": 3, "quoteCount": 1, "viewCount": 1500, "bookmarkCount": 2}
REACTED_TO = {"id": "1900000000000000000", "author": {"id": "11348282", "username": "NASA"}, "unknownFields": ["text"]}
POST = {
    "id": "1900000000000000001",
    "text": "",
    **COUNTS,
    "author": AUTHOR,
    "unknownFields": ["text"],
    "liveEventContext": {
        "title": "US Midterm Elections",
        "url": "https://x.com/i/election/104725482743328773",
        "imageUrl": "https://pbs.twimg.com/media/election.jpg",
    },
    "media": [
        {
            "type": "photo",
            "url": "https://t.co/abc",
            "mediaUrl": "https://pbs.twimg.com/media/GxPhoto.jpg",
            "editedWithNativeEditor": True,
        }
    ],
    "reactionContext": {"reactedToPostId": "1900000000000000000", "reactedToPost": REACTED_TO},
}
REPLY = {**POST, "parentTweet": POST}
EVENT = {
    "id": "42",
    "type": "tweet.new",
    "monitorId": "7",
    "monitorType": "account",
    "occurredAt": "2026-10-13T12:00:00.000Z",
    "data": REPLY,
}

Post = Union[SearchTweet, TweetDetail, EventPost, EventDetailPost, EmbeddedTweet]


async def liked_posts(asynchronous: bool) -> List[Post]:
    _, page = await send_with_mock_transport(
        lambda client: client.x.users.retrieve_likes("11348282"),
        lambda client: client.x.users.retrieve_likes("11348282"),
        {"tweets": [REPLY], "has_next_page": False, "next_cursor": ""},
        asynchronous,
    )
    post = page.tweets[0]
    assert post.parent_tweet is not None
    return [post, post.parent_tweet]


async def post_detail(asynchronous: bool) -> List[Post]:
    _, response = await send_with_mock_transport(
        lambda client: client.x.tweets.retrieve("1900000000000000001"),
        lambda client: client.x.tweets.retrieve("1900000000000000001"),
        {"tweet": REPLY},
        asynchronous,
    )
    assert response.tweet.parent_tweet is not None
    return [response.tweet, response.tweet.parent_tweet]


async def listed_event(asynchronous: bool) -> List[Post]:
    _, response = await send_with_mock_transport(
        lambda client: client.events.list(),
        lambda client: client.events.list(),
        {"events": [EVENT], "hasMore": False},
        asynchronous,
    )
    post = response.events[0].data
    assert isinstance(post, EventPost)
    assert post.parent_tweet is not None
    return [post, post.parent_tweet]


async def event_detail(asynchronous: bool) -> List[Post]:
    _, event = await send_with_mock_transport(
        lambda client: client.events.retrieve("42"),
        lambda client: client.events.retrieve("42"),
        EVENT,
        asynchronous,
    )
    assert isinstance(event.data, EventDetailPost)
    assert event.data.parent_tweet is not None
    return [event.data, event.data.parent_tweet]


READS = [liked_posts, post_detail, listed_event, event_detail]


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize("read", READS)
async def test_posts_carry_the_live_event_and_the_fields_x_did_not_send(
    read: Callable[[bool], Awaitable[List[Post]]], asynchronous: bool
) -> None:
    for post in await read(asynchronous):
        assert post.unknown_fields == ["text"]
        event = post.live_event_context
        assert event is not None
        assert (event.title, event.url, event.image_url) == (
            "US Midterm Elections",
            "https://x.com/i/election/104725482743328773",
            "https://pbs.twimg.com/media/election.jpg",
        )
        assert post.media is not None
        assert post.media[0].edited_with_native_editor is True


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize("read", READS)
async def test_post_authors_carry_the_auxiliary_labels(
    read: Callable[[bool], Awaitable[List[Post]]], asynchronous: bool
) -> None:
    for post in await read(asynchronous):
        assert post.author is not None
        label = post.author.affiliates_highlighted_label
        assert label is not None
        assert label.auxiliary_labels is not None
        auxiliary = label.auxiliary_labels[0]
        assert (auxiliary.description, auxiliary.url, auxiliary.user_label_type) == (
            "Automated by @NASA",
            "https://x.com/NASA",
            "AutomatedLabel",
        )


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize("read", [liked_posts, post_detail])
async def test_reactions_keep_the_post_they_react_to(
    read: Callable[[bool], Awaitable[List[Post]]], asynchronous: bool
) -> None:
    for post in await read(asynchronous):
        assert post.reaction_context is not None
        assert post.reaction_context.reacted_to_post == REACTED_TO


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize("read", [listed_event, event_detail])
async def test_monitor_reactions_type_the_post_they_react_to(
    read: Callable[[bool], Awaitable[List[Post]]], asynchronous: bool
) -> None:
    post = (await read(asynchronous))[0]
    assert isinstance(post, (EventPost, EventDetailPost))
    assert post.reaction_context is not None
    reacted = post.reaction_context.reacted_to_post
    assert reacted is not None
    assert reacted.id == "1900000000000000000"
    assert reacted.unknown_fields == ["text"]
    assert reacted.author is not None
    assert reacted.author.username == "NASA"


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_space_participants_carry_the_auxiliary_labels(asynchronous: bool) -> None:
    space = {"id": "1OGwblLjnQMKB", "admins": [AUTHOR], "speakers": [AUTHOR], "listeners": [AUTHOR]}
    _, response = await send_with_mock_transport(
        lambda client: client.x.spaces.retrieve("1OGwblLjnQMKB"),
        lambda client: client.x.spaces.retrieve("1OGwblLjnQMKB"),
        {"space": space},
        asynchronous,
    )

    for people in (response.space.admins, response.space.speakers, response.space.listeners):
        label = people[0].affiliates_highlighted_label
        assert label is not None
        assert label.auxiliary_labels is not None
        assert label.auxiliary_labels[0].badge_url == AUXILIARY_LABEL["badgeUrl"]
