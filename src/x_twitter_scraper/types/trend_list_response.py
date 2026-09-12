# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TrendListResponse", "Trend"]


class Trend(BaseModel):
    name: str

    description: Optional[str] = None

    promoted_content: Optional[str] = FieldInfo(alias="promotedContent", default=None)
    """Promotion ID for this trend, or null when organic."""

    query: Optional[str] = None

    rank: Optional[int] = None

    tweet_volume: Optional[int] = FieldInfo(alias="tweetVolume", default=None)
    """Estimated post volume for this trend."""

    url: Optional[str] = None
    """Search URL associated with this trend."""


class TrendListResponse(BaseModel):
    total: int

    trends: List[Trend]

    woeid: int
