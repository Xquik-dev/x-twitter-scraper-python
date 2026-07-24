# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import json
from typing import Mapping, cast

from x_twitter_scraper._compat import PYDANTIC_V1
from x_twitter_scraper._models import BaseModel

JSONSchema = Mapping[str, object]


def _resolve_reference(reference: str, root: JSONSchema) -> JSONSchema:
    if not reference.startswith("#/"):
        raise ValueError(f"Unsupported schema reference: {reference}")
    value: object = root
    for token in reference[2:].split("/"):
        token = token.replace("~1", "/").replace("~0", "~")
        if not isinstance(value, Mapping):
            raise ValueError(f"Invalid schema reference: {reference}")
        value = cast(JSONSchema, value)[token]  # pyright: ignore[reportUnnecessaryCast]
    if not isinstance(value, Mapping):
        raise ValueError(f"Schema reference is not an object: {reference}")
    return cast(JSONSchema, value)


def _string_example(schema: JSONSchema) -> str:
    schema_format = schema.get("format")
    if schema_format == "date-time":
        return "2026-01-01T00:00:00Z"
    if schema_format == "date":
        return "2026-01-01"
    if schema_format in {"uri", "url"}:
        return "https://example.com"
    pattern = schema.get("pattern")
    if isinstance(pattern, str) and ("\\d" in pattern or "[0-9]" in pattern):
        return "1"
    minimum_length = schema.get("minLength", 1)
    if not isinstance(minimum_length, int):
        minimum_length = 1
    return "x" * max(1, minimum_length)


def _number_example(schema: JSONSchema, *, integer: bool) -> int | float:
    minimum = schema.get("minimum", 1)
    if not isinstance(minimum, (int, float)):
        minimum = 1
    exclusive = schema.get("exclusiveMinimum")
    if isinstance(exclusive, (int, float)):
        minimum = max(minimum, exclusive + 1)
    return int(minimum) if integer else float(minimum)


def _example_from_schema(
    schema: JSONSchema,
    root: JSONSchema,
    active_references: frozenset[str] = frozenset(),
) -> object:
    reference = schema.get("$ref")
    if isinstance(reference, str):
        if reference in active_references:
            return {}
        return _example_from_schema(
            _resolve_reference(reference, root),
            root,
            active_references | {reference},
        )

    if "const" in schema:
        return schema["const"]
    enum = schema.get("enum")
    if isinstance(enum, list) and enum:
        return cast(list[object], enum)[0]
    if "default" in schema:
        return schema["default"]

    for union_key in ("anyOf", "oneOf"):
        variants = schema.get(union_key)
        if isinstance(variants, list):
            candidates: list[JSONSchema] = []
            for variant in cast(list[object], variants):
                if not isinstance(variant, Mapping):
                    continue
                candidate = cast(JSONSchema, variant)
                if candidate.get("type") != "null":
                    candidates.append(candidate)
            if candidates:
                return _example_from_schema(candidates[0], root, active_references)
            return None

    combined = schema.get("allOf")
    if isinstance(combined, list):
        merged: dict[str, object] = {}
        for part in cast(list[object], combined):
            if not isinstance(part, Mapping):
                continue
            example = _example_from_schema(cast(JSONSchema, part), root, active_references)
            if isinstance(example, Mapping):
                merged.update(cast(Mapping[str, object], example))
        return merged

    schema_type = schema.get("type")
    if isinstance(schema_type, list):
        schema_type = next(
            (value for value in cast(list[object], schema_type) if isinstance(value, str) and value != "null"),
            "null",
        )
    if schema_type == "null":
        return None
    if schema_type == "boolean":
        return True
    if schema_type == "integer":
        return _number_example(schema, integer=True)
    if schema_type == "number":
        return _number_example(schema, integer=False)
    if schema_type == "string":
        return _string_example(schema)
    if schema_type == "array":
        item_schema = schema.get("items")
        minimum_items = schema.get("minItems", 0)
        if not isinstance(item_schema, Mapping) or not isinstance(minimum_items, int):
            return []
        return [
            _example_from_schema(cast(JSONSchema, item_schema), root, active_references) for _ in range(minimum_items)
        ]
    if schema_type == "object" or "properties" in schema:
        properties_value = schema.get("properties", {})
        required_value = schema.get("required", [])
        if not isinstance(properties_value, Mapping) or not isinstance(required_value, list):
            return {}
        properties = cast(Mapping[str, object], properties_value)
        required = cast(list[object], required_value)
        return {
            name: _example_from_schema(cast(JSONSchema, properties[name]), root, active_references)
            for name in required
            if isinstance(name, str) and isinstance(properties.get(name), Mapping)
        }
    return {}


def model_payload(model: type[BaseModel]) -> bytes:
    if PYDANTIC_V1:
        schema = cast(JSONSchema, model.schema(by_alias=True))  # pyright: ignore[reportDeprecated]
    else:
        schema = cast(JSONSchema, model.model_json_schema(by_alias=True))

    value = _example_from_schema(schema, schema)
    if PYDANTIC_V1:
        model.parse_obj(value)  # pyright: ignore[reportDeprecated]
    else:
        model.model_validate(value)
    return json.dumps(value, separators=(",", ":")).encode()
