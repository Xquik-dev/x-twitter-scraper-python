# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MonitorUpdateParams"]


class MonitorUpdateParams(TypedDict, total=False):
    event_types: Annotated[
        List[Literal["tweet.new", "tweet.reply", "tweet.retweet", "tweet.quote", "follower.gained", "follower.lost"]],
        PropertyInfo(alias="eventTypes"),
    ]

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]
