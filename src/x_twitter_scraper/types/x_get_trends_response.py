# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["XGetTrendsResponse", "Trend"]


class Trend(BaseModel):
    name: str

    description: Optional[str] = None

    query: Optional[str] = None

    rank: Optional[int] = None


class XGetTrendsResponse(BaseModel):
    count: int

    trends: List[Trend]

    woeid: int
