# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .style_profile_summary import StyleProfileSummary

__all__ = ["StyleListResponse"]


class StyleListResponse(BaseModel):
    styles: List[StyleProfileSummary]
