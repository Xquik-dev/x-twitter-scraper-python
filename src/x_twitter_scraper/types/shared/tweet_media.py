# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TweetMedia", "FaceRect", "FocusRect", "Sizes", "Tag", "VideoVariant"]


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


class Tag(BaseModel):
    name: Optional[str] = None

    screen_name: Optional[str] = None

    type: Optional[str] = None

    user_id: Optional[str] = None


class VideoVariant(BaseModel):
    content_type: str = FieldInfo(alias="contentType")

    url: str

    bitrate: Optional[int] = None


class TweetMedia(BaseModel):
    """Tweet media."""

    media_url: str = FieldInfo(alias="mediaUrl")
    """Preview URL."""

    type: Literal["photo", "video", "animated_gif"]

    url: str
    """Tweet media link."""

    id: Optional[str] = None
    """Media entity ID."""

    adult_content: Optional[bool] = FieldInfo(alias="adultContent", default=None)
    """Adult-content warning."""

    allow_download: Optional[bool] = FieldInfo(alias="allowDownload", default=None)
    """Direct download permission."""

    alt_text: Optional[str] = FieldInfo(alias="altText", default=None)
    """Accessibility text."""

    aspect_ratio: Optional[List[int]] = FieldInfo(alias="aspectRatio", default=None)
    """Video width and height ratio."""

    availability_reason: Optional[str] = FieldInfo(alias="availabilityReason", default=None)
    """Availability reason."""

    availability_status: Optional[str] = FieldInfo(alias="availabilityStatus", default=None)
    """Availability state."""

    description: Optional[str] = None
    """Media description."""

    display_url: Optional[str] = FieldInfo(alias="displayUrl", default=None)
    """Display URL."""

    duration_millis: Optional[int] = FieldInfo(alias="durationMillis", default=None)
    """Video duration in milliseconds."""

    embeddable: Optional[bool] = None
    """Embeddable status."""

    expanded_url: Optional[str] = FieldInfo(alias="expandedUrl", default=None)
    """Expanded media URL."""

    face_rects: Optional[Dict[str, List[FaceRect]]] = FieldInfo(alias="faceRects", default=None)
    """Face crop rectangles by size."""

    focus_rects: Optional[List[FocusRect]] = FieldInfo(alias="focusRects", default=None)
    """Suggested image crops."""

    graphic_violence: Optional[bool] = FieldInfo(alias="graphicViolence", default=None)
    """Graphic-violence warning."""

    grok_post_id: Optional[str] = FieldInfo(alias="grokPostId", default=None)
    """Grok post ID associated with the media."""

    height: Optional[int] = None
    """Original height."""

    indices: Optional[List[int]] = None
    """Tweet text offsets."""

    media_key: Optional[str] = FieldInfo(alias="mediaKey", default=None)
    """Stable X media key."""

    monetizable: Optional[bool] = None
    """Monetization status."""

    other_sensitive_content: Optional[bool] = FieldInfo(alias="otherSensitiveContent", default=None)

    sizes: Optional[Dict[str, Sizes]] = None
    """Named media renditions and resize modes."""

    source_status_id: Optional[str] = FieldInfo(alias="sourceStatusId", default=None)
    """Source tweet ID for copied media."""

    source_user_id: Optional[str] = FieldInfo(alias="sourceUserId", default=None)
    """Source profile ID for copied media."""

    tags: Optional[List[Tag]] = None
    """Public profiles tagged in the media."""

    title: Optional[str] = None
    """Media title."""

    video_variants: Optional[List[VideoVariant]] = FieldInfo(alias="videoVariants", default=None)
    """Video encodings in source order."""

    visit_site_url: Optional[str] = FieldInfo(alias="visitSiteUrl", default=None)
    """Public destination URL."""

    watch_now_url: Optional[str] = FieldInfo(alias="watchNowUrl", default=None)
    """Public media action URL."""

    width: Optional[int] = None
    """Original width."""
