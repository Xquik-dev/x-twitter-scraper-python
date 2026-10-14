# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import re
from typing import (
    Any,
    Mapping,
)
from urllib.parse import quote

_DOT_SEGMENT_RE = re.compile(r"^(?:\.|%2[eE]){1,2}$")

_PLACEHOLDER_RE = re.compile(r"\{(\w+)\}")


def _interpolate(
    template: str,
    values: Mapping[str, Any],
    safe: str,
) -> str:
    parts = _PLACEHOLDER_RE.split(template)

    for i in range(1, len(parts), 2):
        name = parts[i]
        if name not in values:
            raise KeyError(f"a value for placeholder {{{name}}} was not provided")
        val = values[name]
        if val is None:
            parts[i] = "null"
        elif isinstance(val, bool):
            parts[i] = "true" if val else "false"
        else:
            parts[i] = quote(str(values[name]), safe=safe)

    return "".join(parts)


def path_template(template: str, /, **kwargs: Any) -> str:
    rest, fragment_separator, fragment_template = template.partition("#")
    path_template, query_separator, query_template = rest.partition("?")

    path_result = _interpolate(path_template, kwargs, "!$&'()*+,;=:@")

    for segment in path_result.split("/"):
        if _DOT_SEGMENT_RE.match(segment):
            raise ValueError(f"Constructed path {path_result!r} contains dot-segment {segment!r} which is not allowed")

    result = path_result
    if query_separator:
        result += "?" + _interpolate(query_template, kwargs, "!$'()*+,;:@/?")
    if fragment_separator:
        result += "#" + _interpolate(fragment_template, kwargs, "!$&'()*+,;=:@/?")

    return result
