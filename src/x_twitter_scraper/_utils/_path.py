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

# Matches '.' or '..' where each dot is either literal or percent-encoded (%2e / %2E).
_DOT_SEGMENT_RE = re.compile(r"^(?:\.|%2[eE]){1,2}$")

_PLACEHOLDER_RE = re.compile(r"\{(\w+)\}")


def _interpolate(
    template: str,
    values: Mapping[str, Any],
    safe: str,
) -> str:
    """Replace {name} placeholders, percent-encoding values with the component's safe characters.

    Placeholder names are looked up in `values`. Unreserved characters remain safe.
    Callers supply RFC 3986 component characters: path pchar (§3.3), query (§3.4),
    or fragment (§3.5). Query values additionally encode & and = to prevent injection.
    Path values encode /, while query and fragment values permit / and ?.
    https://datatracker.ietf.org/doc/html/rfc3986#section-3.3

    Raises:
        KeyError: If a placeholder is not found in `values`.
    """
    # re.split with a capturing group returns alternating
    # [text, name, text, name, ..., text] elements.
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
    """Interpolate {name} placeholders in `template` from keyword arguments.

    Args:
        template: The template string containing {name} placeholders.
        **kwargs: Keyword arguments to interpolate into the template.

    Returns:
        The template with placeholders interpolated and percent-encoded.

        Safe characters for percent-encoding are dependent on the URI component.
        Placeholders in path and fragment portions are percent-encoded where the `segment`
        and `fragment` sets from RFC 3986 respectively are considered safe.
        Placeholders in the query portion are percent-encoded where the `query` set from
        RFC 3986 §3.3 is considered safe except for = and & characters.

    Raises:
        KeyError: If a placeholder is not found in `kwargs`.
        ValueError: If resulting path contains /./ or /../ segments (including percent-encoded dot-segments).
    """
    # Split the template into path, query, and fragment portions.
    rest, fragment_separator, fragment_template = template.partition("#")
    path_template, query_separator, query_template = rest.partition("?")

    # Interpolate each portion with the appropriate quoting rules.
    path_result = _interpolate(path_template, kwargs, "!$&'()*+,;=:@")

    # Reject dot-segments (. and ..) in the final assembled path.  The check
    # runs after interpolation so that adjacent placeholders or a mix of static
    # text and placeholders that together form a dot-segment are caught.
    # Also reject percent-encoded dot-segments to protect against incorrectly
    # implemented normalization in servers/proxies.
    for segment in path_result.split("/"):
        if _DOT_SEGMENT_RE.match(segment):
            raise ValueError(f"Constructed path {path_result!r} contains dot-segment {segment!r} which is not allowed")

    result = path_result
    if query_separator:
        result += "?" + _interpolate(query_template, kwargs, "!$'()*+,;:@/?")
    if fragment_separator:
        result += "#" + _interpolate(fragment_template, kwargs, "!$&'()*+,;=:@/?")

    return result
