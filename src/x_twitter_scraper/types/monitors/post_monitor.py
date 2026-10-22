# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "PostEventType",
    "PostMetricReading",
    "PostMetrics",
    "PostMonitor",
    "PostMetricPoint",
    "PostMonitorMetricsBucketMetrics",
    "PostMonitorMetricsBucket",
    "PostMonitorMetrics",
]

PostEventType: TypeAlias = Literal[
    "post.reply.new",
    "post.quote.new",
    "post.likes.changed",
    "post.retweets.changed",
    "post.replies.changed",
    "post.quotes.changed",
    "post.bookmarks.changed",
    "post.views.changed",
    "post.edited",
    "post.deleted",
]


class PostMetricReading(BaseModel):
    """A metric's current value & its gain since tracking began. Both are null when X
    shows no count, as for views on old posts.
    """

    current: Optional[int]

    gain: Optional[int]


class PostMetrics(BaseModel):
    """The 6 metrics of a post."""

    views: PostMetricReading
    """A metric's current value & its gain since tracking began. Both are null when X
    shows no count, as for views on old posts.
    """

    likes: PostMetricReading
    """A metric's current value & its gain since tracking began. Both are null when X
    shows no count, as for views on old posts.
    """

    retweets: PostMetricReading
    """A metric's current value & its gain since tracking began. Both are null when X
    shows no count, as for views on old posts.
    """

    replies: PostMetricReading
    """A metric's current value & its gain since tracking began. Both are null when X
    shows no count, as for views on old posts.
    """

    quotes: PostMetricReading
    """A metric's current value & its gain since tracking began. Both are null when X
    shows no count, as for views on old posts.
    """

    bookmarks: PostMetricReading
    """A metric's current value & its gain since tracking began. Both are null when X
    shows no count, as for views on old posts.
    """


class PostMonitor(BaseModel):
    """Post monitor that tracks 1 X post's replies, quotes, edits & metrics."""

    id: str

    post_id: str = FieldInfo(alias="postId")
    """ID of the post you gave."""

    post_url: str = FieldInfo(alias="postUrl")

    author_id: str = FieldInfo(alias="authorId")
    """Permanent X user ID of the post's author."""

    author_username: str = FieldInfo(alias="authorUsername")

    author_name: str = FieldInfo(alias="authorName")

    text: str
    """Text of the newest version Xquik read."""

    posted_at: datetime = FieldInfo(alias="postedAt")

    event_types: List[PostEventType] = FieldInfo(alias="eventTypes")
    """Post event types to send. Without it, a monitor sends new replies, new quotes,
    like & retweet changes, edits & deletion.
    """

    is_active: bool = FieldInfo(alias="isActive")

    created_at: datetime = FieldInfo(alias="createdAt")

    next_billing_at: datetime = FieldInfo(alias="nextBillingAt")
    """Next hourly credit charge time for this post monitor."""

    metrics: PostMetrics
    """The 6 metrics of a post."""

    name: Optional[str] = None
    """Customer-set label of the post monitor, when set."""

    paused_reason: Optional[
        Literal["insufficient_credits", "x_post_deleted", "x_post_protected", "x_post_unavailable"]
    ] = FieldInfo(alias="pausedReason", default=None)
    """Why Xquik paused this post monitor. insufficient_credits means the balance
    could not pay an hour, so add credits & resume. The other 3 mean X stopped
    showing the post. Absent when the monitor is active or you paused it yourself.
    """

    paused_at: Optional[datetime] = FieldInfo(alias="pausedAt", default=None)
    """When Xquik paused this post monitor."""


class PostMetricPoint(BaseModel):
    """A metric's value at the hour's end & its gain over that hour. Both are null
    when X shows no count.
    """

    value: Optional[int]

    gain: Optional[int]


class PostMonitorMetricsBucketMetrics(BaseModel):
    views: PostMetricPoint
    """A metric's value at the hour's end & its gain over that hour. Both are null
    when X shows no count.
    """

    likes: PostMetricPoint
    """A metric's value at the hour's end & its gain over that hour. Both are null
    when X shows no count.
    """

    retweets: PostMetricPoint
    """A metric's value at the hour's end & its gain over that hour. Both are null
    when X shows no count.
    """

    replies: PostMetricPoint
    """A metric's value at the hour's end & its gain over that hour. Both are null
    when X shows no count.
    """

    quotes: PostMetricPoint
    """A metric's value at the hour's end & its gain over that hour. Both are null
    when X shows no count.
    """

    bookmarks: PostMetricPoint
    """A metric's value at the hour's end & its gain over that hour. Both are null
    when X shows no count.
    """


class PostMonitorMetricsBucket(BaseModel):
    at: datetime
    """Start of the hour."""

    metrics: PostMonitorMetricsBucketMetrics


class PostMonitorMetrics(BaseModel):
    """Hourly metric buckets of 1 post monitor, oldest first."""

    hours: int

    buckets: List[PostMonitorMetricsBucket]
