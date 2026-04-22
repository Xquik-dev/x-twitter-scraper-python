# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AccountCreateResponse"]


class AccountCreateResponse(BaseModel):
    """Sanitized X account summary returned by connect and reauth.

    Includes an optional `loginCountry` field surfaced only when the declared proxy region had no Driver capacity and the login fell back to a single US consumer device for this one-time action. Future activity continues to use the selected `proxy_country`; the field is omitted on normal logins.
    """

    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    health: Literal["healthy", "locked", "needsReauth", "recovering", "suspended", "temporaryIssue"]

    status: str

    x_user_id: str = FieldInfo(alias="xUserId")

    x_username: str = FieldInfo(alias="xUsername")

    login_country: Optional[str] = FieldInfo(alias="loginCountry", default=None)
    """
    ISO-3166-1 alpha-2 country code of the Driver consumer device used for this
    login. Present only when the US fallback was triggered because Driver had no
    capacity in the declared region. Omitted otherwise.
    """
