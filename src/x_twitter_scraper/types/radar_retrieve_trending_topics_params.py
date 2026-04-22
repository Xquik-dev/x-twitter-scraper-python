# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RadarRetrieveTrendingTopicsParams"]


class RadarRetrieveTrendingTopicsParams(TypedDict, total=False):
    after: str
    """Cursor for pagination (from prior response nextCursor)."""

    category: Literal["general", "tech", "dev", "science", "culture", "politics", "business", "entertainment"]
    """Filter by category."""

    hours: int
    """Lookback window in hours (1-168, default 24)."""

    limit: int
    """Number of items to return (1-100, default 50)."""

    region: str
    """Region filter (us, global, etc.)"""

    source: Literal["github", "google_trends", "hacker_news", "polymarket", "reddit", "trustmrr", "wikipedia"]
    """Source filter.

    One of: github, google_trends, hacker_news, polymarket, reddit, trustmrr,
    wikipedia
    """
