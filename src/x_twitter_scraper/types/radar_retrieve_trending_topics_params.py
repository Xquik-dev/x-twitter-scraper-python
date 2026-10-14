# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RadarRetrieveTrendingTopicsParams"]


class RadarRetrieveTrendingTopicsParams(TypedDict, total=False):
    after: str
    """Cursor for pagination, from the prior response's nextCursor.

    A cursor the radar can't read gets 400 `invalid_input`.
    """

    category: Literal["general", "tech", "dev", "science", "culture", "politics", "business", "entertainment"]
    """Filter by category."""

    hours: int
    """Lookback window in hours (1-72, default 6)."""

    limit: int
    """Number of items to return (1-100, default 50)."""

    region: str
    """Region filter. Use `global` or a region code such as `US`, `GB`, `TR`, or `ES`."""

    source: Literal["github", "google_trends", "hacker_news", "polymarket", "reddit", "trustmrr", "wikipedia"]
    """Source filter.

    One of: github, google_trends, hacker_news, polymarket, reddit, trustmrr,
    wikipedia
    """
