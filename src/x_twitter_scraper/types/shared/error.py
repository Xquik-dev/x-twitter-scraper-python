# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Error"]


class Error(BaseModel):
    error: Literal[
        "internal_error",
        "invalid_format",
        "invalid_id",
        "invalid_input",
        "invalid_params",
        "invalid_tool_type",
        "invalid_tweet_id",
        "invalid_tweet_url",
        "invalid_username",
        "missing_params",
        "missing_query",
        "monitor_already_exists",
        "monitor_limit_reached",
        "no_subscription",
        "not_found",
        "stream_registration_failed",
        "subscription_inactive",
        "tweet_not_found",
        "unauthenticated",
        "usage_limit_reached",
        "user_not_found",
        "webhook_inactive",
        "x_api_rate_limited",
        "x_api_unavailable",
        "x_api_unauthorized",
    ]
