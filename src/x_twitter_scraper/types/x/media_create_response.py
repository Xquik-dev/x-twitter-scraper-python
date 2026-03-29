# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MediaCreateResponse"]


class MediaCreateResponse(BaseModel):
    media_id: str = FieldInfo(alias="mediaId")

    success: Literal[True]
