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
    """Bio, up to 160 characters. An emoji counts as 2."""

    location: str
    """Location, up to 30 characters. An emoji counts as 2."""

    name: str
    """Display name, 1 to 50 characters. An emoji counts as 2."""

    url: str
    """Website URL"""
