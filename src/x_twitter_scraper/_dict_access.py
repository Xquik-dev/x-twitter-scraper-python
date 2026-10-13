# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

"""Deprecated dict access for models that replaced a plain dictionary field."""

from __future__ import annotations

import warnings
from typing import ClassVar, KeysView, ItemsView, ValuesView, cast
from datetime import datetime

from ._models import BaseModel

__all__ = [
    "EventDataDictAccess",
    "EventDetailDataDictAccess",
    "ExtractionJobDictAccess",
    "ExtractionResultDictAccess",
    "TweetEntitiesDictAccess",
]


def _as_sent(value: object) -> object:
    """Writes timestamps as the API sends them: milliseconds, and a Z suffix for UTC."""
    if isinstance(value, datetime):
        return value.isoformat(timespec="milliseconds").replace("+00:00", "Z")
    if isinstance(value, dict):
        return {key: _as_sent(item) for key, item in cast("dict[object, object]", value).items()}
    if isinstance(value, list):
        return [_as_sent(item) for item in cast("list[object]", value)]
    return value


class _DeprecatedDictAccess(BaseModel):
    """Reads JSON keys and values through `to_dict()`, as the replaced dictionary held them."""

    _dict_access_owner: ClassVar[str] = ""

    def _json_values(self) -> dict[object, object]:
        warnings.warn(
            f"Dict access on {self._dict_access_owner} is deprecated & goes away in a later minor version. "
            "Use attribute access or to_dict().",
            DeprecationWarning,
            stacklevel=3,
        )
        return cast("dict[object, object]", _as_sent(self.to_dict()))

    def __getitem__(self, key: str) -> object:
        return self._json_values()[key]

    def get(self, key: str, default: object = None) -> object:
        return self._json_values().get(key, default)

    def __contains__(self, key: object) -> bool:
        return key in self._json_values()

    def keys(self) -> KeysView[object]:
        return self._json_values().keys()

    def values(self) -> ValuesView[object]:
        return self._json_values().values()

    def items(self) -> ItemsView[object, object]:
        return self._json_values().items()


class EventDataDictAccess(_DeprecatedDictAccess):
    _dict_access_owner: ClassVar[str] = "Event.data"


class EventDetailDataDictAccess(_DeprecatedDictAccess):
    _dict_access_owner: ClassVar[str] = "EventDetail.data"


class ExtractionJobDictAccess(_DeprecatedDictAccess):
    _dict_access_owner: ClassVar[str] = "an extraction job"


class ExtractionResultDictAccess(_DeprecatedDictAccess):
    _dict_access_owner: ClassVar[str] = "an extraction result row"


class TweetEntitiesDictAccess(_DeprecatedDictAccess):
    _dict_access_owner: ClassVar[str] = "tweet entities"
