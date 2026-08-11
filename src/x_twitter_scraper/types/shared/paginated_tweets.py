# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from ..._models import BaseModel

__all__ = ["PaginatedTweets"]


class PaginatedTweets(BaseModel):
    """
    No-mode search, user Tweet, user reply, and direct reply reads use automatic coverage. Shape, filters, aliases, and billing stay compatible. Unprefixed cursors remain legacy. Follow next_cursor while has_next_page is true. An empty filtered page can still have has_next_page true.
    """

    has_next_page: bool

    next_cursor: str

    tweets: List["SearchTweet"]


from .search_tweet import SearchTweet
