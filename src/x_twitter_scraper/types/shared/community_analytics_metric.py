# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CommunityAnalyticsMetric"]


class CommunityAnalyticsMetric(BaseModel):
    """A community metric for X's latest period & its percent change."""

    change_percent: float = FieldInfo(alias="changePercent")
    """Change in percent from the same figure 1 day earlier. Values stay unrounded."""

    count: int
    """Total for this metric during X's latest period."""
