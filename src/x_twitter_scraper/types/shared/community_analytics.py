# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .community_analytics_metric import CommunityAnalyticsMetric

__all__ = ["CommunityAnalytics", "Metrics"]


class Metrics(BaseModel):
    """The period's activity, each metric with its count and changePercent.

    likes counts likes on community posts and newMembers the accounts that joined.
    posts counts the community posts and replies the replies to them. uniquePosters
    counts the distinct accounts that posted.
    """

    likes: CommunityAnalyticsMetric
    """A community metric for X's latest period & its percent change."""

    new_members: CommunityAnalyticsMetric = FieldInfo(alias="newMembers")
    """A community metric for X's latest period & its percent change."""

    posts: CommunityAnalyticsMetric
    """A community metric for X's latest period & its percent change."""

    replies: CommunityAnalyticsMetric
    """A community metric for X's latest period & its percent change."""

    unique_posters: CommunityAnalyticsMetric = FieldInfo(alias="uniquePosters")
    """A community metric for X's latest period & its percent change."""


class CommunityAnalytics(BaseModel):
    """Community activity & growth for X's latest period."""

    id: str
    """The community ID from your request."""

    metrics: Metrics
    """The period's activity, each metric with its count and changePercent.

    likes counts likes on community posts and newMembers the accounts that joined.
    posts counts the community posts and replies the replies to them. uniquePosters
    counts the distinct accounts that posted.
    """

    period_ends_at: datetime = FieldInfo(alias="periodEndsAt")
    """The end of X's latest period, in UTC."""
