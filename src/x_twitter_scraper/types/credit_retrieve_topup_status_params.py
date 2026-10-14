# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CreditRetrieveTopupStatusParams"]


class CreditRetrieveTopupStatusParams(TypedDict, total=False):
    session_id: Required[str]
    """Top-up session ID to inspect."""
