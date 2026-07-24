# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TicketReplyParams"]


class TicketReplyParams(TypedDict, total=False):
    content: Required[Annotated[str, PropertyInfo(alias="body")]]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
