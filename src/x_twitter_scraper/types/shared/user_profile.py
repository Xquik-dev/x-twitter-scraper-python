# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "UserProfile",
    "AccountBasedIn",
    "AffiliatesHighlightedLabel",
    "HighlightsInfo",
    "IdentityVerification",
    "TipJar",
]


class AccountBasedIn(BaseModel):
    """
    X's best-effort public label inferred from aggregated account-access IP addresses. It does not state nationality, residence, identity, registration, post location, or exact location.
    """

    level: Literal["country", "region"]

    observed_at: datetime = FieldInfo(alias="observedAt")

    value: str


class AffiliatesHighlightedLabel(BaseModel):
    """Organization affiliation label shown on an X profile."""

    badge_url: Optional[str] = FieldInfo(alias="badgeUrl", default=None)

    description: Optional[str] = None

    long_description: Optional[Dict[str, object]] = FieldInfo(alias="longDescription", default=None)
    """Public text, ranges, references, and mention data."""

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


class TipJar(BaseModel):
    """Public payment and creator-support handles shown on X."""

    bandcamp_handle: Optional[str] = FieldInfo(alias="bandcampHandle", default=None)

    bitcoin_handle: Optional[str] = FieldInfo(alias="bitcoinHandle", default=None)

    cash_app_handle: Optional[str] = FieldInfo(alias="cashAppHandle", default=None)

    ethereum_handle: Optional[str] = FieldInfo(alias="ethereumHandle", default=None)

    gofundme_handle: Optional[str] = FieldInfo(alias="gofundmeHandle", default=None)

    is_enabled: Optional[bool] = FieldInfo(alias="isEnabled", default=None)

    patreon_handle: Optional[str] = FieldInfo(alias="patreonHandle", default=None)

    pay_pal_handle: Optional[str] = FieldInfo(alias="payPalHandle", default=None)

    venmo_handle: Optional[str] = FieldInfo(alias="venmoHandle", default=None)


class UserProfile(BaseModel):
    """Public X profile."""

    id: str

    name: str

    username: str

    account_based_in: Optional[AccountBasedIn] = FieldInfo(alias="accountBasedIn", default=None)
    """
    X's best-effort public label inferred from aggregated account-access IP
    addresses. It does not state nationality, residence, identity, registration,
    post location, or exact location.
    """

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

    grok_translated_bio: Optional[Dict[str, object]] = FieldInfo(alias="grokTranslatedBio", default=None)
    """Public profile bio translation returned by X"""

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
    """Account owner's public profile location text"""

    media_count: Optional[int] = FieldInfo(alias="mediaCount", default=None)

    parody_commentary_fan_label: Optional[str] = FieldInfo(alias="parodyCommentaryFanLabel", default=None)

    pinned_tweet_ids: Optional[List[str]] = FieldInfo(alias="pinnedTweetIds", default=None)

    possibly_sensitive: Optional[bool] = FieldInfo(alias="possiblySensitive", default=None)

    professional: Optional[Dict[str, object]] = None
    """Professional metadata with category display settings"""

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

    retweeted_at: Optional[datetime] = FieldInfo(alias="retweetedAt", default=None)
    """UTC repost time with includeRetweetTimestamp.

    Null if the newest profile page has no match or lookup failed; otherwise
    omitted.
    """

    statuses_count: Optional[int] = FieldInfo(alias="statusesCount", default=None)

    super_follow_eligible: Optional[bool] = FieldInfo(alias="superFollowEligible", default=None)

    super_follows_user_profile_active: Optional[bool] = FieldInfo(alias="superFollowsUserProfileActive", default=None)
    """Whether X marks the subscription profile as active."""

    tip_jar: Optional[TipJar] = FieldInfo(alias="tipJar", default=None)
    """Public payment and creator-support handles shown on X."""

    unavailable: Optional[bool] = None

    unavailable_reason: Optional[str] = FieldInfo(alias="unavailableReason", default=None)

    url: Optional[str] = None

    verified: Optional[bool] = None

    verified_type: Optional[str] = FieldInfo(alias="verifiedType", default=None)

    withheld_in_countries: Optional[List[str]] = FieldInfo(alias="withheldInCountries", default=None)

    withheld_scope: Optional[str] = FieldInfo(alias="withheldScope", default=None)
    """Whether X withholds a post or user"""
