# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .draft import Draft
from .._models import BaseModel

__all__ = ["DraftListResponse"]


class DraftListResponse(BaseModel):
    drafts: List[Draft]

    has_more: bool = FieldInfo(alias="hasMore")

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)
