# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RadarItem", "Metadata"]


class Metadata(BaseModel):
    """Source-specific fields.

    Shape varies per source:
    - reddit: { author, authorId?, subreddit, subredditId?,
      subredditSubscribers?, sourceFormat, score?, upvoteRatio?,
      estimatedUpvotes?, estimatedDownvotes?, numberComments?,
      numberCrossposts?, selftext?, contentUrl?, domain?, postHint?,
      linkFlairText?, distinguished?, totalAwardsReceived?, viewCount?,
      editedAt?, galleryImageUrls?, redditVideo?, archived?, contestMode?,
      isCrosspostable?, isMeta?, isNsfw?, isOriginalContent?,
      isRobotIndexable?, isSelf?, isSpoiler?, isVideo?, locked?,
      stickied? }. `score` is Reddit's public net score. Exact public
      upvote and downvote counts are not available. Estimated counts
      derive from the public score and upvote ratio, which Reddit may
      fuzz. Comment bodies are not included. Current items combine
      public listing discovery with server-rendered post data and use
      `sourceFormat: html`; `json` and `rss` remain for legacy rows.
    - github: { starsToday: number }
    - hacker_news: { points: number, numberComments: number }
    - google_trends: { approxTraffic: number }
    - polymarket: { volume24hr: number }
    - wikipedia: { views: number }
    - trustmrr: { mrr, growthPercent, last30Days, total, customers, activeSubscriptions, onSale, xHandle?, category?, askingPrice?, country?, foundedDate?, googleSearchImpressionsLast30Days?, growthMrrPercent?, multiple?, paymentProvider?, profitMarginLast30Days?, rank?, revenuePerVisitor?, targetAudience?, visitorsLast30Days? }
    For the startup growth source, xHandle is the founder's X username
    without @. The rank field is the source's revenue rank. Result order
    represents reported 30-day revenue-growth rank.
    """

    author: Optional[str] = None

    content_url: Optional[str] = FieldInfo(alias="contentUrl", default=None)

    estimated_downvotes: Optional[int] = FieldInfo(alias="estimatedDownvotes", default=None)

    estimated_upvotes: Optional[int] = FieldInfo(alias="estimatedUpvotes", default=None)

    number_comments: Optional[int] = FieldInfo(alias="numberComments", default=None)

    score: Optional[int] = None

    selftext: Optional[str] = None

    source_format: Optional[Literal["html", "json", "rss"]] = FieldInfo(alias="sourceFormat", default=None)
    """Current items use html. json and rss are retained for legacy rows."""

    subreddit: Optional[str] = None

    upvote_ratio: Optional[float] = FieldInfo(alias="upvoteRatio", default=None)

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class RadarItem(BaseModel):
    """
    Trending topic with score, category, source, region, language, and source-specific metadata.
    """

    id: str
    """Radar item identifier."""

    category: Literal["general", "tech", "dev", "science", "culture", "politics", "business", "entertainment"]

    created_at: datetime = FieldInfo(alias="createdAt")

    language: str
    """BCP-47 language code. und means the source did not identify a language."""

    metadata: Metadata
    """Source-specific fields. Shape varies per source:

    - reddit: { author, authorId?, subreddit, subredditId?, subredditSubscribers?,
      sourceFormat, score?, upvoteRatio?, estimatedUpvotes?, estimatedDownvotes?,
      numberComments?, numberCrossposts?, selftext?, contentUrl?, domain?,
      postHint?, linkFlairText?, distinguished?, totalAwardsReceived?, viewCount?,
      editedAt?, galleryImageUrls?, redditVideo?, archived?, contestMode?,
      isCrosspostable?, isMeta?, isNsfw?, isOriginalContent?, isRobotIndexable?,
      isSelf?, isSpoiler?, isVideo?, locked?, stickied? }. `score` is Reddit's
      public net score. Exact public upvote and downvote counts are not available.
      Estimated counts derive from the public score and upvote ratio, which Reddit
      may fuzz. Comment bodies are not included. Current items combine public
      listing discovery with server-rendered post data and use `sourceFormat: html`;
      `json` and `rss` remain for legacy rows.
    - github: { starsToday: number }
    - hacker_news: { points: number, numberComments: number }
    - google_trends: { approxTraffic: number }
    - polymarket: { volume24hr: number }
    - wikipedia: { views: number }
    - trustmrr: { mrr, growthPercent, last30Days, total, customers,
      activeSubscriptions, onSale, xHandle?, category?, askingPrice?, country?,
      foundedDate?, googleSearchImpressionsLast30Days?, growthMrrPercent?,
      multiple?, paymentProvider?, profitMarginLast30Days?, rank?,
      revenuePerVisitor?, targetAudience?, visitorsLast30Days? } For the startup
      growth source, xHandle is the founder's X username without @. The rank field
      is the source's revenue rank. Result order represents reported 30-day
      revenue-growth rank.
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
    """Source image. Startup growth items return the logo here."""

    url: Optional[str] = None
