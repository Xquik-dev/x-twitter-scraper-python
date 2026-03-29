# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = ["MediaCreateParams"]


class MediaCreateParams(TypedDict, total=False):
    account: Required[str]
    """X account (@username or account ID)"""

    file: Required[FileTypes]
    """Media file to upload"""

    is_long_video: bool
