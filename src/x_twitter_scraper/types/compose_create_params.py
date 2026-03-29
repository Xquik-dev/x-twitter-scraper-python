# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ComposeCreateParams"]


class ComposeCreateParams(TypedDict, total=False):
    step: Required[Literal["compose", "refine", "score"]]
    """Workflow step"""

    additional_context: Annotated[str, PropertyInfo(alias="additionalContext")]
    """Extra context or URLs (refine)"""

    call_to_action: Annotated[str, PropertyInfo(alias="callToAction")]
    """Desired call to action (refine)"""

    draft: str
    """Tweet draft text to evaluate (score)"""

    goal: Literal["engagement", "followers", "authority", "conversation"]
    """Optimization goal"""

    has_link: Annotated[bool, PropertyInfo(alias="hasLink")]
    """Whether a link is attached (score)"""

    has_media: Annotated[bool, PropertyInfo(alias="hasMedia")]
    """Whether media is attached (score)"""

    media_type: Annotated[Literal["photo", "video", "none"], PropertyInfo(alias="mediaType")]
    """Media type (refine)"""

    style_username: Annotated[str, PropertyInfo(alias="styleUsername")]
    """Cached style username for voice matching (compose)"""

    tone: str
    """Desired tone (refine)"""

    topic: str
    """Tweet topic (compose, refine)"""
