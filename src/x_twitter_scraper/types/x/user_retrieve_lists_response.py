# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.user_profile import UserProfile

__all__ = [
    "UserRetrieveListsResponse",
    "XList",
    "XListCustomBanner",
    "XListCustomBannerPalette",
    "XListCustomBannerPaletteRgb",
    "XListCustomBannerSalientRect",
    "XListDefaultBanner",
    "XListDefaultBannerPalette",
    "XListDefaultBannerPaletteRgb",
    "XListDefaultBannerSalientRect",
]


class XListCustomBannerPaletteRgb(BaseModel):
    """The color's red, green and blue values."""

    blue: Optional[int] = None

    green: Optional[int] = None

    red: Optional[int] = None


class XListCustomBannerPalette(BaseModel):
    percentage: Optional[float] = None
    """Share of the banner"""

    rgb: Optional[XListCustomBannerPaletteRgb] = None
    """The color's red, green and blue values."""


class XListCustomBannerSalientRect(BaseModel):
    """Area X marks as the subject of the banner, in pixels."""

    height: Optional[int] = None
    """Height of the marked area."""

    left: Optional[int] = None
    """Pixels from the banner's left."""

    top: Optional[int] = None
    """Pixels from the banner's top."""

    width: Optional[int] = None
    """Width of the marked area."""


class XListCustomBanner(BaseModel):
    """Banner the owner uploaded."""

    url: str
    """Banner image URL."""

    height: Optional[int] = None
    """Banner height in pixels."""

    media_id: Optional[str] = FieldInfo(alias="mediaId", default=None)
    """Media ID of an uploaded banner."""

    media_key: Optional[str] = FieldInfo(alias="mediaKey", default=None)
    """Stable media key of an uploaded banner."""

    palette: Optional[List[XListCustomBannerPalette]] = None
    """Dominant colors of an uploaded banner and their shares."""

    salient_rect: Optional[XListCustomBannerSalientRect] = FieldInfo(alias="salientRect", default=None)
    """Area X marks as the subject of the banner, in pixels."""

    width: Optional[int] = None
    """Banner width in pixels."""


class XListDefaultBannerPaletteRgb(BaseModel):
    """The color's red, green and blue values."""

    blue: Optional[int] = None

    green: Optional[int] = None

    red: Optional[int] = None


class XListDefaultBannerPalette(BaseModel):
    percentage: Optional[float] = None
    """Share of the banner"""

    rgb: Optional[XListDefaultBannerPaletteRgb] = None
    """The color's red, green and blue values."""


class XListDefaultBannerSalientRect(BaseModel):
    """Area X marks as the subject of the banner, in pixels."""

    height: Optional[int] = None
    """Height of the marked area."""

    left: Optional[int] = None
    """Pixels from the banner's left."""

    top: Optional[int] = None
    """Pixels from the banner's top."""

    width: Optional[int] = None
    """Width of the marked area."""


class XListDefaultBanner(BaseModel):
    """Banner X shows when the owner uploaded none.

    X picks it per reading account, so 2 calls can return different ones.
    """

    url: str
    """Banner image URL."""

    height: Optional[int] = None
    """Banner height in pixels."""

    media_id: Optional[str] = FieldInfo(alias="mediaId", default=None)
    """Media ID of an uploaded banner."""

    media_key: Optional[str] = FieldInfo(alias="mediaKey", default=None)
    """Stable media key of an uploaded banner."""

    palette: Optional[List[XListDefaultBannerPalette]] = None
    """Dominant colors of an uploaded banner and their shares."""

    salient_rect: Optional[XListDefaultBannerSalientRect] = FieldInfo(alias="salientRect", default=None)
    """Area X marks as the subject of the banner, in pixels."""

    width: Optional[int] = None
    """Banner width in pixels."""


class XList(BaseModel):
    """Public X List with its owner's public profile.

    Leaves out what X tells the reading account, such as whether it follows the List.
    """

    id: str
    """Numeric ID of the List."""

    name: str
    """Name the owner gave the List."""

    banner_url: Optional[str] = FieldInfo(alias="bannerUrl", default=None)
    """URL of the banner the owner uploaded. Absent when the owner uploaded none."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """When the owner made the List."""

    custom_banner: Optional[XListCustomBanner] = FieldInfo(alias="customBanner", default=None)
    """Banner the owner uploaded."""

    default_banner: Optional[XListDefaultBanner] = FieldInfo(alias="defaultBanner", default=None)
    """Banner X shows when the owner uploaded none.

    X picks it per reading account, so 2 calls can return different ones.
    """

    description: Optional[str] = None
    """About text of the List. Empty when the owner wrote none."""

    facepile_urls: Optional[List[str]] = FieldInfo(alias="facepileUrls", default=None)
    """Avatar URLs of a few List members, which X may pick per request."""

    member_count: Optional[int] = FieldInfo(alias="memberCount", default=None)
    """Accounts on the List."""

    members_context: Optional[str] = FieldInfo(alias="membersContext", default=None)
    """Member count as X words it, such as 35 members."""

    owner: Optional[UserProfile] = None
    """Public profile of the account that owns the List."""

    subscriber_count: Optional[int] = FieldInfo(alias="subscriberCount", default=None)
    """Accounts that follow the List, which X calls followers."""

    url: Optional[str] = None
    """List page on x.com."""


class UserRetrieveListsResponse(BaseModel):
    """One page of public X Lists.

    Follow next_cursor while the response reports more pages. Each returned List costs 1 credit.
    """

    has_next_page: bool

    lists: List[XList]

    next_cursor: str
