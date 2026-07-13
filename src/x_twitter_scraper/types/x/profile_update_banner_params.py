# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ProfileUpdateBannerParams"]


class ProfileUpdateBannerParams(TypedDict, total=False):
    account: Required[str]
    """X account (@username or ID) receiving banner from URL"""

    url: Required[str]
    """HTTPS URL to the banner image to download"""
