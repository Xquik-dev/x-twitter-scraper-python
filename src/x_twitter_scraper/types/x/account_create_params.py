# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccountCreateParams"]


class AccountCreateParams(TypedDict, total=False):
    email: Required[str]
    """Account email"""

    password: Required[str]
    """Account password"""

    totp_secret: Required[str]
    """Authenticator App TOTP secret required for durable login"""

    username: Required[str]
    """X username"""
