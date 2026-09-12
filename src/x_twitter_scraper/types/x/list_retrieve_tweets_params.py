# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ListRetrieveTweetsParams"]


class ListRetrieveTweetsParams(TypedDict, total=False):
    any_words: Annotated[str, PropertyInfo(alias="anyWords")]
    """Words or quoted phrases where any one can match.

    Separate with spaces, commas, or lines.
    """

    blue_verified_only: Annotated[bool, PropertyInfo(alias="blueVerifiedOnly")]
    """Only return tweets from Blue-verified authors."""

    cashtags: str
    """Cashtags separated by spaces, commas, or lines."""

    cursor: str
    """Cursor from the previous response.

    Xquik cursors resume automatic coverage. Existing unprefixed cursors keep legacy
    standard behavior.
    """

    exact_phrase: Annotated[str, PropertyInfo(alias="exactPhrase")]
    """Match this literal phrase, including any hyphens."""

    exclude_words: Annotated[str, PropertyInfo(alias="excludeWords")]
    """Words or quoted phrases to exclude. Separate with spaces, commas, or lines."""

    from_user: Annotated[str, PropertyInfo(alias="fromUser")]
    """Filter by author username."""

    hashtags: str
    """Hashtags separated by spaces, commas, or lines."""

    include_replies: Annotated[bool, PropertyInfo(alias="includeReplies")]
    """Include reply tweets unless replies specifies another mode."""

    language: str
    """Filter by language. Alias `lang` is accepted."""

    max_faves: Annotated[int, PropertyInfo(alias="maxFaves")]
    """Maximum likes threshold. maxLikes is also accepted."""

    max_quotes: Annotated[int, PropertyInfo(alias="maxQuotes")]
    """Maximum quotes threshold."""

    max_replies: Annotated[int, PropertyInfo(alias="maxReplies")]
    """Maximum replies threshold."""

    max_retweets: Annotated[int, PropertyInfo(alias="maxRetweets")]
    """Maximum retweets threshold."""

    media_type: Annotated[
        Literal["images", "videos", "gifs", "media", "links", "none"], PropertyInfo(alias="mediaType")
    ]
    """Filter media. Aliases: has_video, has_media."""

    mentioning: str
    """Filter tweets mentioning a username."""

    min_bookmarks: Annotated[int, PropertyInfo(alias="minBookmarks")]
    """Minimum bookmark count threshold."""

    min_likes: Annotated[int, PropertyInfo(alias="minLikes")]
    """Minimum likes. Aliases: minFaves, min_likes, min_faves."""

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

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Automatic pages accept 1-300 Tweets.

    Standard pages keep 1-100. Default 20. Follow next_cursor while the response
    reports more pages. Deprecated aliases remain accepted.
    """

    replies: Literal["include", "exclude", "only"]
    """Only when the caller requests a reply mode."""

    retweets: Literal["include", "exclude", "only"]
    """Only when the caller requests a repost mode."""

    since_date: Annotated[Union[str, date], PropertyInfo(alias="sinceDate", format="iso8601")]
    """Start date in YYYY-MM-DD format."""

    since_time: Annotated[str, PropertyInfo(alias="sinceTime")]
    """Inclusive ISO bound for Tweet creation time."""

    to_user: Annotated[str, PropertyInfo(alias="toUser")]
    """Filter replies sent to a username."""

    until_date: Annotated[Union[str, date], PropertyInfo(alias="untilDate", format="iso8601")]
    """End date in YYYY-MM-DD format."""

    until_time: Annotated[str, PropertyInfo(alias="untilTime")]
    """Exclusive ISO bound for Tweet creation time."""

    verified_only: Annotated[bool, PropertyInfo(alias="verifiedOnly")]
    """Only return tweets from verified authors."""
