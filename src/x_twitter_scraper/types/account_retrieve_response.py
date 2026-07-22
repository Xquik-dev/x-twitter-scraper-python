# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AccountRetrieveResponse", "MonitorBilling", "CreditInfo"]


class MonitorBilling(BaseModel):
    active_daily_estimate: str = FieldInfo(alias="activeDailyEstimate")
    """Estimated daily credits for currently active monitors."""

    active_hourly_burn: str = FieldInfo(alias="activeHourlyBurn")
    """Credits charged each hour for currently active monitors."""

    credits_per_active_monitor_day: str = FieldInfo(alias="creditsPerActiveMonitorDay")
    """Estimated daily credits for 1 active instant monitor."""

    credits_per_active_monitor_hour: str = FieldInfo(alias="creditsPerActiveMonitorHour")
    """Hourly credits charged for 1 active instant monitor."""

    events_included: bool = FieldInfo(alias="eventsIncluded")
    """Webhook and event deliveries are included in monitor billing."""

    instant_check_interval_seconds: int = FieldInfo(alias="instantCheckIntervalSeconds")
    """Active monitors check every 1 second."""

    unlimited_slots: bool = FieldInfo(alias="unlimitedSlots")
    """Monitor slot count is unlimited."""


class CreditInfo(BaseModel):
    auto_topup_amount_dollars: float = FieldInfo(alias="autoTopupAmountDollars")
    """Dollar amount charged when automatic top-up runs."""

    auto_topup_enabled: bool = FieldInfo(alias="autoTopupEnabled")

    auto_topup_threshold: str = FieldInfo(alias="autoTopupThreshold")
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

    credit_info: Optional[CreditInfo] = FieldInfo(alias="creditInfo", default=None)

    x_username: Optional[str] = FieldInfo(alias="xUsername", default=None)
    """Linked X username, omitted when no X account is connected."""
