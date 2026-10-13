# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["XGetHashflagsResponse", "Hashflag", "HashflagAnimation"]


class HashflagAnimation(BaseModel):
    asset_url: str = FieldInfo(alias="assetUrl")
    """Animation file."""

    context: Optional[str] = None
    """What plays the animation, such as Like."""

    priority: Optional[float] = None
    """X's order among the animations of a hashtag."""


class Hashflag(BaseModel):
    """A custom emoji X shows after a hashtag for a set time."""

    animations: List[HashflagAnimation]
    """Animations X plays for the hashtag, such as on a like. Often empty."""

    asset_url: str = FieldInfo(alias="assetUrl")
    """Image of the emoji."""

    ends_at: datetime = FieldInfo(alias="endsAt")
    """When X stops showing the emoji, in UTC."""

    hashtag: str
    """Hashtag text without the hash sign. X also lists some plain phrases."""

    is_hashfetti_enabled: bool = FieldInfo(alias="isHashfettiEnabled")
    """Whether X marks the hashflag for its hashfetti effect."""

    starts_at: datetime = FieldInfo(alias="startsAt")
    """When X starts showing the emoji, in UTC."""


class XGetHashflagsResponse(BaseModel):
    count: int
    """Hashflags returned & charged."""

    hashflags: List[Hashflag]

    total: int
    """Hashflags that match the filters, before limit."""

    message: Optional[str] = None
    """What to send instead. Present only when no hashflag matches."""
