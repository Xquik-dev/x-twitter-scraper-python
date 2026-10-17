# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SpaceParticipant", "AffiliatesHighlightedLabel"]


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


class SpaceParticipant(BaseModel):
    """An account on a Space's stage or in its audience, as X lists it there."""

    id: str

    name: str
    """Name the account shows in the Space"""

    username: str

    affiliates_highlighted_label: Optional[AffiliatesHighlightedLabel] = FieldInfo(
        alias="affiliatesHighlightedLabel", default=None
    )
    """Organization affiliation label shown on an X profile."""

    is_blue_verified: Optional[bool] = FieldInfo(alias="isBlueVerified", default=None)
    """Whether the account has X Premium verification"""

    is_muted_by_admin: Optional[bool] = FieldInfo(alias="isMutedByAdmin", default=None)
    """Whether a host muted the account"""

    is_muted_by_guest: Optional[bool] = FieldInfo(alias="isMutedByGuest", default=None)
    """Whether the account muted itself"""

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)
    """Whether X shows a verified badge in the Space"""

    joined_at: Optional[datetime] = FieldInfo(alias="joinedAt", default=None)
    """When the account joined the Space"""

    periscope_user_id: Optional[str] = FieldInfo(alias="periscopeUserId", default=None)
    """The account's ID in X's broadcast service"""

    profile_picture: Optional[str] = FieldInfo(alias="profilePicture", default=None)
    """Profile picture URL"""

    profile_picture_original: Optional[str] = FieldInfo(alias="profilePictureOriginal", default=None)
    """The participant's profile picture at full size"""

    verified_type: Optional[str] = FieldInfo(alias="verifiedType", default=None)
    """Business or Government badge type"""
