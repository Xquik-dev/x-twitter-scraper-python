# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["GuestWalletTopupParams"]


class GuestWalletTopupParams(TypedDict, total=False):
    amount_minor: Required[int]
    """USD cents accepted for this checkout."""

    currency: Required[Literal["usd"]]

    idempotency_key: Required[Annotated[str, PropertyInfo(alias="Idempotency-Key")]]
