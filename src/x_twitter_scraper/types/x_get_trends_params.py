# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["XGetTrendsParams"]


class XGetTrendsParams(TypedDict, total=False):
    count: int
    """Number of trending topics to return (1-50, default 30)"""

    woeid: int
    """Region WOEID (1=Worldwide, 23424977=US, 23424975=UK, 23424969=Turkey)"""
