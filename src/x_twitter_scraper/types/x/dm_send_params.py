# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

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

    prefer: Annotated[str, PropertyInfo(alias="Prefer")]
    """A long write answers 202 with a status link, then lands on X.

    `wait=<seconds>` asks for the answer within that many seconds, up to 85. If the
    write is still running then, the API answers 202 with Location. Poll Location
    until `terminal` is true, and don't send the write again.
    """

    media_ids: SequenceNotStr[str]
    """Optional array containing exactly 1 uploaded media ID."""
