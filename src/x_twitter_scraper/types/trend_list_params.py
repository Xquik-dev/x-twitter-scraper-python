# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TrendListParams"]


class TrendListParams(TypedDict, total=False):
    count: int

    woeid: int
    """Region WOEID (1=Worldwide, 23424977=US, 23424975=UK, 23424969=Turkey)"""
