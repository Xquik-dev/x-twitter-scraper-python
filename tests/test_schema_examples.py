# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

import pytest
from pydantic import Field

from tests.mock_api_schema import JSONSchema, model_payloads, _example_from_schema
from x_twitter_scraper._models import BaseModel


@pytest.mark.parametrize("minimum", [0.5, 1.5, -1.5, 2])
def test_integer_example_respects_fractional_minimum(minimum: float) -> None:
    schema: JSONSchema = {"type": "integer", "minimum": minimum}
    value = _example_from_schema(schema, schema)
    assert isinstance(value, int)
    assert value >= minimum


@pytest.mark.parametrize(
    ("schema", "expected"),
    [
        ({"type": "string", "format": "date"}, "2026-01-01"),
        ({"type": "string", "format": "uri"}, "https://example.com"),
        ({"type": "string", "pattern": "[0-9]+"}, "1"),
        ({"type": "string", "minLength": "invalid"}, "x"),
        ({"type": "number", "minimum": "invalid"}, 1.0),
        ({"type": "number", "exclusiveMinimum": 2}, 3.0),
        ({"anyOf": [{"type": "null"}, {"const": "value"}]}, "value"),
        ({"oneOf": [None, {"type": "null"}]}, None),
        ({"type": ["null", "boolean"]}, True),
        ({"type": "array", "items": None}, []),
        ({"type": "object", "required": "invalid"}, {}),
        ({"allOf": [{"type": "boolean"}, None, {"default": {"a": 1}}]}, {"a": 1}),
    ],
)
def test_schema_example_variants(schema: JSONSchema, expected: object) -> None:
    assert _example_from_schema(schema, schema) == expected


@pytest.mark.parametrize(
    ("reference", "message"),
    [("external", "Unsupported"), ("#/scalar/nested", "Invalid"), ("#/scalar", "not an object")],
)
def test_invalid_reference_is_rejected(reference: str, message: str) -> None:
    with pytest.raises(ValueError, match=message):
        _example_from_schema({"$ref": reference}, {"scalar": 1})


def test_batch_model_payloads_preserve_shared_aliases() -> None:
    class Shared(BaseModel):
        value: str = Field(alias="valueAlias")

    class First(BaseModel):
        shared: Shared

    class Second(BaseModel):
        shared: Shared
        count: int

    assert model_payloads({First, Second}) == {
        First: b'{"shared":{"valueAlias":"x"}}',
        Second: b'{"shared":{"valueAlias":"x"},"count":1}',
    }
    assert model_payloads(set()) == {}
