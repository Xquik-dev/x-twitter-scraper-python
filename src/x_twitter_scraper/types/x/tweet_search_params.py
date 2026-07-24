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
    """Search query (keywords,"""

    advanced_query: Annotated[str, PropertyInfo(alias="advancedQuery")]
    """Raw advanced search query appended as-is."""

    any_words: Annotated[str, PropertyInfo(alias="anyWords")]
    """Words or quoted phrases where any one can match.

    Separate with spaces, commas, or lines.
    """

    bounding_box: Annotated[str, PropertyInfo(alias="boundingBox")]
    """Geo bounding box, e.g. -74.1 40.6 -73.9 40.8."""

    cashtags: str
    """Cashtags separated by spaces, commas, or lines."""

    conversation_id: Annotated[str, PropertyInfo(alias="conversationId")]
    """Conversation ID filter."""

    cursor: str
    """Pagination cursor from previous response"""

    exact_phrase: Annotated[str, PropertyInfo(alias="exactPhrase")]
    """Exact phrase to match."""

    exclude_words: Annotated[str, PropertyInfo(alias="excludeWords")]
    """Words or quoted phrases to exclude. Separate with spaces, commas, or lines."""

    from_user: Annotated[str, PropertyInfo(alias="fromUser")]
    """Filter by author username."""

    hashtags: str
    """Hashtags separated by spaces, commas, or lines."""

    in_reply_to_tweet_id: Annotated[str, PropertyInfo(alias="inReplyToTweetId")]
    """Only replies to this tweet ID."""

    language: str
    """Language code filter, e.g. en or tr."""

    limit: int
    """Max tweets to return (server paginates internally).

    Omit for single page (~20). This is an upper bound for paid authenticated calls:
    remaining credits can reduce the returned page size, and zero affordable results
    returns 402 insufficient_credits.
    """

    list_id: Annotated[str, PropertyInfo(alias="listId")]
    """Search within a list ID."""

    media_type: Annotated[
        Literal["images", "videos", "gifs", "media", "links", "none"], PropertyInfo(alias="mediaType")
    ]
    """Filter by media type."""

    mentioning: str
    """Filter tweets mentioning a username."""

    min_faves: Annotated[int, PropertyInfo(alias="minFaves")]
    """Minimum likes threshold."""

    min_quotes: Annotated[int, PropertyInfo(alias="minQuotes")]
    """Minimum quote count threshold."""

    min_replies: Annotated[int, PropertyInfo(alias="minReplies")]
    """Minimum replies threshold."""

    min_retweets: Annotated[int, PropertyInfo(alias="minRetweets")]
    """Minimum retweets threshold."""

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

    since_date: Annotated[Union[str, date], PropertyInfo(alias="sinceDate", format="iso8601")]
    """Start date in YYYY-MM-DD format."""

    since_time: Annotated[str, PropertyInfo(alias="sinceTime")]
    """ISO 8601 timestamp - only return tweets after this time"""

    to_user: Annotated[str, PropertyInfo(alias="toUser")]
    """Filter replies sent to a username."""

    until_date: Annotated[Union[str, date], PropertyInfo(alias="untilDate", format="iso8601")]
    """End date in YYYY-MM-DD format."""

    until_time: Annotated[str, PropertyInfo(alias="untilTime")]
    """ISO 8601 timestamp - only return tweets before this time"""

    url: str
    """URL substring or domain filter."""

    verified_only: Annotated[bool, PropertyInfo(alias="verifiedOnly")]
    """Only return tweets from verified authors."""
