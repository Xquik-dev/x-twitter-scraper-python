# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DrawListParams"]


class DrawListParams(TypedDict, total=False):
    cursor: str
    """Cursor for keyset pagination from prior response next_cursor"""

    limit: int
    """Maximum number of items to return (1-100, default 50).

    For paid per-result endpoints, the returned count may be lower when remaining
    credits cannot cover the requested page. If zero paid results are affordable,
    the endpoint returns 402 insufficient_credits.
    """
