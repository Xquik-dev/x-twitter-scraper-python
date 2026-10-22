# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .._dict_access import EventDataDictAccess
from .shared.event_type import EventType
from .shared.tweet_media import TweetMedia
from .shared.user_profile import UserProfile
from .monitors.post_monitor import PostEventType, MonitorPostEdit, MonitorPostDeleted, MonitorPostMetricChange
from .shared.embedded_tweet import EmbeddedTweet
from .shared.soft_intervention import SoftIntervention
from .shared.content_disclosure import ContentDisclosure

__all__ = [
    "Event",
    "Data",
    "DataMonitorPost",
    "DataMonitorPostArticle",
    "DataMonitorPostAuthor",
    "DataMonitorPostAuthorUnavailable",
    "DataMonitorPostCard",
    "DataMonitorPostCardUserReferenceError",
    "DataMonitorPostCardUserReference",
    "DataMonitorPostCashtagAttachment",
    "DataMonitorPostCommunityNote",
    "DataMonitorPostConversationControl",
    "DataMonitorPostCoordinates",
    "DataMonitorPostEdit",
    "DataMonitorPostEntities",
    "DataMonitorPostEntitiesHashtag",
    "DataMonitorPostEntitiesHashtagTag",
    "DataMonitorPostEntitiesHashtagTagInfo",
    "DataMonitorPostEntitiesHashtagTagInfoInfo",
    "DataMonitorPostEntitiesSmarttag",
    "DataMonitorPostEntitiesSmarttagTag",
    "DataMonitorPostEntitiesSmarttagTagInfo",
    "DataMonitorPostEntitiesSmarttagTagInfoInfo",
    "DataMonitorPostEntitiesSymbol",
    "DataMonitorPostEntitiesSymbolTag",
    "DataMonitorPostEntitiesSymbolTagInfo",
    "DataMonitorPostEntitiesSymbolTagInfoInfo",
    "DataMonitorPostEntitiesTimestamp",
    "DataMonitorPostEntitiesTimestampTag",
    "DataMonitorPostEntitiesTimestampTagInfo",
    "DataMonitorPostEntitiesTimestampTagInfoInfo",
    "DataMonitorPostEntitiesURL",
    "DataMonitorPostEntitiesUserMention",
    "DataMonitorPostExclusiveContent",
    "DataMonitorPostGeo",
    "DataMonitorPostInterstitial",
    "DataMonitorPostInterstitialText",
    "DataMonitorPostInterstitialTextEntity",
    "DataMonitorPostInterstitialTextEntityRef",
    "DataMonitorPostLimitedAction",
    "DataMonitorPostLimitedActionPrompt",
    "DataMonitorPostNoteTweet",
    "DataMonitorPostNoteTweetEntities",
    "DataMonitorPostNoteTweetEntitiesHashtag",
    "DataMonitorPostNoteTweetEntitiesHashtagTag",
    "DataMonitorPostNoteTweetEntitiesHashtagTagInfo",
    "DataMonitorPostNoteTweetEntitiesHashtagTagInfoInfo",
    "DataMonitorPostNoteTweetEntitiesSmarttag",
    "DataMonitorPostNoteTweetEntitiesSmarttagTag",
    "DataMonitorPostNoteTweetEntitiesSmarttagTagInfo",
    "DataMonitorPostNoteTweetEntitiesSmarttagTagInfoInfo",
    "DataMonitorPostNoteTweetEntitiesSymbol",
    "DataMonitorPostNoteTweetEntitiesSymbolTag",
    "DataMonitorPostNoteTweetEntitiesSymbolTagInfo",
    "DataMonitorPostNoteTweetEntitiesSymbolTagInfoInfo",
    "DataMonitorPostNoteTweetEntitiesTimestamp",
    "DataMonitorPostNoteTweetEntitiesTimestampTag",
    "DataMonitorPostNoteTweetEntitiesTimestampTagInfo",
    "DataMonitorPostNoteTweetEntitiesTimestampTagInfoInfo",
    "DataMonitorPostNoteTweetEntitiesURL",
    "DataMonitorPostNoteTweetEntitiesUserMention",
    "DataMonitorPostNoteTweetInlineMedia",
    "DataMonitorPostNoteTweetRichtextTag",
    "DataMonitorPostPlace",
    "DataMonitorPostPreviousCounts",
    "DataMonitorPostQuotedTweet",
    "DataMonitorPostQuotedTweetAuthor",
    "DataMonitorPostQuotedTweetPermalink",
    "DataMonitorPostQuotedTweetUnavailable",
    "DataMonitorPostReactionContext",
    "DataMonitorPostReactionContextReactedToUser",
    "DataMonitorPostRetweetedTweet",
    "DataMonitorPostRetweetedTweetAuthor",
    "DataMonitorPostSportsContext",
    "DataMonitorPostSportsContextCompetitor",
    "DataMonitorPostSubscriberBadge",
    "DataMonitorPostTextHighlight",
    "DataMonitorPostTombstone",
    "DataMonitorPostTombstoneText",
    "DataMonitorPostTombstoneTextEntity",
    "DataMonitorPostTombstoneTextEntityRef",
    "DataMonitorProfileChange",
    "DataMonitorLegacyPost",
    "DataMonitorFollow",
]


class DataMonitorPostArticle(BaseModel):
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


class DataMonitorPostAuthor(UserProfile):
    """Public profile with retained legacy monitor fields."""

    raw_verified: Optional[bool] = FieldInfo(alias="rawVerified", default=None)
    """Original X flag. Read verified for the displayed badge."""

    user_name: Optional[str] = FieldInfo(alias="userName", default=None)
    """Legacy username alias. Read username instead."""


class DataMonitorPostAuthorUnavailable(BaseModel):
    """Why the tweet has no author.

    X serves a suspended or deleted account as an unavailable user with a reason such as Suspended or NotFound. Omitted when the author is available.
    """

    reason: str
    """X's reason code."""

    message: Optional[str] = None
    """X's notice text for the reason."""


class DataMonitorPostCardUserReferenceError(BaseModel):
    message: Optional[str] = None

    reason: Optional[str] = None


class DataMonitorPostCardUserReference(UserProfile):
    """Public profile with retained legacy monitor fields."""

    raw_verified: Optional[bool] = FieldInfo(alias="rawVerified", default=None)
    """Original X flag. Read verified for the displayed badge."""

    user_name: Optional[str] = FieldInfo(alias="userName", default=None)
    """Legacy username alias. Read username instead."""


class DataMonitorPostCard(BaseModel):
    id: Optional[str] = None

    binding_values: Optional[Dict[str, object]] = FieldInfo(alias="bindingValues", default=None)
    """Public metadata whose fields are defined by X."""

    name: Optional[str] = None

    platform: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    url: Optional[str] = None

    user_reference_errors: Optional[List[DataMonitorPostCardUserReferenceError]] = FieldInfo(
        alias="userReferenceErrors", default=None
    )
    """Unresolved card user references."""

    user_references: Optional[List[DataMonitorPostCardUserReference]] = FieldInfo(alias="userReferences", default=None)


class DataMonitorPostCashtagAttachment(BaseModel):
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


class DataMonitorPostCommunityNote(BaseModel):
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


class DataMonitorPostConversationControl(BaseModel):
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


class DataMonitorPostCoordinates(BaseModel):
    """Author-published point, with longitude before latitude."""

    coordinates: List[float]

    type: Literal["Point"]


class DataMonitorPostEdit(BaseModel):
    """Lists edit-chain identifiers and the remaining edit window."""

    editable_until_msecs: Optional[str] = FieldInfo(alias="editableUntilMsecs", default=None)

    edit_tweet_ids: Optional[List[str]] = FieldInfo(alias="editTweetIds", default=None)

    initial_tweet_id: Optional[str] = FieldInfo(alias="initialTweetId", default=None)


class DataMonitorPostEntitiesHashtagTagInfoInfo(BaseModel):
    active: Optional[bool] = None
    """Whether X marks the SmartTag active."""

    name: Optional[str] = None

    ticker: Optional[str] = None


class DataMonitorPostEntitiesHashtagTagInfo(BaseModel):
    info: Optional[DataMonitorPostEntitiesHashtagTagInfoInfo] = None


class DataMonitorPostEntitiesHashtagTag(BaseModel):
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    id: Optional[str] = None
    """X's ID for the SmartTag."""

    info: Optional[DataMonitorPostEntitiesHashtagTagInfo] = None


class DataMonitorPostEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[DataMonitorPostEntitiesHashtagTag] = None
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """


class DataMonitorPostEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None
    """Whether X marks the SmartTag active."""

    name: Optional[str] = None

    ticker: Optional[str] = None


class DataMonitorPostEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[DataMonitorPostEntitiesSmarttagTagInfoInfo] = None


class DataMonitorPostEntitiesSmarttagTag(BaseModel):
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    id: Optional[str] = None
    """X's ID for the SmartTag."""

    info: Optional[DataMonitorPostEntitiesSmarttagTagInfo] = None


class DataMonitorPostEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[DataMonitorPostEntitiesSmarttagTag] = None
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    text: Optional[str] = None


class DataMonitorPostEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None
    """Whether X marks the SmartTag active."""

    name: Optional[str] = None

    ticker: Optional[str] = None


class DataMonitorPostEntitiesSymbolTagInfo(BaseModel):
    info: Optional[DataMonitorPostEntitiesSymbolTagInfoInfo] = None


class DataMonitorPostEntitiesSymbolTag(BaseModel):
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    id: Optional[str] = None
    """X's ID for the SmartTag."""

    info: Optional[DataMonitorPostEntitiesSymbolTagInfo] = None


class DataMonitorPostEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[DataMonitorPostEntitiesSymbolTag] = None
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    text: Optional[str] = None


class DataMonitorPostEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None
    """Whether X marks the SmartTag active."""

    name: Optional[str] = None

    ticker: Optional[str] = None


class DataMonitorPostEntitiesTimestampTagInfo(BaseModel):
    info: Optional[DataMonitorPostEntitiesTimestampTagInfoInfo] = None


class DataMonitorPostEntitiesTimestampTag(BaseModel):
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    id: Optional[str] = None
    """X's ID for the SmartTag."""

    info: Optional[DataMonitorPostEntitiesTimestampTagInfo] = None


class DataMonitorPostEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[DataMonitorPostEntitiesTimestampTag] = None
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    text: Optional[str] = None


class DataMonitorPostEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class DataMonitorPostEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class DataMonitorPostEntities(BaseModel):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[DataMonitorPostEntitiesHashtag]] = None

    smarttags: Optional[List[DataMonitorPostEntitiesSmarttag]] = None

    symbols: Optional[List[DataMonitorPostEntitiesSymbol]] = None

    timestamps: Optional[List[DataMonitorPostEntitiesTimestamp]] = None

    urls: Optional[List[DataMonitorPostEntitiesURL]] = None

    user_mentions: Optional[List[DataMonitorPostEntitiesUserMention]] = None


class DataMonitorPostExclusiveContent(BaseModel):
    """Marks a subscriber-only post with the creator whose subscription unlocks it.

    Non-subscribers get the preview text & the subscribe link. Omitted on public posts.
    """

    creator_user_name: str = FieldInfo(alias="creatorUserName")
    """Username of the creator whose subscription unlocks the post."""

    subscribe_url: Optional[str] = FieldInfo(alias="subscribeUrl", default=None)
    """Subscribe link X shows non-subscribers. Omitted when X serves the full post."""


class DataMonitorPostGeo(BaseModel):
    """Author-published point, with latitude before longitude."""

    coordinates: List[float]

    type: Literal["Point"]


class DataMonitorPostInterstitialTextEntityRef(BaseModel):
    screen_name: Optional[str] = FieldInfo(alias="screenName", default=None)

    text: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)


class DataMonitorPostInterstitialTextEntity(BaseModel):
    from_index: Optional[int] = FieldInfo(alias="fromIndex", default=None)
    """Whole number from 0."""

    ref: Optional[DataMonitorPostInterstitialTextEntityRef] = None

    to_index: Optional[int] = FieldInfo(alias="toIndex", default=None)
    """Whole number from 0."""


class DataMonitorPostInterstitialText(BaseModel):
    entities: Optional[List[DataMonitorPostInterstitialTextEntity]] = None
    """Links inside the notice, by character range."""

    rtl: Optional[bool] = None
    """Whether X writes it right to left."""

    text: Optional[str] = None
    """The notice's text."""


class DataMonitorPostInterstitial(BaseModel):
    """
    The notice x.com covers the post with until the reader views it, such as X's public interest notice on a post that broke its rules but stays up.
    """

    display_type: Optional[str] = FieldInfo(alias="displayType", default=None)
    """How x.com shows the notice. `NonCompliant` marks a post that broke X's rules."""

    text: Optional[DataMonitorPostInterstitialText] = None


class DataMonitorPostLimitedActionPrompt(BaseModel):
    cta_type: Optional[str] = FieldInfo(alias="ctaType", default=None)

    headline: Optional[str] = None

    metadata: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    subtext: Optional[str] = None


class DataMonitorPostLimitedAction(BaseModel):
    action: Optional[str] = None

    prompt: Optional[DataMonitorPostLimitedActionPrompt] = None


class DataMonitorPostNoteTweetEntitiesHashtagTagInfoInfo(BaseModel):
    active: Optional[bool] = None
    """Whether X marks the SmartTag active."""

    name: Optional[str] = None

    ticker: Optional[str] = None


class DataMonitorPostNoteTweetEntitiesHashtagTagInfo(BaseModel):
    info: Optional[DataMonitorPostNoteTweetEntitiesHashtagTagInfoInfo] = None


class DataMonitorPostNoteTweetEntitiesHashtagTag(BaseModel):
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    id: Optional[str] = None
    """X's ID for the SmartTag."""

    info: Optional[DataMonitorPostNoteTweetEntitiesHashtagTagInfo] = None


class DataMonitorPostNoteTweetEntitiesHashtag(BaseModel):
    """Provides hashtag text and source offsets within a tweet."""

    text: str

    indices: Optional[List[int]] = None

    tag: Optional[DataMonitorPostNoteTweetEntitiesHashtagTag] = None
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """


class DataMonitorPostNoteTweetEntitiesSmarttagTagInfoInfo(BaseModel):
    active: Optional[bool] = None
    """Whether X marks the SmartTag active."""

    name: Optional[str] = None

    ticker: Optional[str] = None


class DataMonitorPostNoteTweetEntitiesSmarttagTagInfo(BaseModel):
    info: Optional[DataMonitorPostNoteTweetEntitiesSmarttagTagInfoInfo] = None


class DataMonitorPostNoteTweetEntitiesSmarttagTag(BaseModel):
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    id: Optional[str] = None
    """X's ID for the SmartTag."""

    info: Optional[DataMonitorPostNoteTweetEntitiesSmarttagTagInfo] = None


class DataMonitorPostNoteTweetEntitiesSmarttag(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[DataMonitorPostNoteTweetEntitiesSmarttagTag] = None
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    text: Optional[str] = None


class DataMonitorPostNoteTweetEntitiesSymbolTagInfoInfo(BaseModel):
    active: Optional[bool] = None
    """Whether X marks the SmartTag active."""

    name: Optional[str] = None

    ticker: Optional[str] = None


class DataMonitorPostNoteTweetEntitiesSymbolTagInfo(BaseModel):
    info: Optional[DataMonitorPostNoteTweetEntitiesSymbolTagInfoInfo] = None


class DataMonitorPostNoteTweetEntitiesSymbolTag(BaseModel):
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    id: Optional[str] = None
    """X's ID for the SmartTag."""

    info: Optional[DataMonitorPostNoteTweetEntitiesSymbolTagInfo] = None


class DataMonitorPostNoteTweetEntitiesSymbol(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[DataMonitorPostNoteTweetEntitiesSymbolTag] = None
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    text: Optional[str] = None


class DataMonitorPostNoteTweetEntitiesTimestampTagInfoInfo(BaseModel):
    active: Optional[bool] = None
    """Whether X marks the SmartTag active."""

    name: Optional[str] = None

    ticker: Optional[str] = None


class DataMonitorPostNoteTweetEntitiesTimestampTagInfo(BaseModel):
    info: Optional[DataMonitorPostNoteTweetEntitiesTimestampTagInfoInfo] = None


class DataMonitorPostNoteTweetEntitiesTimestampTag(BaseModel):
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    id: Optional[str] = None
    """X's ID for the SmartTag."""

    info: Optional[DataMonitorPostNoteTweetEntitiesTimestampTagInfo] = None


class DataMonitorPostNoteTweetEntitiesTimestamp(BaseModel):
    """Indexed smart-tag, cashtag, or video timestamp metadata."""

    indices: Optional[List[int]] = None

    seconds: Optional[float] = None

    tag: Optional[DataMonitorPostNoteTweetEntitiesTimestampTag] = None
    """X's SmartTag for a cashtag, smarttag or hashtag.

    Xquik leaves out X's trading platforms, which differ by reader.
    """

    text: Optional[str] = None


class DataMonitorPostNoteTweetEntitiesURL(BaseModel):
    """Provides shortened, display, and expanded URLs from tweet text."""

    display_url: Optional[str] = None

    expanded_url: Optional[str] = None

    indices: Optional[List[int]] = None

    url: Optional[str] = None


class DataMonitorPostNoteTweetEntitiesUserMention(BaseModel):
    """Provides profile identity and source offsets for a mention."""

    screen_name: str

    id_str: Optional[str] = None

    indices: Optional[List[int]] = None

    name: Optional[str] = None


class DataMonitorPostNoteTweetEntities(BaseModel):
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    hashtags: Optional[List[DataMonitorPostNoteTweetEntitiesHashtag]] = None

    smarttags: Optional[List[DataMonitorPostNoteTweetEntitiesSmarttag]] = None

    symbols: Optional[List[DataMonitorPostNoteTweetEntitiesSymbol]] = None

    timestamps: Optional[List[DataMonitorPostNoteTweetEntitiesTimestamp]] = None

    urls: Optional[List[DataMonitorPostNoteTweetEntitiesURL]] = None

    user_mentions: Optional[List[DataMonitorPostNoteTweetEntitiesUserMention]] = None


class DataMonitorPostNoteTweetInlineMedia(BaseModel):
    index: int
    """Whole number from 0."""

    media_id: str = FieldInfo(alias="mediaId")


class DataMonitorPostNoteTweetRichtextTag(BaseModel):
    from_index: int = FieldInfo(alias="fromIndex")
    """Whole number from 0."""

    to_index: int = FieldInfo(alias="toIndex")
    """Whole number from 0."""

    types: List[str]


class DataMonitorPostNoteTweet(BaseModel):
    """Complete Note Tweet content and rich-text metadata."""

    text: str

    id: Optional[str] = None
    """X's global ID of the Note, base64 of `NoteTweet:<noteId>`."""

    entities: Optional[DataMonitorPostNoteTweetEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    inline_media: Optional[List[DataMonitorPostNoteTweetInlineMedia]] = FieldInfo(alias="inlineMedia", default=None)
    """Inline media positions in the Note Tweet text."""

    is_expandable: Optional[bool] = FieldInfo(alias="isExpandable", default=None)

    note_id: Optional[str] = FieldInfo(alias="noteId", default=None)
    """The Note's own ID, apart from the post's."""

    richtext_tags: Optional[List[DataMonitorPostNoteTweetRichtextTag]] = FieldInfo(alias="richtextTags", default=None)


class DataMonitorPostPlace(BaseModel):
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


class DataMonitorPostPreviousCounts(BaseModel):
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


class DataMonitorPostQuotedTweetAuthor(UserProfile):
    """Public profile with retained legacy monitor fields."""

    raw_verified: Optional[bool] = FieldInfo(alias="rawVerified", default=None)
    """Original X flag. Read verified for the displayed badge."""

    user_name: Optional[str] = FieldInfo(alias="userName", default=None)
    """Legacy username alias. Read username instead."""


class DataMonitorPostQuotedTweet(EmbeddedTweet):
    """Embedded post with public fields and legacy profile aliases."""

    author: Optional[DataMonitorPostQuotedTweetAuthor] = None  # type: ignore
    """Public profile with retained legacy monitor fields."""


class DataMonitorPostQuotedTweetPermalink(BaseModel):
    """The quoted post's link, kept when X withholds that post."""

    display_url: Optional[str] = FieldInfo(alias="displayUrl", default=None)

    expanded_url: Optional[str] = FieldInfo(alias="expandedUrl", default=None)

    url: Optional[str] = None


class DataMonitorPostQuotedTweetUnavailable(BaseModel):
    """Why X shows no quoted post.

    Omitted when X names no reason, as its legacy answers never do.
    """

    reason: str
    """
    X's reason, such as `Suspended` for a suspended author or `Protected` for an
    author who protects their posts.
    """


class DataMonitorPostReactionContextReactedToUser(UserProfile):
    """Public profile with retained legacy monitor fields."""

    raw_verified: Optional[bool] = FieldInfo(alias="rawVerified", default=None)
    """Original X flag. Read verified for the displayed badge."""

    user_name: Optional[str] = FieldInfo(alias="userName", default=None)
    """Legacy username alias. Read username instead."""


class DataMonitorPostReactionContext(BaseModel):
    reacted_to_post_id: Optional[str] = FieldInfo(alias="reactedToPostId", default=None)

    reacted_to_user: Optional[DataMonitorPostReactionContextReactedToUser] = FieldInfo(
        alias="reactedToUser", default=None
    )
    """Public profile with retained legacy monitor fields."""


class DataMonitorPostRetweetedTweetAuthor(UserProfile):
    """Public profile with retained legacy monitor fields."""

    raw_verified: Optional[bool] = FieldInfo(alias="rawVerified", default=None)
    """Original X flag. Read verified for the displayed badge."""

    user_name: Optional[str] = FieldInfo(alias="userName", default=None)
    """Legacy username alias. Read username instead."""


class DataMonitorPostRetweetedTweet(EmbeddedTweet):
    """Embedded post with public fields and legacy profile aliases."""

    author: Optional[DataMonitorPostRetweetedTweetAuthor] = None  # type: ignore
    """Public profile with retained legacy monitor fields."""


class DataMonitorPostSportsContextCompetitor(BaseModel):
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


class DataMonitorPostSportsContext(BaseModel):
    """Game metadata attached to this post."""

    competitors: Optional[List[DataMonitorPostSportsContextCompetitor]] = None
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


class DataMonitorPostSubscriberBadge(BaseModel):
    """The Subscriber badge X shows on a reply.

    The reply's author subscribes to the creator who started the conversation. Omitted on a post without the badge.
    """

    creator_id: str = FieldInfo(alias="creatorId")
    """Account ID of the creator the author subscribes to."""


class DataMonitorPostTextHighlight(BaseModel):
    end_index: int = FieldInfo(alias="endIndex")
    """The first code point after the match."""

    start_index: int = FieldInfo(alias="startIndex")
    """The first code point of the match."""


class DataMonitorPostTombstoneTextEntityRef(BaseModel):
    screen_name: Optional[str] = FieldInfo(alias="screenName", default=None)

    text: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)


class DataMonitorPostTombstoneTextEntity(BaseModel):
    from_index: Optional[int] = FieldInfo(alias="fromIndex", default=None)
    """Whole number from 0."""

    ref: Optional[DataMonitorPostTombstoneTextEntityRef] = None

    to_index: Optional[int] = FieldInfo(alias="toIndex", default=None)
    """Whole number from 0."""


class DataMonitorPostTombstoneText(BaseModel):
    entities: Optional[List[DataMonitorPostTombstoneTextEntity]] = None

    rtl: Optional[bool] = None
    """Right-to-left text direction."""

    text: Optional[str] = None
    """Human-readable notice text."""


class DataMonitorPostTombstone(BaseModel):
    """Public visibility notice attached to an available tweet."""

    text: Optional[DataMonitorPostTombstoneText] = None

    type: Optional[str] = None
    """Visibility notice type."""


class DataMonitorPost(EventDataDictAccess):
    """Monitored post with public fields and retained legacy fields."""

    id: str

    bookmark_count: int = FieldInfo(alias="bookmarkCount")

    like_count: int = FieldInfo(alias="likeCount")

    quote_count: int = FieldInfo(alias="quoteCount")

    reply_count: int = FieldInfo(alias="replyCount")

    retweet_count: int = FieldInfo(alias="retweetCount")

    text: str

    view_count: int = FieldInfo(alias="viewCount")

    article: Optional[DataMonitorPostArticle] = None
    """Describes an X Article preview and its lifecycle metadata."""

    author: Optional[DataMonitorPostAuthor] = None
    """Public profile with retained legacy monitor fields."""

    author_unavailable: Optional[DataMonitorPostAuthorUnavailable] = FieldInfo(alias="authorUnavailable", default=None)
    """Why the tweet has no author.

    X serves a suspended or deleted account as an unavailable user with a reason
    such as Suspended or NotFound. Omitted when the author is available.
    """

    card: Optional[DataMonitorPostCard] = None

    cashtag_attachments: Optional[List[DataMonitorPostCashtagAttachment]] = FieldInfo(
        alias="cashtagAttachments", default=None
    )
    """Price charts the author attached under the post, 1 per cashtag.

    Absent when the post has none. X may send a cashtag without a chart window.
    """

    community_id: Optional[str] = FieldInfo(alias="communityId", default=None)
    """Community ID."""

    community_name: Optional[str] = FieldInfo(alias="communityName", default=None)
    """Community name. Present when X sends it with the post."""

    community_note: Optional[DataMonitorPostCommunityNote] = FieldInfo(alias="communityNote", default=None)
    """Community Note presentation metadata returned by X."""

    content_disclosure: Optional[ContentDisclosure] = FieldInfo(alias="contentDisclosure", default=None)
    """
    Content disclosure metadata shown by X when a tweet is labeled as paid
    partnership content or AI-generated media.
    """

    conversation_control: Optional[DataMonitorPostConversationControl] = FieldInfo(
        alias="conversationControl", default=None
    )
    """Reply policy & conversation owner."""

    conversation_id: Optional[str] = FieldInfo(alias="conversationId", default=None)

    coordinates: Optional[DataMonitorPostCoordinates] = None
    """Author-published point, with longitude before latitude."""

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    display_text_range: Optional[List[int]] = FieldInfo(alias="displayTextRange", default=None)

    edit: Optional[DataMonitorPostEdit] = None
    """Lists edit-chain identifiers and the remaining edit window."""

    entities: Optional[DataMonitorPostEntities] = None
    """Lists hashtags, symbols, links, and mentions from tweet text."""

    exclusive_content: Optional[DataMonitorPostExclusiveContent] = FieldInfo(alias="exclusiveContent", default=None)
    """Marks a subscriber-only post with the creator whose subscription unlocks it.

    Non-subscribers get the preview text & the subscribe link. Omitted on public
    posts.
    """

    geo: Optional[DataMonitorPostGeo] = None
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

    interstitial: Optional[DataMonitorPostInterstitial] = None
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

    limited_actions: Optional[List[DataMonitorPostLimitedAction]] = FieldInfo(alias="limitedActions", default=None)
    """Public restrictions & prompts."""

    media: Optional[List[TweetMedia]] = None
    """Media, omitted when unavailable."""

    note_tweet: Optional[DataMonitorPostNoteTweet] = FieldInfo(alias="noteTweet", default=None)
    """Complete Note Tweet content and rich-text metadata."""

    parent_tweet: Optional[EmbeddedTweet] = FieldInfo(alias="parentTweet", default=None)
    """A parent, quoted or retweeted tweet.

    It has the TweetPublicData fields and an author. Nesting stops after 4 levels.
    """

    place: Optional[DataMonitorPostPlace] = None
    """Describes public place metadata on a geotagged tweet."""

    possibly_sensitive: Optional[bool] = FieldInfo(alias="possiblySensitive", default=None)

    post_cta: Optional[Dict[str, object]] = FieldInfo(alias="postCta", default=None)
    """Public metadata whose fields are defined by X."""

    previous_counts: Optional[DataMonitorPostPreviousCounts] = FieldInfo(alias="previousCounts", default=None)
    """Engagement counts retained from a prior tweet edit."""

    quoted_tweet: Optional[DataMonitorPostQuotedTweet] = None
    """Embedded post with public fields and legacy profile aliases."""

    quoted_tweet_id: Optional[str] = FieldInfo(alias="quotedTweetId", default=None)

    quoted_tweet_permalink: Optional[DataMonitorPostQuotedTweetPermalink] = FieldInfo(
        alias="quotedTweetPermalink", default=None
    )
    """The quoted post's link, kept when X withholds that post."""

    quoted_tweet_unavailable: Optional[DataMonitorPostQuotedTweetUnavailable] = FieldInfo(
        alias="quotedTweetUnavailable", default=None
    )
    """Why X shows no quoted post.

    Omitted when X names no reason, as its legacy answers never do.
    """

    reaction_context: Optional[DataMonitorPostReactionContext] = FieldInfo(alias="reactionContext", default=None)

    retweeted_tweet: Optional[DataMonitorPostRetweetedTweet] = None
    """Embedded post with public fields and legacy profile aliases."""

    retweeted_at: Optional[datetime] = FieldInfo(alias="retweetedAt", default=None)
    """Repost event time in UTC. Null when unavailable; omitted for other posts."""

    scopes: Optional[Dict[str, object]] = None
    """Public metadata whose fields are defined by X."""

    soft_intervention: Optional[SoftIntervention] = FieldInfo(alias="softIntervention", default=None)
    """The label X shows under a post whose reach it limits.

    It links to the page that explains it.
    """

    source: Optional[str] = None
    """The app the post was sent from, as X labels it. X sends it for some posts only."""

    sports_context: Optional[DataMonitorPostSportsContext] = FieldInfo(alias="sportsContext", default=None)
    """Game metadata attached to this post."""

    subscriber_badge: Optional[DataMonitorPostSubscriberBadge] = FieldInfo(alias="subscriberBadge", default=None)
    """The Subscriber badge X shows on a reply.

    The reply's author subscribes to the creator who started the conversation.
    Omitted on a post without the badge.
    """

    text_highlights: Optional[List[DataMonitorPostTextHighlight]] = FieldInfo(alias="textHighlights", default=None)
    """Where `text` matches the search, on each row a search read.

    Offsets count code points of `text`, as `displayTextRange` does. Empty when X
    marks nothing in the post. X marks matches only in a post's first 280
    characters.
    """

    tombstone: Optional[DataMonitorPostTombstone] = None
    """Public visibility notice attached to an available tweet."""

    type: Optional[str] = None

    unavailable_author_id: Optional[str] = FieldInfo(alias="unavailableAuthorId", default=None)
    """The author's ID when X withholds the author's profile."""

    unknown_counts: Optional[List[str]] = FieldInfo(alias="unknownCounts", default=None)
    """X did not send these counts, so each 0 means unknown."""

    unmentioned_user_ids: Optional[List[str]] = FieldInfo(alias="unmentionedUserIds", default=None)
    """User IDs that left this conversation."""

    url: Optional[str] = None

    view_state: Optional[str] = FieldInfo(alias="viewState", default=None)


class DataMonitorProfileChange(EventDataDictAccess):
    """Changed profile field with its previous and current values.

    The field of a count event is followers or following, with both counts as integers.
    """

    field: str

    user_id: str = FieldInfo(alias="userId")
    """Permanent X user ID."""

    username: str
    """Username observed for this change."""

    change: Optional[int] = None
    """Current count minus previous count. Only on the 2 count events."""

    current: Union[str, bool, int, List[str], None] = None
    """Profile text, flag, count, or pinned post IDs. Missing values are omitted."""

    previous: Union[str, bool, int, List[str], None] = None
    """Profile text, flag, count, or pinned post IDs. Missing values are omitted."""


class DataMonitorLegacyPost(EventDataDictAccess):
    """Older stored posts remain readable. Fields can be missing or null."""

    id: Optional[str] = None

    author: Optional[Dict[str, object]] = None

    quoted_tweet: Optional[Dict[str, object]] = None

    retweeted_tweet: Optional[Dict[str, object]] = None

    text: Optional[str] = None

    if TYPE_CHECKING:
        # Pydantic <2.8 rejects a value on __pydantic_extra__ at runtime.
        # https://github.com/pydantic/pydantic/pull/9659
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class DataMonitorFollow(EventDataDictAccess):
    """The other account of a following or follower event, with the profile fields a user lookup returns.

    It holds the ID alone when X fails the profile lookup.
    """

    id: str
    """The other account's X user ID."""

    followed_at: Optional[datetime] = FieldInfo(alias="followedAt", default=None)
    """X's time of the follow, on following.added & follower.added.

    It is missing when X gives none, as for an account that returns to a list.
    """

    followed_at_exact: Optional[bool] = FieldInfo(alias="followedAtExact", default=None)
    """Whether followedAt is X's exact time of this follow.

    When several accounts join between 2 checks, X times the first, the second &
    the last. Each other one holds the earliest time its follow can have, with false
    here.
    """

    reason: Optional[Literal["unavailable", "unfollowed"]] = None
    """Why the account left the list, on following.removed & follower.removed.

    unavailable means X no longer serves the account. unfollowed means X's follow
    check says the follow ended. It is missing when X fails the check. Xquik sends
    no removal while X still confirms the follow.
    """

    if TYPE_CHECKING:
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


Data: TypeAlias = Union[
    DataMonitorPost,
    DataMonitorProfileChange,
    MonitorPostMetricChange,
    MonitorPostEdit,
    DataMonitorLegacyPost,
    MonitorPostDeleted,
    DataMonitorFollow,
]


class Event(BaseModel):
    """Monitor event summary with source metadata and occurrence time."""

    id: str

    data: Data
    """Post fields match REST. Legacy fields remain available."""

    monitor_id: str = FieldInfo(alias="monitorId")
    """
    Account monitor ID for account events, or keyword monitor ID for keyword events.
    """

    monitor_type: Literal["account", "keyword", "post"] = FieldInfo(alias="monitorType")
    """Source monitor type."""

    occurred_at: datetime = FieldInfo(alias="occurredAt")

    type: Union[EventType, PostEventType]
    """Type of monitor event fired when account activity occurs.

    tweet.deleted fires once X confirms the account deleted a post the monitor saw.
    Its data is the post as last seen. broadcast.started & space.started fire when
    the account posts its running live video or Space. Their data is that post. A
    live the account does not post is not seen. following.added & following.removed
    fire when the account follows or unfollows someone, with that account's profile.
    Keyword monitors take the 10 post types only.
    """

    author_id: Optional[str] = FieldInfo(alias="authorId", default=None)
    """Permanent X user ID of the monitored post's author, present for post events."""

    author_username: Optional[str] = FieldInfo(alias="authorUsername", default=None)
    """Username of the monitored post's author, present for post events."""

    keyword_monitor_id: Optional[str] = FieldInfo(alias="keywordMonitorId", default=None)
    """Keyword monitor ID, present for keyword monitor events."""

    monitor_name: Optional[str] = FieldInfo(alias="monitorName", default=None)
    """Your monitor label when Xquik created the event, present when set.

    A rename leaves the event's label unchanged.
    """

    post_id: Optional[str] = FieldInfo(alias="postId", default=None)
    """ID of the monitored post, present for post events."""

    post_url: Optional[str] = FieldInfo(alias="postUrl", default=None)
    """Link to the monitored post, present for post events."""

    query: Optional[str] = None
    """Keyword query, present for keyword monitor events."""

    username: Optional[str] = None
    """Current account username, present for account monitor events."""

    x_user_id: Optional[str] = FieldInfo(alias="xUserId", default=None)
    """
    Permanent X user ID of the monitored account, present for account monitor
    events. It stays the same after a username change.
    """
