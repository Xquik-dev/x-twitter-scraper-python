# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

import json
from typing import Callable
from datetime import datetime
from typing_extensions import override

from .._types import JsonValue
from .._compat import PydanticModel, model_dump

# json.loads declares Any, and without an object hook it returns only JSON values. https://docs.python.org/3/library/json.html#json-to-py-table
json_loads: Callable[[str | bytes | bytearray], JsonValue] = json.loads


def openapi_dumps(obj: object) -> bytes:
    return (
        _CustomEncoder(
            ensure_ascii=False,
            separators=(",", ":"),
            allow_nan=False,
        )
        .encode(obj)
        .encode()
    )


class _CustomEncoder(json.JSONEncoder):
    @override
    def default(self, o: object) -> object:
        if isinstance(o, datetime):
            return o.isoformat()
        if isinstance(o, PydanticModel):
            return model_dump(o, exclude_unset=True, mode="json", by_alias=True)
        default: object = super().default(o)
        return default
