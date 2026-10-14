# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AccountRetrieveResponse", "MonitorBilling", "Subscription", "CreditInfo"]


class MonitorBilling(BaseModel):
    active_daily_estimate: str = FieldInfo(alias="activeDailyEstimate")
    """Daily credits for currently active monitors."""

    active_hourly_burn: str = FieldInfo(alias="activeHourlyBurn")
    """Credits charged each hour for currently active monitors."""

    credits_per_active_monitor_day: Literal["720"] = FieldInfo(alias="creditsPerActiveMonitorDay")
    """Daily credits charged for 1 active monitor."""

    credits_per_active_monitor_hour: Literal["30"] = FieldInfo(alias="creditsPerActiveMonitorHour")
    """Hourly credits charged for 1 active monitor. It is a monitor's only charge."""

    events_included: bool = FieldInfo(alias="eventsIncluded")
    """Webhook and event deliveries are included in monitor billing."""

    instant_check_interval_seconds: int = FieldInfo(alias="instantCheckIntervalSeconds")
    """Active monitors check every 1 second."""

    unlimited_slots: bool = FieldInfo(alias="unlimitedSlots")
    """Monitor slot count is unlimited."""


class Subscription(BaseModel):
    """Subscription state without billing provider identifiers."""

    status: Literal["none", "active", "past_due", "canceling", "incomplete"]

    current_period_end: Optional[datetime] = FieldInfo(alias="currentPeriodEnd", default=None)
    """Renewal date, or the end date when canceling."""

    current_period_start: Optional[datetime] = FieldInfo(alias="currentPeriodStart", default=None)

    tier: Optional[Literal["starter", "pro", "business"]] = None


class CreditInfo(BaseModel):
    auto_topup_amount_dollars: float = FieldInfo(alias="autoTopupAmountDollars")
    """Dollar amount charged when automatic top-up runs."""

    auto_topup_enabled: bool = FieldInfo(alias="autoTopupEnabled")

    auto_topup_stopped: bool = FieldInfo(alias="autoTopupStopped")
    """
    True when 3 declined charges in a row on one card stopped automatic top-up while
    it stays enabled. A paid top-up, a paid plan renewal, or the next automatic
    top-up on a new card clears it.
    """

    auto_topup_threshold: Literal["10000", "50000", "100000", "250000"] = FieldInfo(alias="autoTopupThreshold")
    """Bigint string threshold that triggers automatic top-up when enabled."""

    balance: str
    """Bigint string to preserve precision above Number.MAX_SAFE_INTEGER."""

    lifetime_purchased: str = FieldInfo(alias="lifetimePurchased")
    """Total purchased credits as a bigint string."""

    lifetime_used: str = FieldInfo(alias="lifetimeUsed")
    """Total consumed credits as a bigint string."""


class AccountRetrieveResponse(BaseModel):
    monitor_billing: MonitorBilling = FieldInfo(alias="monitorBilling")

    monitors_allowed: int = FieldInfo(alias="monitorsAllowed")
    """Deprecated.

    Monitor slots are unlimited, so this is always Number.MAX_SAFE_INTEGER.
    """

    monitors_used: int = FieldInfo(alias="monitorsUsed")

    plan: Literal["active", "inactive"]

    subscription: Subscription
    """Subscription state without billing provider identifiers."""

    credit_info: Optional[CreditInfo] = FieldInfo(alias="creditInfo", default=None)

    x_username: Optional[str] = FieldInfo(alias="xUsername", default=None)
    """Linked X username, omitted when no X account is connected."""
