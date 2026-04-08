# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UserRetrieveMentionsParams"]


class UserRetrieveMentionsParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor for mentions"""

    since_time: Annotated[str, PropertyInfo(alias="sinceTime")]
    """Unix timestamp - return mentions after this time"""

    until_time: Annotated[str, PropertyInfo(alias="untilTime")]
    """Unix timestamp - return mentions before this time"""
