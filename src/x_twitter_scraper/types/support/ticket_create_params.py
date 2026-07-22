# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TicketCreateParams"]


class TicketCreateParams(TypedDict, total=False):
    content: Required[Annotated[str, PropertyInfo(alias="body")]]

    subject: Required[str]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
