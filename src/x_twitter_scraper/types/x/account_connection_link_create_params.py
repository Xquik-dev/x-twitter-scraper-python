# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AccountConnectionLinkCreateParams"]


class AccountConnectionLinkCreateParams(TypedDict, total=False):
    account_id: Annotated[str, PropertyInfo(alias="accountId")]
    """The ID of 1 of your X accounts. The link then reconnects that account."""

    reference: str
    """Your own ID for this person. It comes back when you read the link."""

    return_url: Annotated[str, PropertyInfo(alias="returnUrl")]
    """A public https URL the page offers as a button once the account connects.

    Xquik never redirects by itself, & never adds the token.
    """
