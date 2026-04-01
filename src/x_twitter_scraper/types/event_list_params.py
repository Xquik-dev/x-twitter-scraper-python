# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EventListParams"]


class EventListParams(TypedDict, total=False):
    after: str
    """Cursor for pagination"""

    event_type: Annotated[
        Literal["tweet.new", "tweet.reply", "tweet.retweet", "tweet.quote", "follower.gained", "follower.lost"],
        PropertyInfo(alias="eventType"),
    ]

    limit: int

    monitor_id: Annotated[str, PropertyInfo(alias="monitorId")]
