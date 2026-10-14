# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CommunityRetrieveModeratorsParams"]


class CommunityRetrieveModeratorsParams(TypedDict, total=False):
    bio_contains: Annotated[str, PropertyInfo(alias="bioContains")]
    """Match any comma-separated or line-separated bio term, ignoring case."""

    blue_verified_only: Annotated[bool, PropertyInfo(alias="blueVerifiedOnly")]
    """Only return profiles X marks as blue verified.

    X marks many business & government accounts blue too. Use verifiedType for 1
    badge type.
    """

    business_email_only: Annotated[bool, PropertyInfo(alias="businessEmailOnly")]
    """Only return profiles that publish an email outside free webmail, such as Gmail."""

    cursor: str
    """Pagination cursor for collection results.

    Also read as next_cursor, next_token, pagination_token or continuation_token.
    """

    email_domains: Annotated[str, PropertyInfo(alias="emailDomains")]
    """Only return profiles with an email at one of these domains.

    Separate domains with commas. Subdomains match.
    """

    fields: str
    """Fields to keep in each row, comma-separated.

    Use dots for nested fields, such as author.username. A list keeps the field in
    each item. Case & underscores do not matter. A row that lacks a field leaves it
    out. Cursors, counts & diagnostics always stay. An unknown name answers 400
    unknown_field with the valid names, before any read. The price stays the same.
    SDK row types then hold only the named fields.
    """

    has_email: Annotated[bool, PropertyInfo(alias="hasEmail")]
    """Only return profiles that publish an email."""

    has_location: Annotated[bool, PropertyInfo(alias="hasLocation")]
    """Only return profiles with a location."""

    has_website: Annotated[bool, PropertyInfo(alias="hasWebsite")]
    """Only return profiles with a website."""

    location_contains: Annotated[str, PropertyInfo(alias="locationContains")]
    """Match a location substring, ignoring case."""

    max_followers: Annotated[int, PropertyInfo(alias="maxFollowers")]
    """Maximum follower count. Missing counts pass this maximum."""

    max_following: Annotated[int, PropertyInfo(alias="maxFollowing")]
    """Profiles may follow at most this many accounts."""

    max_statuses: Annotated[int, PropertyInfo(alias="maxStatuses")]
    """Maximum post count. maxPosts is also accepted."""

    min_account_age_days: Annotated[int, PropertyInfo(alias="minAccountAgeDays")]
    """Minimum account age in whole days."""

    min_followers: Annotated[int, PropertyInfo(alias="minFollowers")]
    """Minimum follower count. Filtering happens before billing."""

    min_following: Annotated[int, PropertyInfo(alias="minFollowing")]
    """Profiles must follow at least this many accounts."""

    min_statuses: Annotated[int, PropertyInfo(alias="minStatuses")]
    """Minimum post count. minPosts is also accepted."""

    omit: str
    """Fields to drop from each row, comma-separated.

    It takes the same names as fields. With fields, it drops from the kept fields.
    """

    username_contains: Annotated[str, PropertyInfo(alias="usernameContains")]
    """Match a username substring, ignoring case."""

    verified_only: Annotated[bool, PropertyInfo(alias="verifiedOnly")]
    """Only return verified profiles."""

    verified_type: Annotated[str, PropertyInfo(alias="verifiedType")]
    """Match the verification type exactly, ignoring case."""
