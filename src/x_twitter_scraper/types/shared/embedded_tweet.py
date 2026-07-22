# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .tweet_media import TweetMedia
from .user_profile import UserProfile
from .content_disclosure import ContentDisclosure

__all__ = ["EmbeddedTweet"]


class EmbeddedTweet(BaseModel):
    """Quoted or retweeted tweet context.

    Every object includes id, text, and engagement metrics. A zero metric can mean X did not report the count. Author, media, and conversation fields appear when available.
    """

    id: str

    bookmark_count: int = FieldInfo(alias="bookmarkCount")

    like_count: int = FieldInfo(alias="likeCount")

    quote_count: int = FieldInfo(alias="quoteCount")

    reply_count: int = FieldInfo(alias="replyCount")

    retweet_count: int = FieldInfo(alias="retweetCount")

    text: str

    view_count: int = FieldInfo(alias="viewCount")

    author: Optional[UserProfile] = None
    """X user profile with bio, follower counts, and verification status."""

    content_disclosure: Optional[ContentDisclosure] = FieldInfo(alias="contentDisclosure", default=None)
    """
    Content disclosure metadata shown by X when a tweet is labeled as paid
    partnership content or AI-generated media.
    """

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    display_text_range: Optional[List[int]] = FieldInfo(alias="displayTextRange", default=None)

    entities: Optional[Dict[str, object]] = None

    in_reply_to_id: Optional[str] = FieldInfo(alias="inReplyToId", default=None)

    in_reply_to_user_id: Optional[str] = FieldInfo(alias="inReplyToUserId", default=None)

    in_reply_to_username: Optional[str] = FieldInfo(alias="inReplyToUsername", default=None)

    is_limited_reply: Optional[bool] = FieldInfo(alias="isLimitedReply", default=None)

    is_note_tweet: Optional[bool] = FieldInfo(alias="isNoteTweet", default=None)

    is_quote_status: Optional[bool] = FieldInfo(alias="isQuoteStatus", default=None)

    is_reply: Optional[bool] = FieldInfo(alias="isReply", default=None)

    lang: Optional[str] = None

    media: Optional[List[TweetMedia]] = None

    source: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None
