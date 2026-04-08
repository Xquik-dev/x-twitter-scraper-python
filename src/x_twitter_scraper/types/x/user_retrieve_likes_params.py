# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UserRetrieveLikesParams"]


class UserRetrieveLikesParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor for liked tweets"""
