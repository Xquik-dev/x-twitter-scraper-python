# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import FileTypes, SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["TicketCreateParams"]


class TicketCreateParams(TypedDict, total=False):
    subject: Required[str]
    """Non-empty support ticket subject."""

    attachments: SequenceNotStr[FileTypes]
    """1 to 4 support image or video uploads."""

    content: Annotated[str, PropertyInfo(alias="body")]
    """Non-empty support message text."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
