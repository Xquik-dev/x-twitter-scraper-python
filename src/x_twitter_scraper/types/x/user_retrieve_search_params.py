# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UserRetrieveSearchParams"]


class UserRetrieveSearchParams(TypedDict, total=False):
    q: Required[str]
    """Search query"""

    cursor: str
    """Pagination cursor"""
