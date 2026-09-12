# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Mapping, Iterable
from dataclasses import dataclass
from urllib.parse import parse_qs, urlencode
from typing_extensions import get_args

from ._types import Query as Params, NotGiven, ArrayFormat, NestedFormat, not_given
from ._utils import is_list, is_tuple, is_mapping


@dataclass(kw_only=True, eq=False, repr=False)
class Querystring:
    array_format: ArrayFormat = "repeat"
    nested_format: NestedFormat = "brackets"

    def parse(self, query: str) -> Mapping[str, object]:
        # Note: custom format syntax is not supported yet
        return parse_qs(query)

    def stringify(
        self,
        params: Params,
        *,
        array_format: ArrayFormat | NotGiven = not_given,
        nested_format: NestedFormat | NotGiven = not_given,
    ) -> str:
        return urlencode(
            self.stringify_items(
                params,
                array_format=array_format,
                nested_format=nested_format,
            )
        )

    def stringify_items(
        self,
        params: Params,
        *,
        array_format: ArrayFormat | NotGiven = not_given,
        nested_format: NestedFormat | NotGiven = not_given,
    ) -> list[tuple[str, str]]:
        opts = Querystring(
            array_format=self.array_format if isinstance(array_format, NotGiven) else array_format,
            nested_format=self.nested_format if isinstance(nested_format, NotGiven) else nested_format,
        )
        return [item for key, value in params.items() for item in self._stringify_item(key, value, opts)]

    def _stringify_item(
        self,
        key: str,
        value: object,
        opts: Querystring,
    ) -> list[tuple[str, str]]:
        entries: Iterable[tuple[str, object]]
        if is_mapping(value):
            nested_format = opts.nested_format
            entries = (
                (f"{key}.{subkey}" if nested_format == "dots" else f"{key}[{subkey}]", subvalue)
                for subkey, subvalue in value.items()
            )
        elif is_list(value) or is_tuple(value):
            array_format = opts.array_format
            if array_format == "comma":
                return [(key, ",".join(self._primitive_value_to_str(item) for item in value if item is not None))]
            if array_format not in ("repeat", "indices", "brackets"):
                raise NotImplementedError(
                    f"Unknown array_format value: {array_format}, choose from {', '.join(get_args(ArrayFormat))}"
                )
            entries = (
                (
                    f"{key}[{i}]" if array_format == "indices" else key + "[]" if array_format == "brackets" else key,
                    item,
                )
                for i, item in enumerate(value)
            )
        else:
            serialised = self._primitive_value_to_str(value)
            return [(key, serialised)] if serialised else []
        return [pair for subkey, item in entries for pair in self._stringify_item(subkey, item, opts)]

    def _primitive_value_to_str(self, value: object) -> str:
        # copied from httpx
        if value is True:
            return "true"
        elif value is False:
            return "false"
        elif value is None:
            return ""
        return str(value)


_qs = Querystring()
parse = _qs.parse
stringify = _qs.stringify
stringify_items = _qs.stringify_items
