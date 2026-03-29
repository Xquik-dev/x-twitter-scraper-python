# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SubscribeCreateResponse"]


class SubscribeCreateResponse(BaseModel):
    url: str

    message: Optional[str] = None

    status: Optional[Literal["checkout_created", "already_subscribed", "payment_issue"]] = None
