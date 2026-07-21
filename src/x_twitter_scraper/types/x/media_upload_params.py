# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MediaUploadParams"]


class MediaUploadParams(TypedDict, total=False):
    account: Required[str]
    """X account (@username or ID) uploading media from URL"""

    url: Required[str]
    """HTTPS URL to download and upload as media"""

    idempotency_key: Required[Annotated[str, PropertyInfo(alias="Idempotency-Key")]]
