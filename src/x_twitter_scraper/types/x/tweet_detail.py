# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .tweet_author import TweetAuthor
from ..shared.tweet_media import TweetMedia
from ..shared.embedded_tweet import EmbeddedTweet
from ..shared.content_disclosure import ContentDisclosure

__all__ = ["TweetDetail"]


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

    author: Optional[TweetAuthor] = None
    """Tweet author profile.

    The lookup route always includes follower count and verification state. Other
    profile fields appear when available.
    """

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

    lang: Optional[str] = None
    """Tweet language code"""

    media: Optional[List[TweetMedia]] = None
    """Attached media items, omitted when the tweet has no media"""

    quoted_tweet: Optional[EmbeddedTweet] = None
    """Quoted or retweeted tweet context.

    Every object includes id, text, and engagement metrics. A zero metric can mean X
    did not report the count. Author, media, and conversation fields appear when
    available.
    """

    retweeted_tweet: Optional[EmbeddedTweet] = None
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
