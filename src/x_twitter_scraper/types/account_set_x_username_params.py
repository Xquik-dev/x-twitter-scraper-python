# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccountSetXUsernameParams"]


class AccountSetXUsernameParams(TypedDict, total=False):
    username: Required[str]
    """X username without @"""
