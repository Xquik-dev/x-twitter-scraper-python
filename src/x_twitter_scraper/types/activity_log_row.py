# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import Union

from .._models import BaseModel

__all__ = ["ActivityLogRow"]


class ActivityLogRow(BaseModel):
    """1 Activity log row.

    A cut list ends with a row whose category is notice and whose activity says
    where it stopped.
    """

    time: str
    """ISO 8601 time in UTC to the millisecond. Empty on the notice row."""

    category: str

    type: str

    activity: str

    status: str

    source: str

    target: str

    results: Union[int, str]
    """Result count, or an empty string when the activity has none."""

    credits: Union[int, str]
    """Credits, or an empty string when the activity has none."""

    details: str

    id: str
    """Activity ID. client.activity.retrieve returns its full record."""

    link: str
