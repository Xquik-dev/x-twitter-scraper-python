# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .tweet_author import TweetAuthor
from ..._dict_access import TweetEntitiesDictAccess
from ..shared.tweet_media import TweetMedia
from ..shared.user_profile import UserProfile
from ..shared.embedded_tweet import EmbeddedTweet
from ..shared.content_disclosure import ContentDisclosure

__all__ = [
    "TweetDetail",
    "Article",
    "AuthorUnavailable",
    "Card",
    "CardUserReferenceError",
    "CashtagAttachment",
    "CommunityNote",
    "ConversationControl",
    "Coordinates",
    "Edit",
    "Entities",
    "EntitiesHashtag",
    "EntitiesHashtagTag",
    "EntitiesHashtagTagInfo",
    "EntitiesHashtagTagInfoInfo",
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
    "ExclusiveContent",
    "Geo",
    "Interstitial",
    "InterstitialText",
    "InterstitialTextEntity",
    "InterstitialTextEntityRef",
    "LimitedAction",
    "LimitedActionPrompt",
    "NoteTweet",
    "NoteTweetEntities",
    "NoteTweetEntitiesHashtag",
    "NoteTweetEntitiesHashtagTag",
    "NoteTweetEntitiesHashtagTagInfo",
    "NoteTweetEntitiesHashtagTagInfoInfo",
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
    "QuotedTweetPermalink",
    "QuotedTweetUnavailable",
    "ReactionContext",
    "SportsContext",
    "SportsContextCompetitor",
    "SubscriberBadge",
    "TextHighlight",
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


class AuthorUnavailable(BaseModel):
    """Why the tweet has no author.

    X serves a suspended or deleted account as an unavailable user with a reason such as Suspended or NotFound. Omitted when the author is available.
    """

    reason: str
    """X's reason code."""

    message: Optional[str] = None
    """X's notice text for the reason."""


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


class CashtagAttachment(BaseModel):
    cashtag: str
    """The cashtag with its `$`."""

    candle_size: Optional[str] = FieldInfo(alias="candleSize", default=None)
    """Span of each candle."""

    end_time: Optional[datetime] = FieldInfo(alias="endTime", default=None)
    """Time of the chart's last price."""

    size_variant: Optional[int] = FieldInfo(alias="sizeVariant", default=None)
    """X's size for the chart."""

    start_time: Optional[datetime] = FieldInfo(alias="startTime", default=None)
    """Time of the chart's first candle."""

    timeframe: Optional[str] = None
    """Span the chart covers."""


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
    """Reply policy & conversation owner."""

    allowed_country_codes: Optional[List[str]] = FieldInfo(alias="allowedCountryCodes", default=None)
    """Regions whose accounts may reply, as country codes.

    Sent with the `country_of_origin` mode.
    """

    invite_via_mention: Optional[bool] = FieldInfo(alias="inviteViaMention", default=None)

    mode: Optional[str] = None
    """
    Reply policy from X's newer field, such as `my_network`, `premium` or
    `country_of_origin`. Omitted when X sends none.
    """

    owner_id: Optional[str] = FieldInfo(alias="ownerId", default=None)
    """The conversation owner's account ID."""

    owner_username: Optional[str] = FieldInfo(alias="ownerUsername", default=None)

    policy: Optional[str] = None


class Coordinates(BaseModel):
    """Author-published point, with longitude before latitude."""

    coordinates: List[float]

    type: Literal["Point"]


class Edit(BaseModel):
    """Lists edit-chain identifiers and the remaining edit window."""

    editable_until_msecs: Optional[str] = FieldInfo(alias="editableUntilMsecs", default=None)

    edit_tweet_ids: Optional[List[str]] = FieldInfo(alias="editTweetIds", default=None)

    initial_tweet_id: Optional[str] = FieldInfo(alias="initialTweetId", default=None)


class EntitiesHashtagTagInfoInfo(BaseModel):
    active: Optional[bool] = None
    """Whether X marks the SmartTag active."""

    name: Optional[str] = None

    ticker: Optional[str] = None


class EntitiesHashtagTagInfo(BaseModel):
    info: Optional[EntitiesHashtagTagInfoInfo] = None


class EntitiesHashtagTag(BaseModel):
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    id: Optional[str] = None
    """X's ID for the SmartTag."""

    info: Optional[EntitiesHashtagTagInfo] = None


class EntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[EntitiesHashtagTag] = None
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """


class EntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None
    """Whether X marks the SmartTag active."""

    name: Optional[str] = None

    ticker: Optional[str] = None


class EntitiesSmarttagTagInfo(BaseModel):
    info: Optional[EntitiesSmarttagTagInfoInfo] = None


class EntitiesSmarttagTag(BaseModel):
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    id: Optional[str] = None
    """X's ID for the SmartTag."""

    info: Optional[EntitiesSmarttagTagInfo] = None


class EntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[EntitiesSmarttagTag] = None
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    text: Optional[str] = None


class EntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None
    """Whether X marks the SmartTag active."""

    name: Optional[str] = None

    ticker: Optional[str] = None


class EntitiesSymbolTagInfo(BaseModel):
    info: Optional[EntitiesSymbolTagInfoInfo] = None


class EntitiesSymbolTag(BaseModel):
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    id: Optional[str] = None
    """X's ID for the SmartTag."""

    info: Optional[EntitiesSymbolTagInfo] = None


class EntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[EntitiesSymbolTag] = None
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    text: Optional[str] = None


class EntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None
    """Whether X marks the SmartTag active."""

    name: Optional[str] = None

    ticker: Optional[str] = None


class EntitiesTimestampTagInfo(BaseModel):
    info: Optional[EntitiesTimestampTagInfoInfo] = None


class EntitiesTimestampTag(BaseModel):
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    id: Optional[str] = None
    """X's ID for the SmartTag."""

    info: Optional[EntitiesTimestampTagInfo] = None


class EntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[EntitiesTimestampTag] = None
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

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


class Entities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[EntitiesHashtag]] = None

    smarttags: Optional[List[EntitiesSmarttag]] = None

    symbols: Optional[List[EntitiesSymbol]] = None

    timestamps: Optional[List[EntitiesTimestamp]] = None

    urls: Optional[List[EntitiesURL]] = None

    user_mentions: Optional[List[EntitiesUserMention]] = None


class ExclusiveContent(BaseModel):
    """Marks a subscriber-only post with the creator whose subscription unlocks it.

    Non-subscribers get the preview text & the subscribe link. Omitted on public posts.
    """

    creator_user_name: str = FieldInfo(alias="creatorUserName")
    """Username of the creator whose subscription unlocks the post."""

    subscribe_url: Optional[str] = FieldInfo(alias="subscribeUrl", default=None)
    """Subscribe link X shows non-subscribers. Omitted when X serves the full post."""


class Geo(BaseModel):
    """Author-published point, with latitude before longitude."""

    coordinates: List[float]

    type: Literal["Point"]


class InterstitialTextEntityRef(BaseModel):
    screen_name: Optional[str] = FieldInfo(alias="screenName", default=None)

    text: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)


class InterstitialTextEntity(BaseModel):
    from_index: Optional[int] = FieldInfo(alias="fromIndex", default=None)
    """Whole number from 0."""

    ref: Optional[InterstitialTextEntityRef] = None

    to_index: Optional[int] = FieldInfo(alias="toIndex", default=None)
    """Whole number from 0."""


class InterstitialText(BaseModel):
    entities: Optional[List[InterstitialTextEntity]] = None
    """Links inside the notice, by character range."""

    rtl: Optional[bool] = None
    """Whether X writes it right to left."""

    text: Optional[str] = None
    """The notice's text."""


class Interstitial(BaseModel):
    """
    The notice x.com covers the post with until the reader views it, such as X's public interest notice on a post that broke its rules but stays up.
    """

    display_type: Optional[str] = FieldInfo(alias="displayType", default=None)
    """How x.com shows the notice. `NonCompliant` marks a post that broke X's rules."""

    text: Optional[InterstitialText] = None


class LimitedActionPrompt(BaseModel):
    cta_type: Optional[str] = FieldInfo(alias="ctaType", default=None)

    headline: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    subtext: Optional[str] = None


class LimitedAction(BaseModel):
    action: Optional[str] = None

    prompt: Optional[LimitedActionPrompt] = None


class NoteTweetEntitiesHashtagTagInfoInfo(BaseModel):
    active: Optional[bool] = None
    """Whether X marks the SmartTag active."""

    name: Optional[str] = None

    ticker: Optional[str] = None


class NoteTweetEntitiesHashtagTagInfo(BaseModel):
    info: Optional[NoteTweetEntitiesHashtagTagInfoInfo] = None


class NoteTweetEntitiesHashtagTag(BaseModel):
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    id: Optional[str] = None
    """X's ID for the SmartTag."""

    info: Optional[NoteTweetEntitiesHashtagTagInfo] = None


class NoteTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[NoteTweetEntitiesHashtagTag] = None
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """


class NoteTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None
    """Whether X marks the SmartTag active."""

    name: Optional[str] = None

    ticker: Optional[str] = None


class NoteTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[NoteTweetEntitiesSmarttagTagInfoInfo] = None


class NoteTweetEntitiesSmarttagTag(BaseModel):
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    id: Optional[str] = None
    """X's ID for the SmartTag."""

    info: Optional[NoteTweetEntitiesSmarttagTagInfo] = None


class NoteTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[NoteTweetEntitiesSmarttagTag] = None
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    text: Optional[str] = None


class NoteTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None
    """Whether X marks the SmartTag active."""

    name: Optional[str] = None

    ticker: Optional[str] = None


class NoteTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[NoteTweetEntitiesSymbolTagInfoInfo] = None


class NoteTweetEntitiesSymbolTag(BaseModel):
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    id: Optional[str] = None
    """X's ID for the SmartTag."""

    info: Optional[NoteTweetEntitiesSymbolTagInfo] = None


class NoteTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[NoteTweetEntitiesSymbolTag] = None
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    text: Optional[str] = None


class NoteTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None
    """Whether X marks the SmartTag active."""

    name: Optional[str] = None

    ticker: Optional[str] = None


class NoteTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[NoteTweetEntitiesTimestampTagInfoInfo] = None


class NoteTweetEntitiesTimestampTag(BaseModel):
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    id: Optional[str] = None
    """X's ID for the SmartTag."""

    info: Optional[NoteTweetEntitiesTimestampTagInfo] = None


class NoteTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[NoteTweetEntitiesTimestampTag] = None
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

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


class NoteTweetEntities(TweetEntitiesDictAccess):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[NoteTweetEntitiesHashtag]] = None

    smarttags: Optional[List[NoteTweetEntitiesSmarttag]] = None

    symbols: Optional[List[NoteTweetEntitiesSymbol]] = None

    timestamps: Optional[List[NoteTweetEntitiesTimestamp]] = None

    urls: Optional[List[NoteTweetEntitiesURL]] = None

    user_mentions: Optional[List[NoteTweetEntitiesUserMention]] = None


class NoteTweetInlineMedia(BaseModel):
    index: int
    """Whole number from 0."""

    media_id: str = FieldInfo(alias="mediaId")


class NoteTweetRichtextTag(BaseModel):
    from_index: int = FieldInfo(alias="fromIndex")
    """Whole number from 0."""

    to_index: int = FieldInfo(alias="toIndex")
    """Whole number from 0."""

    types: List[str]


class NoteTweet(BaseModel):
    """Complete Note Tweet content and rich-text metadata."""

    text: str

    id: Optional[str] = None
    """X's global ID of the Note, base64 of `NoteTweet:<noteId>`."""

    entities: Optional[NoteTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    inline_media: Optional[List[NoteTweetInlineMedia]] = FieldInfo(alias="inlineMedia", default=None)
    """Inline media positions in the Note Tweet text."""

    is_expandable: Optional[bool] = FieldInfo(alias="isExpandable", default=None)

    note_id: Optional[str] = FieldInfo(alias="noteId", default=None)
    """The Note's own ID, apart from the post's."""

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
    """Whole number from 0."""

    like_count: Optional[int] = FieldInfo(alias="likeCount", default=None)
    """Whole number from 0."""

    quote_count: Optional[int] = FieldInfo(alias="quoteCount", default=None)
    """Whole number from 0."""

    reply_count: Optional[int] = FieldInfo(alias="replyCount", default=None)
    """Whole number from 0."""

    retweet_count: Optional[int] = FieldInfo(alias="retweetCount", default=None)
    """Whole number from 0."""


class QuotedTweetPermalink(BaseModel):
    """The quoted post's link, kept when X withholds that post."""

    display_url: Optional[str] = FieldInfo(alias="displayUrl", default=None)

    expanded_url: Optional[str] = FieldInfo(alias="expandedUrl", default=None)

    url: Optional[str] = None


class QuotedTweetUnavailable(BaseModel):
    """Why X shows no quoted post.

    Omitted when X names no reason, as its legacy answers never do.
    """

    reason: str
    """
    X's reason, such as `Suspended` for a suspended author or `Protected` for an
    author who protects their posts.
    """


class ReactionContext(BaseModel):
    """Public post & user this reaction references."""

    reacted_to_post_id: Optional[str] = FieldInfo(alias="reactedToPostId", default=None)
    """Referenced post ID."""

    reacted_to_user: Optional[UserProfile] = FieldInfo(alias="reactedToUser", default=None)
    """Public X profile."""


class SportsContextCompetitor(BaseModel):
    abbreviation: Optional[str] = None
    """Team abbreviation."""

    color: Optional[str] = None
    """Team display color."""

    dark_logo_url: Optional[str] = FieldInfo(alias="darkLogoUrl", default=None)
    """Logo for dark backgrounds."""

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)
    """Active competitor."""

    is_winner: Optional[bool] = FieldInfo(alias="isWinner", default=None)
    """Winning competitor."""

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """Logo for light backgrounds."""

    name: Optional[str] = None
    """Team name."""

    score: Optional[str] = None
    """Score display text."""

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)
    """Team ID."""


class SportsContext(BaseModel):
    """Game metadata attached to this post."""

    competitors: Optional[List[SportsContextCompetitor]] = None
    """Teams & reported scores."""

    game_id: Optional[str] = FieldInfo(alias="gameId", default=None)
    """Game ID."""

    league: Optional[str] = None
    """League ID."""

    scheduled_at_ms: Union[float, str, None] = FieldInfo(alias="scheduledAtMs", default=None)
    """Scheduled Unix milliseconds, retaining the source type."""

    state: Optional[str] = None
    """Reported game state."""

    status_text: Optional[str] = FieldInfo(alias="statusText", default=None)
    """Game progress text."""

    title: Optional[str] = None
    """Game title."""

    url: Optional[str] = None
    """Game link."""


class SubscriberBadge(BaseModel):
    """The Subscriber badge X shows on a reply.

    The reply's author subscribes to the creator who started the conversation. Omitted on a post without the badge.
    """

    creator_id: str = FieldInfo(alias="creatorId")
    """Account ID of the creator the author subscribes to."""


class TextHighlight(BaseModel):
    end_index: int = FieldInfo(alias="endIndex")
    """The first code point after the match."""

    start_index: int = FieldInfo(alias="startIndex")
    """The first code point of the match."""


class TombstoneTextEntityRef(BaseModel):
    screen_name: Optional[str] = FieldInfo(alias="screenName", default=None)

    text: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)


class TombstoneTextEntity(BaseModel):
    from_index: Optional[int] = FieldInfo(alias="fromIndex", default=None)
    """Whole number from 0."""

    ref: Optional[TombstoneTextEntityRef] = None

    to_index: Optional[int] = FieldInfo(alias="toIndex", default=None)
    """Whole number from 0."""


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
    """Author profile.

    Lookups always include follower count & verification. Other fields depend on
    availability.
    """

    author_unavailable: Optional[AuthorUnavailable] = FieldInfo(alias="authorUnavailable", default=None)
    """Why the tweet has no author.

    X serves a suspended or deleted account as an unavailable user with a reason
    such as Suspended or NotFound. Omitted when the author is available.
    """

    card: Optional[Card] = None
    """Describes a public card and its referenced profiles."""

    cashtag_attachments: Optional[List[CashtagAttachment]] = FieldInfo(alias="cashtagAttachments", default=None)
    """Price charts the author attached under the post, 1 per cashtag.

    Absent when the post has none. X may send a cashtag without a chart window.
    """

    community_id: Optional[str] = FieldInfo(alias="communityId", default=None)
    """Community ID."""

    community_name: Optional[str] = FieldInfo(alias="communityName", default=None)
    """Community name. Present when X sends it with the post."""

    community_note: Optional[CommunityNote] = FieldInfo(alias="communityNote", default=None)
    """Community Note presentation metadata returned by X."""

    content_disclosure: Optional[ContentDisclosure] = FieldInfo(alias="contentDisclosure", default=None)
    """
    Content disclosure metadata shown by X when a tweet is labeled as paid
    partnership content or AI-generated media.
    """

    conversation_control: Optional[ConversationControl] = FieldInfo(alias="conversationControl", default=None)
    """Reply policy & conversation owner."""

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    coordinates: Optional[Coordinates] = None
    """Author-published point, with longitude before latitude."""

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    display_text_range: Optional[List[int]] = FieldInfo(alias="displayTextRange", default=None)

    edit: Optional[Edit] = None
    """Lists edit-chain identifiers and the remaining edit window."""

    entities: Optional[Entities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    exclusive_content: Optional[ExclusiveContent] = FieldInfo(alias="exclusiveContent", default=None)
    """Marks a subscriber-only post with the creator whose subscription unlocks it.

    Non-subscribers get the preview text & the subscribe link. Omitted on public
    posts.
    """

    geo: Optional[Geo] = None
    """Author-published point, with latitude before longitude."""

    grok_share_attachment: Optional[Dict[str, object]] = FieldInfo(alias="grokShareAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    grok_translated_post: Optional[Dict[str, object]] = FieldInfo(alias="grokTranslatedPost", default=None)
    """Grok's translation of the post, as X shows it."""

    has_community_notes: Optional[bool] = FieldInfo(alias="hasCommunityNotes", default=None)
    """Whether X holds Community Notes on the post, shown or not."""

    in_reply_to_id: Optional[str] = FieldInfo(alias="inReplyToId", default=None)

    in_reply_to_user_id: Optional[str] = FieldInfo(alias="inReplyToUserId", default=None)

    in_reply_to_username: Optional[str] = FieldInfo(alias="inReplyToUsername", default=None)

    interstitial: Optional[Interstitial] = None
    """
    The notice x.com covers the post with until the reader views it, such as X's
    public interest notice on a post that broke its rules but stays up.
    """

    is_limited_reply: Optional[bool] = FieldInfo(alias="isLimitedReply", default=None)

    is_note_tweet: Optional[bool] = FieldInfo(alias="isNoteTweet", default=None)

    is_pinned: Optional[bool] = FieldInfo(alias="isPinned", default=None)

    is_quote_status: Optional[bool] = FieldInfo(alias="isQuoteStatus", default=None)

    is_reply: Optional[bool] = FieldInfo(alias="isReply", default=None)

    is_retweet: Optional[bool] = FieldInfo(alias="isRetweet", default=None)

    is_translatable: Optional[bool] = FieldInfo(alias="isTranslatable", default=None)

    jetfuel_attachment: Optional[Dict[str, object]] = FieldInfo(alias="jetfuelAttachment", default=None)
    """Public metadata whose fields are defined by X."""

    lang: Optional[str] = None

    limited_actions: Optional[List[LimitedAction]] = FieldInfo(alias="limitedActions", default=None)
    """Public restrictions & prompts."""

    media: Optional[List[TweetMedia]] = None
    """Media, omitted when unavailable."""

    note_tweet: Optional[NoteTweet] = FieldInfo(alias="noteTweet", default=None)
    """Complete Note Tweet content and rich-text metadata."""

    parent_tweet: Optional[EmbeddedTweet] = FieldInfo(alias="parentTweet", default=None)
    """A parent, quoted or retweeted tweet.

    It has the TweetPublicData fields and an author. Nesting stops after 4 levels.
    """

    place: Optional[Place] = None
    """Describes public place metadata on a geotagged tweet."""

    possibly_sensitive: Optional[bool] = FieldInfo(alias="possiblySensitive", default=None)

    post_cta: Optional[Dict[str, object]] = FieldInfo(alias="postCta", default=None)
    """Public metadata whose fields are defined by X."""

    previous_counts: Optional[PreviousCounts] = FieldInfo(alias="previousCounts", default=None)
    """Engagement counts retained from a prior tweet edit."""

    quoted_tweet: Optional[EmbeddedTweet] = None
    """A parent, quoted or retweeted tweet.

    It has the TweetPublicData fields and an author. Nesting stops after 4 levels.
    """

    quoted_tweet_id: Optional[str] = FieldInfo(alias="quotedTweetId", default=None)

    quoted_tweet_permalink: Optional[QuotedTweetPermalink] = FieldInfo(alias="quotedTweetPermalink", default=None)
    """The quoted post's link, kept when X withholds that post."""

    quoted_tweet_unavailable: Optional[QuotedTweetUnavailable] = FieldInfo(alias="quotedTweetUnavailable", default=None)
    """Why X shows no quoted post.

    Omitted when X names no reason, as its legacy answers never do.
    """

    reaction_context: Optional[ReactionContext] = FieldInfo(alias="reactionContext", default=None)
    """Public post & user this reaction references."""

    retweeted_tweet: Optional[EmbeddedTweet] = None
    """A parent, quoted or retweeted tweet.

    It has the TweetPublicData fields and an author. Nesting stops after 4 levels.
    """

    retweeted_at: Optional[datetime] = FieldInfo(alias="retweetedAt", default=None)
    """Repost event time in UTC. Null when unavailable; omitted for other posts."""

    scopes: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    source: Optional[str] = None
    """The app the post was sent from, as X labels it. X sends it for some posts only."""

    sports_context: Optional[SportsContext] = FieldInfo(alias="sportsContext", default=None)
    """Game metadata attached to this post."""

    subscriber_badge: Optional[SubscriberBadge] = FieldInfo(alias="subscriberBadge", default=None)
    """The Subscriber badge X shows on a reply.

    The reply's author subscribes to the creator who started the conversation.
    Omitted on a post without the badge.
    """

    text_highlights: Optional[List[TextHighlight]] = FieldInfo(alias="textHighlights", default=None)
    """Where `text` matches the search, on each row a search read.

    Offsets count code points of `text`, as `displayTextRange` does. Empty when X
    marks nothing in the post. X marks matches only in a post's first 280
    characters.
    """

    tombstone: Optional[Tombstone] = None
    """Public visibility notice attached to an available tweet."""

    type: Optional[str] = None

    unavailable_author_id: Optional[str] = FieldInfo(alias="unavailableAuthorId", default=None)
    """The author's ID when X withholds the author's profile."""

    unmentioned_user_ids: Optional[List[str]] = FieldInfo(alias="unmentionedUserIds", default=None)
    """User IDs that left this conversation."""

    url: Optional[str] = None

    view_state: Optional[str] = FieldInfo(alias="viewState", default=None)
