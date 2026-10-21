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

LABEL = {
    "displayType": "Fosnr",
    "engagementNudge": True,
    "text": {
        "text": "This Post may violate X's rules against Abuse.",
        "rtl": False,
        "entities": [
            {
                "fromIndex": 22,
                "toIndex": 29,
                "ref": {"type": "TimelineUrl", "url": "https://help.x.com/rules", "urlType": "ExternalUrl"},
            }
        ],
    },
    "url": {"url": "https://help.x.com/rules-and-policies/enforcement-options", "urlType": "ExternalUrl"},
}
COUNTS = {"likeCount": 42, "retweetCount": 5, "replyCount": 3, "quoteCount": 1, "viewCount": 1500, "bookmarkCount": 2}
POST = {"id": "1900000000000000001", "text": "Launch day", **COUNTS, "softIntervention": LABEL}
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
        lambda client: client.x.users.retrieve_likes("44196397"),
        lambda client: client.x.users.retrieve_likes("44196397"),
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


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize("read", [liked_posts, post_detail, listed_event, event_detail])
async def test_post_reads_return_the_label_x_shows_on_limited_posts(
    read: Callable[[bool], Awaitable[List[Post]]], asynchronous: bool
) -> None:
    for post in await read(asynchronous):
        label = post.soft_intervention
        assert label is not None
        assert (label.display_type, label.engagement_nudge) == ("Fosnr", True)
        assert label.text is not None
        assert (label.text.text, label.text.rtl) == ("This Post may violate X's rules against Abuse.", False)
        assert label.text.entities is not None
        entity = label.text.entities[0]
        assert (entity.from_index, entity.to_index) == (22, 29)
        assert entity.ref is not None
        assert (entity.ref.type, entity.ref.url, entity.ref.url_type) == (
            "TimelineUrl",
            "https://help.x.com/rules",
            "ExternalUrl",
        )
        assert label.url is not None
        assert (label.url.url, label.url.url_type) == (
            "https://help.x.com/rules-and-policies/enforcement-options",
            "ExternalUrl",
        )
