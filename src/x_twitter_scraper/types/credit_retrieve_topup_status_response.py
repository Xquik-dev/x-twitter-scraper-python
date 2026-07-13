# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CreditRetrieveTopupStatusResponse"]


class CreditRetrieveTopupStatusResponse(BaseModel):
    status: Literal["paid", "processing", "failed", "expired"]

    amount_dollars: Optional[int] = None
    """Dollar amount requested for the top-up."""

    credits: Optional[str] = None
    """Bigint string credit amount granted or pending."""
