# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    event_types: Required[
        Annotated[
            List[
                Literal["tweet.new", "tweet.reply", "tweet.retweet", "tweet.quote", "follower.gained", "follower.lost"]
            ],
            PropertyInfo(alias="eventTypes"),
        ]
    ]
    """Array of event types to subscribe to."""

    url: Required[str]
    """HTTPS URL"""
