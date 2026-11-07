# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .._dict_access import ExtractionResultDictAccess
from .extraction_job import ExtractionJob
from .shared.tweet_media import TweetMedia

__all__ = ["ExtractionRetrieveResponse", "Result", "ResultQuotedPost", "ResultQuotedPostAuthor"]


class ResultQuotedPostAuthor(BaseModel):
    name: Optional[str] = None

    profile_picture: Optional[str] = FieldInfo(alias="profilePicture", default=None)

    user_name: Optional[str] = FieldInfo(alias="userName", default=None)


class ResultQuotedPost(BaseModel):
    """The quoted post's ID, text, date & author with outputPreset=flat."""

    id: Optional[str] = None

    author: Optional[ResultQuotedPostAuthor] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    text: Optional[str] = None


class Result(ExtractionResultDictAccess):
    """Represents a public row across supported extraction modes."""

    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    x_user_id: str = FieldInfo(alias="xUserId")

    bookmark_count: Optional[int] = FieldInfo(alias="bookmarkCount", default=None)
    """Whole number from 0."""

    email: Optional[str] = None
    """First email the account publishes on its profile, with outputPreset=flat.

    Default nested output uses enrichmentData.user.email, beside
    enrichmentData.user.contactInfo. Absent when the profile publishes none.
    """

    enrichment_data: Optional[Dict[str, object]] = FieldInfo(alias="enrichmentData", default=None)
    """Public metadata whose fields are defined by X."""

    like_count: Optional[int] = FieldInfo(alias="likeCount", default=None)
    """Whole number from 0."""

    is_deleted: Optional[bool] = FieldInfo(alias="isDeleted", default=None)
    """True on a post its author deleted from X after Xquik saw it, with outputPreset=flat.

    Default nested output uses enrichmentData.tweet.isDeleted. An account post list
    with a date range adds such posts from the last 30 days. Absent on every other
    row.
    """

    media: Optional[List[TweetMedia]] = None
    """Attached media with outputPreset=flat.

    Default nested output uses enrichmentData.tweet.media.
    """

    possibly_sensitive: Optional[bool] = FieldInfo(alias="possiblySensitive", default=None)
    """X's sensitive flag on the post with outputPreset=flat.

    Default nested output uses enrichmentData.tweet.possiblySensitive.
    """

    quote_count: Optional[int] = FieldInfo(alias="quoteCount", default=None)
    """Whole number from 0."""

    quoted_media: Optional[List[TweetMedia]] = FieldInfo(alias="quotedMedia", default=None)
    """Media of the quoted post with outputPreset=flat.

    Default nested output uses enrichmentData.tweet.quotedMedia.
    """

    quoted_possibly_sensitive: Optional[bool] = FieldInfo(alias="quotedPossiblySensitive", default=None)
    """X's sensitive flag on the quoted post with outputPreset=flat.

    Default nested output uses enrichmentData.tweet.quotedPossiblySensitive.
    """

    quoted_post: Optional[ResultQuotedPost] = FieldInfo(alias="quotedPost", default=None)
    """The quoted post's ID, text, date & author with outputPreset=flat.

    Default nested output uses enrichmentData.tweet.quotedPost.
    """

    reply_count: Optional[int] = FieldInfo(alias="replyCount", default=None)
    """Whole number from 0."""

    retweet_count: Optional[int] = FieldInfo(alias="retweetCount", default=None)
    """Whole number from 0."""

    tweet_created_at: Optional[datetime] = FieldInfo(alias="tweetCreatedAt", default=None)

    tweet_id: Optional[str] = FieldInfo(alias="tweetId", default=None)

    tweet_text: Optional[str] = FieldInfo(alias="tweetText", default=None)

    tweet_url: Optional[str] = FieldInfo(alias="tweetUrl", default=None)

    verified_type: Optional[str] = FieldInfo(alias="verifiedType", default=None)
    """Badge type X shows on the account, with outputPreset=flat.

    Business is the gold badge of a verified organization. Government is the grey
    badge of a government or multilateral account. Blue is the badge of X Premium.
    Default nested output uses enrichmentData.user.verifiedType. Absent when the
    account has none of these badges.
    """

    view_count: Optional[int] = FieldInfo(alias="viewCount", default=None)
    """Whole number from 0."""

    x_display_name: Optional[str] = FieldInfo(alias="xDisplayName", default=None)

    x_followers_count: Optional[int] = FieldInfo(alias="xFollowersCount", default=None)
    """Followers of the account.

    Absent when X sends no count, as for the hosts & speakers of a Space, and never
    0 in its place.
    """

    x_profile_image_url: Optional[str] = FieldInfo(alias="xProfileImageUrl", default=None)

    x_username: Optional[str] = FieldInfo(alias="xUsername", default=None)

    x_verified: Optional[bool] = FieldInfo(alias="xVerified", default=None)

    if TYPE_CHECKING:
        # Pydantic <2.8 rejects a value on __pydantic_extra__ at runtime.
        # https://github.com/pydantic/pydantic/pull/9659
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ExtractionRetrieveResponse(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")

    job: ExtractionJob
    """Extraction job tracking status, tool type, and result count."""

    poll_after_ms: int = FieldInfo(alias="pollAfterMs")

    results: List[Result]

    wait_url: str = FieldInfo(alias="waitUrl")

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
