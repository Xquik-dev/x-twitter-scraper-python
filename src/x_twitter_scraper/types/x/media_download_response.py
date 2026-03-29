# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MediaDownloadResponse"]


class MediaDownloadResponse(BaseModel):
    cache_hit: Optional[bool] = FieldInfo(alias="cacheHit", default=None)

    gallery_url: Optional[str] = FieldInfo(alias="galleryUrl", default=None)

    total_media: Optional[int] = FieldInfo(alias="totalMedia", default=None)

    total_tweets: Optional[int] = FieldInfo(alias="totalTweets", default=None)

    tweet_id: Optional[str] = FieldInfo(alias="tweetId", default=None)
