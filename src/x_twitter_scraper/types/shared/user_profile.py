# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UserProfile", "AffiliatesHighlightedLabel", "HighlightsInfo", "IdentityVerification"]


class AffiliatesHighlightedLabel(BaseModel):
    """Organization affiliation label shown on an X profile."""

    badge_url: Optional[str] = FieldInfo(alias="badgeUrl", default=None)

    description: Optional[str] = None

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)

    user_label_display_type: Optional[str] = FieldInfo(alias="userLabelDisplayType", default=None)

    user_label_type: Optional[str] = FieldInfo(alias="userLabelType", default=None)


class HighlightsInfo(BaseModel):
    """Profile highlight availability and count metadata."""

    can_highlight_tweets: Optional[bool] = FieldInfo(alias="canHighlightTweets", default=None)

    highlighted_tweets: Optional[str] = FieldInfo(alias="highlightedTweets", default=None)


class IdentityVerification(BaseModel):
    """Identity verification metadata displayed by X."""

    description: Optional[str] = None

    is_identity_verified: Optional[bool] = FieldInfo(alias="isIdentityVerified", default=None)

    verified_since_msec: Optional[str] = FieldInfo(alias="verifiedSinceMsec", default=None)


class UserProfile(BaseModel):
    """X user profile with bio, follower counts, and verification status."""

    id: str

    name: str

    username: str

    affiliates_highlighted_label: Optional[AffiliatesHighlightedLabel] = FieldInfo(
        alias="affiliatesHighlightedLabel", default=None
    )
    """Organization affiliation label shown on an X profile."""

    automated_by: Optional[str] = FieldInfo(alias="automatedBy", default=None)

    business_account_affiliates_count: Optional[int] = FieldInfo(alias="businessAccountAffiliatesCount", default=None)

    community_role: Optional[str] = FieldInfo(alias="communityRole", default=None)
    """Community role when returned by community member reads"""

    cover_picture: Optional[str] = FieldInfo(alias="coverPicture", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    creator_subscriptions_count: Optional[int] = FieldInfo(alias="creatorSubscriptionsCount", default=None)

    description: Optional[str] = None

    favourites_count: Optional[int] = FieldInfo(alias="favouritesCount", default=None)

    followers: Optional[int] = None

    following: Optional[int] = None

    has_custom_timelines: Optional[bool] = FieldInfo(alias="hasCustomTimelines", default=None)

    has_graduated_access: Optional[bool] = FieldInfo(alias="hasGraduatedAccess", default=None)

    has_hidden_subscriptions_on_profile: Optional[bool] = FieldInfo(
        alias="hasHiddenSubscriptionsOnProfile", default=None
    )

    highlights_info: Optional[HighlightsInfo] = FieldInfo(alias="highlightsInfo", default=None)
    """Profile highlight availability and count metadata."""

    identity_verification: Optional[IdentityVerification] = FieldInfo(alias="identityVerification", default=None)
    """Identity verification metadata displayed by X."""

    is_automated: Optional[bool] = FieldInfo(alias="isAutomated", default=None)

    is_blue_verified: Optional[bool] = FieldInfo(alias="isBlueVerified", default=None)
    """Whether X shows a blue verification badge"""

    is_profile_translatable: Optional[bool] = FieldInfo(alias="isProfileTranslatable", default=None)

    is_translator: Optional[bool] = FieldInfo(alias="isTranslator", default=None)

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)
    """Whether X marks the profile as verified"""

    location: Optional[str] = None

    media_count: Optional[int] = FieldInfo(alias="mediaCount", default=None)

    parody_commentary_fan_label: Optional[str] = FieldInfo(alias="parodyCommentaryFanLabel", default=None)

    pinned_tweet_ids: Optional[List[str]] = FieldInfo(alias="pinnedTweetIds", default=None)

    possibly_sensitive: Optional[bool] = FieldInfo(alias="possiblySensitive", default=None)

    profile_bio: Optional[Dict[str, object]] = None
    """Structured profile bio with entity annotations"""

    profile_banner_url: Optional[str] = FieldInfo(alias="profileBannerUrl", default=None)
    """Original X profile banner field when available"""

    profile_description_language: Optional[str] = FieldInfo(alias="profileDescriptionLanguage", default=None)

    profile_image_shape: Optional[str] = FieldInfo(alias="profileImageShape", default=None)

    profile_interstitial_type: Optional[str] = FieldInfo(alias="profileInterstitialType", default=None)

    profile_picture: Optional[str] = FieldInfo(alias="profilePicture", default=None)

    profile_sort_enabled: Optional[bool] = FieldInfo(alias="profileSortEnabled", default=None)

    profile_translator_type: Optional[str] = FieldInfo(alias="profileTranslatorType", default=None)

    protected: Optional[bool] = None
    """Whether the profile protects its posts"""

    statuses_count: Optional[int] = FieldInfo(alias="statusesCount", default=None)

    super_follow_eligible: Optional[bool] = FieldInfo(alias="superFollowEligible", default=None)

    unavailable: Optional[bool] = None

    unavailable_reason: Optional[str] = FieldInfo(alias="unavailableReason", default=None)

    url: Optional[str] = None

    verified: Optional[bool] = None

    verified_type: Optional[str] = FieldInfo(alias="verifiedType", default=None)

    withheld_in_countries: Optional[List[str]] = FieldInfo(alias="withheldInCountries", default=None)
