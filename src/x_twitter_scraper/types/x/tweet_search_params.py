# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TweetSearchParams"]


class TweetSearchParams(TypedDict, total=False):
    q: Required[str]
    """Query, Tweet ID, or status URL. Valid inline bounds apply per page."""

    advanced_query: Annotated[str, PropertyInfo(alias="advancedQuery")]
    """Raw advanced search query appended as-is."""

    any_words: Annotated[str, PropertyInfo(alias="anyWords")]
    """Words or quoted phrases where any one can match.

    Separate with spaces, commas, or lines.
    """

    blue_verified_only: Annotated[bool, PropertyInfo(alias="blueVerifiedOnly")]
    """Only return tweets from Blue-verified authors."""

    bounding_box: Annotated[str, PropertyInfo(alias="boundingBox")]
    """Geo bounding box, e.g. -74.1 40.6 -73.9 40.8."""

    card_name: Annotated[str, PropertyInfo(alias="cardName")]
    """Match the Tweet card name."""

    cashtags: str
    """Cashtags separated by spaces, commas, or lines."""

    conversation_id: Annotated[str, PropertyInfo(alias="conversationId")]
    """Conversation ID filter."""

    cursor: str
    """Cursor from the previous response.

    Xquik cursors resume automatic coverage. Existing unprefixed cursors keep legacy
    standard behavior.
    """

    exact_phrase: Annotated[str, PropertyInfo(alias="exactPhrase")]
    """Exact phrase to match."""

    exclude_source: Annotated[str, PropertyInfo(alias="excludeSource")]
    """Exclude a source application."""

    exclude_words: Annotated[str, PropertyInfo(alias="excludeWords")]
    """Words or quoted phrases to exclude. Separate with spaces, commas, or lines."""

    from_user: Annotated[str, PropertyInfo(alias="fromUser")]
    """Filter by author username."""

    geocode: str
    """Match latitude, longitude, and radius."""

    hashtags: str
    """Hashtags separated by spaces, commas, or lines."""

    in_reply_to_tweet_id: Annotated[str, PropertyInfo(alias="inReplyToTweetId")]
    """Only replies to this tweet ID."""

    language: str
    """Language code filter, e.g. en or tr."""

    limit: int
    """Result upper bound.

    Omit it for the existing 20-row page size. Explicit coverage defaults to 2000
    and allows 10000. For paid requests, remaining credits can reduce results. Zero
    affordable results returns 402.
    """

    list_id: Annotated[str, PropertyInfo(alias="listId")]
    """Search within a list ID."""

    max_faves: Annotated[int, PropertyInfo(alias="maxFaves")]
    """Maximum likes threshold. maxLikes is also accepted."""

    max_id: Annotated[str, PropertyInfo(alias="maxId")]
    """Return Tweets older than this Tweet ID."""

    max_quotes: Annotated[int, PropertyInfo(alias="maxQuotes")]
    """Maximum quotes threshold."""

    max_replies: Annotated[int, PropertyInfo(alias="maxReplies")]
    """Maximum replies threshold."""

    max_retweets: Annotated[int, PropertyInfo(alias="maxRetweets")]
    """Maximum retweets threshold."""

    media_type: Annotated[
        Literal["images", "videos", "gifs", "media", "links", "none"], PropertyInfo(alias="mediaType")
    ]
    """Filter by media type."""

    mentioning: str
    """Filter tweets mentioning a username."""

    min_bookmarks: Annotated[int, PropertyInfo(alias="minBookmarks")]
    """Minimum bookmark count threshold."""

    min_faves: Annotated[int, PropertyInfo(alias="minFaves")]
    """Minimum likes threshold."""

    min_quotes: Annotated[int, PropertyInfo(alias="minQuotes")]
    """Minimum quote count threshold."""

    min_replies: Annotated[int, PropertyInfo(alias="minReplies")]
    """Minimum replies threshold."""

    min_retweets: Annotated[int, PropertyInfo(alias="minRetweets")]
    """Minimum retweets threshold."""

    min_views: Annotated[int, PropertyInfo(alias="minViews")]
    """Minimum view count threshold."""

    mode: Literal["standard", "coverage"]
    """Omit mode for resumable maximum coverage.

    Standard keeps legacy pagination. Coverage returns diagnostics once and rejects
    cursors.
    """

    native_retweets: Annotated[bool, PropertyInfo(alias="nativeRetweets")]
    """Only return native reposts."""

    near: str
    """Match a place name."""

    news: bool
    """Only return news results."""

    place: str
    """Search within a place ID."""

    place_country: Annotated[str, PropertyInfo(alias="placeCountry")]
    """Search within a country code."""

    point_radius: Annotated[str, PropertyInfo(alias="pointRadius")]
    """Geo point radius, e.g. -73.99 40.73 25mi."""

    query_type: Annotated[Literal["Latest", "Top"], PropertyInfo(alias="queryType")]
    """Sort order - Latest (chronological) or Top (engagement-ranked)"""

    quotes: Literal["include", "exclude", "only"]
    """Quote mode."""

    quotes_of_tweet_id: Annotated[str, PropertyInfo(alias="quotesOfTweetId")]
    """Only quotes of this tweet ID."""

    replies: Literal["include", "exclude", "only"]
    """Reply mode."""

    retweets: Literal["include", "exclude", "only"]
    """Retweet mode."""

    retweets_of_tweet_id: Annotated[str, PropertyInfo(alias="retweetsOfTweetId")]
    """Only retweets of this tweet ID."""

    safe: bool
    """Enable the safe-search filter."""

    since_date: Annotated[Union[str, date], PropertyInfo(alias="sinceDate", format="iso8601")]
    """Start date in YYYY-MM-DD format."""

    since_id: Annotated[str, PropertyInfo(alias="sinceId")]
    """Return Tweets newer than this Tweet ID."""

    since_time: Annotated[str, PropertyInfo(alias="sinceTime")]
    """Inclusive ISO bound."""

    source: str
    """Match the source application."""

    to_user: Annotated[str, PropertyInfo(alias="toUser")]
    """Filter replies sent to a username."""

    until_date: Annotated[Union[str, date], PropertyInfo(alias="untilDate", format="iso8601")]
    """End date in YYYY-MM-DD format."""

    until_time: Annotated[str, PropertyInfo(alias="untilTime")]
    """Exclusive ISO bound."""

    url: str
    """URL substring or domain filter."""

    verified_only: Annotated[bool, PropertyInfo(alias="verifiedOnly")]
    """Only return tweets from verified authors."""

    within: str
    """Set the radius for the near filter."""

    within_time: Annotated[str, PropertyInfo(alias="withinTime")]
    """Match Tweets inside a recent time window."""
