# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountUpdateLocaleParams"]


class AccountUpdateLocaleParams(TypedDict, total=False):
    locale: Required[Literal["en", "tr", "es"]]
