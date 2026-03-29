# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CommunityDeleteParams"]


class CommunityDeleteParams(TypedDict, total=False):
    account: Required[str]
    """X account (@username or account ID)"""

    community_name: Required[str]
    """Community name for confirmation"""
