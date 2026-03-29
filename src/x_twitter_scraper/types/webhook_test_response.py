# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebhookTestResponse"]


class WebhookTestResponse(BaseModel):
    status_code: int = FieldInfo(alias="statusCode")

    success: bool

    error: Optional[str] = None
