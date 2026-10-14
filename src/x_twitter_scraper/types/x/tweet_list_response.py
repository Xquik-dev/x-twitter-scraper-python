# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paginated_tweets import PaginatedTweets

__all__ = ["TweetListResponse", "TweetListResponseSkipped"]


class TweetListResponseSkipped(BaseModel):
    entry: str
    """The entry as sent."""

    reason: str
    """Why the entry names no post."""


class TweetListResponse(PaginatedTweets):
    skipped: Optional[List[TweetListResponseSkipped]] = None
    """Each `ids` entry that names no post, with why.

    Absent when every entry names a post.
    """
