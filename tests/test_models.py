# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

import json
from typing import TYPE_CHECKING, Any, Dict, List, Union, Iterable, Optional, cast
from datetime import datetime, timezone
from collections import deque
from typing_extensions import Literal, Protocol, Annotated, TypedDict, TypeAliasType

import pytest
import pydantic
from pydantic import Field

from x_twitter_scraper._utils import PropertyInfo
from x_twitter_scraper._compat import PYDANTIC_V1, parse_obj, model_dump, model_json
from x_twitter_scraper._models import DISCRIMINATOR_CACHE, BaseModel, EagerIterable, construct_type
from x_twitter_scraper._base_client import BasePage


class BasicModel(BaseModel):
    foo: str


class NamedModel(BaseModel):
    name: str


class BooleanBarModel(BaseModel):
    bar: bool


class ThingModel(BaseModel):
    thing: str


class LevelModel(BaseModel):
    level: int


class DatetimeModel(BaseModel):
    created_at: datetime


class AliasedOptionalModel(BaseModel):
    foo: Optional[str] = Field(alias="FOO", default=None)


class StringVariant(BaseModel):
    type: Literal["a"]
    data: str


class IntegerVariant(BaseModel):
    type: Literal["b"]
    data: int


class BooleanVariant(BaseModel):
    type: Literal["c"]
    data: bool


@pytest.mark.parametrize("value", ["hello", 1], ids=["correct type", "mismatched"])
def test_basic(value: object) -> None:
    m = BasicModel.construct(foo=value)
    assert m.foo == value


def test_directly_nested_model() -> None:
    class NestedModel(BaseModel):
        nested: BasicModel

    m = NestedModel.construct(nested={"foo": "Foo!"})
    assert m.nested.foo == "Foo!"


def test_optional_nested_model() -> None:
    class NestedModel(BaseModel):
        nested: Optional[BasicModel]

    m1 = NestedModel.construct(nested=None)
    assert m1.nested is None

    m2 = NestedModel.construct(nested={"foo": "bar"})
    assert m2.nested is not None
    assert m2.nested.foo == "bar"


class ListNestedModel(BaseModel):
    nested: List[BasicModel]


class OptionalListNestedModel(BaseModel):
    nested: Optional[List[BasicModel]]


@pytest.mark.parametrize("model_type", [ListNestedModel, OptionalListNestedModel])
def test_list_nested_model(model_type: type[ListNestedModel] | type[OptionalListNestedModel]) -> None:
    model = model_type.construct(nested=[{"foo": "bar"}, {"foo": "2"}])
    assert model.nested is not None
    assert isinstance(model.nested, list)
    assert len(model.nested) == 2
    assert model.nested[0].foo == "bar"
    assert model.nested[1].foo == "2"


@pytest.mark.parametrize("model_type", [ListNestedModel, OptionalListNestedModel])
@pytest.mark.parametrize("value", [None, True, {1}, [False]])
def test_list_nested_model_preserves_mismatched_values(
    model_type: type[ListNestedModel] | type[OptionalListNestedModel], value: object
) -> None:
    actual = model_type.construct(nested=value).nested
    assert actual == value
    assert type(actual) is type(value)


def test_list_optional_items_nested_model() -> None:
    class NestedModel(BaseModel):
        nested: List[Optional[BasicModel]]

    m = NestedModel.construct(nested=[None, {"foo": "bar"}])
    assert m.nested is not None
    assert isinstance(m.nested, list)
    assert len(m.nested) == 2
    assert m.nested[0] is None
    assert m.nested[1] is not None
    assert m.nested[1].foo == "bar"


@pytest.mark.parametrize(
    "annotation,value",
    [
        (BasicModel, "hello!"),
        (Optional[BasicModel], {"foo"}),
        (List[Optional[BasicModel]], "foo"),
        (List[Optional[BasicModel]], [False]),
        (List[str], False),
        (Dict[str, str], False),
    ],
)
def test_nested_construction_preserves_mismatched_values(annotation: object, value: object) -> None:
    model_type = pydantic.create_model("NestedModel", __base__=BaseModel, nested=(annotation, ...))
    actual: object = model_type.construct(nested=value).__dict__["nested"]
    assert actual == value
    assert type(actual) is type(value)


def test_raw_dictionary() -> None:
    class NestedModel(BaseModel):
        nested: Dict[str, str]

    m = NestedModel.construct(nested={"hello": "world"})
    assert m.nested == {"hello": "world"}


def test_nested_dictionary_model() -> None:
    class NestedModel(BaseModel):
        nested: Dict[str, BasicModel]

    m = NestedModel.construct(nested={"hello": {"foo": "bar"}})
    assert isinstance(m.nested, dict)
    assert m.nested["hello"].foo == "bar"

    # mismatched types
    m = NestedModel.construct(nested={"hello": False})
    assert cast(Any, m.nested["hello"]) is False


@pytest.mark.parametrize("unknown, expected", [(1, 1), ({"foo_bar": True}, {"foo_bar": True})])
def test_unknown_fields(unknown: object, expected: object) -> None:
    model = BasicModel.construct(foo="foo", unknown=unknown)
    assert model.foo == "foo"
    assert cast(Any, model).unknown == expected
    assert model_dump(model) == {"foo": "foo", "unknown": expected}


def test_strict_validation_unknown_fields() -> None:
    model = parse_obj(BasicModel, dict(foo="hello!", user="Robert"))
    assert model.foo == "hello!"
    assert cast(Any, model).user == "Robert"

    assert model_dump(model) == {"foo": "hello!", "user": "Robert"}


@pytest.mark.parametrize("value, expected", [(1, 1), ({"hello": False}, {"hello": False})])
def test_aliases(value: object, expected: object) -> None:
    class Model(BaseModel):
        my_field: int = Field(alias="myField")

    model = Model.construct(myField=value)
    assert cast(Any, model.my_field) == expected


def test_repr() -> None:
    model = BasicModel(foo="bar")
    assert str(model) == "BasicModel(foo='bar')"
    assert repr(model) == "BasicModel(foo='bar')"


def test_repr_nested_model() -> None:
    class Child(BaseModel):
        name: str
        age: int

    class Parent(BaseModel):
        name: str
        child: Child

    model = Parent(name="Robert", child=Child(name="Foo", age=5))
    assert str(model) == "Parent(name='Robert', child=Child(name='Foo', age=5))"
    assert repr(model) == "Parent(name='Robert', child=Child(name='Foo', age=5))"


def test_optional_list() -> None:
    class Model(BaseModel):
        items: Optional[List[NamedModel]]

    m = Model.construct(items=None)
    assert m.items is None

    m = Model.construct(items=[])
    assert m.items == []

    m = Model.construct(items=[{"name": "Robert"}])
    assert m.items is not None
    assert len(m.items) == 1
    assert m.items[0].name == "Robert"


def test_nested_union_of_models() -> None:
    class Model(BaseModel):
        foo: Union[BooleanBarModel, ThingModel]

    m = Model.construct(foo={"thing": "hello"})
    assert isinstance(m.foo, ThingModel)
    assert m.foo.thing == "hello"


def test_nested_union_of_mixed_types() -> None:
    class Model(BaseModel):
        foo: Union[BooleanBarModel, Literal[True], Literal["CARD_HOLDER"]]

    m = Model.construct(foo=True)
    assert m.foo is True

    m = Model.construct(foo="CARD_HOLDER")
    assert m.foo == "CARD_HOLDER"

    m = Model.construct(foo={"bar": False})
    assert isinstance(m.foo, BooleanBarModel)
    assert m.foo.bar is False


def test_nested_union_multiple_variants() -> None:
    class Submodel3(BaseModel):
        foo: int

    class Model(BaseModel):
        foo: Union[BooleanBarModel, ThingModel, None, Submodel3]

    m = Model.construct(foo={"thing": "hello"})
    assert isinstance(m.foo, ThingModel)
    assert m.foo.thing == "hello"

    m = Model.construct(foo=None)
    assert m.foo is None

    m = Model.construct()
    assert m.foo is None

    m = Model.construct(foo={"foo": "1"})
    assert isinstance(m.foo, Submodel3)
    assert m.foo.foo == 1


def test_nested_union_invalid_data() -> None:
    class ExtraName(Protocol):
        name: object

    class Model(BaseModel):
        foo: Union[LevelModel, NamedModel]

    m = Model.construct(foo=True)
    assert cast(object, m.foo) is True

    m = Model.construct(foo={"name": 3})
    if PYDANTIC_V1:
        assert isinstance(m.foo, NamedModel)
        assert m.foo.name == "3"
    else:
        assert isinstance(m.foo, LevelModel)
        assert cast(ExtraName, m.foo).name == 3


def test_list_of_unions() -> None:
    class Model(BaseModel):
        items: List[Union[LevelModel, NamedModel]]

    m = Model.construct(items=[{"level": 1}, {"name": "Robert"}])
    assert len(m.items) == 2
    assert isinstance(m.items[0], LevelModel)
    assert m.items[0].level == 1
    assert isinstance(m.items[1], NamedModel)
    assert m.items[1].name == "Robert"

    m = Model.construct(items=[{"level": -1}, 156])
    assert len(m.items) == 2
    assert isinstance(m.items[0], LevelModel)
    assert m.items[0].level == -1
    assert cast(Any, m.items[1]) == 156


def test_union_of_lists() -> None:
    class Model(BaseModel):
        items: Union[List[LevelModel], List[NamedModel]]

    # with one valid entry
    m = Model.construct(items=[{"name": "Robert"}])
    assert len(m.items) == 1
    assert isinstance(m.items[0], NamedModel)
    assert m.items[0].name == "Robert"

    # with two entries pointing to different types
    m = Model.construct(items=[{"level": 1}, {"name": "Robert"}])
    assert len(m.items) == 2
    assert isinstance(m.items[0], LevelModel)
    assert m.items[0].level == 1
    assert isinstance(m.items[1], LevelModel)
    assert cast(Any, m.items[1]).name == "Robert"

    # with two entries pointing to *completely* different types
    m = Model.construct(items=[{"level": -1}, 156])
    assert len(m.items) == 2
    assert isinstance(m.items[0], LevelModel)
    assert m.items[0].level == -1
    assert cast(Any, m.items[1]) == 156


def test_dict_of_union() -> None:
    class Model(BaseModel):
        data: Dict[str, Union[NamedModel, BasicModel]]

    m = Model.construct(data={"hello": {"name": "there"}, "foo": {"foo": "bar"}})
    assert len(list(m.data.keys())) == 2
    assert isinstance(m.data["hello"], NamedModel)
    assert m.data["hello"].name == "there"
    assert isinstance(m.data["foo"], BasicModel)
    assert m.data["foo"].foo == "bar"

    # TODO: test mismatched type


def test_double_nested_union() -> None:
    class SubModel2(BaseModel):
        bar: str

    class Model(BaseModel):
        data: Dict[str, List[Union[NamedModel, SubModel2]]]

    m = Model.construct(data={"foo": [{"bar": "baz"}, {"name": "Robert"}]})
    assert len(m.data["foo"]) == 2

    entry1 = m.data["foo"][0]
    assert isinstance(entry1, SubModel2)
    assert entry1.bar == "baz"

    entry2 = m.data["foo"][1]
    assert isinstance(entry2, NamedModel)
    assert entry2.name == "Robert"

    # TODO: test mismatched type


def test_union_of_dict() -> None:
    class Model(BaseModel):
        data: Union[Dict[str, NamedModel], Dict[str, BasicModel]]

    m = Model.construct(data={"hello": {"name": "there"}, "foo": {"foo": "bar"}})
    assert len(list(m.data.keys())) == 2
    assert isinstance(m.data["hello"], NamedModel)
    assert m.data["hello"].name == "there"
    assert isinstance(m.data["foo"], NamedModel)
    assert cast(Any, m.data["foo"]).foo == "bar"


@pytest.mark.parametrize("validated", [False, True], ids=["construct", "validate"])
def test_iso8601_datetime(validated: bool) -> None:
    expected = datetime(2019, 12, 27, 18, 11, 19, 117000, tzinfo=timezone.utc)

    if PYDANTIC_V1:
        expected_json = '{"created_at": "2019-12-27T18:11:19.117000+00:00"}'
    else:
        expected_json = '{"created_at":"2019-12-27T18:11:19.117000Z"}'

    values = {"created_at": "2019-12-27T18:11:19.117Z"}
    model = parse_obj(DatetimeModel, values) if validated else DatetimeModel.construct(_fields_set=None, **values)
    assert model.created_at == expected
    assert model_json(model) == expected_json


def test_does_not_coerce_int() -> None:
    class Model(BaseModel):
        bar: int

    assert Model.construct(bar=1).bar == 1
    assert Model.construct(bar=10.9).bar == 10.9
    assert Model.construct(bar="19").bar == "19"  # type: ignore[comparison-overlap]
    assert Model.construct(bar=False).bar is False


@pytest.mark.parametrize("value,expected,kind", [(10, 10.0, float), (10.12, 10.12, float), (2**53 + 1, 2**53 + 1, int)])
def test_int_to_float_safe_conversion(value: int | float, expected: int | float, kind: type) -> None:
    class Model(BaseModel):
        float_field: float

    m = Model.construct(float_field=value)
    assert m.float_field == expected
    assert isinstance(m.float_field, kind)


@pytest.mark.parametrize("validated", [False, True], ids=["construct", "validate"])
def test_deprecated_alias(validated: bool) -> None:
    class Model(BaseModel):
        resource_id: str = Field(alias="model_id")

        @property
        def model_id(self) -> str:
            return self.resource_id

    m = parse_obj(Model, {"model_id": "id"}) if validated else Model.construct(model_id="id")
    assert m.model_id == "id"
    assert m.resource_id == "id"
    assert m.resource_id is m.model_id


@pytest.mark.parametrize(
    "values,expected", [({}, None), ({"resource_id": None}, None), ({"resource_id": "foo"}, "foo")]
)
def test_omitted_fields(values: dict[str, str | None], expected: str | None) -> None:
    class Model(BaseModel):
        resource_id: Optional[str] = None

    m = Model.construct(_fields_set=None, **values)
    assert m.resource_id is expected if expected is None else m.resource_id == expected
    assert m.model_fields_set == set(values)


@pytest.mark.parametrize("as_json", [False, True], ids=["dict", "json"])
@pytest.mark.parametrize("api_defaults", [False, True], ids=["model_dump", "to"])
def test_model_serialization(as_json: bool, api_defaults: bool) -> None:
    if api_defaults:
        dump = BaseModel.to_json if as_json else BaseModel.to_dict
    else:
        dump = BaseModel.model_dump_json if as_json else BaseModel.model_dump

    def decode(value: object) -> object:
        decoded: object = json.loads(value) if isinstance(value, str) else value
        assert isinstance(value, str if as_json else dict)
        return decoded

    key = "FOO" if api_defaults else "foo"
    m = AliasedOptionalModel(FOO="hello")
    assert decode(dump(m)) == {key: "hello"}
    if api_defaults:
        assert decode(m.to_json(use_api_names=False) if as_json else m.to_dict(use_api_names=False)) == {"foo": "hello"}
    else:
        native_dump = BaseModel.model_dump_json if as_json else BaseModel.model_dump
        assert decode(native_dump(m, include={"bar"})) == {}
        assert decode(native_dump(m, exclude={"foo"})) == {}
        assert decode(native_dump(m, include={"foo"})) == {"foo": "hello"}
        assert decode(native_dump(m, by_alias=True)) == {"FOO": "hello"}
        if PYDANTIC_V1:
            with pytest.raises(ValueError, match="round_trip is only supported in Pydantic v2"):
                native_dump(m, round_trip=True)
            with pytest.raises(ValueError, match="polymorphic_serialization is only supported in Pydantic v2"):
                native_dump(m, polymorphic_serialization=True)

    m2 = AliasedOptionalModel()
    assert decode(dump(m2)) == ({} if api_defaults else {"foo": None})
    assert decode(dump(m2, exclude_unset=True)) == {}
    assert decode(dump(m2, exclude_unset=False)) == {key: None}
    assert decode(dump(m2, exclude_none=True)) == {}
    assert decode(dump(m2, exclude_defaults=True)) == {}
    assert decode(dump(m2, exclude_unset=False, exclude_none=True)) == {}
    assert decode(dump(m2, exclude_unset=False, exclude_defaults=True)) == {}

    m3 = AliasedOptionalModel(FOO=None)
    assert decode(dump(m3)) == {key: None}
    assert decode(dump(m3, exclude_none=True)) == {}
    assert decode(dump(m3, exclude_defaults=True)) == {}
    if PYDANTIC_V1:
        with pytest.raises(ValueError, match="warnings is only supported in Pydantic v2"):
            dump(m, warnings=False)


def test_serialization_formatting() -> None:
    m = AliasedOptionalModel(FOO="hello")
    assert m.to_json(indent=None) == ('{"FOO": "hello"}' if PYDANTIC_V1 else '{"FOO":"hello"}')
    assert m.model_dump_json(indent=2) == '{\n  "foo": "hello"\n}'
    time_str = "2024-03-21T11:39:01.275859"
    moment = DatetimeModel.construct(created_at=time_str)
    assert moment.to_dict(mode="python") == {"created_at": datetime.fromisoformat(time_str)}
    assert moment.to_dict(mode="json") == {"created_at": time_str}


def test_compat_method_no_error_for_warnings() -> None:
    m = BasicModel(foo="hello")
    assert isinstance(model_dump(m, warnings=False), dict)


def test_type_compat() -> None:
    # our model type can be assigned to Pydantic's model type

    def takes_pydantic(model: pydantic.BaseModel) -> None:  # noqa: ARG001
        ...

    class OurModel(BaseModel):
        foo: Optional[str] = None

    takes_pydantic(OurModel())


def test_annotated_types() -> None:
    class Model(BaseModel):
        value: str

    m = construct_type(
        value={"value": "foo"},
        type_=cast(Any, Annotated[Model, "random metadata"]),
    )
    assert isinstance(m, Model)
    assert m.value == "foo"


@pytest.mark.parametrize(
    "value, is_b, expected_data",
    [
        ({"type": "b", "data": "foo"}, True, "foo"),
        # Pydantic v1 coerces the string field; v2 preserves the invalid input.
        ({"type": "a", "data": 100}, False, "100" if PYDANTIC_V1 else 100),
        ({"type": "c", "data": None, "new_thing": "bar"}, False, None),
    ],
    ids=["invalid integer", "invalid string", "unknown variant"],
)
def test_discriminated_unions_invalid_data(value: dict[str, object], is_b: bool, expected_data: object) -> None:
    m = construct_type(
        value=value,
        type_=cast(Any, Annotated[Union[StringVariant, IntegerVariant], PropertyInfo(discriminator="type")]),
    )
    assert isinstance(m, IntegerVariant if is_b else StringVariant)
    assert m.type == value["type"]
    assert m.data == expected_data
    if "new_thing" in value:
        assert cast(Any, m).new_thing == "bar"


@pytest.mark.parametrize("variant", ["b", "c"])
def test_discriminated_unions_invalid_data_nested_unions(variant: str) -> None:
    m = construct_type(
        value={"type": variant, "data": "foo"},
        type_=cast(
            Any,
            Annotated[Union[Union[StringVariant, IntegerVariant], BooleanVariant], PropertyInfo(discriminator="type")],
        ),
    )
    assert isinstance(m, IntegerVariant if variant == "b" else BooleanVariant)
    assert m.type == variant
    assert m.data == "foo"  # type: ignore[comparison-overlap]


@pytest.mark.parametrize(
    "variant,value,expected",
    [("b", "foo", "foo"), ("a", 100, "100" if PYDANTIC_V1 else 100)],
)
def test_discriminated_unions_with_aliases_invalid_data(variant: str, value: object, expected: object) -> None:
    class A(BaseModel):
        foo_type: Literal["a"] = Field(alias="type")

        data: str

    class B(BaseModel):
        foo_type: Literal["b"] = Field(alias="type")

        data: int

    m = construct_type(
        value={"type": variant, "data": value},
        type_=cast(Any, Annotated[Union[A, B], PropertyInfo(discriminator="foo_type")]),
    )
    assert isinstance(m, B if variant == "b" else A)
    assert m.foo_type == variant
    assert m.data == expected


def test_discriminated_unions_overlapping_discriminators_invalid_data() -> None:
    class A(BaseModel):
        type: Literal["a"]

        data: bool

    class B(BaseModel):
        type: Literal["a"]

        data: int

    m = construct_type(
        value={"type": "a", "data": "foo"},
        type_=cast(Any, Annotated[Union[A, B], PropertyInfo(discriminator="type")]),
    )
    assert isinstance(m, B)
    assert m.type == "a"
    assert m.data == "foo"  # type: ignore[comparison-overlap]


def test_discriminated_unions_invalid_data_uses_cache() -> None:
    class A(StringVariant):
        pass

    class B(IntegerVariant):
        pass

    UnionType = cast(Any, Union[A, B])

    assert not DISCRIMINATOR_CACHE.get(UnionType)

    m = construct_type(
        value={"type": "b", "data": "foo"}, type_=cast(Any, Annotated[UnionType, PropertyInfo(discriminator="type")])
    )
    assert isinstance(m, B)
    assert m.type == "b"
    assert m.data == "foo"  # type: ignore[comparison-overlap]

    discriminator = DISCRIMINATOR_CACHE.get(UnionType)
    assert discriminator is not None

    m = construct_type(
        value={"type": "b", "data": "foo"}, type_=cast(Any, Annotated[UnionType, PropertyInfo(discriminator="type")])
    )
    assert isinstance(m, B)
    assert m.type == "b"
    assert m.data == "foo"  # type: ignore[comparison-overlap]

    # if the discriminator details object stays the same between invocations then
    # we hit the cache
    assert DISCRIMINATOR_CACHE.get(UnionType) is discriminator


def test_type_alias_type() -> None:
    Alias = TypeAliasType("Alias", str)  # pyright: ignore

    class Model(BaseModel):
        alias: Alias
        union: Union[int, Alias]
        many: list[Alias]
        annotated: Annotated[Alias, Field(alias="annotatedAlias")]

    m = construct_type(value={"alias": "foo", "union": "bar", "many": ["baz"], "annotatedAlias": "qux"}, type_=Model)
    assert isinstance(m, Model)
    assert isinstance(m.alias, str)
    assert m.alias == "foo"
    assert isinstance(m.union, str)
    assert m.union == "bar"
    assert m.many == ["baz"]
    assert m.annotated == "qux"


def test_field_named_cls() -> None:
    class Model(BaseModel):
        cls: str

    m = construct_type(value={"cls": "foo"}, type_=Model)
    assert isinstance(m, Model)
    assert isinstance(m.cls, str)
    assert m.cls == "foo"


def test_discriminated_union_case() -> None:
    class A(BaseModel):
        type: Literal["a"]

        data: bool

    class B(BaseModel):
        type: Literal["b"]

        data: List[Union[A, object]]

    class ModelA(BaseModel):
        type: Literal["modelA"]

        data: int

    class ModelB(BaseModel):
        type: Literal["modelB"]

        required: str

        data: Union[A, B]

    # when constructing ModelA | ModelB, value data doesn't match ModelB exactly - missing `required`
    m = construct_type(
        value={"type": "modelB", "data": {"type": "a", "data": True}},
        type_=cast(Any, Annotated[Union[ModelA, ModelB], PropertyInfo(discriminator="type")]),
    )

    assert isinstance(m, ModelB)


def test_nested_discriminated_union() -> None:
    class InnerType1(BaseModel):
        type: Literal["type_1"]

    class InnerModel(BaseModel):
        inner_value: str

    class InnerType2(BaseModel):
        type: Literal["type_2"]
        some_inner_model: InnerModel

    class Type1(BaseModel):
        base_type: Literal["base_type_1"]
        value: Annotated[
            Union[
                InnerType1,
                InnerType2,
            ],
            PropertyInfo(discriminator="type"),
        ]

    class Type2(BaseModel):
        base_type: Literal["base_type_2"]

    T = Annotated[
        Union[
            Type1,
            Type2,
        ],
        PropertyInfo(discriminator="base_type"),
    ]

    model = construct_type(
        type_=T,
        value={
            "base_type": "base_type_1",
            "value": {
                "type": "type_2",
            },
        },
    )
    assert isinstance(model, Type1)
    assert isinstance(model.value, InnerType2)


@pytest.mark.parametrize("inherited", [False, True])
def test_extra_properties(inherited: bool) -> None:
    class Item(BaseModel):
        prop: int

    class Model(BaseModel):
        __pydantic_extra__: Dict[str, Item] = Field(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        other: str

        if TYPE_CHECKING:

            def __getattr__(self, attr: str) -> Item: ...

    class Child(Model):
        pass

    model = construct_type(
        type_=Child if inherited else Model,
        value={
            "a": {"prop": 1},
            "other": "foo",
        },
    )
    assert isinstance(model, Model)
    assert model.a.prop == 1
    assert isinstance(model.a, Item)
    assert model.other == "foo"


# NOTE: Workaround for Pydantic Iterable behavior.
# Iterable fields are replaced with a ValidatorIterator and may be consumed
# during serialization, which can cause subsequent dumps to return empty data.
# See: https://github.com/pydantic/pydantic/issues/9541
@pytest.mark.parametrize(
    "data, expected_validated",
    [
        ([1, 2, 3], [1, 2, 3]),
        ((1, 2, 3), (1, 2, 3)),
        (set([1, 2, 3]), set([1, 2, 3])),
        (iter([1, 2, 3]), [1, 2, 3]),
        ([], []),
        ((x for x in [1, 2, 3]), [1, 2, 3]),
        (map(lambda x: x, [1, 2, 3]), [1, 2, 3]),
        (frozenset([1, 2, 3]), frozenset([1, 2, 3])),
        (deque([1, 2, 3]), deque([1, 2, 3])),
    ],
    ids=["list", "tuple", "set", "iterator", "empty", "generator", "map", "frozenset", "deque"],
)
def test_iterable_construction(data: Iterable[int], expected_validated: Iterable[int]) -> None:
    class TypeWithIterable(TypedDict):
        items: EagerIterable[int]

    class Model(BaseModel):
        data: TypeWithIterable

    m = parse_obj(Model, {"data": {"items": data}})
    assert m.data["items"] == expected_validated
    assert type(m.data["items"]) is type(expected_validated)

    # Verify repeated dumps don't lose data (the original bug)
    assert m.model_dump()["data"]["items"] == list(expected_validated)
    assert m.model_dump()["data"]["items"] == list(expected_validated)


def test_iterable_construction_str_falls_back_to_list() -> None:
    # str is iterable (over chars), but str(list_of_chars) produces the list's repr
    # rather than reconstructing a string from items. We special-case str to fall
    # back to list instead of attempting reconstruction.
    class TypeWithIterable(TypedDict):
        items: EagerIterable[str]

    class Model(BaseModel):
        data: TypeWithIterable

    m = parse_obj(Model, {"data": {"items": "hello"}})

    # falls back to list of chars rather than calling str(["h", "e", "l", "l", "o"])
    assert m.data["items"] == ["h", "e", "l", "l", "o"]
    assert m.model_dump()["data"]["items"] == ["h", "e", "l", "l", "o"]


@pytest.mark.parametrize("value", ["ordinary", 7])
def test_eager_iterable_union_preserves_scalar(value: str | int) -> None:
    class Model(BaseModel):
        items: Union[EagerIterable[int], int, str]

    model = parse_obj(Model, {"items": value})
    assert model.items == value
    assert model.model_dump() == {"items": value}
    assert model.model_dump(mode="json") == {"items": value}
    assert json.loads(model.model_dump_json()) == {"items": value}


@pytest.mark.parametrize("invalid", [None, "invalid"])
def test_eager_iterable_rejects_invalid_items(invalid: object) -> None:
    class Model(BaseModel):
        items: EagerIterable[int]

    with pytest.raises(pydantic.ValidationError) as error:
        parse_obj(Model, {"items": [1, invalid]})
    assert error.value.errors()[0]["loc"] == ("items", 1)
    assert "items" in str(error.value)


@pytest.mark.parametrize("exclude_unset, exclude_defaults", [(True, False), (False, True), (True, True)])
def test_eager_iterable_preserves_default_exclusions(exclude_unset: bool, exclude_defaults: bool) -> None:
    class Model(BaseModel):
        items: EagerIterable[int] = (1, 2)

    model = Model()
    assert model.model_dump(exclude_unset=exclude_unset, exclude_defaults=exclude_defaults) == {}
    assert json.loads(model.model_dump_json(exclude_unset=exclude_unset, exclude_defaults=exclude_defaults)) == {}
    assert model.items == (1, 2)


def test_base_page_requires_item_implementation() -> None:
    with pytest.raises(
        NotImplementedError, match=r"^Page items unavailable\. Implement _get_page_items in the page subclass\.$"
    ):
        BasePage[int]().has_next_page()
