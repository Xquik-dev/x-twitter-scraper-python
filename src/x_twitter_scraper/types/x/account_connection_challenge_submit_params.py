# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccountConnectionChallengeSubmitParams"]


class AccountConnectionChallengeSubmitParams(TypedDict, total=False):
    email_code: Required[str]
    """Code sent to the account email."""
