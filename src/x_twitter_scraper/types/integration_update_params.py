# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["IntegrationUpdateParams"]


class IntegrationUpdateParams(TypedDict, total=False):
    event_types: Annotated[
        List[Literal["tweet.new", "tweet.reply", "tweet.retweet", "tweet.quote", "follower.gained", "follower.lost"]],
        PropertyInfo(alias="eventTypes"),
    ]

    filters: Dict[str, object]

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]

    message_template: Annotated[Dict[str, object], PropertyInfo(alias="messageTemplate")]

    name: str

    scope_all_monitors: Annotated[bool, PropertyInfo(alias="scopeAllMonitors")]

    silent_push: Annotated[bool, PropertyInfo(alias="silentPush")]
