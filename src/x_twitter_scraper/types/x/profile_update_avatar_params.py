# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ProfileUpdateAvatarParams"]


class ProfileUpdateAvatarParams(TypedDict, total=False):
    account: Required[str]
    """X account (@username or ID) receiving avatar from URL"""

    url: Required[str]
    """HTTPS URL to the avatar image to download"""

    idempotency_key: Required[Annotated[str, PropertyInfo(alias="Idempotency-Key")]]
