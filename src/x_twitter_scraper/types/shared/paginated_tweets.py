# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .search_tweet import SearchTweet

__all__ = ["PaginatedTweets"]


class PaginatedTweets(BaseModel):
    """Paginated tweet results.

    The item count can be lower than pageSize when the source returns fewer tweets, filters remove tweets, or remaining credits cover fewer results. Follow next_cursor while has_next_page is true. An empty page can still have has_next_page true after filtering. Zero affordable results returns 402 insufficient_credits.
    """

    has_next_page: bool

    next_cursor: str

    tweets: List[SearchTweet]
