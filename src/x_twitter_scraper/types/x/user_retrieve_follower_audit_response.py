# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "UserRetrieveFollowerAuditResponse",
    "Audit",
    "AuditAccount",
    "AuditAccountAverages",
    "AuditAccountSample",
    "AuditArrivalBand",
    "AuditClass",
    "AuditCohort",
    "AuditCoverage",
    "AuditQuality",
    "AuditSignal",
    "AuditVerified",
    "AuditedFollower",
    "FollowerClass",
    "FollowerValueCount",
]

FollowerClass: TypeAlias = Literal["automated", "inactive", "likelyFake", "likelyReal", "tooNew"]


class AuditAccountAverages(BaseModel):
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


class AuditAccountSample(BaseModel):
    """The recent posts the read covered."""

    newest_at: Optional[datetime] = FieldInfo(alias="newestAt")
    """When the newest post the averages used went up."""

    oldest_at: Optional[datetime] = FieldInfo(alias="oldestAt")
    """When the oldest post the averages used went up."""

    posts: float
    """Posts the averages used.

    Reposts and the pinned post stay out, so this can be lower than `read`.
    """

    read: float
    """Posts read, reposts and the pinned post included."""


class AuditAccount(BaseModel):
    """Engagement insights of 1 profile.

    Engagements are likes, replies, reposts and quotes. A rate is null when nothing divides it, such as a profile without posts of its own.
    """

    account_age_days: Optional[float] = FieldInfo(alias="accountAgeDays")
    """Whole days since the account joined X."""

    averages: Optional[AuditAccountAverages]
    """Each count per post of the sample. Null without posts."""

    engagement_per_view: Optional[float] = FieldInfo(alias="engagementPerView")
    """Engagements as a percent of views across the sample."""

    engagement_rate: Optional[float] = FieldInfo(alias="engagementRate")
    """Average engagements per post, as a percent of followers."""

    followers: float
    """Followers."""

    following: float
    """Accounts the user follows."""

    median_views: Optional[float] = FieldInfo(alias="medianViews")
    """
    Middle view count of the sample, so 1 viral post moves it less than the average.
    Null without posts.
    """

    posts: float
    """Posts the user has made."""

    posts_per_day: Optional[float] = FieldInfo(alias="postsPerDay")
    """Sampled posts per day, from the oldest one until now."""

    posts_private: bool = FieldInfo(alias="postsPrivate")
    """True when only the account's followers see its posts.

    The report then has its counts only.
    """

    sample: AuditAccountSample
    """The recent posts the read covered."""

    top_post_id: Optional[str] = FieldInfo(alias="topPostId")
    """The sampled post with the most engagements."""

    user_id: str = FieldInfo(alias="userId")
    """ID of the profile the insights describe."""

    user_name: str = FieldInfo(alias="userName")
    """Username of that profile."""


class AuditArrivalBand(BaseModel):
    count: int

    from_: int = FieldInfo(alias="from")

    percent: float

    read: int

    to: int


class AuditClass(BaseModel):
    class_: FollowerClass = FieldInfo(alias="class")
    """What 1 follower looks like from its public profile."""

    count: int

    percent: float


class AuditCohort(BaseModel):
    count: int

    likely_fake: int = FieldInfo(alias="likelyFake")

    percent: float

    week_start_ms: int = FieldInfo(alias="weekStartMs")


class AuditCoverage(BaseModel):
    percent: float

    read: int

    total: int


class AuditQuality(BaseModel):
    grade: Literal["A", "B", "C", "D", "F"]

    score: int


class AuditSignal(BaseModel):
    count: int

    id: str

    percent: float

    points: int


class AuditVerified(BaseModel):
    count: int

    percent: float


class AuditedFollower(BaseModel):
    """1 follower the audit read, with its class, score & signals."""

    class_: FollowerClass = FieldInfo(alias="class")
    """What 1 follower looks like from its public profile."""

    followers: int

    following: int

    id: str

    joined_at_ms: Optional[int] = FieldInfo(alias="joinedAtMs", default=None)

    likes: int

    name: str

    owner: Optional[str] = None
    """Account that runs an automated follower, when X names it."""

    picture_url: Optional[str] = FieldInfo(alias="pictureUrl", default=None)

    position: int

    posts: int

    score: int

    signals: List[str]

    user_name: str = FieldInfo(alias="userName")


class FollowerValueCount(BaseModel):
    """How many followers share 1 value, such as a language or place."""

    count: int

    percent: float

    value: str


class Audit(BaseModel):
    """Report on the followers read.

    Classes rest on public profile signals, so they say what a profile looks like, never who runs it.
    """

    account: AuditAccount
    """Engagement insights of 1 profile.

    Engagements are likes, replies, reposts and quotes. A rate is null when nothing
    divides it, such as a profile without posts of its own.
    """

    arrival_bands: List[AuditArrivalBand] = FieldInfo(alias="arrivalBands")
    """Likely fake share by position in the newest-first list."""

    classes: List[AuditClass]

    cohorts: List[AuditCohort]
    """Followers who joined X in the same UTC week."""

    coverage: AuditCoverage

    followers: List[AuditedFollower]

    languages: List[FollowerValueCount]

    places: List[FollowerValueCount]

    quality: AuditQuality

    signals: List[AuditSignal]

    top_followers: List[AuditedFollower] = FieldInfo(alias="topFollowers")

    verified: AuditVerified


class UserRetrieveFollowerAuditResponse(BaseModel):
    audit: Audit
    """Report on the followers read.

    Classes rest on public profile signals, so they say what a profile looks like,
    never who runs it.
    """
