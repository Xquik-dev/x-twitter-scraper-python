# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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

    tweets: List[SearchTweet]

    unavailable_ids: List[str]
    """Users with no account on X or with protected posts, in first-seen request order.

    They cost nothing.
    """

    unprocessed_ids: List[str]
    """Users the call did not read, in first-seen request order.

    Their read failed, the call ran out of time or credits ran out. They cost
    nothing. Send them again.
    """
