# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MediaDownloadResponse", "Item"]


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

    retweets: Optional[int]

    tweet_id: str = FieldInfo(alias="tweetId")

    tweet_text: str = FieldInfo(alias="tweetText")

    views: Optional[int]


class MediaDownloadResponse(BaseModel):
    cache_hit: Optional[bool] = FieldInfo(alias="cacheHit", default=None)

    gallery_url: Optional[str] = FieldInfo(alias="galleryUrl", default=None)

    items: Optional[List[Item]] = None
    """The post's files saved to your gallery. Single downloads only."""

    total_media: Optional[int] = FieldInfo(alias="totalMedia", default=None)

    total_tweets: Optional[int] = FieldInfo(alias="totalTweets", default=None)

    tweet_id: Optional[str] = FieldInfo(alias="tweetId", default=None)
