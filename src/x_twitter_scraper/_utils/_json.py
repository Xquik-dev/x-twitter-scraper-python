# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

import json
from typing import Any
from datetime import datetime
from typing_extensions import override

import pydantic

from .._compat import model_dump


def openapi_dumps(obj: Any) -> bytes:
    return json.dumps(
        obj,
        cls=_CustomEncoder,
        ensure_ascii=False,
        separators=(",", ":"),
        allow_nan=False,
    ).encode()


class _CustomEncoder(json.JSONEncoder):
    @override
    def default(self, o: Any) -> Any:
        if isinstance(o, datetime):
            return o.isoformat()
        if isinstance(o, pydantic.BaseModel):
            return model_dump(o, exclude_unset=True, mode="json", by_alias=True)
        return super().default(o)
