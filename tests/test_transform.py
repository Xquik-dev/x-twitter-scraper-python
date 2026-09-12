# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import io
import os
import pathlib
from typing import Any, Dict, List, Union, Iterable, Optional, cast
from datetime import date, datetime
from typing_extensions import Required, Annotated, TypedDict

import anyio
import pytest

from x_twitter_scraper._types import Base64FileInput, omit, not_given
from x_twitter_scraper._utils import (
    PropertyInfo,
    transform as _transform,
    parse_datetime,
    async_transform as _async_transform,
)
from x_twitter_scraper._compat import PYDANTIC_V1
from x_twitter_scraper._models import BaseModel

SAMPLE_FILE_PATH = pathlib.Path(__file__).parent.joinpath("sample_file.txt")


async def transform(
    data: object,
    expected_type: object,
    use_async: bool,
) -> object:
    if use_async:
        return await _async_transform(data, expected_type=expected_type)

    return _transform(data, expected_type=expected_type)


parametrize = pytest.mark.parametrize("use_async", [False, True], ids=["sync", "async"])


class Foo1(TypedDict):
    foo_bar: Annotated[str, PropertyInfo(alias="fooBar")]


class Foo2(TypedDict):
    bar: Bar2


class Bar2(TypedDict):
    this_thing: Annotated[int, PropertyInfo(alias="this__thing")]
    baz: Annotated[Baz2, PropertyInfo(alias="Baz")]


class Baz2(TypedDict):
    my_baz: Annotated[str, PropertyInfo(alias="myBaz")]


class Foo3(TypedDict):
    things: List[Bar3]


class Bar3(TypedDict):
    my_field: Annotated[str, PropertyInfo(alias="myField")]


class Foo4(TypedDict):
    foo: Union[Foo1, Baz4]


class Baz4(TypedDict):
    foo_baz: Annotated[str, PropertyInfo(alias="fooBaz")]


class Foo5(TypedDict):
    foo: Annotated[Union[Foo1, List[Baz4]], PropertyInfo(alias="FOO")]


class Foo6(TypedDict):
    bar: Annotated[str, PropertyInfo(alias="Bar")]


class Foo7(TypedDict):
    bar: Annotated[List[Bar7], PropertyInfo(alias="bAr")]
    foo: Bar7


class Bar7(TypedDict):
    foo: str


@parametrize
@pytest.mark.parametrize(
    "schema,data,expected",
    [
        (Foo1, {"foo_bar": "hello"}, {"fooBar": "hello"}),
        (Foo2, {"bar": {"this_thing": 1}}, {"bar": {"this__thing": 1}}),
        (Foo2, {"bar": {"baz": {"my_baz": "foo"}}}, {"bar": {"Baz": {"myBaz": "foo"}}}),
        (
            Foo3,
            {"things": [{"my_field": "foo"}, {"my_field": "foo2"}]},
            {"things": [{"myField": "foo"}, {"myField": "foo2"}]},
        ),
        (Foo4, {"foo": {"foo_bar": "bar"}}, {"foo": {"fooBar": "bar"}}),
        (Foo4, {"foo": {"foo_baz": "baz"}}, {"foo": {"fooBaz": "baz"}}),
        (Foo4, {"foo": {"foo_baz": "baz", "foo_bar": "bar"}}, {"foo": {"fooBaz": "baz", "fooBar": "bar"}}),
        (Foo5, {"foo": {"foo_bar": "bar"}}, {"FOO": {"fooBar": "bar"}}),
        (Foo5, {"foo": [{"foo_baz": "baz"}, {"foo_baz": "baz"}]}, {"FOO": [{"fooBaz": "baz"}, {"fooBaz": "baz"}]}),
        (Foo6, {"bar": "bar", "baz_": {"FOO": 1}}, {"Bar": "bar", "baz_": {"FOO": 1}}),
        (Foo7, {"bar": "<foo>"}, {"bAr": "<foo>"}),
        (Foo7, {"foo": "<foo>"}, {"foo": "<foo>"}),
    ],
    ids=[
        "top-level",
        "recursive",
        "deep-recursive",
        "list",
        "union-first",
        "union-second",
        "union-both",
        "aliased-union",
        "aliased-list",
        "unknown-keys",
        "invalid-list",
        "invalid-object",
    ],
)
async def test_alias_shapes(
    use_async: bool, schema: object, data: dict[str, object], expected: dict[str, object]
) -> None:
    assert await transform(data, schema, use_async) == expected


class DatetimeDict(TypedDict, total=False):
    foo: Annotated[datetime, PropertyInfo(format="iso8601")]

    bar: Annotated[Optional[datetime], PropertyInfo(format="iso8601")]

    required: Required[Annotated[Optional[datetime], PropertyInfo(format="iso8601")]]

    list_: Required[Annotated[Optional[List[datetime]], PropertyInfo(format="iso8601")]]

    union: Annotated[Union[int, datetime], PropertyInfo(format="iso8601")]


class DateDict(TypedDict, total=False):
    foo: Annotated[date, PropertyInfo(format="iso8601")]


class DatetimeModel(BaseModel):
    foo: datetime


class DateModel(BaseModel):
    foo: Optional[date]


@parametrize
@pytest.mark.asyncio
async def test_iso8601_format(use_async: bool) -> None:
    dt = datetime.fromisoformat("2023-02-23T14:16:36.337692+00:00")
    tz = "+00:00" if PYDANTIC_V1 else "Z"
    assert await transform({"foo": dt}, DatetimeDict, use_async) == {"foo": "2023-02-23T14:16:36.337692+00:00"}
    assert await transform(DatetimeModel(foo=dt), Any, use_async) == {"foo": "2023-02-23T14:16:36.337692" + tz}

    dt = dt.replace(tzinfo=None)
    assert await transform({"foo": dt}, DatetimeDict, use_async) == {"foo": "2023-02-23T14:16:36.337692"}
    assert await transform(DatetimeModel(foo=dt), Any, use_async) == {"foo": "2023-02-23T14:16:36.337692"}

    assert await transform({"foo": None}, DateDict, use_async) == {"foo": None}
    assert await transform(DateModel(foo=None), Any, use_async) == {"foo": None}
    assert await transform({"foo": date.fromisoformat("2023-02-23")}, DateDict, use_async) == {"foo": "2023-02-23"}
    assert await transform(DateModel(foo=date.fromisoformat("2023-02-23")), DateDict, use_async) == {
        "foo": "2023-02-23"
    }


@parametrize
@pytest.mark.asyncio
@pytest.mark.parametrize("field, unchanged", [("bar", None), ("required", None), ("union", "foo")])
async def test_datetime_field_wrappers(use_async: bool, field: str, unchanged: object) -> None:
    dt = datetime.fromisoformat("2023-02-23T14:16:36.337692+00:00")
    data: dict[str, object] = {field: dt}
    assert await transform(data, DatetimeDict, use_async) == {field: "2023-02-23T14:16:36.337692+00:00"}
    assert await transform({field: unchanged}, DatetimeDict, use_async) == {field: unchanged}


@parametrize
@pytest.mark.asyncio
async def test_nested_list_iso6801_format(use_async: bool) -> None:
    dt1 = datetime.fromisoformat("2023-02-23T14:16:36.337692+00:00")
    dt2 = parse_datetime("2022-01-15T06:34:23Z")
    assert await transform({"list_": [dt1, dt2]}, DatetimeDict, use_async) == {
        "list_": ["2023-02-23T14:16:36.337692+00:00", "2022-01-15T06:34:23+00:00"]
    }


@parametrize
@pytest.mark.asyncio
async def test_datetime_custom_format(use_async: bool) -> None:
    dt = parse_datetime("2022-01-15T06:34:23Z")

    result = await transform(dt, Annotated[datetime, PropertyInfo(format="custom", format_template="%H")], use_async)
    assert result == "06"


class DateDictWithRequiredAlias(TypedDict, total=False):
    required_prop: Required[Annotated[date, PropertyInfo(format="iso8601", alias="prop")]]


@parametrize
@pytest.mark.asyncio
async def test_datetime_with_alias(use_async: bool) -> None:
    assert await transform({"required_prop": None}, DateDictWithRequiredAlias, use_async) == {"prop": None}
    assert await transform(
        {"required_prop": date.fromisoformat("2023-02-23")}, DateDictWithRequiredAlias, use_async
    ) == {"prop": "2023-02-23"}


class MyModel(BaseModel):
    foo: str


@parametrize
@pytest.mark.parametrize(
    "validated,values",
    [(True, {"foo": "hi!"}), (False, {"foo": "hi!"}), (False, {}), (False, {"my_untyped_field": True})],
    ids=["validated", "constructed", "empty", "unknown-field"],
)
async def test_pydantic_dictionary(use_async: bool, validated: bool, values: dict[str, object]) -> None:
    model = MyModel(foo="hi!") if validated else MyModel.construct(_fields_set=None, **values)
    assert await transform(model, Any, use_async) == values


@parametrize
@pytest.mark.asyncio
@pytest.mark.parametrize("nested", [False, True], ids=["scalar", "object"])
async def test_pydantic_mismatched_types(use_async: bool, nested: bool) -> None:
    model = MyModel.construct(foo=MyModel.construct(hello="world") if nested else True)
    if PYDANTIC_V1:
        params = await transform(model, Any, use_async)
    else:
        with pytest.warns(UserWarning):
            params = await transform(model, Any, use_async)
    assert cast(Any, params) == {"foo": {"hello": "world"} if nested else True}


class ModelNestedObjects(BaseModel):
    nested: MyModel


@parametrize
@pytest.mark.asyncio
async def test_pydantic_nested_objects(use_async: bool) -> None:
    model = ModelNestedObjects.construct(nested={"foo": "stainless"})
    assert isinstance(model.nested, MyModel)
    assert await transform(model, Any, use_async) == {"nested": {"foo": "stainless"}}


class ModelWithDefaultField(BaseModel):
    foo: str
    with_none_default: Union[str, None] = None
    with_str_default: str = "foo"


@parametrize
@pytest.mark.asyncio
@pytest.mark.parametrize(
    "values, expected_none, expected_str",
    [
        ({}, None, "foo"),
        ({"with_none_default": None, "with_str_default": "foo"}, None, "foo"),
        ({"with_none_default": "bar", "with_str_default": "baz"}, "bar", "baz"),
    ],
    ids=["unset", "explicit-defaults", "overrides"],
)
async def test_pydantic_default_field(
    use_async: bool, values: dict[str, object], expected_none: str | None, expected_str: str
) -> None:
    model = ModelWithDefaultField.construct(_fields_set=None, **values)
    assert model.with_none_default is None if expected_none is None else model.with_none_default == expected_none
    assert model.with_str_default == expected_str
    assert await transform(model, Any, use_async) == values


class TypedDictIterableUnion(TypedDict):
    foo: Annotated[Union[Foo1, Iterable[Baz4]], PropertyInfo(alias="FOO")]


@parametrize
@pytest.mark.asyncio
async def test_iterable_of_dictionaries(use_async: bool) -> None:
    assert await transform({"foo": [{"foo_baz": "bar"}]}, TypedDictIterableUnion, use_async) == {
        "FOO": [{"fooBaz": "bar"}]
    }
    assert await transform({"foo": ({"foo_baz": "bar"},)}, TypedDictIterableUnion, use_async) == {
        "FOO": [{"fooBaz": "bar"}]
    }

    def my_iter() -> Iterable[Baz4]:
        yield {"foo_baz": "hello"}
        yield {"foo_baz": "world"}

    assert await transform({"foo": my_iter()}, TypedDictIterableUnion, use_async) == {
        "FOO": [{"fooBaz": "hello"}, {"fooBaz": "world"}]
    }


@parametrize
@pytest.mark.asyncio
async def test_dictionary_items(use_async: bool) -> None:
    assert await transform({"foo": {"foo_baz": "bar"}}, Dict[str, Baz4], use_async) == {"foo": {"fooBaz": "bar"}}


class TypedDictIterableUnionStr(TypedDict):
    foo: Annotated[Union[str, Iterable[Baz4]], PropertyInfo(alias="FOO")]


@parametrize
@pytest.mark.asyncio
async def test_iterable_union_str(use_async: bool) -> None:
    assert await transform({"foo": "bar"}, TypedDictIterableUnionStr, use_async) == {"FOO": "bar"}
    assert await transform(iter([{"foo_baz": "bar"}]), Union[str, Iterable[Baz4]], use_async) == [{"fooBaz": "bar"}]


class TypedDictBase64Input(TypedDict):
    foo: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]


@parametrize
@pytest.mark.asyncio
@pytest.mark.parametrize("path", [SAMPLE_FILE_PATH, anyio.Path(SAMPLE_FILE_PATH)], ids=["pathlib", "anyio"])
async def test_base64_file_input(use_async: bool, path: os.PathLike[str]) -> None:
    # strings are left as-is
    assert await transform({"foo": "bar"}, TypedDictBase64Input, use_async) == {"foo": "bar"}

    # Paths are automatically converted to base64.
    assert await transform({"foo": path}, TypedDictBase64Input, use_async) == {"foo": "SGVsbG8sIHdvcmxkIQo="}

    # io instances are automatically converted to base64
    assert await transform({"foo": io.StringIO("Hello, world!")}, TypedDictBase64Input, use_async) == {
        "foo": "SGVsbG8sIHdvcmxkIQ=="
    }
    assert await transform({"foo": io.BytesIO(b"Hello, world!")}, TypedDictBase64Input, use_async) == {
        "foo": "SGVsbG8sIHdvcmxkIQ=="
    }


@parametrize
@pytest.mark.asyncio
async def test_transform_skipping(use_async: bool) -> None:
    # lists of ints are left as-is
    data = [1, 2, 3]
    assert await transform(data, List[int], use_async) is data

    # iterables of ints are converted to a list
    iterator = iter([1, 2, 3])
    assert await transform(iterator, Iterable[int], use_async) == [1, 2, 3]


@parametrize
@pytest.mark.asyncio
@pytest.mark.parametrize("sentinel", [not_given, omit], ids=["not-given", "omit"])
async def test_strips_sentinels(use_async: bool, sentinel: object) -> None:
    assert await transform({"foo_bar": "bar"}, Foo1, use_async) == {"fooBar": "bar"}
    assert await transform({"foo_bar": sentinel}, Foo1, use_async) == {}


@parametrize
@pytest.mark.parametrize("raw_path", [os.fsencode(SAMPLE_FILE_PATH), 42], ids=["bytes", "invalid"])
async def test_base64_path_protocol_values(use_async: bool, raw_path: object) -> None:
    class PathInput:
        def __fspath__(self) -> object:
            return raw_path

    if isinstance(raw_path, bytes):
        assert await transform({"foo": PathInput()}, TypedDictBase64Input, use_async) == {"foo": "SGVsbG8sIHdvcmxkIQo="}
    else:
        with pytest.raises(TypeError, match="File paths must resolve to strings or bytes"):
            await transform({"foo": PathInput()}, TypedDictBase64Input, use_async)
