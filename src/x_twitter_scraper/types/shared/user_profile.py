# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UserProfile"]


class UserProfile(BaseModel):
    """X user profile with bio, follower counts, and verification status."""

    id: str

    name: str

    username: str

    automated_by: Optional[str] = FieldInfo(alias="automatedBy", default=None)

    can_dm: Optional[bool] = FieldInfo(alias="canDm", default=None)

    community_role: Optional[str] = FieldInfo(alias="communityRole", default=None)
    """Community role when returned by community member reads"""

    cover_picture: Optional[str] = FieldInfo(alias="coverPicture", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    favourites_count: Optional[int] = FieldInfo(alias="favouritesCount", default=None)

    followers: Optional[int] = None

    following: Optional[int] = None

    has_custom_timelines: Optional[bool] = FieldInfo(alias="hasCustomTimelines", default=None)

    is_automated: Optional[bool] = FieldInfo(alias="isAutomated", default=None)

    is_blue_verified: Optional[bool] = FieldInfo(alias="isBlueVerified", default=None)
    """Whether X shows a blue verification badge"""

    is_translator: Optional[bool] = FieldInfo(alias="isTranslator", default=None)

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)
    """Whether X marks the profile as verified"""

    location: Optional[str] = None

    media_count: Optional[int] = FieldInfo(alias="mediaCount", default=None)

    pinned_tweet_ids: Optional[List[str]] = FieldInfo(alias="pinnedTweetIds", default=None)

    possibly_sensitive: Optional[bool] = FieldInfo(alias="possiblySensitive", default=None)

    profile_bio: Optional[Dict[str, object]] = None
    """Structured profile bio with entity annotations"""

    profile_banner_url: Optional[str] = FieldInfo(alias="profileBannerUrl", default=None)
    """Original X profile banner field when available"""

    profile_picture: Optional[str] = FieldInfo(alias="profilePicture", default=None)

    protected: Optional[bool] = None
    """Whether the profile protects its posts"""

    statuses_count: Optional[int] = FieldInfo(alias="statusesCount", default=None)

    unavailable: Optional[bool] = None

    unavailable_reason: Optional[str] = FieldInfo(alias="unavailableReason", default=None)

    url: Optional[str] = None

    verified: Optional[bool] = None

    verified_type: Optional[str] = FieldInfo(alias="verifiedType", default=None)

    viewer_followed_by: Optional[bool] = FieldInfo(alias="viewerFollowedBy", default=None)
    """Whether this profile follows the authenticated viewer"""

    viewer_following: Optional[bool] = FieldInfo(alias="viewerFollowing", default=None)
    """Whether the authenticated viewer follows this profile"""

    withheld_in_countries: Optional[List[str]] = FieldInfo(alias="withheldInCountries", default=None)
