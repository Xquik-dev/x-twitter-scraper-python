# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .tweet_author import TweetAuthor
from ..shared.tweet_media import TweetMedia
from ..shared.content_disclosure import ContentDisclosure

__all__ = [
    "TweetDetail",
    "Article",
    "Card",
    "CommunityNote",
    "Edit",
    "NoteTweet",
    "NoteTweetRichtextTag",
    "Place",
    "PreviousCounts",
]


class Article(BaseModel):
    """Article metadata attached to a tweet."""

    id: Optional[str] = None

    cover_media_url: Optional[str] = FieldInfo(alias="coverMediaUrl", default=None)

    preview_text: Optional[str] = FieldInfo(alias="previewText", default=None)

    title: Optional[str] = None


class Card(BaseModel):
    """Public card metadata attached to a tweet."""

    id: Optional[str] = None

    binding_values: Optional[Dict[str, object]] = FieldInfo(alias="bindingValues", default=None)

    name: Optional[str] = None

    url: Optional[str] = None


class CommunityNote(BaseModel):
    """Community Note presentation metadata returned by X."""

    id: Optional[str] = None

    destination_url: Optional[str] = FieldInfo(alias="destinationUrl", default=None)

    footer: Optional[str] = None

    short_title: Optional[str] = FieldInfo(alias="shortTitle", default=None)

    subtitle: Optional[str] = None

    title: Optional[str] = None

    visual_style: Optional[str] = FieldInfo(alias="visualStyle", default=None)


class Edit(BaseModel):
    """Edit history metadata returned by X."""

    editable_until_msecs: Optional[str] = FieldInfo(alias="editableUntilMsecs", default=None)

    edit_tweet_ids: Optional[List[str]] = FieldInfo(alias="editTweetIds", default=None)


class NoteTweetRichtextTag(BaseModel):
    from_index: int = FieldInfo(alias="fromIndex")

    to_index: int = FieldInfo(alias="toIndex")

    types: List[str]


class NoteTweet(BaseModel):
    """Complete Note Tweet content and rich-text metadata."""

    text: str

    id: Optional[str] = None

    entities: Optional[Dict[str, object]] = None

    is_expandable: Optional[bool] = FieldInfo(alias="isExpandable", default=None)

    richtext_tags: Optional[List[NoteTweetRichtextTag]] = FieldInfo(alias="richtextTags", default=None)


class Place(BaseModel):
    """Public place metadata attached to a tweet."""

    id: Optional[str] = None

    bounding_box: Optional[Dict[str, object]] = FieldInfo(alias="boundingBox", default=None)

    country: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)

    name: Optional[str] = None

    place_type: Optional[str] = FieldInfo(alias="placeType", default=None)

    url: Optional[str] = None


class PreviousCounts(BaseModel):
    """Engagement counts retained from a prior tweet edit."""

    bookmark_count: Optional[int] = FieldInfo(alias="bookmarkCount", default=None)

    like_count: Optional[int] = FieldInfo(alias="likeCount", default=None)

    quote_count: Optional[int] = FieldInfo(alias="quoteCount", default=None)

    reply_count: Optional[int] = FieldInfo(alias="replyCount", default=None)

    retweet_count: Optional[int] = FieldInfo(alias="retweetCount", default=None)


class TweetDetail(BaseModel):
    """Full tweet with text, engagement metrics, media, and metadata.

    A zero metric can mean X did not report the count.
    """

    id: str

    bookmark_count: int = FieldInfo(alias="bookmarkCount")

    like_count: int = FieldInfo(alias="likeCount")

    quote_count: int = FieldInfo(alias="quoteCount")

    reply_count: int = FieldInfo(alias="replyCount")

    retweet_count: int = FieldInfo(alias="retweetCount")

    text: str

    view_count: int = FieldInfo(alias="viewCount")

    article: Optional[Article] = None
    """Article metadata attached to a tweet."""

    author: Optional[TweetAuthor] = None
    """Tweet author profile.

    The lookup route always includes follower count and verification state. Other
    profile fields appear when available.
    """

    card: Optional[Card] = None
    """Public card metadata attached to a tweet."""

    community_note: Optional[CommunityNote] = FieldInfo(alias="communityNote", default=None)
    """Community Note presentation metadata returned by X."""

    content_disclosure: Optional[ContentDisclosure] = FieldInfo(alias="contentDisclosure", default=None)
    """
    Content disclosure metadata shown by X when a tweet is labeled as paid
    partnership content or AI-generated media.
    """

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)
    """ID of the root tweet in the conversation thread"""

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    display_text_range: Optional[List[int]] = FieldInfo(alias="displayTextRange", default=None)
    """Start and end offsets for rendered tweet text"""

    edit: Optional[Edit] = None
    """Edit history metadata returned by X."""

    entities: Optional[Dict[str, object]] = None
    """Parsed entities from the tweet text (URLs, mentions, hashtags, media)"""

    in_reply_to_id: Optional[str] = FieldInfo(alias="inReplyToId", default=None)
    """Tweet ID being replied to"""

    in_reply_to_user_id: Optional[str] = FieldInfo(alias="inReplyToUserId", default=None)
    """User ID being replied to"""

    in_reply_to_username: Optional[str] = FieldInfo(alias="inReplyToUsername", default=None)
    """Username being replied to"""

    is_limited_reply: Optional[bool] = FieldInfo(alias="isLimitedReply", default=None)
    """Whether replies are limited for this tweet"""

    is_note_tweet: Optional[bool] = FieldInfo(alias="isNoteTweet", default=None)
    """Whether this is a Note Tweet (long-form post, up to 25,000 characters)"""

    is_quote_status: Optional[bool] = FieldInfo(alias="isQuoteStatus", default=None)
    """Whether this tweet quotes another tweet"""

    is_reply: Optional[bool] = FieldInfo(alias="isReply", default=None)
    """Whether this tweet is a reply to another tweet"""

    is_translatable: Optional[bool] = FieldInfo(alias="isTranslatable", default=None)

    lang: Optional[str] = None
    """Tweet language code"""

    media: Optional[List[TweetMedia]] = None
    """Attached media items, omitted when the tweet has no media"""

    note_tweet: Optional[NoteTweet] = FieldInfo(alias="noteTweet", default=None)
    """Complete Note Tweet content and rich-text metadata."""

    place: Optional[Place] = None
    """Public place metadata attached to a tweet."""

    possibly_sensitive: Optional[bool] = FieldInfo(alias="possiblySensitive", default=None)

    previous_counts: Optional[PreviousCounts] = FieldInfo(alias="previousCounts", default=None)
    """Engagement counts retained from a prior tweet edit."""

    quoted_tweet: Optional["EmbeddedTweet"] = None
    """Quoted or retweeted tweet context.

    Every object includes id, text, and engagement metrics. A zero metric can mean X
    did not report the count. Author, media, and conversation fields appear when
    available.
    """

    retweeted_tweet: Optional["EmbeddedTweet"] = None
    """Quoted or retweeted tweet context.

    Every object includes id, text, and engagement metrics. A zero metric can mean X
    did not report the count. Author, media, and conversation fields appear when
    available.
    """

    source: Optional[str] = None
    """Client application used to post this tweet"""

    type: Optional[str] = None
    """Tweet result type"""

    url: Optional[str] = None
    """Tweet permalink URL"""

    view_state: Optional[str] = FieldInfo(alias="viewState", default=None)


from ..shared.embedded_tweet import EmbeddedTweet
