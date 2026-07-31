# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TweetMedia", "FaceRect", "FocusRect", "Sizes", "VideoVariant"]


class FaceRect(BaseModel):
    h: int

    w: int

    x: int

    y: int


class FocusRect(BaseModel):
    h: int

    w: int

    x: int

    y: int


class Sizes(BaseModel):
    h: int

    resize: str

    w: int


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

    id: Optional[str] = None
    """X media entity ID."""

    allow_download: Optional[bool] = FieldInfo(alias="allowDownload", default=None)
    """Whether X permits direct media download."""

    alt_text: Optional[str] = FieldInfo(alias="altText", default=None)
    """Accessibility text supplied for the media."""

    aspect_ratio: Optional[List[int]] = FieldInfo(alias="aspectRatio", default=None)
    """Video aspect ratio as width and height."""

    availability_status: Optional[str] = FieldInfo(alias="availabilityStatus", default=None)
    """Media availability state reported by X."""

    display_url: Optional[str] = FieldInfo(alias="displayUrl", default=None)
    """Display-friendly media URL reported by X."""

    duration_millis: Optional[int] = FieldInfo(alias="durationMillis", default=None)
    """Video duration in milliseconds."""

    expanded_url: Optional[str] = FieldInfo(alias="expandedUrl", default=None)
    """Expanded X media URL."""

    face_rects: Optional[Dict[str, List[FaceRect]]] = FieldInfo(alias="faceRects", default=None)
    """Face-aware crop rectangles grouped by media size."""

    focus_rects: Optional[List[FocusRect]] = FieldInfo(alias="focusRects", default=None)
    """Suggested image crops reported by X."""

    height: Optional[int] = None
    """Original media height."""

    indices: Optional[List[int]] = None
    """Media entity offsets in the tweet text."""

    media_key: Optional[str] = FieldInfo(alias="mediaKey", default=None)
    """Stable X media key."""

    monetizable: Optional[bool] = None
    """Whether X reports the media as monetizable."""

    sizes: Optional[Dict[str, Sizes]] = None
    """Named media renditions and resize modes."""

    video_variants: Optional[List[VideoVariant]] = FieldInfo(alias="videoVariants", default=None)
    """Available video encodings, ordered as returned"""

    width: Optional[int] = None
    """Original media width."""
