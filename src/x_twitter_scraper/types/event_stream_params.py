# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EventStreamParams"]


class EventStreamParams(TypedDict, total=False):
    include: Literal["post_metrics"]
    """Set to post_metrics to also get each post monitor's saved numbers.

    Any other value is refused.
    """

    look_back: Annotated[bool, PropertyInfo(alias="lookBack")]
    """Set to true to resume 30 seconds before Last-Event-ID, so late events still arrive.

    Events you have can arrive again, so skip IDs you've seen. An ID the stream
    can't find starts 5 minutes back, not 30 days.
    """
