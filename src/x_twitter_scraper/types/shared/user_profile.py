# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "UserProfile",
    "AccountBasedIn",
    "AffiliatesHighlightedLabel",
    "Birthdate",
    "ContactInfo",
    "ContactInfoEmail",
    "ContactInfoLink",
    "ContactInfoPhone",
    "HighlightsInfo",
    "IdentityVerification",
    "TipJar",
    "UsernameChanges",
    "VerificationReason",
    "VerificationReasonEntity",
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


class Birthdate(BaseModel):
    """The parts of the birthday the account made public."""

    day: Optional[int] = None

    month: Optional[int] = None

    year: Optional[int] = None


class ContactInfoEmail(BaseModel):
    domain: str
    """The part after the @ sign."""

    source: Literal["bio", "name", "location"]
    """Profile field that holds the email."""

    value: str
    """The email address."""

    written_as: Optional[str] = FieldInfo(alias="writtenAs", default=None)
    """The account's own spelling, sent when it spelled the email out."""


class ContactInfoLink(BaseModel):
    network: str
    """Site the link belongs to, such as `linkedin`, `github` or `telegram`.

    Any other site is `website`.
    """

    source: Literal["url", "bio"]
    """`url` for the website field, `bio` for a bio link."""

    url: str
    """The link, as X expands it."""


class ContactInfoPhone(BaseModel):
    source: Literal["bio", "name", "location", "url"]
    """Profile field that holds the number."""

    value: str
    """The digits, with a leading + when the account wrote a country code."""

    written_as: Optional[str] = FieldInfo(alias="writtenAs", default=None)
    """The account's own spelling of the number."""


class ContactInfo(BaseModel):
    """Emails, phone numbers & links the account publishes on its own profile.

    Omitted when it publishes none.
    """

    emails: Optional[List[ContactInfoEmail]] = None
    """Emails in the bio, name or location, lowercased."""

    links: Optional[List[ContactInfoLink]] = None
    """The profile's website & the links in its bio."""

    phones: Optional[List[ContactInfoPhone]] = None
    """Phone numbers on the profile. Only a spelling that can be nothing else counts."""


class HighlightsInfo(BaseModel):
    """Profile highlight availability and count metadata."""

    can_highlight_tweets: Optional[bool] = FieldInfo(alias="canHighlightTweets", default=None)

    highlighted_tweets: Optional[str] = FieldInfo(alias="highlightedTweets", default=None)


class IdentityVerification(BaseModel):
    """Identity verification X shows on the profile & its About page."""

    description: Optional[str] = None

    is_identity_verified: Optional[bool] = FieldInfo(alias="isIdentityVerified", default=None)
    """Whether the owner verified their ID with X."""

    override_verified_year: Optional[int] = FieldInfo(alias="overrideVerifiedYear", default=None)
    """The year X shows as the start of verification, in place of verifiedSinceMsec."""

    verified_since_msec: Optional[str] = FieldInfo(alias="verifiedSinceMsec", default=None)
    """When X verified the account, in milliseconds since 1970, as text."""


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


class UsernameChanges(BaseModel):
    """How often the account changed its username."""

    count: int
    """Whole number from 0."""

    last_changed_at: Optional[datetime] = FieldInfo(alias="lastChangedAt", default=None)
    """Time of the latest change, omitted when there is none."""


class VerificationReasonEntity(BaseModel):
    from_index: Optional[int] = FieldInfo(alias="fromIndex", default=None)
    """Whole number from 0."""

    to_index: Optional[int] = FieldInfo(alias="toIndex", default=None)
    """Whole number from 0."""

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)


class VerificationReason(BaseModel):
    """X's text on why the profile is verified, with its links."""

    entities: Optional[List[VerificationReasonEntity]] = None
    """Links inside the text, by character range."""

    text: Optional[str] = None


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

    account_based_in_accurate: Optional[bool] = FieldInfo(alias="accountBasedInAccurate", default=None)
    """False when X notes accountBasedIn may be inaccurate."""

    account_based_in_unavailable: Optional[bool] = FieldInfo(alias="accountBasedInUnavailable", default=None)
    """True when X withheld accountBasedIn from this read. Retry later."""

    advertiser_account_service_levels: Optional[List[str]] = FieldInfo(
        alias="advertiserAccountServiceLevels", default=None
    )
    """X Ads services the account uses, such as `analytics`, `media_studio` or `smb`.

    Empty for an account without ads.
    """

    advertiser_account_type: Optional[str] = FieldInfo(alias="advertiserAccountType", default=None)
    """The account's X Ads type.

    `none` for an account without ads, or `promotable_user` for one that may run
    them.
    """

    affiliates_highlighted_label: Optional[AffiliatesHighlightedLabel] = FieldInfo(
        alias="affiliatesHighlightedLabel", default=None
    )
    """Organization affiliation label shown on an X profile."""

    affiliate_username: Optional[str] = FieldInfo(alias="affiliateUsername", default=None)
    """
    Handle of the organization X shows the account is affiliated with, from its
    About page.
    """

    automated_by: Optional[str] = FieldInfo(alias="automatedBy", default=None)

    birthdate: Optional[Birthdate] = None
    """The parts of the birthday the account made public."""

    business_account_affiliates_count: Optional[int] = FieldInfo(alias="businessAccountAffiliatesCount", default=None)
    """Whole number from 0."""

    business_profile_state: Optional[str] = FieldInfo(alias="businessProfileState", default=None)
    """Whether X treats the profile as a business profile. `none` or `enabled`."""

    community_role: Optional[str] = FieldInfo(alias="communityRole", default=None)
    """Community role when returned by community member reads"""

    connected_via: Optional[str] = FieldInfo(alias="connectedVia", default=None)
    """How the account first connected to X."""

    connected_via_accurate: Optional[bool] = FieldInfo(alias="connectedViaAccurate", default=None)
    """False when X notes that country may be inaccurate."""

    contact_info: Optional[ContactInfo] = FieldInfo(alias="contactInfo", default=None)
    """Emails, phone numbers & links the account publishes on its own profile.

    Omitted when it publishes none.
    """

    cover_picture: Optional[str] = FieldInfo(alias="coverPicture", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)
    """Account creation time."""

    creator_subscriptions_count: Optional[int] = FieldInfo(alias="creatorSubscriptionsCount", default=None)
    """Whole number from 0."""

    default_profile: Optional[bool] = FieldInfo(alias="defaultProfile", default=None)
    """Whether the profile keeps X's default theme."""

    default_profile_image: Optional[bool] = FieldInfo(alias="defaultProfileImage", default=None)
    """Whether the profile keeps X's default avatar."""

    description: Optional[str] = None

    email: Optional[str] = None
    """First email the account publishes on its profile, lowercased.

    Omitted when it publishes none.
    """

    fast_followers_count: Optional[int] = FieldInfo(alias="fastFollowersCount", default=None)
    """Followers X counts as fast followers."""

    favourites_count: Optional[int] = FieldInfo(alias="favouritesCount", default=None)

    followers: Optional[int] = None
    """
    Omitted when X sends no count, as for the account that first posted reused
    media.
    """

    following: Optional[int] = None

    geo_enabled: Optional[bool] = FieldInfo(alias="geoEnabled", default=None)
    """Whether the profile may add a location to posts."""

    grok_translated_bio: Optional[Dict[str, object]] = FieldInfo(alias="grokTranslatedBio", default=None)
    """Public profile bio translation returned by X"""

    has_custom_timelines: Optional[bool] = FieldInfo(alias="hasCustomTimelines", default=None)

    has_extended_profile: Optional[bool] = FieldInfo(alias="hasExtendedProfile", default=None)
    """Whether the profile filled X's extended fields, such as a birth date.

    True or false.
    """

    has_graduated_access: Optional[bool] = FieldInfo(alias="hasGraduatedAccess", default=None)

    has_hidden_subscriptions_on_profile: Optional[bool] = FieldInfo(
        alias="hasHiddenSubscriptionsOnProfile", default=None
    )

    highlights_info: Optional[HighlightsInfo] = FieldInfo(alias="highlightsInfo", default=None)
    """Profile highlight availability and count metadata."""

    identity_verification: Optional[IdentityVerification] = FieldInfo(alias="identityVerification", default=None)
    """Identity verification X shows on the profile & its About page."""

    is_automated: Optional[bool] = FieldInfo(alias="isAutomated", default=None)

    is_blue_verified: Optional[bool] = FieldInfo(alias="isBlueVerified", default=None)
    """Whether X shows a blue verification badge"""

    is_profile_translatable: Optional[bool] = FieldInfo(alias="isProfileTranslatable", default=None)

    is_translation_enabled: Optional[bool] = FieldInfo(alias="isTranslationEnabled", default=None)
    """Whether the account turned on X's translation of its posts. True or false."""

    is_translator: Optional[bool] = FieldInfo(alias="isTranslator", default=None)

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)
    """Whether X marks the profile as verified"""

    listed_count: Optional[int] = FieldInfo(alias="listedCount", default=None)
    """Public lists that include the profile."""

    location: Optional[str] = None
    """Account owner's public profile location text"""

    media_count: Optional[int] = FieldInfo(alias="mediaCount", default=None)

    normal_followers_count: Optional[int] = FieldInfo(alias="normalFollowersCount", default=None)
    """Followers minus fast followers."""

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

    profile_picture_original: Optional[str] = FieldInfo(alias="profilePictureOriginal", default=None)
    """The same profile picture at full size, as the account uploaded it.

    Download this one for the image.
    """

    profile_sort_enabled: Optional[bool] = FieldInfo(alias="profileSortEnabled", default=None)

    profile_translator_type: Optional[str] = FieldInfo(alias="profileTranslatorType", default=None)

    protected: Optional[bool] = None
    """Whether the profile protects its posts"""

    redirects_to_username: Optional[str] = FieldInfo(alias="redirectsToUsername", default=None)
    """
    Handle x.com sends this profile's visitors to, such as the new handle of a
    renamed account whose old handle now holds a placeholder. Missing when x.com
    shows the profile itself.
    """

    retweeted_at: Optional[datetime] = FieldInfo(alias="retweetedAt", default=None)
    """UTC repost time with includeRetweetTimestamp.

    Null if the newest profile page has no match or lookup failed; otherwise
    omitted.
    """

    statuses_count: Optional[int] = FieldInfo(alias="statusesCount", default=None)

    subscribers_count: Optional[int] = FieldInfo(alias="subscribersCount", default=None)
    """Accounts subscribed to the profile's paid Subscriptions. 0 when it has none."""

    super_follow_eligible: Optional[bool] = FieldInfo(alias="superFollowEligible", default=None)

    super_follows_user_profile_active: Optional[bool] = FieldInfo(alias="superFollowsUserProfileActive", default=None)
    """Whether X marks the subscription profile as active."""

    tip_jar: Optional[TipJar] = FieldInfo(alias="tipJar", default=None)
    """Public payment and creator-support handles shown on X."""

    unavailable: Optional[bool] = None

    unavailable_reason: Optional[str] = FieldInfo(alias="unavailableReason", default=None)

    url: Optional[str] = None

    username_changes: Optional[UsernameChanges] = FieldInfo(alias="usernameChanges", default=None)
    """How often the account changed its username."""

    verification_reason: Optional[VerificationReason] = FieldInfo(alias="verificationReason", default=None)
    """X's text on why the profile is verified, with its links."""

    verified: Optional[bool] = None

    verified_type: Optional[str] = FieldInfo(alias="verifiedType", default=None)

    withheld_in_countries: Optional[List[str]] = FieldInfo(alias="withheldInCountries", default=None)

    withheld_scope: Optional[str] = FieldInfo(alias="withheldScope", default=None)
    """Whether X withholds a post or user"""
