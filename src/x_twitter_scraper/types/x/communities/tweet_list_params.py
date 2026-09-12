# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TweetListParams"]


class TweetListParams(TypedDict, total=False):
    community_id: Required[Annotated[str, PropertyInfo(alias="communityId")]]
    """Numeric ID of the community whose posts to search"""

    q: Required[str]
    """Search query"""

    cursor: str
    """Pagination cursor for community search"""

    language: str
    """Filter by language. Alias `lang` is accepted."""

    media_type: Annotated[
        Literal["images", "videos", "gifs", "media", "links", "none"], PropertyInfo(alias="mediaType")
    ]
    """Filter media. Aliases: has_video, has_media."""

    min_likes: Annotated[int, PropertyInfo(alias="minLikes")]
    """Minimum likes. Aliases: minFaves, min_likes, min_faves."""

    min_replies: Annotated[int, PropertyInfo(alias="minReplies")]
    """Minimum replies threshold."""

    min_retweets: Annotated[int, PropertyInfo(alias="minRetweets")]
    """Minimum retweets threshold."""

    min_views: Annotated[int, PropertyInfo(alias="minViews")]
    """Minimum view count threshold."""

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Maximum page items (1-100, default 20).

    Source, filters, or credits can reduce results. Follow next_cursor while the
    response reports more pages. Deprecated limit and count aliases remain accepted.
    """

    query_type: Annotated[Literal["Latest", "Top"], PropertyInfo(alias="queryType")]
    """Sort order (Latest or Top)"""

    since_date: Annotated[Union[str, date], PropertyInfo(alias="sinceDate", format="iso8601")]
    """Start date in YYYY-MM-DD format."""

    until_date: Annotated[Union[str, date], PropertyInfo(alias="untilDate", format="iso8601")]
    """End date in YYYY-MM-DD format."""

    verified_only: Annotated[bool, PropertyInfo(alias="verifiedOnly")]
    """Only return tweets from verified authors."""
