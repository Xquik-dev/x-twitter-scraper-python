# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .tweet_media import TweetMedia
from .user_profile import UserProfile
from .embedded_tweet import EmbeddedTweet
from .content_disclosure import ContentDisclosure

__all__ = ["SearchTweet"]


class SearchTweet(BaseModel):
    """Tweet returned from search results with inline author info.

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

    author: Optional[UserProfile] = None
    """X user profile with bio, follower counts, and verification status."""

    content_disclosure: Optional[ContentDisclosure] = FieldInfo(alias="contentDisclosure", default=None)
    """
    Content disclosure metadata shown by X when a tweet is labeled as paid
    partnership content or AI-generated media.
    """

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)
    """Root tweet ID for the search result conversation"""

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    display_text_range: Optional[List[int]] = FieldInfo(alias="displayTextRange", default=None)
    """Rendered text's start and end offsets."""

    entities: Optional[Dict[str, object]] = None
    """
    Parsed search-result entities including URLs, mentions, hashtags, and media
    markers
    """

    in_reply_to_id: Optional[str] = FieldInfo(alias="inReplyToId", default=None)
    """ID of the tweet this result replies to."""

    in_reply_to_user_id: Optional[str] = FieldInfo(alias="inReplyToUserId", default=None)
    """ID of the user this result replies to."""

    in_reply_to_username: Optional[str] = FieldInfo(alias="inReplyToUsername", default=None)
    """Username this result replies to."""

    is_limited_reply: Optional[bool] = FieldInfo(alias="isLimitedReply", default=None)
    """Whether the tweet has limited reply permissions"""

    is_note_tweet: Optional[bool] = FieldInfo(alias="isNoteTweet", default=None)
    """True for Note Tweets (long-form content, up to 25,000 characters)"""

    is_quote_status: Optional[bool] = FieldInfo(alias="isQuoteStatus", default=None)
    """True when this search result quotes another tweet"""

    is_reply: Optional[bool] = FieldInfo(alias="isReply", default=None)
    """True when this search result is a reply"""

    lang: Optional[str] = None
    """Search result language code."""

    media: Optional[List[TweetMedia]] = None
    """Search-result media attachments, omitted when no media is present"""

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
    """Client application used to post the tweet"""

    type: Optional[str] = None

    url: Optional[str] = None
    """Search result permalink."""
