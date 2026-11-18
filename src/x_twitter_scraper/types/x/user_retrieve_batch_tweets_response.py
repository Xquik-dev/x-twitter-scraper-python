# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.search_tweet import SearchTweet

__all__ = ["UserRetrieveBatchTweetsResponse"]


class UserRetrieveBatchTweetsResponse(BaseModel):
    """
    Each user's newest posts, in the order the users were named, with the pinned post first. The ID lists name the requested IDs or usernames. A profile link is named by its username.
    """

    has_next_page: Literal[False]
    """Always false. The answer holds every post in 1 page."""

    next_cursor: str
    """Always empty. The answer holds every post in 1 page."""

    not_found_ids: List[str]
    """
    The unavailable users no account holds, as X answers for an account that was
    deactivated or deleted, in first-seen request order.
    """

    protected_ids: List[str]
    """
    The unavailable users whose posts only approved followers see, in first-seen
    request order.
    """

    suspended_ids: List[str]
    """The unavailable users X suspended, in first-seen request order."""

    tweets: List[SearchTweet]

    unavailable_ids: List[str]
    """Users with no account on X or with protected posts, in first-seen request order.

    They cost nothing. not_found_ids, suspended_ids and protected_ids split them by
    X's answer.
    """

    unprocessed_ids: List[str]
    """Users the call did not read, in first-seen request order.

    Their read failed, the call ran out of time or credits ran out. They cost
    nothing. Send them again.
    """
