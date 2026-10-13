# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TweetCheckRepostResponse"]


class TweetCheckRepostResponse(BaseModel):
    checked_posts: int = FieldInfo(alias="checkedPosts")
    """How many of the account's newest posts the check read."""

    complete: bool
    """Whether the check read the account's whole timeline."""

    is_retweeted: bool = FieldInfo(alias="isRetweeted")
    """Whether the account reposted the post."""

    retweeted_at: Optional[str] = FieldInfo(alias="retweetedAt", default=None)
    """When the account reposted it, else null."""

    retweet_id: Optional[str] = FieldInfo(alias="retweetId", default=None)
    """The ID of the account's repost, else null."""

    tweet_id: str = FieldInfo(alias="tweetId")

    user_id: str = FieldInfo(alias="userId")
