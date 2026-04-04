# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ExtractionRetrieveResponse"]


class ExtractionRetrieveResponse(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")

    job: Dict[str, object]
    """Extraction job metadata — shape varies by tool type (JSON)"""

    results: List[Dict[str, object]]

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
