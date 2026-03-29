# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PlatformLinkLookupParams"]


class PlatformLinkLookupParams(TypedDict, total=False):
    platform: Required[str]

    platform_user_id: Required[Annotated[str, PropertyInfo(alias="platformUserId")]]
