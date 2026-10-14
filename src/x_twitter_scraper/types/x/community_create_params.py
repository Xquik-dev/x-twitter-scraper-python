# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CommunityCreateParams"]


class CommunityCreateParams(TypedDict, total=False):
    account: Required[str]
    """X account (@username or ID) creating the community"""

    name: Required[str]
    """Community name, 1 to 100 characters, as X takes it"""

    idempotency_key: Required[Annotated[str, PropertyInfo(alias="Idempotency-Key")]]

    description: str
    """Community description"""
