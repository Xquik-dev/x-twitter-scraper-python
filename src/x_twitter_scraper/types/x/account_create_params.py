# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccountCreateParams"]


class AccountCreateParams(TypedDict, total=False):
    email: Required[str]
    """Account email"""

    password: Required[str]
    """Account password"""

    username: Required[str]
    """X username"""

    proxy_country: str
    """Proxy country code"""

    totp_secret: str
    """TOTP secret for 2FA"""
