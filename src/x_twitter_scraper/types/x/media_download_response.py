# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.image_filter_summary import ImageFilterSummary

__all__ = ["MediaDownloadResponse", "Item", "ItemQuality"]


class ItemQuality(BaseModel):
    """1 MP4 size X stores for a video."""

    bitrate: int

    height: int

    url: str

    width: int


class Item(BaseModel):
    """1 file saved to your gallery."""

    id: str
    """Gallery file ID."""

    author_avatar: Optional[str] = FieldInfo(alias="authorAvatar")

    author_display_name: str = FieldInfo(alias="authorDisplayName")

    author_username: str = FieldInfo(alias="authorUsername")

    created_at: datetime = FieldInfo(alias="createdAt")
    """When the file joined your gallery."""

    file_size: Optional[str] = FieldInfo(alias="fileSize")
    """File size in bytes, as a string."""

    likes: Optional[int]

    media_type: Literal["photo", "video", "animated_gif"] = FieldInfo(alias="mediaType")

    media_url: str = FieldInfo(alias="mediaUrl")
    """Link to the file.

    It goes to X when X flagged the post or its media at save time, or sent no post
    flag. Xquik keeps no copy of those files.
    """

    poster_url: Optional[str] = FieldInfo(alias="posterUrl")
    """Cover image of a video or GIF.

    Null for photos & files first saved to Xquik before 2026-11-03.
    """

    qualities: List[ItemQuality]
    """The MP4 sizes X stores for a video, highest bitrate first.

    Empty for photos, GIFs & files first saved to Xquik before 2026-11-03.
    """

    retweets: Optional[int]

    tweet_id: str = FieldInfo(alias="tweetId")

    tweet_text: str = FieldInfo(alias="tweetText")

    views: Optional[int]


class MediaDownloadResponse(BaseModel):
    cache_hit: Optional[bool] = FieldInfo(alias="cacheHit", default=None)

    gallery_url: Optional[str] = FieldInfo(alias="galleryUrl", default=None)

    image_filter: Optional[ImageFilterSummary] = FieldInfo(alias="imageFilter", default=None)
    """What the image filter asked & how many posts it kept."""

    items: Optional[List[Item]] = None
    """The post's files saved to your gallery.

    Single downloads only. Empty when imageShows kept no photo.
    """

    total_media: Optional[int] = FieldInfo(alias="totalMedia", default=None)

    total_tweets: Optional[int] = FieldInfo(alias="totalTweets", default=None)

    tweet_id: Optional[str] = FieldInfo(alias="tweetId", default=None)
