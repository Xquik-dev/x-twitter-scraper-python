# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["XAutocompleteSearchResponse", "Cashtag", "Hashtag", "Topic", "User", "UserBadge"]


class Cashtag(BaseModel):
    """A stock or crypto token X suggests for the query."""

    ticker: str
    """Ticker symbol without the $."""

    chain_logo_url: Optional[str] = FieldInfo(alias="chainLogoUrl", default=None)
    """Logo of the token's chain. Tokens only."""

    contract_address: Optional[str] = FieldInfo(alias="contractAddress", default=None)
    """Token contract address. Tokens only."""

    currency: Optional[str] = None
    """Currency of price & marketCap."""

    daily_change_percent: Optional[float] = FieldInfo(alias="dailyChangePercent", default=None)
    """Price change over the last 24 hours, in percent."""

    exchange_short_name: Optional[str] = FieldInfo(alias="exchangeShortName", default=None)
    """Stock exchange. Stocks only."""

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)
    """Logo image URL."""

    market_cap: Optional[str] = FieldInfo(alias="marketCap", default=None)
    """Market capitalization as decimal text."""

    name: Optional[str] = None
    """Company or token name."""

    price: Optional[str] = None
    """Latest price as decimal text, which keeps every digit."""

    smart_tag: Optional[str] = FieldInfo(alias="smartTag", default=None)
    """X's tag for the asset. $TICKER for a stock, chain:contract for a token."""


class Hashtag(BaseModel):
    """A hashtag X suggests for the query."""

    hashtag: str
    """Suggested hashtag, with its"""

    inline: Optional[bool] = None
    """X's inline flag for the hashtag."""

    score: Optional[float] = None
    """X's rounded relevance score for the hashtag."""

    tokens: Optional[List[str]] = None
    """Normalized text tokens X matches the hashtag by."""


class Topic(BaseModel):
    """A search phrase X suggests for the query."""

    topic: str
    """Suggested search phrase."""

    inline: Optional[bool] = None
    """X's inline flag for the phrase."""

    score: Optional[float] = None
    """X's rounded relevance score for the phrase."""

    tokens: Optional[List[str]] = None
    """Normalized text tokens X matches the phrase by."""


class UserBadge(BaseModel):
    """1 affiliation badge."""

    badge_type: Optional[str] = FieldInfo(alias="badgeType", default=None)
    """Kind of badge."""

    badge_url: Optional[str] = FieldInfo(alias="badgeUrl", default=None)
    """Badge image URL."""

    description: Optional[str] = None
    """Name of the affiliated account."""


class User(BaseModel):
    """An account X suggests for the query."""

    id: str
    """X user ID."""

    name: str
    """Display name."""

    username: str
    """Handle without the @."""

    badges: Optional[List[UserBadge]] = None
    """Affiliation badges X shows beside the name."""

    inline: Optional[bool] = None
    """X's inline flag for the account."""

    is_blue_verified: Optional[bool] = FieldInfo(alias="isBlueVerified", default=None)
    """Whether X shows a blue verification badge."""

    is_persona_media_genable: Optional[bool] = FieldInfo(alias="isPersonaMediaGenable", default=None)
    """X's flag for whether media can be generated from this account's persona."""

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)
    """Whether the account holds X's legacy verification."""

    location: Optional[str] = None
    """Public profile location text. Omitted when empty."""

    profile_picture: Optional[str] = FieldInfo(alias="profilePicture", default=None)
    """Avatar URL."""

    protected: Optional[bool] = None
    """Whether the account protects its posts."""

    score: Optional[float] = None
    """X's rounded relevance score for the account."""

    tokens: Optional[List[str]] = None
    """Normalized text tokens X matches the account by."""

    verified: Optional[bool] = None
    """Whether X shows any verification badge."""

    verified_type: Optional[str] = FieldInfo(alias="verifiedType", default=None)
    """Verification category, such as Government or Business.

    Omitted when X names none.
    """


class XAutocompleteSearchResponse(BaseModel):
    """What X suggests for a partial search query.

    Each list keeps X's order. A list is empty when X suggests none of its type or types leaves it out.
    """

    cashtags: List[Cashtag]
    """Suggested stocks & crypto tokens."""

    count: int
    """Suggestions returned across all 4 lists. Each costs 1 credit."""

    hashtags: List[Hashtag]
    """Suggested hashtags."""

    query: str
    """The query you sent, trimmed."""

    topics: List[Topic]
    """Suggested search phrases that are not hashtags."""

    users: List[User]
    """Suggested accounts."""
