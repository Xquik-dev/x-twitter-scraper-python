# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ProfileUpdateParams"]


class ProfileUpdateParams(TypedDict, total=False):
    account: Required[str]
    """X account (@username or ID) to update profile"""

    idempotency_key: Required[Annotated[str, PropertyInfo(alias="Idempotency-Key")]]

    prefer: Annotated[str, PropertyInfo(alias="Prefer")]
    """A long write answers 202 with a status link, then lands on X.

    `wait=<seconds>` asks for the answer within that many seconds, up to 85. If the
    write is still running then, the API answers 202 with Location. Poll Location
    until `terminal` is true, and don't send the write again.
    """

    description: str
    """Bio, up to 160 characters. An emoji counts as 2."""

    location: str
    """Location, up to 30 characters. An emoji counts as 2."""

    name: str
    """Display name, 1 to 50 characters. An emoji counts as 2."""

    url: str
    """Website URL"""
