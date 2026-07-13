# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TweetMedia", "VideoVariant"]


class VideoVariant(BaseModel):
    content_type: str = FieldInfo(alias="contentType")

    url: str

    bitrate: Optional[int] = None


class TweetMedia(BaseModel):
    """Normalized media attached to a tweet."""

    media_url: str = FieldInfo(alias="mediaUrl")
    """Media preview URL"""

    type: Literal["photo", "video", "animated_gif"]

    url: str
    """X media link from the tweet"""

    video_variants: Optional[List[VideoVariant]] = FieldInfo(alias="videoVariants", default=None)
    """Available video encodings, ordered as returned"""
