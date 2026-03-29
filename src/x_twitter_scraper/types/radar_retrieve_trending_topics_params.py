# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RadarRetrieveTrendingTopicsParams"]


class RadarRetrieveTrendingTopicsParams(TypedDict, total=False):
    category: str
    """Filter by category (general, tech, dev, etc.)"""

    count: int
    """Number of items to return"""

    hours: int
    """Lookback window in hours"""

    region: str
    """Region filter (us, global, etc.)"""

    source: str
    """Source filter.

    One of: github, google_trends, hacker_news, polymarket, reddit, trustmrr,
    wikipedia
    """
