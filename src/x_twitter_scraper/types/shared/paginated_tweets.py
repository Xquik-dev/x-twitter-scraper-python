# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .search_tweet import SearchTweet

__all__ = ["PaginatedTweets", "SearchContext", "SearchContextSmartTag"]


class SearchContextSmartTag(BaseModel):
    """X's card for the cashtag the search names."""

    id: str
    """The ticker X matched."""

    active: Optional[bool] = None
    """Whether X lists the ticker as active."""

    supports_ohlc: Optional[bool] = FieldInfo(alias="supportsOhlc", default=None)
    """Whether X charts the ticker with open, high, low & close prices."""


class SearchContext(BaseModel):
    """What X shows beside a search's posts that is the same for every reader.

    Present on a search for a cashtag X has a card for, such as $BTC.
    """

    smart_tag: SearchContextSmartTag = FieldInfo(alias="smartTag")
    """X's card for the cashtag the search names."""


class PaginatedTweets(BaseModel):
    """Follow next_cursor while the response reports more pages.

    A page can hold fewer rows than its limit & still report more. That report decides, not the row count. A page can be empty & still report more, filtered or not. Automatic search, user Tweet & reply coverage keeps shape, filters, aliases & billing. Unprefixed cursors are legacy.
    """

    has_next_page: bool

    next_cursor: str

    tweets: List[SearchTweet]

    filtered_count: Optional[int] = None
    """Whole number from 0."""

    read_back_to: Optional[datetime] = FieldInfo(alias="readBackTo", default=None)
    """How far back a filtered Latest search has read, in UTC.

    Every newer post was checked, so an empty page still moves this time back.
    """

    search_context: Optional[SearchContext] = FieldInfo(alias="searchContext", default=None)
    """What X shows beside a search's posts that is the same for every reader.

    Present on a search for a cashtag X has a card for, such as $BTC.
    """

    searched_query: Optional[str] = FieldInfo(alias="searchedQuery", default=None)
    """Search q as X ran it, when Xquik fixed it."""

    window_complete: Optional[Literal[True]] = FieldInfo(alias="windowComplete", default=None)
    """Present on a last page whose sources all read past its start time."""
