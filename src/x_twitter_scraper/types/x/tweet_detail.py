# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .tweet_author import TweetAuthor
from ..shared.user_profile import UserProfile

__all__ = [
    "TweetDetail",
    "ContentDisclosure",
    "ContentDisclosureAdvertising",
    "ContentDisclosureAIGenerated",
    "Media",
    "MediaVideoVariant",
    "QuotedTweet",
    "QuotedTweetContentDisclosure",
    "QuotedTweetContentDisclosureAdvertising",
    "QuotedTweetContentDisclosureAIGenerated",
    "QuotedTweetMedia",
    "QuotedTweetMediaVideoVariant",
    "RetweetedTweet",
    "RetweetedTweetContentDisclosure",
    "RetweetedTweetContentDisclosureAdvertising",
    "RetweetedTweetContentDisclosureAIGenerated",
    "RetweetedTweetMedia",
    "RetweetedTweetMediaVideoVariant",
]


class ContentDisclosureAdvertising(BaseModel):
    is_paid_promotion: Optional[bool] = FieldInfo(alias="isPaidPromotion", default=None)
    """True when X labels the tweet as paid promotion content."""


class ContentDisclosureAIGenerated(BaseModel):
    can_edit: Optional[bool] = FieldInfo(alias="canEdit", default=None)
    """Whether the disclosure can be edited on X."""

    detection_source: Optional[str] = FieldInfo(alias="detectionSource", default=None)
    """Source of the AI-generated media disclosure."""

    has_ai_generated_media: Optional[bool] = FieldInfo(alias="hasAiGeneratedMedia", default=None)
    """True when X labels the tweet as containing AI-generated media."""


class ContentDisclosure(BaseModel):
    """
    Content disclosure metadata shown by X when a tweet is labeled as paid partnership content or AI-generated media.
    """

    advertising: Optional[ContentDisclosureAdvertising] = None

    ai_generated: Optional[ContentDisclosureAIGenerated] = FieldInfo(alias="aiGenerated", default=None)


class MediaVideoVariant(BaseModel):
    content_type: str = FieldInfo(alias="contentType")

    url: str

    bitrate: Optional[int] = None


class Media(BaseModel):
    """Normalized media attached to a tweet."""

    media_url: str = FieldInfo(alias="mediaUrl")
    """Media preview URL"""

    type: Literal["photo", "video", "animated_gif"]

    url: str
    """X media link from the tweet"""

    video_variants: Optional[List[MediaVideoVariant]] = FieldInfo(alias="videoVariants", default=None)
    """Available video encodings, ordered as returned"""


class QuotedTweetContentDisclosureAdvertising(BaseModel):
    is_paid_promotion: Optional[bool] = FieldInfo(alias="isPaidPromotion", default=None)
    """True when X labels the tweet as paid promotion content."""


class QuotedTweetContentDisclosureAIGenerated(BaseModel):
    can_edit: Optional[bool] = FieldInfo(alias="canEdit", default=None)
    """Whether the disclosure can be edited on X."""

    detection_source: Optional[str] = FieldInfo(alias="detectionSource", default=None)
    """Source of the AI-generated media disclosure."""

    has_ai_generated_media: Optional[bool] = FieldInfo(alias="hasAiGeneratedMedia", default=None)
    """True when X labels the tweet as containing AI-generated media."""


class QuotedTweetContentDisclosure(BaseModel):
    """
    Content disclosure metadata shown by X when a tweet is labeled as paid partnership content or AI-generated media.
    """

    advertising: Optional[QuotedTweetContentDisclosureAdvertising] = None

    ai_generated: Optional[QuotedTweetContentDisclosureAIGenerated] = FieldInfo(alias="aiGenerated", default=None)


class QuotedTweetMediaVideoVariant(BaseModel):
    content_type: str = FieldInfo(alias="contentType")

    url: str

    bitrate: Optional[int] = None


class QuotedTweetMedia(BaseModel):
    """Normalized media attached to a tweet."""

    media_url: str = FieldInfo(alias="mediaUrl")
    """Media preview URL"""

    type: Literal["photo", "video", "animated_gif"]

    url: str
    """X media link from the tweet"""

    video_variants: Optional[List[QuotedTweetMediaVideoVariant]] = FieldInfo(alias="videoVariants", default=None)
    """Available video encodings, ordered as returned"""


class QuotedTweet(BaseModel):
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

    content_disclosure: Optional[QuotedTweetContentDisclosure] = FieldInfo(alias="contentDisclosure", default=None)
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

    media: Optional[List[QuotedTweetMedia]] = None

    source: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None


class RetweetedTweetContentDisclosureAdvertising(BaseModel):
    is_paid_promotion: Optional[bool] = FieldInfo(alias="isPaidPromotion", default=None)
    """True when X labels the tweet as paid promotion content."""


class RetweetedTweetContentDisclosureAIGenerated(BaseModel):
    can_edit: Optional[bool] = FieldInfo(alias="canEdit", default=None)
    """Whether the disclosure can be edited on X."""

    detection_source: Optional[str] = FieldInfo(alias="detectionSource", default=None)
    """Source of the AI-generated media disclosure."""

    has_ai_generated_media: Optional[bool] = FieldInfo(alias="hasAiGeneratedMedia", default=None)
    """True when X labels the tweet as containing AI-generated media."""


class RetweetedTweetContentDisclosure(BaseModel):
    """
    Content disclosure metadata shown by X when a tweet is labeled as paid partnership content or AI-generated media.
    """

    advertising: Optional[RetweetedTweetContentDisclosureAdvertising] = None

    ai_generated: Optional[RetweetedTweetContentDisclosureAIGenerated] = FieldInfo(alias="aiGenerated", default=None)


class RetweetedTweetMediaVideoVariant(BaseModel):
    content_type: str = FieldInfo(alias="contentType")

    url: str

    bitrate: Optional[int] = None


class RetweetedTweetMedia(BaseModel):
    """Normalized media attached to a tweet."""

    media_url: str = FieldInfo(alias="mediaUrl")
    """Media preview URL"""

    type: Literal["photo", "video", "animated_gif"]

    url: str
    """X media link from the tweet"""

    video_variants: Optional[List[RetweetedTweetMediaVideoVariant]] = FieldInfo(alias="videoVariants", default=None)
    """Available video encodings, ordered as returned"""


class RetweetedTweet(BaseModel):
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

    content_disclosure: Optional[RetweetedTweetContentDisclosure] = FieldInfo(alias="contentDisclosure", default=None)
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

    media: Optional[List[RetweetedTweetMedia]] = None

    source: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None


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

    media: Optional[List[Media]] = None
    """Attached media items, omitted when the tweet has no media"""

    quoted_tweet: Optional[QuotedTweet] = None
    """Quoted or retweeted tweet context.

    Every object includes id, text, and engagement metrics. A zero metric can mean X
    did not report the count. Author, media, and conversation fields appear when
    available.
    """

    retweeted_tweet: Optional[RetweetedTweet] = None
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
