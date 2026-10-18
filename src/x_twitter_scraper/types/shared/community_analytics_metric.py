# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CommunityAnalyticsMetric"]


class CommunityAnalyticsMetric(BaseModel):
    """X reports each metric's count and percentage change for its latest period."""

    change_percent: float = FieldInfo(alias="changePercent")
    """Read the unrounded percentage change from one day earlier."""

    count: int
    """Read this metric's total for X's latest period."""
