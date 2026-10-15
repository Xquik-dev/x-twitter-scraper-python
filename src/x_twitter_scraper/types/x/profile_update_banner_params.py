# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["ProfileUpdateBannerParams"]


class ProfileUpdateBannerParams(TypedDict, total=False):
    account: Required[str]
    """X account (@username or ID) receiving banner from URL"""

    url: str
    """HTTPS URL to the banner image to download"""

    idempotency_key: Required[Annotated[str, PropertyInfo(alias="Idempotency-Key")]]

    file: FileTypes
    """Banner image (max 15 MiB)"""
