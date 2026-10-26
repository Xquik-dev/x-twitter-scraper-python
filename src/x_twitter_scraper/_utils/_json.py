# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

import json
from datetime import datetime
from typing_extensions import override

from .._compat import PydanticModel, model_dump


def openapi_dumps(obj: object) -> bytes:
    return _CustomEncoder(
        ensure_ascii=False,
        separators=(",", ":"),
        allow_nan=False,
    ).encode(obj).encode()


class _CustomEncoder(json.JSONEncoder):
    @override
    def default(self, o: object) -> object:
        if isinstance(o, datetime):
            return o.isoformat()
        if isinstance(o, PydanticModel):
            return model_dump(o, exclude_unset=True, mode="json", by_alias=True)
        default: object = super().default(o)
        return default
