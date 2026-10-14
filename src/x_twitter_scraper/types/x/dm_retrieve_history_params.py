# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DmRetrieveHistoryParams"]


class DmRetrieveHistoryParams(TypedDict, total=False):
    account: Required[str]
    """
    X handle (without the `@` prefix) of the connected X account used to read the
    conversation. The account must be a participant in the conversation.
    """

    cursor: str
    """Pagination cursor for collection results.

    Also read as next_cursor, next_token, pagination_token or continuation_token.
    """

    max_id: Annotated[str, PropertyInfo(alias="maxId")]
    """Legacy pagination cursor (backward compat)"""
