# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .radar_item import RadarItem

__all__ = ["RadarRetrieveTrendingTopicsResponse"]


class RadarRetrieveTrendingTopicsResponse(BaseModel):
    items: List[RadarItem]

    total: int
