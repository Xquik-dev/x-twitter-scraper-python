# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from ..._models import BaseModel

__all__ = ["PaginatedTweets"]


class PaginatedTweets(BaseModel):
    """Paginated tweets.

    Source visibility, filters, or remaining credits can reduce results. An empty filtered page can still have has_next_page true. Follow next_cursor while has_next_page is true. Zero affordable results returns 402 insufficient_credits.
    """

    has_next_page: bool

    next_cursor: str

    tweets: List["SearchTweet"]


from .search_tweet import SearchTweet
