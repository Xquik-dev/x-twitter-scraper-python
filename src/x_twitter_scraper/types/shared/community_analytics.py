# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .community_analytics_metric import CommunityAnalyticsMetric

__all__ = ["CommunityAnalytics", "Metrics"]


class Metrics(BaseModel):
    """X reports activity counts and percentage changes for its latest period."""

    likes: CommunityAnalyticsMetric
    """Count likes on community posts."""

    new_members: CommunityAnalyticsMetric = FieldInfo(alias="newMembers")
    """Count accounts that joined the community."""

    posts: CommunityAnalyticsMetric
    """Count community posts."""

    replies: CommunityAnalyticsMetric
    """Count replies to community posts."""

    unique_posters: CommunityAnalyticsMetric = FieldInfo(alias="uniquePosters")
    """Count distinct accounts that posted in the community."""


class CommunityAnalytics(BaseModel):
    """X reports community activity and growth for its latest period."""

    id: str
    """Identify the community from your request."""

    metrics: Metrics
    """Read each activity metric's count and percentage change."""

    period_ends_at: datetime = FieldInfo(alias="periodEndsAt")
    """Read when X's latest period ends in UTC."""
