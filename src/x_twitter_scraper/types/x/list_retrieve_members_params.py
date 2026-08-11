# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ListRetrieveMembersParams"]


class ListRetrieveMembersParams(TypedDict, total=False):
    bio_contains: Annotated[str, PropertyInfo(alias="bioContains")]
    """Match any comma-separated or line-separated bio term, ignoring case."""

    cursor: str
    """Pagination cursor for list members"""

    has_location: Annotated[bool, PropertyInfo(alias="hasLocation")]
    """Only return profiles with a location."""

    has_website: Annotated[bool, PropertyInfo(alias="hasWebsite")]
    """Only return profiles with a website."""

    location_contains: Annotated[str, PropertyInfo(alias="locationContains")]
    """Match a location substring, ignoring case."""

    max_followers: Annotated[int, PropertyInfo(alias="maxFollowers")]
    """Maximum follower count. Missing counts pass this maximum."""

    max_following: Annotated[int, PropertyInfo(alias="maxFollowing")]
    """Maximum following count."""

    max_statuses: Annotated[int, PropertyInfo(alias="maxStatuses")]
    """Maximum post count. maxPosts is also accepted."""

    min_account_age_days: Annotated[int, PropertyInfo(alias="minAccountAgeDays")]
    """Minimum account age in whole days."""

    min_followers: Annotated[int, PropertyInfo(alias="minFollowers")]
    """Minimum follower count. Filtering happens before billing."""

    min_following: Annotated[int, PropertyInfo(alias="minFollowing")]
    """Minimum following count."""

    min_statuses: Annotated[int, PropertyInfo(alias="minStatuses")]
    """Minimum post count. minPosts is also accepted."""

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Members per page (20-200, default 20)"""

    username_contains: Annotated[str, PropertyInfo(alias="usernameContains")]
    """Match a username substring, ignoring case."""

    verified_only: Annotated[bool, PropertyInfo(alias="verifiedOnly")]
    """Only return verified profiles."""

    verified_type: Annotated[str, PropertyInfo(alias="verifiedType")]
    """Match the verification type exactly, ignoring case."""
