# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .search_tweet import SearchTweet

__all__ = ["PaginatedTweets"]


class PaginatedTweets(BaseModel):
    """
    Automatic search, user Tweet, and reply coverage preserves shape, filters, aliases, and billing. Follow next_cursor while the response reports more pages. An empty filtered page can still require continuation. Unprefixed cursors are legacy.
    """

    has_next_page: bool

    next_cursor: str

    tweets: List[SearchTweet]

    filtered_count: Optional[int] = None
