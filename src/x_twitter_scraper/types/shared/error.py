# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Error", "ErrorValue", "ErrorValueStructuredError", "FieldError"]


class ErrorValueStructuredError(BaseModel):
    code: Literal[
        "internal_error",
        "account_already_connected",
        "account_needs_reauth",
        "account_not_found",
        "account_required",
        "account_restricted",
        "api_key_limit_reached",
        "article_not_found",
        "closed",
        "dm_not_permitted",
        "invalid_format",
        "invalid_id",
        "invalid_input",
        "invalid_media_url",
        "invalid_message_id",
        "invalid_params",
        "invalid_tool_type",
        "invalid_tweet_id",
        "invalid_tweet_url",
        "invalid_user_id",
        "invalid_user_ids",
        "invalid_username",
        "invalid_json",
        "insufficient_credits",
        "job_not_found",
        "login_cooldown",
        "login_failed",
        "media_download_failed",
        "media_too_large",
        "missing_params",
        "missing_query",
        "monitor_already_exists",
        "monitor_profile_unavailable",
        "no_media",
        "no_credits",
        "no_subscription",
        "not_found",
        "payment_failed",
        "rate_limit_exceeded",
        "service_unavailable",
        "style_not_found",
        "subscription_inactive",
        "tweet_not_found",
        "unauthenticated",
        "unsupported_field",
        "user_not_found",
        "body_too_large",
        "bookmark_folders_unavailable",
        "broadcast_not_found",
        "checkout_unavailable",
        "connection_challenge_expired",
        "connection_challenge_inactive",
        "coverage_cursor_gone",
        "coverage_cursor_unavailable",
        "cursor_account_unavailable",
        "draft_not_found",
        "draw_too_large",
        "expired",
        "favoriters_unavailable",
        "forbidden",
        "guest_wallet_unavailable",
        "guest_wallets_disabled",
        "guest_wallets_unavailable",
        "idempotency_conflict",
        "idempotency_in_progress",
        "idempotency_key_conflict",
        "invalid_broadcast_id",
        "invalid_community_id",
        "invalid_community_topic",
        "invalid_complete_replies_request",
        "invalid_coverage_cursor",
        "invalid_coverage_request",
        "invalid_cursor",
        "invalid_idempotency_key",
        "invalid_job_filter",
        "invalid_job_id",
        "invalid_list_id",
        "invalid_output_options",
        "invalid_payment_amount",
        "invalid_range",
        "invalid_reply_options",
        "invalid_space_id",
        "likes_unavailable",
        "list_not_found",
        "login_rate_limited",
        "login_service_unavailable",
        "missing_idempotency_key",
        "missing_ids",
        "missing_url",
        "no_cached_style",
        "pagination_stalled",
        "passkey_required",
        "rate_limited",
        "read_request_timeout",
        "replay_unavailable",
        "replies_incomplete",
        "retweeters_incomplete",
        "search_unavailable",
        "space_canceled",
        "space_not_ended",
        "support_media_rate_limit",
        "support_request_rate_limit",
        "telegram_unavailable",
        "too_many_ids",
        "too_many_streams",
        "too_many_tweets",
        "unknown_field",
        "unsupported_media_combination",
        "unsupported_media_type",
        "webhook_inactive",
        "write_tracking_unavailable",
        "x_write_unconfirmed",
        "x_account_feature_required",
        "x_account_protected",
        "x_account_suspended",
        "x_api_rate_limited",
        "x_api_unavailable",
        "x_api_unauthorized",
        "x_auth_failure",
        "x_automation_refused",
        "x_community_not_joined",
        "x_community_not_selectable",
        "x_community_post_public",
        "x_community_post_removed",
        "x_content_too_long",
        "x_daily_limit",
        "x_dm_not_allowed",
        "x_dm_not_deleted",
        "x_dm_not_sent",
        "x_duplicate_action",
        "x_login_auth_failed",
        "x_login_challenge",
        "x_login_denied",
        "x_login_failed",
        "x_login_rate_limited",
        "x_login_service_unavailable",
        "x_login_suspended",
        "x_image_invalid",
        "x_media_rejected",
        "x_post_not_sent",
        "x_rate_limited",
        "x_rejected",
        "x_reply_not_allowed",
        "x_reply_target_unavailable",
        "x_target_not_found",
        "x_transient_error",
        "x_user_lookup_failed",
        "x_write_ambiguous",
        "x_write_failed",
    ]

    message: str

    type: Literal[
        "api_error",
        "authentication_error",
        "billing_error",
        "dependency_error",
        "invalid_request_error",
        "permission_error",
        "rate_limit_error",
    ]


ErrorValue: TypeAlias = Union[
    Literal[
        "internal_error",
        "account_already_connected",
        "account_needs_reauth",
        "account_not_found",
        "account_required",
        "account_restricted",
        "api_key_limit_reached",
        "article_not_found",
        "closed",
        "dm_not_permitted",
        "invalid_format",
        "invalid_id",
        "invalid_input",
        "invalid_media_url",
        "invalid_message_id",
        "invalid_params",
        "invalid_tool_type",
        "invalid_tweet_id",
        "invalid_tweet_url",
        "invalid_user_id",
        "invalid_user_ids",
        "invalid_username",
        "invalid_json",
        "insufficient_credits",
        "job_not_found",
        "login_cooldown",
        "login_failed",
        "media_download_failed",
        "media_too_large",
        "missing_params",
        "missing_query",
        "monitor_already_exists",
        "monitor_profile_unavailable",
        "no_media",
        "no_credits",
        "no_subscription",
        "not_found",
        "payment_failed",
        "rate_limit_exceeded",
        "service_unavailable",
        "style_not_found",
        "subscription_inactive",
        "tweet_not_found",
        "unauthenticated",
        "unsupported_field",
        "user_not_found",
        "body_too_large",
        "bookmark_folders_unavailable",
        "broadcast_not_found",
        "checkout_unavailable",
        "connection_challenge_expired",
        "connection_challenge_inactive",
        "coverage_cursor_gone",
        "coverage_cursor_unavailable",
        "cursor_account_unavailable",
        "draft_not_found",
        "draw_too_large",
        "expired",
        "favoriters_unavailable",
        "forbidden",
        "guest_wallet_unavailable",
        "guest_wallets_disabled",
        "guest_wallets_unavailable",
        "idempotency_conflict",
        "idempotency_in_progress",
        "idempotency_key_conflict",
        "invalid_broadcast_id",
        "invalid_community_id",
        "invalid_community_topic",
        "invalid_complete_replies_request",
        "invalid_coverage_cursor",
        "invalid_coverage_request",
        "invalid_cursor",
        "invalid_idempotency_key",
        "invalid_job_filter",
        "invalid_job_id",
        "invalid_list_id",
        "invalid_output_options",
        "invalid_payment_amount",
        "invalid_range",
        "invalid_reply_options",
        "invalid_space_id",
        "likes_unavailable",
        "list_not_found",
        "login_rate_limited",
        "login_service_unavailable",
        "missing_idempotency_key",
        "missing_ids",
        "missing_url",
        "no_cached_style",
        "pagination_stalled",
        "passkey_required",
        "rate_limited",
        "read_request_timeout",
        "replay_unavailable",
        "replies_incomplete",
        "retweeters_incomplete",
        "search_unavailable",
        "space_canceled",
        "space_not_ended",
        "support_media_rate_limit",
        "support_request_rate_limit",
        "telegram_unavailable",
        "too_many_ids",
        "too_many_streams",
        "too_many_tweets",
        "unknown_field",
        "unsupported_media_combination",
        "unsupported_media_type",
        "webhook_inactive",
        "write_tracking_unavailable",
        "x_write_unconfirmed",
        "x_account_feature_required",
        "x_account_protected",
        "x_account_suspended",
        "x_api_rate_limited",
        "x_api_unavailable",
        "x_api_unauthorized",
        "x_auth_failure",
        "x_automation_refused",
        "x_community_not_joined",
        "x_community_not_selectable",
        "x_community_post_public",
        "x_community_post_removed",
        "x_content_too_long",
        "x_daily_limit",
        "x_dm_not_allowed",
        "x_dm_not_deleted",
        "x_dm_not_sent",
        "x_duplicate_action",
        "x_login_auth_failed",
        "x_login_challenge",
        "x_login_denied",
        "x_login_failed",
        "x_login_rate_limited",
        "x_login_service_unavailable",
        "x_login_suspended",
        "x_image_invalid",
        "x_media_rejected",
        "x_post_not_sent",
        "x_rate_limited",
        "x_rejected",
        "x_reply_not_allowed",
        "x_reply_target_unavailable",
        "x_target_not_found",
        "x_transient_error",
        "x_user_lookup_failed",
        "x_write_ambiguous",
        "x_write_failed",
    ],
    ErrorValueStructuredError,
]


class FieldError(BaseModel):
    code: Literal["unknown_field"]

    field: str
    """The name as the request wrote it."""

    message: str
    """What to send instead."""

    path: Literal["query.fields", "query.omit"]
    """The parameter that held the name."""

    suggestion: Optional[str] = None
    """The closest valid name, when 1 is close."""


class Error(BaseModel):
    """Error response.

    Default v1 returns a legacy string code. Send `xquik-api-contract: 2026-04-29` for the structured best-practice error object.
    """

    error: ErrorValue

    allowed_fields: Optional[List[str]] = FieldInfo(alias="allowedFields", default=None)
    """
    With unknown_field: the valid names where the first unknown name in fields or
    omit stopped.
    """

    field_errors: Optional[List[FieldError]] = FieldInfo(alias="fieldErrors", default=None)
    """
    With unknown_field: each unknown name in fields or omit, with the name it most
    likely meant.
    """

    message: Optional[str] = None
    """Human-readable error guidance."""

    reason: Optional[str] = None
    """Machine-readable reason.

    A login failure names its cause, such as temporary_issue. A user_not_found
    answer names why X shows no profile: not_found or suspended. A tweet_not_found
    answer names why X shows no post, when X said: deleted, author_suspended or
    protected.
    """

    retry_after: Optional[int] = FieldInfo(alias="retryAfter", default=None)
    """Seconds until the next permitted request."""

    retry_after_ms: Optional[int] = FieldInfo(alias="retryAfterMs", default=None)
    """Required wait in milliseconds."""
