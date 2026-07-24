# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["DmSendParams"]


class DmSendParams(TypedDict, total=False):
    account: Required[str]
    """X account (@username or ID) sending the DM"""

    text: Required[str]

    idempotency_key: Required[Annotated[str, PropertyInfo(alias="Idempotency-Key")]]

    media_ids: SequenceNotStr[str]
    """Optional array containing exactly 1 uploaded media ID."""
