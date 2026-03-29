# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = ["ProfileUpdateAvatarParams"]


class ProfileUpdateAvatarParams(TypedDict, total=False):
    account: Required[str]
    """X account (@username or account ID)"""

    file: Required[FileTypes]
    """Avatar image (max 716KB)"""
