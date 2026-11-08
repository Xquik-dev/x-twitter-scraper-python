# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UserRetrieveInsightsResponse", "Insights", "InsightsAverages", "InsightsSample"]


class InsightsAverages(BaseModel):
    """Each count per post of the sample. Null without posts."""

    bookmarks: float
    """Bookmarks."""

    engagements: float
    """Likes, replies, reposts and quotes per post."""

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


class InsightsSample(BaseModel):
    """The recent posts the read covered."""

    newest_at: Optional[datetime] = FieldInfo(alias="newestAt", default=None)
    """When the newest post the averages used went up."""

    oldest_at: Optional[datetime] = FieldInfo(alias="oldestAt", default=None)
    """When the oldest post the averages used went up."""

    posts: float
    """Posts the averages used.

    Reposts and the pinned post stay out, so this can be lower than `read`.
    """

    read: float
    """Posts read, reposts and the pinned post included."""


class Insights(BaseModel):
    """Engagement insights of one profile.

    Engagements are likes, replies, reposts and quotes. A rate is null when nothing divides it, such as a profile without posts of its own.
    """

    account_age_days: Optional[float] = FieldInfo(alias="accountAgeDays", default=None)
    """Whole days since the account joined X."""

    averages: Optional[InsightsAverages] = None
    """Each count per post of the sample. Null without posts."""

    engagement_per_view: Optional[float] = FieldInfo(alias="engagementPerView", default=None)
    """Engagements as a percent of views across the sample."""

    engagement_rate: Optional[float] = FieldInfo(alias="engagementRate", default=None)
    """Average engagements per post, as a percent of followers."""

    followers: float
    """Followers."""

    following: float
    """Accounts the user follows."""

    median_views: Optional[float] = FieldInfo(alias="medianViews", default=None)
    """
    Middle view count of the sample, so 1 viral post moves it less than the average.
    Null without posts.
    """

    posts: float
    """Posts the user has made."""

    posts_per_day: Optional[float] = FieldInfo(alias="postsPerDay", default=None)
    """Sampled posts per day, from the oldest one until now."""

    posts_private: bool = FieldInfo(alias="postsPrivate")
    """True when only the account's followers see its posts.

    The report then has its counts only.
    """

    sample: InsightsSample
    """The recent posts the read covered."""

    top_post_id: Optional[str] = FieldInfo(alias="topPostId", default=None)
    """The sampled post with the most engagements."""

    user_id: str = FieldInfo(alias="userId")
    """ID of the profile the insights describe."""

    user_name: str = FieldInfo(alias="userName")
    """Username of that profile."""


class UserRetrieveInsightsResponse(BaseModel):
    insights: Insights
    """Engagement insights of one profile.

    Engagements are likes, replies, reposts and quotes. A rate is null when nothing
    divides it, such as a profile without posts of its own.
    """

    message: Optional[str] = None
    """Says why the report has counts only."""
