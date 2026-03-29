# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FollowerRetrieveCheckParams"]


class FollowerRetrieveCheckParams(TypedDict, total=False):
    source: Required[str]
    """Username to check (without @)"""

    target: Required[str]
    """Target username (without @)"""
