# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccountReauthParams"]


class AccountReauthParams(TypedDict, total=False):
    password: Required[str]
    """Updated account password"""

    email: str
    """Email for the X account (updates stored email)"""

    totp_secret: str
    """TOTP secret for 2FA re-authentication"""
