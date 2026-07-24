# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["ComposeCreateParams", "ComposePrepareRequest", "ComposeRefineRequest", "ComposeScoreRequest"]


class ComposePrepareRequest(TypedDict, total=False):
    step: Required[Literal["compose"]]

    topic: Required[str]
    """Subject for the post."""

    goal: Literal["engagement", "followers", "authority", "conversation"]
    """Editorial goal used to order the rules and questions."""

    style_username: Annotated[str, PropertyInfo(alias="styleUsername")]
    """Username from a style analysis saved to this account."""


class ComposeRefineRequest(TypedDict, total=False):
    goal: Required[Literal["engagement", "followers", "authority", "conversation"]]
    """Editorial goal for the guidance."""

    step: Required[Literal["refine"]]

    tone: Required[str]
    """Requested writing tone."""

    topic: Required[str]
    """Subject for the post."""

    additional_context: Annotated[str, PropertyInfo(alias="additionalContext")]
    """Audience, constraints, sources, or other writing context."""

    call_to_action: Annotated[str, PropertyInfo(alias="callToAction")]
    """Specific action the draft should request."""

    media_type: Annotated[Literal["photo", "video", "none"], PropertyInfo(alias="mediaType")]
    """Planned media type."""


class ComposeScoreRequest(TypedDict, total=False):
    draft: Required[str]
    """Full post text for deterministic editorial checks."""

    step: Required[Literal["score"]]

    has_link: Annotated[bool, PropertyInfo(alias="hasLink")]
    """True when a separate link card is attached."""

    has_media: Annotated[bool, PropertyInfo(alias="hasMedia")]
    """Accepted for backward compatibility. Text checks ignore this field."""


ComposeCreateParams: TypeAlias = Union[ComposePrepareRequest, ComposeRefineRequest, ComposeScoreRequest]
