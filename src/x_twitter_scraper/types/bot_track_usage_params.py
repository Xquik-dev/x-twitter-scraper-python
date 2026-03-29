# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BotTrackUsageParams"]


class BotTrackUsageParams(TypedDict, total=False):
    input_tokens: Required[Annotated[int, PropertyInfo(alias="inputTokens")]]

    output_tokens: Required[Annotated[int, PropertyInfo(alias="outputTokens")]]

    platform_user_id: Required[Annotated[str, PropertyInfo(alias="platformUserId")]]
