# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .search_tweet import SearchTweet

__all__ = ["PaginatedTweets"]


class PaginatedTweets(BaseModel):
    """Paginated list of tweets with cursor-based navigation."""

    has_next_page: bool

    next_cursor: str

    tweets: List[SearchTweet]
