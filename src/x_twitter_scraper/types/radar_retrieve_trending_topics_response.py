# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RadarRetrieveTrendingTopicsResponse", "Item"]


class Item(BaseModel):
    category: str

    published_at: datetime = FieldInfo(alias="publishedAt")

    region: str

    score: float

    source: str

    title: str

    description: Optional[str] = None

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None


class RadarRetrieveTrendingTopicsResponse(BaseModel):
    items: List[Item]

    total: int
