# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

"""Deprecated dict access for models that replaced a plain dictionary field."""

from __future__ import annotations

import warnings
from typing import ClassVar

from ._models import BaseModel

__all__ = ["EventDataDictAccess", "EventDetailDataDictAccess"]


class _DeprecatedDictAccess(BaseModel):
    """Reads JSON keys through `to_dict()`, as the replaced dictionary did."""

    _dict_access_owner: ClassVar[str] = ""

    def _dict_access_message(self) -> str:
        return (
            f"Dict access on {self._dict_access_owner} is deprecated & goes away in a later minor version. "
            "Use attribute access or to_dict()."
        )

    def __getitem__(self, key: str) -> object:
        warnings.warn(self._dict_access_message(), DeprecationWarning, stacklevel=2)
        return self.to_dict(mode="json")[key]

    def get(self, key: str, default: object = None) -> object:
        warnings.warn(self._dict_access_message(), DeprecationWarning, stacklevel=2)
        return self.to_dict(mode="json").get(key, default)

    def __contains__(self, key: object) -> bool:
        warnings.warn(self._dict_access_message(), DeprecationWarning, stacklevel=2)
        return key in self.to_dict(mode="json")


class EventDataDictAccess(_DeprecatedDictAccess):
    _dict_access_owner: ClassVar[str] = "Event.data"


class EventDetailDataDictAccess(_DeprecatedDictAccess):
    _dict_access_owner: ClassVar[str] = "EventDetail.data"
