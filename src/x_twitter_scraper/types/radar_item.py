# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RadarItem"]


class RadarItem(BaseModel):
    """
    Trending topic with score, category, source, region, language, and source-specific metadata.
    """

    id: str
    """Internal numeric identifier (stringified bigint)."""

    category: Literal["general", "tech", "dev", "science", "culture", "politics", "business", "entertainment"]

    created_at: datetime = FieldInfo(alias="createdAt")

    language: str

    metadata: Dict[str, object]
    """Source-specific fields. Shape varies per source:

    - reddit: { subreddit: string, author: string }
    - github: { starsToday: number }
    - hacker_news: { points: number, numberComments: number }
    - google_trends: { approxTraffic: number }
    - polymarket: { volume24hr: number }
    - wikipedia: { views: number }
    - trustmrr: { mrr, growthPercent, last30Days, total, customers,
      activeSubscriptions, onSale, xHandle?, category?, askingPrice?, country?,
      growthMrrPercent?, multiple?, paymentProvider?, rank? }
    """

    published_at: datetime = FieldInfo(alias="publishedAt")

    region: str

    score: float

    source: Literal["github", "google_trends", "hacker_news", "polymarket", "reddit", "trustmrr", "wikipedia"]

    source_id: str = FieldInfo(alias="sourceId")
    """Source-specific identifier used for deduplication."""

    title: str

    description: Optional[str] = None

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)

    url: Optional[str] = None
