# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["FollowCreateParams"]


class FollowCreateParams(TypedDict, total=False):
    account: Required[str]
    """X account identifier (@username or account ID)"""

    idempotency_key: Required[Annotated[str, PropertyInfo(alias="Idempotency-Key")]]
