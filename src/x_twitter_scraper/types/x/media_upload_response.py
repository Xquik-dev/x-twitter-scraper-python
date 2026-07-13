# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MediaUploadResponse"]


class MediaUploadResponse(BaseModel):
    media_id: str = FieldInfo(alias="mediaId")

    media_url: str = FieldInfo(alias="mediaUrl")
    """Public media URL for tweet `media` arrays."""

    success: Literal[True]
