# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ExtractionEstimateCostResponse"]


class ExtractionEstimateCostResponse(BaseModel):
    allowed: bool

    credits_available: str = FieldInfo(alias="creditsAvailable")

    credits_required: str = FieldInfo(alias="creditsRequired")

    estimated_results: int = FieldInfo(alias="estimatedResults")

    source: Literal[
        "followers",
        "following",
        "paginationCap",
        "posts",
        "quoteCount",
        "replyCount",
        "resultsLimit",
        "retweetCount",
        "unknown",
    ]

    resolved_x_user_id: Optional[str] = FieldInfo(alias="resolvedXUserId", default=None)
