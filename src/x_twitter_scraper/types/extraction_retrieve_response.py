# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .._dict_access import ExtractionResultDictAccess
from .extraction_job import ExtractionJob
from .shared.tweet_media import TweetMedia

__all__ = ["ExtractionRetrieveResponse", "Result"]


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

    media: Optional[List[TweetMedia]] = None
    """Attached media with outputPreset=flat.

    Default nested output uses enrichmentData.tweet.media.
    """

    quote_count: Optional[int] = FieldInfo(alias="quoteCount", default=None)
    """Whole number from 0."""

    reply_count: Optional[int] = FieldInfo(alias="replyCount", default=None)
    """Whole number from 0."""

    retweet_count: Optional[int] = FieldInfo(alias="retweetCount", default=None)
    """Whole number from 0."""

    tweet_created_at: Optional[datetime] = FieldInfo(alias="tweetCreatedAt", default=None)

    tweet_id: Optional[str] = FieldInfo(alias="tweetId", default=None)

    tweet_text: Optional[str] = FieldInfo(alias="tweetText", default=None)

    tweet_url: Optional[str] = FieldInfo(alias="tweetUrl", default=None)

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
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
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
