# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Any, Callable, cast
from datetime import datetime, timezone
from itertools import product

import pytest

from x_twitter_scraper._models import validate_type, construct_type_unchecked
from x_twitter_scraper.types.x import TweetGetRepliesResponse
from x_twitter_scraper.types.shared import UserProfile, EmbeddedTweet
from x_twitter_scraper.types.shared.embedded_tweet import QuotedTweet, RetweetedTweet

COUNTS = {"retweetCount": 5, "replyCount": 3, "likeCount": 42, "quoteCount": 1, "viewCount": 1500, "bookmarkCount": 2}
POST = {"id": "1234567890", "text": "Just launched!", "createdAt": "2025-01-15T12:00:00Z", **COUNTS}
AUTHOR = {"id": "11348282", "username": "NASA", "name": "NASA", "followers": 92376187}
TAG = {"id": "TSLA", "info": {"info": {"active": True, "name": "Tesla", "ticker": "TSLA"}}}
ENTITIES = {"hashtags": [{"text": "TSLA", "indices": [0, 5], "tag": TAG}]}
NESTED = {**POST, "author": AUTHOR, "communityName": "Build in Public", "entities": ENTITIES}
SOFT_INTERVENTION = {
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
EMBEDDED = {
    **POST,
    "type": "tweet",
    "url": "https://x.com/example_user/status/1234567890",
    "lang": "en",
    "isReply": True,
    "isLimitedReply": False,
    "isNoteTweet": True,
    "isPinned": True,
    "isQuoteStatus": True,
    "isRetweet": True,
    "quotedTweetId": "1234567890",
    "quotedTweetPermalink": {"displayUrl": "x.com/example_user/status/1234567890", "url": "https://t.co/quoted"},
    "quotedTweetUnavailable": {"reason": "Suspended"},
    "retweetedAt": "2026-09-11T20:24:45.000Z",
    "inReplyToId": "1234567890",
    "inReplyToUserId": "9876543210",
    "inReplyToUsername": "example_user",
    "conversationId": "1234567890",
    "conversationControl": {"allowedCountryCodes": ["TR"], "mode": "country_of_origin", "ownerId": "9876543210"},
    "limitedActions": [{"action": "Reply", "prompt": {"ctaType": "SeeConversation"}}],
    "source": "Twitter Web App",
    "displayTextRange": [0, 13],
    "textHighlights": [{"startIndex": 5, "endIndex": 13}],
    "contentDisclosure": {"advertising": {"isPaidPromotion": True}},
    "article": {"id": "article-1", "title": "Launch"},
    "authorUnavailable": {"reason": "Suspended", "message": "Account suspended"},
    "unavailableAuthorId": "9876543210",
    "card": {"name": "summary", "userReferences": [AUTHOR]},
    "cashtagAttachments": [
        {
            "cashtag": "$TSLA",
            "candleSize": "5m",
            "timeframe": "1D",
            "startTime": "2026-10-09T13:30:00.000Z",
            "endTime": "2026-10-09T13:42:08.796Z",
            "sizeVariant": 1,
        }
    ],
    "communityId": "community-1",
    "communityName": "Build in Public",
    "communityNote": {"id": "note-1", "title": "Context"},
    "hasCommunityNotes": True,
    "edit": {"editTweetIds": ["1234567890"]},
    "exclusiveContent": {"creatorUserName": "NASA", "subscribeUrl": "https://x.com/NASA/subscribe"},
    "isTranslatable": True,
    "grokShareAttachment": {"conversationId": "grok-1"},
    "grokTranslatedPost": {"text": "Launched", "lang": "en"},
    "jetfuelAttachment": {"id": "jetfuel-1"},
    "noteTweet": {"text": "Just launched!", "noteId": "note-1", "entities": ENTITIES},
    "place": {"id": "place-1", "name": "Istanbul"},
    "coordinates": {"coordinates": [28.97, 41.01], "type": "Point"},
    "geo": {"coordinates": [41.01, 28.97], "type": "Point"},
    "postCta": {"text": "Read more"},
    "possiblySensitive": False,
    "previousCounts": COUNTS,
    "reactionContext": {"reactedToPostId": "1234567890", "reactedToUser": AUTHOR},
    "sportsContext": {
        "gameId": "game-1",
        "league": "league-1",
        "competitors": [{"teamId": "team-1", "color": "ffffff", "isActive": True, "isWinner": False}],
    },
    "subscriberBadge": {"creatorId": "11348282"},
    "tombstone": {"text": {"text": "Notice", "entities": [{"ref": {"screenName": "NASA", "text": "NASA"}}]}},
    "interstitial": {"displayType": "NonCompliant", "text": {"text": "Notice"}},
    "softIntervention": SOFT_INTERVENTION,
    "unmentionedUserIds": ["9876543210"],
    "viewState": "EnabledWithCount",
    "entities": ENTITIES,
    "scopes": {"followers": True},
    "media": [{"mediaUrl": "https://example.com/photo.jpg", "type": "photo", "url": "https://t.co/photo"}],
    "author": AUTHOR,
    "parentTweet": {**NESTED, "extra": {"source": "parent"}},
    "quoted_tweet": {**NESTED, "extra": {"source": "quote"}},
    "retweeted_tweet": {**NESTED, "extra": {"source": "repost"}},
}
PARSERS = [
    pytest.param(construct_type_unchecked, id="loose"),
    pytest.param(validate_type, id="strict"),
]
NESTED_PATHS = [
    path for depth in range(4) for path in product(("parent_tweet", "quoted_tweet", "retweeted_tweet"), repeat=depth)
]


@pytest.mark.parametrize("parse", PARSERS)
@pytest.mark.parametrize("path", NESTED_PATHS)
@pytest.mark.parametrize("unknown_counts", [None, ["bookmarkCount", "viewCount"], ["futureCount"]])
def test_replies_read_unknown_counts_on_posts_and_embedded_posts(
    parse: Callable[..., Any], path: tuple[str, ...], unknown_counts: list[str] | None
) -> None:
    post: dict[str, object] = {**POST, "bookmarkCount": 0, "viewCount": 0}
    if unknown_counts is not None:
        post["unknownCounts"] = unknown_counts
    value: object = post
    for field in reversed(path):
        nested: dict[str, object] = {**post}
        nested["parentTweet" if field == "parent_tweet" else field] = value
        value = nested
    response = cast(
        TweetGetRepliesResponse,
        parse(
            type_=TweetGetRepliesResponse,
            value={"tweets": [{**post, "retweeted_tweet": value}], "has_next_page": False, "next_cursor": ""},
        ),
    )
    tweets = response.tweets
    assert tweets is not None
    tweet = tweets[0]
    assert tweet.unknown_counts == unknown_counts
    assert tweet.bookmark_count == 0
    assert tweet.view_count == 0
    embedded = tweet.retweeted_tweet
    assert isinstance(embedded, EmbeddedTweet)
    assert embedded.unknown_counts == unknown_counts
    for field in path:
        embedded = getattr(embedded, field)

    assert embedded.unknown_counts == unknown_counts
    assert embedded.bookmark_count == 0
    assert embedded.view_count == 0


@pytest.mark.parametrize("parse", PARSERS)
@pytest.mark.parametrize("field", ["parentTweet", "quoted_tweet", "retweeted_tweet"])
def test_replies_read_fully_populated_embedded_posts(parse: Callable[..., Any], field: str) -> None:
    response = cast(
        TweetGetRepliesResponse,
        parse(
            type_=TweetGetRepliesResponse,
            value={"tweets": [{**POST, field: EMBEDDED}], "has_next_page": False, "next_cursor": ""},
        ),
    )
    tweets = response.tweets
    assert tweets is not None
    tweet = tweets[0]
    embedded: object = tweet.parent_tweet if field == "parentTweet" else getattr(tweet, field)
    assert isinstance(embedded, EmbeddedTweet)
    assert (embedded.id, embedded.text, embedded.like_count, embedded.view_count) == (
        "1234567890",
        "Just launched!",
        42,
        1500,
    )
    assert embedded.created_at == "2025-01-15T12:00:00Z"
    assert embedded.retweeted_at == datetime(2026, 9, 11, 20, 24, 45, tzinfo=timezone.utc)
    assert isinstance(embedded.author, UserProfile)
    assert (embedded.author.username, embedded.author.followers) == ("NASA", 92376187)
    assert embedded.author_unavailable is not None
    assert embedded.author_unavailable.reason == "Suspended"
    assert embedded.cashtag_attachments is not None
    assert embedded.cashtag_attachments[0].cashtag == "$TSLA"
    assert embedded.cashtag_attachments[0].start_time == datetime(2026, 10, 9, 13, 30, tzinfo=timezone.utc)
    assert embedded.community_name == "Build in Public"
    assert embedded.coordinates is not None
    assert embedded.coordinates.coordinates == [28.97, 41.01]
    assert embedded.geo is not None
    assert embedded.geo.coordinates == [41.01, 28.97]
    assert embedded.exclusive_content is not None
    assert embedded.exclusive_content.creator_user_name == "NASA"
    assert embedded.grok_translated_post == {"text": "Launched", "lang": "en"}
    assert embedded.has_community_notes is True
    assert embedded.interstitial is not None
    assert embedded.interstitial.text is not None
    assert embedded.interstitial.text.text == "Notice"
    assert (embedded.is_pinned, embedded.is_retweet) == (True, True)
    assert embedded.quoted_tweet_permalink is not None
    assert embedded.quoted_tweet_permalink.url == "https://t.co/quoted"
    assert embedded.quoted_tweet_unavailable is not None
    assert embedded.quoted_tweet_unavailable.reason == "Suspended"
    assert embedded.subscriber_badge is not None
    assert embedded.subscriber_badge.creator_id == "11348282"
    assert embedded.text_highlights is not None
    assert (embedded.text_highlights[0].start_index, embedded.text_highlights[0].end_index) == (5, 13)
    assert embedded.unavailable_author_id == "9876543210"
    assert embedded.conversation_control is not None
    assert embedded.conversation_control.allowed_country_codes == ["TR"]
    assert embedded.entities is not None
    assert embedded.entities.hashtags is not None
    assert embedded.entities.hashtags[0].tag is not None
    assert embedded.entities.hashtags[0].tag.id == "TSLA"
    assert embedded.note_tweet is not None
    assert embedded.note_tweet.note_id == "note-1"
    assert embedded.sports_context is not None
    assert embedded.sports_context.league == "league-1"
    assert isinstance(embedded.parent_tweet, QuotedTweet)
    assert isinstance(embedded.quoted_tweet, QuotedTweet)
    assert isinstance(embedded.retweeted_tweet, RetweetedTweet)
    for nested in (embedded.parent_tweet, embedded.quoted_tweet, embedded.retweeted_tweet):
        assert nested.text == "Just launched!"
        assert nested.community_name == "Build in Public"
        assert isinstance(nested.author, UserProfile)
        assert nested.author.username == "NASA"
        assert nested.entities is not None
        assert nested.entities.hashtags is not None
        assert nested.entities.hashtags[0].tag is not None
        assert nested.entities.hashtags[0].tag.id == "TSLA"


@pytest.mark.parametrize("parse", PARSERS)
@pytest.mark.parametrize("path", NESTED_PATHS)
def test_nested_posts_keep_typed_fields_at_every_depth(parse: Callable[..., Any], path: tuple[str, ...]) -> None:
    value: object = EMBEDDED
    for field in reversed(path):
        nested: dict[str, object] = {**POST}
        nested["parentTweet" if field == "parent_tweet" else field] = value
        value = nested
    embedded = parse(type_=EmbeddedTweet, value=value)
    for field in path:
        embedded = getattr(embedded, field)

    assert embedded.text == "Just launched!"
    assert isinstance(embedded.author, UserProfile)
    assert embedded.author.username == "NASA"
    assert embedded.author_unavailable.reason == "Suspended"
    assert embedded.cashtag_attachments[0].cashtag == "$TSLA"
    assert embedded.community_name == "Build in Public"
    assert embedded.coordinates.coordinates == [28.97, 41.01]
    assert embedded.exclusive_content.creator_user_name == "NASA"
    assert embedded.geo.coordinates == [41.01, 28.97]
    assert embedded.grok_translated_post == {"text": "Launched", "lang": "en"}
    assert embedded.has_community_notes is True
    assert embedded.interstitial.text.text == "Notice"
    assert embedded.is_pinned is True
    assert embedded.is_retweet is True
    assert embedded.quoted_tweet_permalink.url == "https://t.co/quoted"
    assert embedded.quoted_tweet_unavailable.reason == "Suspended"
    assert embedded.subscriber_badge.creator_id == "11348282"
    assert embedded.text_highlights[0].start_index == 5
    assert embedded.unavailable_author_id == "9876543210"
    assert embedded.conversation_control.allowed_country_codes == ["TR"]
    assert embedded.entities.hashtags[0].tag.info.info.active is True
    assert embedded.note_tweet.note_id == "note-1"
    assert embedded.note_tweet.entities.hashtags[0].tag.id == "TSLA"
    assert embedded.sports_context.league == "league-1"
    assert embedded.sports_context.competitors[0].color == "ffffff"
    assert embedded.tombstone.text.entities[0].ref.screen_name == "NASA"
    assert embedded.soft_intervention.display_type == "Fosnr"
    assert embedded.soft_intervention.engagement_nudge is True
    assert embedded.soft_intervention.text.entities[0].to_index == 29
    assert embedded.soft_intervention.text.entities[0].ref.url == "https://help.x.com/rules"
    assert embedded.soft_intervention.url.url_type == "ExternalUrl"


@pytest.mark.parametrize("parse", PARSERS)
@pytest.mark.parametrize("path", NESTED_PATHS)
def test_embedded_posts_parse_without_added_fields(parse: Callable[..., Any], path: tuple[str, ...]) -> None:
    value: object = POST
    for field in reversed(path):
        nested: dict[str, object] = {**POST}
        nested["parentTweet" if field == "parent_tweet" else field] = value
        value = nested
    embedded = parse(type_=EmbeddedTweet, value=value)
    for field in path:
        embedded = getattr(embedded, field)

    assert embedded.text == "Just launched!"
    assert embedded.author is None
    assert embedded.author_unavailable is None
    assert embedded.cashtag_attachments is None
    assert embedded.community_name is None
    assert embedded.coordinates is None
    assert embedded.exclusive_content is None
    assert embedded.geo is None
    assert embedded.grok_translated_post is None
    assert embedded.has_community_notes is None
    assert embedded.interstitial is None
    assert embedded.soft_intervention is None
    assert embedded.is_pinned is None
    assert embedded.is_retweet is None
    if len(path) < 3:
        assert embedded.parent_tweet is None
    assert embedded.quoted_tweet_permalink is None
    assert embedded.quoted_tweet_unavailable is None
    assert embedded.subscriber_badge is None
    assert embedded.text_highlights is None
    assert embedded.unavailable_author_id is None
