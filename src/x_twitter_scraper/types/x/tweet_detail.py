# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TweetDetail", "Media"]


class Media(BaseModel):
    media_url: Optional[str] = FieldInfo(alias="mediaUrl", default=None)

    type: Optional[Literal["photo", "video", "animated_gif"]] = None

    url: Optional[str] = None


class TweetDetail(BaseModel):
    """Full tweet with text, engagement metrics, media, and metadata."""

    id: str

    bookmark_count: int = FieldInfo(alias="bookmarkCount")

    like_count: int = FieldInfo(alias="likeCount")

    quote_count: int = FieldInfo(alias="quoteCount")

    reply_count: int = FieldInfo(alias="replyCount")

    retweet_count: int = FieldInfo(alias="retweetCount")

    text: str

    view_count: int = FieldInfo(alias="viewCount")

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)
    """ID of the root tweet in the conversation thread"""

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    entities: Optional[Dict[str, object]] = None
    """Parsed entities from the tweet text (URLs, mentions, hashtags, media)"""

    is_note_tweet: Optional[bool] = FieldInfo(alias="isNoteTweet", default=None)
    """Whether this is a Note Tweet (long-form post, up to 25,000 characters)"""

    is_quote_status: Optional[bool] = FieldInfo(alias="isQuoteStatus", default=None)
    """Whether this tweet quotes another tweet"""

    is_reply: Optional[bool] = FieldInfo(alias="isReply", default=None)
    """Whether this tweet is a reply to another tweet"""

    media: Optional[List[Media]] = None
    """Attached media items, omitted when the tweet has no media"""

    quoted_tweet: Optional[Dict[str, object]] = None
    """The quoted tweet object, present when isQuoteStatus is true"""

    source: Optional[str] = None
    """Client application used to post this tweet"""
