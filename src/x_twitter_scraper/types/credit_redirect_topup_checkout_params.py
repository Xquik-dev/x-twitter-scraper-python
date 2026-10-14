# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CreditRedirectTopupCheckoutParams"]


class CreditRedirectTopupCheckoutParams(TypedDict, total=False):
    session_id: Required[str]
    """Billing session ID returned by the top-up billing flow."""
