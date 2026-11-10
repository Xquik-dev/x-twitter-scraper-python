# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["MediaUploadParams"]


class MediaUploadParams(TypedDict, total=False):
    account: Required[str]
    """X account (@username or ID) uploading media"""

    file: FileTypes
    """Media file to upload, up to 15 MB.
    A larger file gets 413 `media_too_large` before any account lookup.
    """

    is_long_video: bool
    """Set true only for video/mp4 multipart uploads longer than 140 seconds."""

    url: str
    """HTTPS URL to download and upload as media, up to 15 MB.
    Another scheme gets 400 `invalid_media_url`.
    """

    idempotency_key: Required[Annotated[str, PropertyInfo(alias="Idempotency-Key")]]

    prefer: Annotated[str, PropertyInfo(alias="Prefer")]
    """A long write answers 202 with a status link, then lands on X.

    `wait=<seconds>` asks for the answer within that many seconds, up to 85. If the
    write is still running then, the API answers 202 with Location. Poll Location
    until `terminal` is true, and don't send the write again.
    """
