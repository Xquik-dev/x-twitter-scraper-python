# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TweetGetInsightsResponse", "Insights", "InsightsMetrics"]


class InsightsMetrics(BaseModel):
    """The public counts of one tweet."""

    bookmarks: float
    """Bookmarks."""

    likes: float
    """Likes."""

    quotes: float
    """Quotes."""

    replies: float
    """Replies."""

    reposts: float
    """Reposts."""

    views: float
    """Views."""


class Insights(BaseModel):
    """Engagement insights of one tweet.

    Engagements are likes, replies, reposts and quotes. A rate is null when nothing divides it, such as a tweet without views.
    """

    age_hours: Optional[float] = FieldInfo(alias="ageHours", default=None)
    """Hours since the tweet went up."""

    amplification: Optional[float] = None
    """Reposts and quotes per like."""

    author_id: Optional[str] = FieldInfo(alias="authorId", default=None)
    """ID of the author."""

    author_user_name: Optional[str] = FieldInfo(alias="authorUserName", default=None)
    """Username of the author."""

    conversation: Optional[float] = None
    """Replies per like."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """When the tweet went up."""

    engagement_per_view: Optional[float] = FieldInfo(alias="engagementPerView", default=None)
    """Engagements as a percent of views."""

    engagement_rate: Optional[float] = FieldInfo(alias="engagementRate", default=None)
    """Engagements as a percent of the author's followers."""

    engagements: float
    """Likes, replies, reposts and quotes."""

    engagements_per_hour: Optional[float] = FieldInfo(alias="engagementsPerHour", default=None)
    """Engagements per hour since the tweet went up."""

    metrics: InsightsMetrics
    """The public counts of one tweet."""

    tweet_id: str = FieldInfo(alias="tweetId")
    """ID of the tweet the insights describe."""


class TweetGetInsightsResponse(BaseModel):
    insights: Insights
    """Engagement insights of one tweet.

    Engagements are likes, replies, reposts and quotes. A rate is null when nothing
    divides it, such as a tweet without views.
    """
