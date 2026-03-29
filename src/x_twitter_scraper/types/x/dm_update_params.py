# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["DmUpdateParams"]


class DmUpdateParams(TypedDict, total=False):
    account: Required[str]
    """X account (@username or account ID)"""

    text: Required[str]

    media_ids: SequenceNotStr[str]

    reply_to_message_id: str
