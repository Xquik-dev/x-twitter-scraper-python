# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = ["ProfileUpdateBannerParams"]


class ProfileUpdateBannerParams(TypedDict, total=False):
    account: Required[str]
    """X account (@username or account ID)"""

    file: Required[FileTypes]
    """Banner image (max 2MB)"""
