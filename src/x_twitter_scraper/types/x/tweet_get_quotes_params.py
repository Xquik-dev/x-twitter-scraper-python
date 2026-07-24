# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TweetGetQuotesParams"]


class TweetGetQuotesParams(TypedDict, total=False):
    any_words: Annotated[str, PropertyInfo(alias="anyWords")]
    """Words or quoted phrases where any one can match.

    Separate with spaces, commas, or lines.
    """

    cashtags: str
    """Cashtags separated by spaces, commas, or lines."""

    conversation_id: Annotated[str, PropertyInfo(alias="conversationId")]
    """Conversation ID filter."""

    cursor: str
    """Pagination cursor for quote tweets"""

    exact_phrase: Annotated[str, PropertyInfo(alias="exactPhrase")]
    """Exact phrase to match."""

    exclude_words: Annotated[str, PropertyInfo(alias="excludeWords")]
    """Words or quoted phrases to exclude. Separate with spaces, commas, or lines."""

    from_user: Annotated[str, PropertyInfo(alias="fromUser")]
    """Filter by author username."""

    hashtags: str
    """Hashtags separated by spaces, commas, or lines."""

    include_replies: Annotated[bool, PropertyInfo(alias="includeReplies")]
    """Include reply quotes (default false)"""

    in_reply_to_tweet_id: Annotated[str, PropertyInfo(alias="inReplyToTweetId")]
    """Only replies to this tweet ID."""

    language: str
    """Language code filter, e.g. en or tr."""

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

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Maximum items requested from this page (1-100, default 20).

    The response can contain fewer items because the source returned fewer, filters
    removed items, or remaining credits cover fewer results. Keep requesting
    next_cursor while has_next_page is true, even when a page is empty. The
    deprecated limit and count aliases remain accepted.
    """

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
    """Unix timestamp - return quotes posted after this time"""

    to_user: Annotated[str, PropertyInfo(alias="toUser")]
    """Filter replies sent to a username."""

    until_date: Annotated[Union[str, date], PropertyInfo(alias="untilDate", format="iso8601")]
    """End date in YYYY-MM-DD format."""

    until_time: Annotated[str, PropertyInfo(alias="untilTime")]
    """Unix timestamp - return quotes posted before this time"""

    url: str
    """URL substring or domain filter."""

    verified_only: Annotated[bool, PropertyInfo(alias="verifiedOnly")]
    """Only return tweets from verified authors."""
