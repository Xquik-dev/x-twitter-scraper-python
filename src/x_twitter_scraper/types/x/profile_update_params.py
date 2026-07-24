# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ProfileUpdateParams"]


class ProfileUpdateParams(TypedDict, total=False):
    account: Required[str]
    """X account (@username or ID) to update profile"""

    idempotency_key: Required[Annotated[str, PropertyInfo(alias="Idempotency-Key")]]

    description: str
    """Bio description"""

    location: str

    name: str
    """Display name"""

    url: str
    """Website URL"""
