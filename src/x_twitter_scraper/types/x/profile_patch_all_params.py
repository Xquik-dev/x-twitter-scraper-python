# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ProfilePatchAllParams"]


class ProfilePatchAllParams(TypedDict, total=False):
    account: Required[str]
    """X account (@username or account ID)"""

    description: str
    """Bio description"""

    location: str

    name: str
    """Display name"""

    url: str
    """Website URL"""
