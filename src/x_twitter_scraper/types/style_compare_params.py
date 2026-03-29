# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["StyleCompareParams"]


class StyleCompareParams(TypedDict, total=False):
    username1: Required[str]
    """First username to compare"""

    username2: Required[str]
    """Second username to compare"""
