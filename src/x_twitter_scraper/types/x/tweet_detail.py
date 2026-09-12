# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .tweet_author import TweetAuthor
from ..shared.tweet_media import TweetMedia
from ..shared.user_profile import UserProfile
from ..shared.embedded_tweet import EmbeddedTweet
from ..shared.content_disclosure import ContentDisclosure

__all__ = [
    "TweetDetail",
    "Article",
    "Card",
    "CardUserReferenceError",
    "CommunityNote",
    "ConversationControl",
    "Edit",
    "Entities",
    "EntitiesHashtag",
    "EntitiesSmarttag",
    "EntitiesSmarttagTag",
    "EntitiesSmarttagTagInfo",
    "EntitiesSmarttagTagInfoInfo",
    "EntitiesSymbol",
    "EntitiesSymbolTag",
    "EntitiesSymbolTagInfo",
    "EntitiesSymbolTagInfoInfo",
    "EntitiesTimestamp",
    "EntitiesTimestampTag",
    "EntitiesTimestampTagInfo",
    "EntitiesTimestampTagInfoInfo",
    "EntitiesURL",
    "EntitiesUserMention",
    "LimitedAction",
    "LimitedActionPrompt",
    "NoteTweet",
    "NoteTweetEntities",
    "NoteTweetEntitiesHashtag",
    "NoteTweetEntitiesSmarttag",
    "NoteTweetEntitiesSmarttagTag",
    "NoteTweetEntitiesSmarttagTagInfo",
    "NoteTweetEntitiesSmarttagTagInfoInfo",
    "NoteTweetEntitiesSymbol",
    "NoteTweetEntitiesSymbolTag",
    "NoteTweetEntitiesSymbolTagInfo",
    "NoteTweetEntitiesSymbolTagInfoInfo",
    "NoteTweetEntitiesTimestamp",
    "NoteTweetEntitiesTimestampTag",
    "NoteTweetEntitiesTimestampTagInfo",
    "NoteTweetEntitiesTimestampTagInfoInfo",
    "NoteTweetEntitiesURL",
    "NoteTweetEntitiesUserMention",
    "NoteTweetInlineMedia",
    "NoteTweetRichtextTag",
    "Place",
    "PreviousCounts",
    "ReactionContext",
    "SportsContext",
    "SportsContextCompetitor",
    "Tombstone",
    "TombstoneText",
    "TombstoneTextEntity",
    "TombstoneTextEntityRef",
]


class Article(BaseModel):
    """Describes an X Article preview and its lifecycle metadata."""

    id: Optional[str] = None

    cover_media: Optional[Dict[str, object]] = FieldInfo(alias="coverMedia", default=None)
    """Public metadata whose fields are defined by X."""

    cover_media_url: Optional[str] = FieldInfo(alias="coverMediaUrl", default=None)

    lifecycle_state: Optional[Dict[str, object]] = FieldInfo(alias="lifecycleState", default=None)
    """Public metadata whose fields are defined by X."""

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    preview_text: Optional[str] = FieldInfo(alias="previewText", default=None)

    title: Optional[str] = None


class CardUserReferenceError(BaseModel):
    message: Optional[str] = None

    reason: Optional[str] = None


class Card(BaseModel):
    """Describes a public card and its referenced profiles."""

    id: Optional[str] = None

    binding_values: Optional[Dict[str, object]] = FieldInfo(alias="bindingValues", default=None)
    """Public metadata whose fields are defined by X."""

    name: Optional[str] = None

    platform: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    url: Optional[str] = None

    user_reference_errors: Optional[List[CardUserReferenceError]] = FieldInfo(alias="userReferenceErrors", default=None)
    """Unresolved card user references."""

    user_references: Optional[List[UserProfile]] = FieldInfo(alias="userReferences", default=None)


class CommunityNote(BaseModel):
    """Community Note presentation metadata returned by X."""

    id: Optional[str] = None

    destination_url: Optional[str] = FieldInfo(alias="destinationUrl", default=None)

    footer: Optional[str] = None

    footer_icon_type: Optional[str] = FieldInfo(alias="footerIconType", default=None)

    icon_type: Optional[str] = FieldInfo(alias="iconType", default=None)

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    short_title: Optional[str] = FieldInfo(alias="shortTitle", default=None)

    subtitle: Optional[str] = None

    title: Optional[str] = None

    visual_style: Optional[str] = FieldInfo(alias="visualStyle", default=None)


class ConversationControl(BaseModel):
    """Public reply policy and conversation owner."""

    invite_via_mention: Optional[bool] = FieldInfo(alias="inviteViaMention", default=None)

    owner_username: Optional[str] = FieldInfo(alias="ownerUsername", default=None)

    policy: Optional[str] = None


class Edit(BaseModel):
    """Lists edit-chain identifiers and the remaining edit window."""

    editable_until_msecs: Optional[str] = FieldInfo(alias="editableUntilMsecs", default=None)

    edit_tweet_ids: Optional[List[str]] = FieldInfo(alias="editTweetIds", default=None)

    initial_tweet_id: Optional[str] = FieldInfo(alias="initialTweetId", default=None)


class EntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None


class EntitiesSmarttagTagInfoInfo(BaseModel):
    name: Optional[str] = None

    ticker: Optional[str] = None


class EntitiesSmarttagTagInfo(BaseModel):
    info: Optional[EntitiesSmarttagTagInfoInfo] = None


class EntitiesSmarttagTag(BaseModel):
    info: Optional[EntitiesSmarttagTagInfo] = None


class EntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[EntitiesSmarttagTag] = None

    text: Optional[str] = None


class EntitiesSymbolTagInfoInfo(BaseModel):
    name: Optional[str] = None

    ticker: Optional[str] = None


class EntitiesSymbolTagInfo(BaseModel):
    info: Optional[EntitiesSymbolTagInfoInfo] = None


class EntitiesSymbolTag(BaseModel):
    info: Optional[EntitiesSymbolTagInfo] = None


class EntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[EntitiesSymbolTag] = None

    text: Optional[str] = None


class EntitiesTimestampTagInfoInfo(BaseModel):
    name: Optional[str] = None

    ticker: Optional[str] = None


class EntitiesTimestampTagInfo(BaseModel):
    info: Optional[EntitiesTimestampTagInfoInfo] = None


class EntitiesTimestampTag(BaseModel):
    info: Optional[EntitiesTimestampTagInfo] = None


class EntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[EntitiesTimestampTag] = None

    text: Optional[str] = None


class EntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class EntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class Entities(BaseModel):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[EntitiesHashtag]] = None

    smarttags: Optional[List[EntitiesSmarttag]] = None

    symbols: Optional[List[EntitiesSymbol]] = None

    timestamps: Optional[List[EntitiesTimestamp]] = None

    urls: Optional[List[EntitiesURL]] = None

    user_mentions: Optional[List[EntitiesUserMention]] = None


class LimitedActionPrompt(BaseModel):
    cta_type: Optional[str] = FieldInfo(alias="ctaType", default=None)

    headline: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    subtext: Optional[str] = None


class LimitedAction(BaseModel):
    action: Optional[str] = None

    prompt: Optional[LimitedActionPrompt] = None


class NoteTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None


class NoteTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    name: Optional[str] = None

    ticker: Optional[str] = None


class NoteTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[NoteTweetEntitiesSmarttagTagInfoInfo] = None


class NoteTweetEntitiesSmarttagTag(BaseModel):
    info: Optional[NoteTweetEntitiesSmarttagTagInfo] = None


class NoteTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[NoteTweetEntitiesSmarttagTag] = None

    text: Optional[str] = None


class NoteTweetEntitiesSymbolTagInfoInfo(BaseModel):
    name: Optional[str] = None

    ticker: Optional[str] = None


class NoteTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[NoteTweetEntitiesSymbolTagInfoInfo] = None


class NoteTweetEntitiesSymbolTag(BaseModel):
    info: Optional[NoteTweetEntitiesSymbolTagInfo] = None


class NoteTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[NoteTweetEntitiesSymbolTag] = None

    text: Optional[str] = None


class NoteTweetEntitiesTimestampTagInfoInfo(BaseModel):
    name: Optional[str] = None

    ticker: Optional[str] = None


class NoteTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[NoteTweetEntitiesTimestampTagInfoInfo] = None


class NoteTweetEntitiesTimestampTag(BaseModel):
    info: Optional[NoteTweetEntitiesTimestampTagInfo] = None


class NoteTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[NoteTweetEntitiesTimestampTag] = None

    text: Optional[str] = None


class NoteTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class NoteTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class NoteTweetEntities(BaseModel):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[NoteTweetEntitiesHashtag]] = None

    smarttags: Optional[List[NoteTweetEntitiesSmarttag]] = None

    symbols: Optional[List[NoteTweetEntitiesSymbol]] = None

    timestamps: Optional[List[NoteTweetEntitiesTimestamp]] = None

    urls: Optional[List[NoteTweetEntitiesURL]] = None

    user_mentions: Optional[List[NoteTweetEntitiesUserMention]] = None


class NoteTweetInlineMedia(BaseModel):
    index: int

    media_id: str = FieldInfo(alias="mediaId")


class NoteTweetRichtextTag(BaseModel):
    from_index: int = FieldInfo(alias="fromIndex")

    to_index: int = FieldInfo(alias="toIndex")

    types: List[str]


class NoteTweet(BaseModel):
    """Complete Note Tweet content and rich-text metadata."""

    text: str

    id: Optional[str] = None

    entities: Optional[NoteTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    inline_media: Optional[List[NoteTweetInlineMedia]] = FieldInfo(alias="inlineMedia", default=None)
    """Inline media positions in the Note Tweet text."""

    is_expandable: Optional[bool] = FieldInfo(alias="isExpandable", default=None)

    richtext_tags: Optional[List[NoteTweetRichtextTag]] = FieldInfo(alias="richtextTags", default=None)


class Place(BaseModel):
    """Describes public place metadata on a geotagged tweet."""

    id: Optional[str] = None

    bounding_box: Optional[Dict[str, object]] = FieldInfo(alias="boundingBox", default=None)
    """Public metadata whose fields are defined by X."""

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


class ReactionContext(BaseModel):
    """Public post and user referenced by this reaction."""

    reacted_to_post_id: Optional[str] = FieldInfo(alias="reactedToPostId", default=None)
    """Referenced post ID."""

    reacted_to_user: Optional[UserProfile] = FieldInfo(alias="reactedToUser", default=None)
    """Public X profile."""


class SportsContextCompetitor(BaseModel):
    abbreviation: Optional[str] = None
    """Team abbreviation."""

    dark_logo_url: Optional[str] = FieldInfo(alias="darkLogoUrl", default=None)
    """Team logo for dark backgrounds."""

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """Team logo for light backgrounds."""

    name: Optional[str] = None
    """Team name."""

    score: Optional[str] = None
    """Score display text."""

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)
    """Team ID."""


class SportsContext(BaseModel):
    """Sports game context attached to the post, when available."""

    competitors: Optional[List[SportsContextCompetitor]] = None
    """Teams and their reported scores."""

    game_id: Optional[str] = FieldInfo(alias="gameId", default=None)
    """Game ID."""

    scheduled_at_ms: Union[float, str, None] = FieldInfo(alias="scheduledAtMs", default=None)
    """Scheduled Unix time in milliseconds, preserving the source representation."""

    state: Optional[str] = None
    """Game state reported by the source."""

    status_text: Optional[str] = FieldInfo(alias="statusText", default=None)
    """Display text for game progress."""

    title: Optional[str] = None
    """Game title."""

    url: Optional[str] = None
    """Game link."""


class TombstoneTextEntityRef(BaseModel):
    type: Optional[str] = None

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)


class TombstoneTextEntity(BaseModel):
    from_index: Optional[int] = FieldInfo(alias="fromIndex", default=None)

    ref: Optional[TombstoneTextEntityRef] = None

    to_index: Optional[int] = FieldInfo(alias="toIndex", default=None)


class TombstoneText(BaseModel):
    entities: Optional[List[TombstoneTextEntity]] = None

    rtl: Optional[bool] = None
    """Right-to-left text direction."""

    text: Optional[str] = None
    """Human-readable notice text."""


class Tombstone(BaseModel):
    """Public visibility notice attached to an available tweet."""

    text: Optional[TombstoneText] = None

    type: Optional[str] = None
    """Visibility notice type."""


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
    """Describes an X Article preview and its lifecycle metadata."""

    author: Optional[TweetAuthor] = None
    """Tweet author profile.

    The lookup route always includes follower count and verification state. Other
    profile fields appear when available.
    """

    card: Optional[Card] = None
    """Describes a public card and its referenced profiles."""

    community_id: Optional[str] = FieldInfo(alias="communityId", default=None)
    """Community ID."""

    community_note: Optional[CommunityNote] = FieldInfo(alias="communityNote", default=None)
    """Community Note presentation metadata returned by X."""

    content_disclosure: Optional[ContentDisclosure] = FieldInfo(alias="contentDisclosure", default=None)
    """
    Content disclosure metadata shown by X when a tweet is labeled as paid
    partnership content or AI-generated media.
    """

    conversation_control: Optional[ConversationControl] = FieldInfo(alias="conversationControl", default=None)
    """Public reply policy and conversation owner."""

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    display_text_range: Optional[List[int]] = FieldInfo(alias="displayTextRange", default=None)

    edit: Optional[Edit] = None
    """Lists edit-chain identifiers and the remaining edit window."""

    entities: Optional[Entities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    grok_share_attachment: Optional[Dict[str, object]] = FieldInfo(alias="grokShareAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    in_reply_to_id: Optional[str] = FieldInfo(alias="inReplyToId", default=None)

    in_reply_to_user_id: Optional[str] = FieldInfo(alias="inReplyToUserId", default=None)

    in_reply_to_username: Optional[str] = FieldInfo(alias="inReplyToUsername", default=None)

    is_limited_reply: Optional[bool] = FieldInfo(alias="isLimitedReply", default=None)

    is_note_tweet: Optional[bool] = FieldInfo(alias="isNoteTweet", default=None)

    is_quote_status: Optional[bool] = FieldInfo(alias="isQuoteStatus", default=None)

    is_reply: Optional[bool] = FieldInfo(alias="isReply", default=None)

    is_translatable: Optional[bool] = FieldInfo(alias="isTranslatable", default=None)

    jetfuel_attachment: Optional[Dict[str, object]] = FieldInfo(alias="jetfuelAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    lang: Optional[str] = None

    limited_actions: Optional[List[LimitedAction]] = FieldInfo(alias="limitedActions", default=None)
    """Public interaction restrictions and user-facing prompts."""

    media: Optional[List[TweetMedia]] = None
    """Attached media items, omitted when unavailable."""

    note_tweet: Optional[NoteTweet] = FieldInfo(alias="noteTweet", default=None)
    """Complete Note Tweet content and rich-text metadata."""

    place: Optional[Place] = None
    """Describes public place metadata on a geotagged tweet."""

    possibly_sensitive: Optional[bool] = FieldInfo(alias="possiblySensitive", default=None)

    post_cta: Optional[Dict[str, object]] = FieldInfo(alias="postCta", default=None)
    """Public metadata whose fields are defined by X."""

    previous_counts: Optional[PreviousCounts] = FieldInfo(alias="previousCounts", default=None)
    """Engagement counts retained from a prior tweet edit."""

    quoted_tweet: Optional[EmbeddedTweet] = None
    """Quoted or retweeted tweet context."""

    quoted_tweet_id: Optional[str] = FieldInfo(alias="quotedTweetId", default=None)
    """Quoted tweet ID."""

    reaction_context: Optional[ReactionContext] = FieldInfo(alias="reactionContext", default=None)
    """Public post and user referenced by this reaction."""

    retweeted_tweet: Optional[EmbeddedTweet] = None
    """Quoted or retweeted tweet context."""

    retweeted_at: Optional[datetime] = FieldInfo(alias="retweetedAt", default=None)
    """Repost event time in UTC. Null when unavailable; omitted for other posts."""

    scopes: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    source: Optional[str] = None

    sports_context: Optional[SportsContext] = FieldInfo(alias="sportsContext", default=None)
    """Sports game context attached to the post, when available."""

    tombstone: Optional[Tombstone] = None
    """Public visibility notice attached to an available tweet."""

    type: Optional[str] = None

    unmentioned_user_ids: Optional[List[str]] = FieldInfo(alias="unmentionedUserIds", default=None)
    """User IDs that left this conversation."""

    url: Optional[str] = None

    view_state: Optional[str] = FieldInfo(alias="viewState", default=None)
