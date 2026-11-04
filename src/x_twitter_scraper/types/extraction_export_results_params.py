# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExtractionExportResultsParams"]


class ExtractionExportResultsParams(TypedDict, total=False):
    format: Required[Literal["csv", "json", "md", "md-document", "pdf", "txt", "xlsx"]]
    """Export file format"""

    business_email_only: Annotated[bool, PropertyInfo(alias="businessEmailOnly")]
    """
    Require an email outside free webmail, such as Gmail, in the row's Email column.
    """

    change: Literal["added", "removed"]
    """
    With compare, `added` keeps this run's new rows and `removed` keeps the earlier
    run's rows that this run lacks.

    The default is `added`. A run of another account ignores it.
    """

    compare: str
    """ID of another run of this tool.

    For an earlier whole run of the same account, the export holds only the rows that
    differ. For a run of another account, it holds only this run's rows that the other
    run also lists.
    """

    email_domains: Annotated[str, PropertyInfo(alias="emailDomains")]
    """Require the row's email at one of these domains.

    Separate domains with commas. Subdomains match.
    """

    has_description: Annotated[bool, PropertyInfo(alias="hasDescription")]
    """Require a non-empty description."""

    has_email: Annotated[bool, PropertyInfo(alias="hasEmail")]
    """Require an email in the row's Email column."""

    has_location: Annotated[bool, PropertyInfo(alias="hasLocation")]
    """Require a non-empty location."""

    has_media: Annotated[bool, PropertyInfo(alias="hasMedia")]
    """Require media."""

    has_website: Annotated[bool, PropertyInfo(alias="hasWebsite")]
    """Require a website on the profile."""

    hide_fake: Annotated[bool, PropertyInfo(alias="hideFake")]
    """Drop accounts with at least 3 of these signs.

    No posts, a default picture, an empty bio, or following at least 100 accounts and 10
    times their followers.
    """

    hide_inactive: Annotated[bool, PropertyInfo(alias="hideInactive")]
    """
    Drop accounts with under 1 post a month since joining that are at least 180 days
    old.
    """

    joined_since: Annotated[Union[str, date], PropertyInfo(alias="joinedSince", format="iso8601")]
    """Keep accounts that joined X on this UTC day or later."""

    joined_until: Annotated[Union[str, date], PropertyInfo(alias="joinedUntil", format="iso8601")]
    """Keep accounts that joined X before this UTC day."""

    lang: str
    """Filter by language code."""

    location: str
    """Keep accounts whose location contains this text."""

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
    """Include results on or after this date, from 00:00 UTC.

    An ISO 8601 time starts at that instant. Results without a post date are left
    out. An empty value sets no filter.
    """

    until_date: Annotated[Union[str, date], PropertyInfo(alias="untilDate", format="iso8601")]
    """Include results on or before this date, inclusive, through 23:59:59 UTC.

    An ISO 8601 time ends at that instant. Results without a post date are left out.
    An empty value sets no filter.
    """

    verified: bool
    """Filter by verified status."""
