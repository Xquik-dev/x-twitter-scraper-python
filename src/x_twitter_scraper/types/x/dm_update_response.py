# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DmUpdateResponse"]


class DmUpdateResponse(BaseModel):
    message_id: str = FieldInfo(alias="messageId")

    success: Literal[True]
