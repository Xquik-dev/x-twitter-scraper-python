# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
import inspect
import weakref
from typing import (
    IO,
    TYPE_CHECKING,
    Any,
    Type,
    Union,
    Generic,
    TypeVar,
    Callable,
    Iterable,
    Optional,
    AsyncIterable,
    cast,
)
from datetime import date, datetime
from typing_extensions import (
    List,
    Unpack,
    Literal,
    ClassVar,
    Protocol,
    Required,
    Annotated,
    ParamSpec,
    TypeAlias,
    TypedDict,
    TypeGuard,
    final,
    override,
    get_type_hints,
    runtime_checkable,
)

import pydantic
from pydantic.fields import FieldInfo

from ._types import (
    Body,
    IncEx,
    Query,
    ModelT,
    Headers,
    Timeout,
    NotGiven,
    AnyMapping,
    PostParser,
    RequestOptions,
    HttpxRequestFiles,
)
from ._utils import (
    PropertyInfo,
    is_list,
    memoize,
    is_given,
    json_safe,
    is_mapping,
    parse_date,
    is_iterable,
    coerce_boolean,
    parse_datetime,
    strip_not_given,
    extract_type_arg,
    is_annotated_type,
    is_type_alias_type,
    strip_annotated_type,
)
from ._compat import (
    PYDANTIC_V1,
    ConfigDict,
    GenericModel as BaseGenericModel,
    get_args,
    is_union,
    parse_obj,
    get_origin,
    is_literal_type,
    get_model_config,
    get_model_fields,
    field_get_default,
)
from ._constants import RAW_RESPONSE_HEADER

if TYPE_CHECKING:
    from pydantic import GetCoreSchemaHandler
    from pydantic.v1 import BaseModel as V1BaseModel, ValidationError as V1ValidationError
    from pydantic_core import CoreSchema, core_schema
    from pydantic.v1.fields import ModelField as V1ModelField
    from pydantic_core.core_schema import ModelField, ModelSchema, LiteralSchema, ModelFieldsSchema
else:
    from pydantic import BaseModel as V1BaseModel, ValidationError as V1ValidationError

    try:
        from pydantic_core import CoreSchema, core_schema
    except ImportError:
        CoreSchema = None
        core_schema = None

__all__ = ["BaseModel", "GenericModel"]

_T = TypeVar("_T")
_BaseModelT = TypeVar("_BaseModelT", bound="BaseModel")

P = ParamSpec("P")


@runtime_checkable
class _ConfigProtocol(Protocol):
    allow_population_by_field_name: bool


if PYDANTIC_V1 and not TYPE_CHECKING:
    from ._type_aliases import AliasModelMetaclass as _ModelMetaclass
else:
    from pydantic._internal._model_construction import ModelMetaclass as _ModelMetaclass


class BaseModel(pydantic.BaseModel, metaclass=_ModelMetaclass):
    if PYDANTIC_V1:

        @property
        @override
        def model_fields_set(self) -> set[str]:
            return self.__fields_set__  # type: ignore

        class Config(pydantic.BaseConfig):  # pyright: ignore[reportDeprecated]
            extra: Any = pydantic.Extra.allow  # type: ignore
    else:
        model_config: ClassVar[ConfigDict] = ConfigDict(
            extra="allow", defer_build=coerce_boolean(os.environ.get("DEFER_PYDANTIC_BUILD", "true"))
        )

    def to_dict(
        self,
        *,
        mode: Literal["json", "python"] = "python",
        use_api_names: bool = True,
        exclude_unset: bool = True,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        warnings: bool = True,
    ) -> dict[str, object]:
        """Recursively generate a dictionary representation of the model.

        By default, fields that were not set by the API will not be included,
        and keys will match the API response, *not* the property names from the model.

        Args:
            mode:
                If mode is 'json', the dictionary will only contain JSON serializable types. e.g. `datetime` will be turned into a string, `"2024-3-22T18:11:19.117000Z"`.
                If mode is 'python', the dictionary may contain any Python objects. e.g. `datetime(2024, 3, 22)`

            use_api_names: Whether to use the key that the API responded with or the property name. Defaults to `True`.
            exclude_unset: Whether to exclude fields that have not been explicitly set.
            exclude_defaults: Whether to exclude fields that are set to their default value from the output.
            exclude_none: Whether to exclude fields that have a value of `None` from the output.
            warnings: Whether to log warnings when invalid fields are encountered. This is only supported in Pydantic v2.
        """
        data = self.model_dump(
            mode=mode,
            by_alias=use_api_names,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            warnings=warnings,
        )
        return cast("dict[str, object]", data)

    def to_json(
        self,
        *,
        indent: int | None = 2,
        use_api_names: bool = True,
        exclude_unset: bool = True,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        warnings: bool = True,
    ) -> str:
        """Generates a JSON string representing this model as it would be received from or sent to the API (but with indentation).

        By default, fields that were not set by the API will not be included,
        and keys will match the API response, *not* the property names from the model.

        Args:
            indent: Indentation to use in the JSON output. If `None` is passed, the output will be compact. Defaults to `2`
            use_api_names: Whether to use the key that the API responded with or the property name. Defaults to `True`.
            exclude_unset: Whether to exclude fields that have not been explicitly set.
            exclude_defaults: Whether to exclude fields that have the default value.
            exclude_none: Whether to exclude fields that have a value of `None`.
            warnings: Whether to show any warnings that occurred during serialization. This is only supported in Pydantic v2.
        """
        return self.model_dump_json(
            indent=indent,
            by_alias=use_api_names,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            warnings=warnings,
        )

    @override
    def __str__(self) -> str:
        return f"{self.__repr_name__()}({self.__repr_str__(', ')})"  # type: ignore[misc]

    @classmethod
    @override
    def construct(  # pyright: ignore[reportIncompatibleMethodOverride]
        __cls: Type[ModelT],
        _fields_set: set[str] | None = None,
        **values: object,
    ) -> ModelT:
        m = __cls.__new__(__cls)
        fields_values: dict[str, object] = {}

        config = get_model_config(__cls)
        populate_by_name = (
            config.allow_population_by_field_name
            if isinstance(config, _ConfigProtocol)
            else config.get("populate_by_name")
        )

        if _fields_set is None:
            _fields_set = set()

        model_fields = get_model_fields(__cls)
        for name, field in model_fields.items():
            key = field.alias
            if key is None or (key not in values and populate_by_name):
                key = name

            if key in values:
                fields_values[name] = _construct_field(value=values[key], field=field, key=key)
                _fields_set.add(name)
            else:
                fields_values[name] = field_get_default(field)

        extra_field_type = _get_extra_fields_type(__cls)

        _extra = {}
        for key, value in values.items():
            if key not in model_fields:
                parsed = construct_type(value=value, type_=extra_field_type) if extra_field_type is not None else value

                if PYDANTIC_V1:
                    _fields_set.add(key)
                    fields_values[key] = parsed
                else:
                    _extra[key] = parsed

        object.__setattr__(m, "__dict__", fields_values)

        if PYDANTIC_V1:
            m._init_private_attributes()  # type: ignore

            object.__setattr__(m, "__fields_set__", _fields_set)
        else:
            object.__setattr__(m, "__pydantic_private__", None)
            object.__setattr__(m, "__pydantic_extra__", _extra)
            object.__setattr__(m, "__pydantic_fields_set__", _fields_set)

        return m

    if not TYPE_CHECKING:
        model_construct = construct

    if PYDANTIC_V1:

        @override
        def model_dump(
            self,
            *,
            mode: Literal["json", "python"] | str = "python",
            include: IncEx | None = None,
            exclude: IncEx | None = None,
            context: Any | None = None,
            by_alias: bool | None = None,
            exclude_unset: bool = False,
            exclude_defaults: bool = False,
            exclude_none: bool = False,
            exclude_computed_fields: bool = False,
            round_trip: bool = False,
            warnings: bool | Literal["none", "warn", "error"] = True,
            fallback: Callable[[Any], Any] | None = None,
            serialize_as_any: bool = False,
            polymorphic_serialization: bool | None = None,
        ) -> dict[str, Any]:
            """Usage docs: https://docs.pydantic.dev/2.4/concepts/serialization/#modelmodel_dump

            Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

            Args:
                mode: The mode in which `to_python` should run.
                    If mode is 'json', the output will only contain JSON serializable types.
                    If mode is 'python', the output may contain non-JSON-serializable Python objects.
                include: A set of fields to include in the output.
                exclude: A set of fields to exclude from the output.
                context: Additional context to pass to the serializer.
                by_alias: Whether to use the field's alias in the dictionary key if defined.
                exclude_unset: Whether to exclude fields that have not been explicitly set.
                exclude_defaults: Whether to exclude fields that are set to their default value.
                exclude_none: Whether to exclude fields that have a value of `None`.
                exclude_computed_fields: Whether to exclude computed fields.
                round_trip: If True, dumped values should be valid as input for non-idempotent types such as Json[T].
                warnings: How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors,
                    "error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError].
                fallback: A function to call when an unknown value is encountered. If not provided,
                    a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError] error is raised.
                serialize_as_any: Whether to serialize fields with duck-typing serialization behavior.
                polymorphic_serialization: Whether to serialize model subclasses polymorphically.

            Returns:
                A dictionary representation of the model.
            """
            if mode not in {"json", "python"}:
                raise ValueError("mode must be either 'json' or 'python'")
            if round_trip != False:
                raise ValueError("round_trip is only supported in Pydantic v2")
            if warnings != True:
                raise ValueError("warnings is only supported in Pydantic v2")
            if context is not None:
                raise ValueError("context is only supported in Pydantic v2")
            if serialize_as_any != False:
                raise ValueError("serialize_as_any is only supported in Pydantic v2")
            if polymorphic_serialization is not None:
                raise ValueError("polymorphic_serialization is only supported in Pydantic v2")
            if fallback is not None:
                raise ValueError("fallback is only supported in Pydantic v2")
            if exclude_computed_fields != False:
                raise ValueError("exclude_computed_fields is only supported in Pydantic v2")
            dumped = super().dict(  # pyright: ignore[reportDeprecated]
                include=include,
                exclude=exclude,
                by_alias=by_alias if by_alias is not None else False,
                exclude_unset=exclude_unset,
                exclude_defaults=exclude_defaults,
                exclude_none=exclude_none,
            )

            from ._eager_serialization import serialize_fields

            dumped = serialize_fields(dumped, cast(V1BaseModel, self), include, exclude, bool(by_alias))
            return cast("dict[str, Any]", json_safe(dumped)) if mode == "json" else dumped

        @override
        def model_dump_json(
            self,
            *,
            indent: int | None = None,
            ensure_ascii: bool = False,
            include: IncEx | None = None,
            exclude: IncEx | None = None,
            context: Any | None = None,
            by_alias: bool | None = None,
            exclude_unset: bool = False,
            exclude_defaults: bool = False,
            exclude_none: bool = False,
            exclude_computed_fields: bool = False,
            round_trip: bool = False,
            warnings: bool | Literal["none", "warn", "error"] = True,
            fallback: Callable[[Any], Any] | None = None,
            serialize_as_any: bool = False,
            polymorphic_serialization: bool | None = None,
        ) -> str:
            """Usage docs: https://docs.pydantic.dev/2.4/concepts/serialization/#modelmodel_dump_json

            Generates a JSON representation of the model using Pydantic's `to_json` method.

            Args:
                indent: Indentation to use in the JSON output. If None is passed, the output will be compact.
                include: Field(s) to include in the JSON output. Can take either a string or set of strings.
                exclude: Field(s) to exclude from the JSON output. Can take either a string or set of strings.
                by_alias: Whether to serialize using field aliases.
                exclude_unset: Whether to exclude fields that have not been explicitly set.
                exclude_defaults: Whether to exclude fields that have the default value.
                exclude_none: Whether to exclude fields that have a value of `None`.
                round_trip: Whether to use serialization/deserialization between JSON and class instance.
                warnings: Whether to show any warnings that occurred during serialization.
                polymorphic_serialization: Whether to serialize model subclasses polymorphically.

            Returns:
                A JSON string representation of the model.
            """
            if round_trip != False:
                raise ValueError("round_trip is only supported in Pydantic v2")
            if warnings != True:
                raise ValueError("warnings is only supported in Pydantic v2")
            if context is not None:
                raise ValueError("context is only supported in Pydantic v2")
            if serialize_as_any != False:
                raise ValueError("serialize_as_any is only supported in Pydantic v2")
            if polymorphic_serialization is not None:
                raise ValueError("polymorphic_serialization is only supported in Pydantic v2")
            if fallback is not None:
                raise ValueError("fallback is only supported in Pydantic v2")
            if ensure_ascii != False:
                raise ValueError("ensure_ascii is only supported in Pydantic v2")
            if exclude_computed_fields != False:
                raise ValueError("exclude_computed_fields is only supported in Pydantic v2")
            return super().json(  # type: ignore[reportDeprecated]
                indent=indent,
                include=include,
                exclude=exclude,
                by_alias=by_alias if by_alias is not None else False,
                exclude_unset=exclude_unset,
                exclude_defaults=exclude_defaults,
                exclude_none=exclude_none,
            )


class _EagerIterable(Generic[_T]):
    @classmethod
    def __get_validators__(cls) -> Iterable[Callable[..., object]]:
        yield cls._validate_v1

    @classmethod
    def _validate_v1(cls, value: Iterable[object], field: V1ModelField) -> object:
        def validate_items(items: list[object]) -> list[object]:
            if not field.sub_fields:
                return items
            validated: list[object] = []
            for index, item in enumerate(items):
                parsed, error = field.sub_fields[0].validate(item, {}, loc=(index,))
                if error:
                    raise V1ValidationError([error], V1BaseModel)
                validated.append(parsed)
            return validated

        return cls._validate(value, validate_items)

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        source_type: Any,
        handler: GetCoreSchemaHandler,
    ) -> CoreSchema:
        (item_type,) = get_args(source_type) or (Any,)
        item_schema: CoreSchema = handler.generate_schema(item_type)
        list_of_items_schema: CoreSchema = core_schema.list_schema(item_schema)

        return core_schema.no_info_wrap_validator_function(
            cls._validate,
            list_of_items_schema,
            serialization=core_schema.wrap_serializer_function_ser_schema(
                cls._serialize,
                info_arg=False,
                schema=list_of_items_schema,
            ),
        )

    @staticmethod
    def _validate(v: Iterable[object], handler: Callable[[list[object]], list[object]]) -> Any:
        original_type: type[Any] = type(v)

        if is_list(v):
            items: list[object] = v
        else:
            try:
                items = list(v)
            except TypeError as e:
                raise ValueError("Value is not iterable") from e

        validated: list[object] = handler(items)

        if original_type is list:
            return validated
        if issubclass(original_type, str):
            return validated
        try:
            return original_type(validated)
        except (TypeError, ValueError):
            return validated

    @staticmethod
    def _serialize(v: object, handler: Callable[[object], object]) -> object:
        if isinstance(v, str) or not is_iterable(v):
            from pydantic_core import PydanticSerializationUnexpectedValue

            raise PydanticSerializationUnexpectedValue("Expected a validated iterable container")
        return handler(v if is_list(v) else list(v))


if PYDANTIC_V1 and not TYPE_CHECKING:
    EagerIterable = _EagerIterable
else:
    EagerIterable: TypeAlias = Annotated[Iterable[_T], _EagerIterable]


def _construct_field(value: object, field: FieldInfo, key: str) -> object:
    if value is None:
        return field_get_default(field)

    if PYDANTIC_V1:
        type_ = cast(type, field.outer_type_)  # type: ignore
    else:
        type_ = field.annotation  # type: ignore

    if type_ is None:
        raise RuntimeError(f"Unexpected field type is None for {key}")

    return construct_type(value=value, type_=type_, metadata=getattr(field, "metadata", None))


def _get_extra_fields_type(cls: type[pydantic.BaseModel]) -> object | None:
    if PYDANTIC_V1:
        if not any(
            "__pydantic_extra__" in base.__annotations__ for base in cls.__mro__ if hasattr(base, "__annotations__")
        ):
            return None
        annotation = get_type_hints(cls).get("__pydantic_extra__")
        arguments: tuple[object, ...] = get_args(annotation)
        return arguments[1] if get_origin(annotation) is dict and len(arguments) == 2 else None

    schema = cls.__pydantic_core_schema__
    if schema["type"] == "model":
        fields = schema["schema"]
        if fields["type"] == "model-fields":
            extras = fields.get("extras_schema")
            if extras and "cls" in extras:
                return extras["cls"]  # type: ignore[no-any-return]

    return None


def is_basemodel(type_: type) -> bool:
    if is_union(type_):
        for variant in get_args(type_):
            if is_basemodel(variant):
                return True

        return False

    return is_basemodel_type(type_)


def is_basemodel_type(type_: type) -> TypeGuard[type[BaseModel] | type[GenericModel]]:
    origin = get_origin(type_) or type_
    if not inspect.isclass(origin):
        return False
    return issubclass(origin, BaseModel) or issubclass(origin, GenericModel)


def build(
    base_model_cls: Callable[P, _BaseModelT],
    *args: P.args,
    **kwargs: P.kwargs,
) -> _BaseModelT:
    if args:
        raise TypeError(
            "Received positional arguments which are not supported; Keyword arguments must be used instead",
        )

    return cast(_BaseModelT, construct_type(type_=base_model_cls, value=kwargs))


def construct_type_unchecked(*, value: object, type_: type[_T]) -> _T:
    return cast(_T, construct_type(value=value, type_=type_))


def construct_type(*, value: object, type_: object, metadata: Optional[List[Any]] = None) -> object:
    original_type = None

    type_ = cast("type[object]", type_)
    if is_type_alias_type(type_):
        original_type = type_  # type: ignore[unreachable]
        type_ = type_.__value__  # type: ignore[unreachable]

    if metadata is not None and len(metadata) > 0:
        meta: tuple[Any, ...] = tuple(metadata)
    elif is_annotated_type(type_):
        meta = get_args(type_)[1:]
        type_ = extract_type_arg(type_, 0)
    else:
        meta = tuple()

    origin = get_origin(type_) or type_
    args = get_args(type_)

    if is_union(origin):
        try:
            validation_type: type[object] = original_type or type_
            return validate_type(type_=validation_type, value=value)
        except Exception:
            pass

        discriminator = _build_discriminated_union_meta(union=type_, meta_annotations=meta)
        if discriminator and is_mapping(value):
            variant_value = value.get(discriminator.field_alias_from or discriminator.field_name)
            if variant_value and isinstance(variant_value, str):
                variant_type = discriminator.mapping.get(variant_value)
                if variant_type:
                    return construct_type(type_=variant_type, value=value)

        for variant in args:
            try:
                return construct_type(value=value, type_=variant)
            except Exception:
                continue

        raise RuntimeError(f"Could not convert data into a valid instance of {type_}")

    if origin == dict:
        if not is_mapping(value):
            return value

        _, items_type = get_args(type_) or (Any, Any)
        return {key: construct_type(value=item, type_=items_type) for key, item in value.items()}

    if (
        not is_literal_type(type_)
        and inspect.isclass(origin)
        and (issubclass(origin, BaseModel) or issubclass(origin, GenericModel))
    ):
        if is_list(value):
            return [cast(Any, type_).construct(**entry) if is_mapping(entry) else entry for entry in value]

        if is_mapping(value):
            if issubclass(type_, BaseModel):
                return type_.construct(**value)  # type: ignore[arg-type]

            return cast(Any, type_).construct(**value)

    if origin == list:
        if not is_list(value):
            return value

        inner_type = args[0]
        return [construct_type(value=entry, type_=inner_type) for entry in value]

    if origin == float:
        if isinstance(value, int):
            coerced = float(value)
            if coerced != value:
                return value
            return coerced

        return value

    if type_ == datetime:
        try:
            return parse_datetime(value)  # type: ignore
        except Exception:
            return value

    if type_ == date:
        try:
            return parse_date(value)  # type: ignore
        except Exception:
            return value

    return value


@runtime_checkable
class CachedDiscriminatorType(Protocol):
    __discriminator__: DiscriminatorDetails


DISCRIMINATOR_CACHE: weakref.WeakKeyDictionary[type, DiscriminatorDetails] = weakref.WeakKeyDictionary()


class DiscriminatorDetails:
    field_name: str

    field_alias_from: str | None

    mapping: dict[str, type]

    def __init__(
        self,
        *,
        mapping: dict[str, type],
        discriminator_field: str,
        discriminator_alias: str | None,
    ) -> None:
        self.mapping = mapping
        self.field_name = discriminator_field
        self.field_alias_from = discriminator_alias


def _build_discriminated_union_meta(*, union: type, meta_annotations: tuple[Any, ...]) -> DiscriminatorDetails | None:
    cached = DISCRIMINATOR_CACHE.get(union)
    if cached is not None:
        return cached

    discriminator_field_name: str | None = None

    for annotation in meta_annotations:
        if isinstance(annotation, PropertyInfo) and annotation.discriminator is not None:
            discriminator_field_name = annotation.discriminator
            break

    if not discriminator_field_name:
        return None

    mapping: dict[str, type] = {}
    discriminator_alias: str | None = None

    for variant in get_args(union):
        variant = strip_annotated_type(variant)
        if is_basemodel_type(variant):
            if PYDANTIC_V1:
                field_info = cast("dict[str, FieldInfo]", variant.__fields__).get(discriminator_field_name)  # pyright: ignore[reportDeprecated, reportUnnecessaryCast]
                if not field_info:
                    continue

                discriminator_alias = field_info.alias

                if (annotation := getattr(field_info, "annotation", None)) and is_literal_type(annotation):
                    for entry in get_args(annotation):
                        if isinstance(entry, str):
                            mapping[entry] = variant
            else:
                field = _extract_field_schema_pv2(variant, discriminator_field_name)
                if not field:
                    continue

                discriminator_alias = field.get("serialization_alias")

                field_schema = field["schema"]

                if field_schema["type"] == "literal":
                    for entry in cast("LiteralSchema", field_schema)["expected"]:
                        if isinstance(entry, str):
                            mapping[entry] = variant

    if not mapping:
        return None

    details = DiscriminatorDetails(
        mapping=mapping,
        discriminator_field=discriminator_field_name,
        discriminator_alias=discriminator_alias,
    )
    DISCRIMINATOR_CACHE.setdefault(union, details)
    return details


def _extract_field_schema_pv2(model: type[BaseModel], field_name: str) -> ModelField | None:
    schema = model.__pydantic_core_schema__
    if schema["type"] == "definitions":
        schema = schema["schema"]

    if schema["type"] != "model":
        return None

    schema = cast("ModelSchema", schema)
    fields_schema = schema["schema"]
    if fields_schema["type"] != "model-fields":
        return None

    fields_schema = cast("ModelFieldsSchema", fields_schema)
    field = fields_schema["fields"].get(field_name)
    if not field:
        return None

    return cast("ModelField", field)  # pyright: ignore[reportUnnecessaryCast]


def validate_type(*, type_: type[_T], value: object) -> _T:
    origin = get_origin(type_) or type_
    if inspect.isclass(origin) and issubclass(origin, pydantic.BaseModel):
        return cast(_T, parse_obj(cast("type[pydantic.BaseModel]", type_), value))

    return _validate_non_model_type(type_=type_, value=value)


if TYPE_CHECKING:
    GenericModel = BaseModel
else:

    class GenericModel(BaseGenericModel, BaseModel):
        pass


if not PYDANTIC_V1:
    from pydantic import TypeAdapter as _TypeAdapter

    _CachedTypeAdapter = memoize(_TypeAdapter)

    if TYPE_CHECKING:
        from pydantic import TypeAdapter
    else:
        TypeAdapter = _CachedTypeAdapter

    def _validate_non_model_type(*, type_: type[_T], value: object) -> _T:
        return TypeAdapter(type_).validate_python(value)

elif not TYPE_CHECKING:

    class RootModel(GenericModel, Generic[_T]):
        __root__: _T

    def _validate_non_model_type(*, type_: type[_T], value: object) -> _T:
        model = _create_pydantic_model(type_).validate(value)
        return cast(_T, model.__root__)

    def _create_pydantic_model(type_: _T) -> Type[RootModel[_T]]:
        return RootModel[type_]  # type: ignore


class SecurityOptions(TypedDict, total=False):
    api_key: bool
    oauth_bearer: bool


class FinalRequestOptionsInput(RequestOptions, total=False):
    method: Required[str]
    url: Required[str]
    files: HttpxRequestFiles | None
    content: Union[bytes, bytearray, IO[bytes], Iterable[bytes], AsyncIterable[bytes], None]
    json_data: Body


@final
class FinalRequestOptions(pydantic.BaseModel):
    method: str
    url: str
    params: Query = {}
    headers: Union[Headers, NotGiven] = NotGiven()
    max_retries: Union[int, NotGiven] = NotGiven()
    timeout: Union[float, Timeout, None, NotGiven] = NotGiven()
    files: Union[HttpxRequestFiles, None] = None
    idempotency_key: Union[str, None] = None
    post_parser: Union[PostParser, NotGiven] = NotGiven()
    follow_redirects: Union[bool, None] = None
    security: SecurityOptions = {
        "api_key": True,
        "oauth_bearer": True,
    }

    content: Union[bytes, bytearray, IO[bytes], Iterable[bytes], AsyncIterable[bytes], None] = None
    json_data: Union[Body, None] = None
    extra_json: Union[AnyMapping, None] = None

    if PYDANTIC_V1:

        class Config(pydantic.BaseConfig):  # pyright: ignore[reportDeprecated]
            arbitrary_types_allowed: bool = True
    else:
        model_config: ClassVar[ConfigDict] = ConfigDict(arbitrary_types_allowed=True)

    def get_max_retries(self, max_retries: int) -> int:
        if isinstance(self.max_retries, NotGiven):
            return max_retries
        return self.max_retries

    def _strip_raw_response_header(self) -> None:
        if not is_given(self.headers):
            return

        if self.headers.get(RAW_RESPONSE_HEADER):
            self.headers = {**self.headers}
            self.headers.pop(RAW_RESPONSE_HEADER)

    @classmethod
    @override
    def construct(  # type: ignore
        cls,
        _fields_set: set[str] | None = None,
        **values: Unpack[FinalRequestOptionsInput],
    ) -> FinalRequestOptions:
        kwargs: dict[str, Any] = {key: strip_not_given(value) for key, value in values.items()}
        if PYDANTIC_V1:
            return cast(FinalRequestOptions, super().construct(_fields_set, **kwargs))  # pyright: ignore[reportDeprecated]
        return super().model_construct(_fields_set, **kwargs)

    if not TYPE_CHECKING:
        model_construct = construct
