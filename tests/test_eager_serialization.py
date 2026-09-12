# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Union
from typing_extensions import TypedDict

import pytest
from pydantic import Field

from x_twitter_scraper._types import IncEx
from x_twitter_scraper._compat import parse_obj
from x_twitter_scraper._models import BaseModel, EagerIterable


class Payload(TypedDict):
    items: EagerIterable[int]


class NumericPayload(TypedDict):
    items: tuple[int, ...]


class TextPayload(TypedDict):
    items: EagerIterable[str]
    nullable: str | None


class OtherPayload(TypedDict):
    other: EagerIterable[int]


class Child(BaseModel):
    items: EagerIterable[int] = Field(alias="ITEMS")


class Envelope(BaseModel):
    child: Child
    mapping: dict[str, Payload]
    sequence: list[Child]
    pair: tuple[str, EagerIterable[int]]
    ordinary: tuple[int, ...]
    scalar: Union[EagerIterable[int], int, str]


@pytest.mark.parametrize(
    "include, exclude, expected",
    [
        (
            None,
            None,
            {
                "child": {"ITEMS": [1, 2]},
                "mapping": {"key": {"items": [3, 4]}},
                "sequence": [{"ITEMS": [5, 6]}],
                "pair": ("name", [7, 8]),
                "ordinary": (9, 10),
                "scalar": "ordinary",
            },
        ),
        ({"pair": {1}}, None, {"pair": ([7, 8],)}),
        ({"sequence"}, {"sequence": {"__all__": {"items": {-1}}}}, {"sequence": [{"ITEMS": [5]}]}),
    ],
)
def test_nested_eager_serialization(include: IncEx | None, exclude: IncEx | None, expected: dict[str, object]) -> None:
    model = parse_obj(
        Envelope,
        {
            "child": {"ITEMS": (1, 2)},
            "mapping": {"key": {"items": (3, 4)}},
            "sequence": [{"ITEMS": (5, 6)}],
            "pair": ("name", (7, 8)),
            "ordinary": (9, 10),
            "scalar": "ordinary",
        },
    )
    assert model.model_dump(by_alias=True, include=include, exclude=exclude) == expected
    assert model.model_dump(by_alias=True, include=include, exclude=exclude) == expected
    assert model.child.items == (1, 2)
    assert model.pair == ("name", (7, 8))
    assert model.mapping["key"]["items"] == (3, 4)
    assert model.sequence[0].items == (5, 6)


def test_union_serialization_matches_item_types() -> None:
    class Model(BaseModel):
        items: Union[tuple[int, ...], EagerIterable[str]]
        mapping: Union[dict[str, tuple[int, ...]], dict[str, EagerIterable[str]]]
        keyed: Union[dict[int, tuple[int, ...]], dict[str, EagerIterable[int]]]
        record: Union[NumericPayload, TextPayload]
        missing: Union[OtherPayload, Payload]

    model = parse_obj(
        Model,
        {
            "items": ("a", "b"),
            "mapping": {"key": ("a", "b")},
            "keyed": {"key": (1, 2)},
            "record": {"items": ("a", "b"), "nullable": None},
            "missing": {"items": (1, 2)},
        },
    )
    expected = {
        "items": ["a", "b"],
        "mapping": {"key": ["a", "b"]},
        "keyed": {"key": [1, 2]},
        "record": {"items": ["a", "b"], "nullable": None},
        "missing": {"items": [1, 2]},
    }
    assert model.model_dump() == expected
    assert model.model_dump() == expected
    assert model.items == ("a", "b")
    assert model.mapping == {"key": ("a", "b")}
    assert model.keyed == {"key": (1, 2)}
    assert model.record == {"items": ("a", "b"), "nullable": None}
    assert model.missing == {"items": (1, 2)}
