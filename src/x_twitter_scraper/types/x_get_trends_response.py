# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["XGetTrendsResponse", "Trend"]


class Trend(BaseModel):
    name: str

    description: Optional[str] = None

    promoted_content: Optional[str] = FieldInfo(alias="promotedContent", default=None)
    """Promotion identifier from X. Null for organic trends."""

    query: Optional[str] = None

    rank: Optional[int] = None

    tweet_volume: Optional[int] = FieldInfo(alias="tweetVolume", default=None)
    """Approximate public post volume when X supplies it."""

    url: Optional[str] = None
    """X search URL for the trend."""


class XGetTrendsResponse(BaseModel):
    count: int

    trends: List[Trend]

    woeid: int
