# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExtractionExportResultsParams"]


class ExtractionExportResultsParams(TypedDict, total=False):
    format: Required[Literal["csv", "json", "md", "md-document", "pdf", "txt", "xlsx"]]
    """Export file format"""

    has_description: Annotated[bool, PropertyInfo(alias="hasDescription")]
    """Require a non-empty description."""

    has_location: Annotated[bool, PropertyInfo(alias="hasLocation")]
    """Require a non-empty location."""

    has_media: Annotated[bool, PropertyInfo(alias="hasMedia")]
    """Require media."""

    lang: str
    """Filter by language code."""

    max_followers: Annotated[int, PropertyInfo(alias="maxFollowers")]
    """Maximum follower count."""

    max_following: Annotated[int, PropertyInfo(alias="maxFollowing")]
    """Maximum following count."""

    max_posts: Annotated[int, PropertyInfo(alias="maxPosts")]
    """Maximum post count."""

    min_followers: Annotated[int, PropertyInfo(alias="minFollowers")]
    """Minimum follower count."""

    min_following: Annotated[int, PropertyInfo(alias="minFollowing")]
    """Minimum following count."""

    min_likes: Annotated[int, PropertyInfo(alias="minLikes")]
    """Minimum like count."""

    min_posts: Annotated[int, PropertyInfo(alias="minPosts")]
    """Minimum post count."""

    min_replies: Annotated[int, PropertyInfo(alias="minReplies")]
    """Minimum reply count."""

    min_retweets: Annotated[int, PropertyInfo(alias="minRetweets")]
    """Minimum repost count."""

    min_views: Annotated[int, PropertyInfo(alias="minViews")]
    """Minimum view count."""

    search: str
    """Search exported result text."""

    since_date: Annotated[Union[str, date], PropertyInfo(alias="sinceDate", format="iso8601")]
    """Include results on or after this date."""

    until_date: Annotated[Union[str, date], PropertyInfo(alias="untilDate", format="iso8601")]
    """Include results on or before this date."""

    verified: bool
    """Filter by verified status."""
