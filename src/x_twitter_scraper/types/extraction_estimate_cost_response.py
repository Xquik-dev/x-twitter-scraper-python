# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ExtractionEstimateCostResponse"]


class ExtractionEstimateCostResponse(BaseModel):
    allowed: bool

    estimated_results: int = FieldInfo(alias="estimatedResults")

    projected_percent: float = FieldInfo(alias="projectedPercent")

    source: str

    usage_percent: float = FieldInfo(alias="usagePercent")
