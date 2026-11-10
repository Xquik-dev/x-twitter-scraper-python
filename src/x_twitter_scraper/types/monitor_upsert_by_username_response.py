# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from .monitor import Monitor

__all__ = ["MonitorUpsertByUsernameResponse"]


class MonitorUpsertByUsernameResponse(Monitor):
    """Account monitor that a call created, turned back on or updated."""

    created: bool
    """True when this call created the monitor or turned it back on.

    False when it updated a running monitor.
    """
