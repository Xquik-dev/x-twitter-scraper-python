# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DrawListParams"]


class DrawListParams(TypedDict, total=False):
    after: str
    """Cursor for keyset pagination"""

    limit: int
    """Maximum number of items to return (1-100, default 50)"""
