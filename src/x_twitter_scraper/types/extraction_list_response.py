# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .extraction_job import ExtractionJob

__all__ = ["ExtractionListResponse"]


class ExtractionListResponse(BaseModel):
    extractions: List[ExtractionJob]

    has_more: bool = FieldInfo(alias="hasMore")

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
