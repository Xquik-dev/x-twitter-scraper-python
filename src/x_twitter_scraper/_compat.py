# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar
from functools import cached_property as cached_property
from typing_extensions import Literal, TypedDict

import pydantic
from pydantic.fields import FieldInfo

from ._types import IncEx

_ModelT = TypeVar("_ModelT", bound=pydantic.BaseModel)

PYDANTIC_V1 = pydantic.VERSION.startswith("1.")

# The type checkers run with Pydantic 2 only, so each branch for Pydantic 1 sits behind `not TYPE_CHECKING`, which both checkers treat as unreachable. https://mypy.readthedocs.io/en/stable/common_issues.html#python-version-and-system-platform-checks
if PYDANTIC_V1 and not TYPE_CHECKING:
    from pydantic.typing import (
        get_args as get_args,
        is_union as is_union,
        get_origin as get_origin,
        is_typeddict as is_typeddict,
        is_literal_type as is_literal_type,
    )
    from pydantic.datetime_parse import parse_date as parse_date, parse_datetime as parse_datetime
else:
    from ._utils import (
        get_args as get_args,
        is_union as is_union,
        get_origin as get_origin,
        parse_date as parse_date,
        is_typeddict as is_typeddict,
        parse_datetime as parse_datetime,
        is_literal_type as is_literal_type,
    )


if PYDANTIC_V1 and not TYPE_CHECKING:
    ConfigDict = None
else:
    from pydantic import ConfigDict as ConfigDict

# pydantic.BaseModel takes Any in its constructor, so mypy reads the bare class as containing Any. This name typed as the class keeps isinstance checks free of it. https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-disallow-any-expr
PydanticModel: type[pydantic.BaseModel] = pydantic.BaseModel


def parse_obj(model: type[_ModelT], value: object) -> _ModelT:
    if PYDANTIC_V1 and not TYPE_CHECKING:
        return model.parse_obj(value)
    return model.model_validate(value)


def field_is_required(field: FieldInfo) -> bool:
    if PYDANTIC_V1 and not TYPE_CHECKING:
        return field.required
    return field.is_required()


def field_get_default(field: FieldInfo) -> object:
    value: object = field.get_default()
    if PYDANTIC_V1:
        return value
    from pydantic_core import PydanticUndefined

    if value == PydanticUndefined:
        return None
    return value


def field_outer_type(field: FieldInfo) -> object:
    if PYDANTIC_V1 and not TYPE_CHECKING:
        return field.outer_type_
    annotation: object = field.annotation
    return annotation


def get_model_config(model: type[pydantic.BaseModel]) -> object:
    if PYDANTIC_V1 and not TYPE_CHECKING:
        return model.__config__
    return model.model_config


def get_model_fields(model: type[pydantic.BaseModel]) -> dict[str, FieldInfo]:
    if PYDANTIC_V1 and not TYPE_CHECKING:
        return model.__fields__
    return model.model_fields


def model_copy(model: _ModelT, *, deep: bool = False) -> _ModelT:
    if PYDANTIC_V1 and not TYPE_CHECKING:
        return model.copy(deep=deep)
    return model.model_copy(deep=deep)


def model_json(model: pydantic.BaseModel, *, indent: int | None = None) -> str:
    if PYDANTIC_V1 and not TYPE_CHECKING:
        return model.json(indent=indent)
    return model.model_dump_json(indent=indent)


class _ModelDumpKwargs(TypedDict, total=False, closed=True):
    by_alias: bool


def model_dump(
    model: pydantic.BaseModel,
    *,
    exclude: IncEx | None = None,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    warnings: bool = True,
    mode: Literal["json", "python"] = "python",
    by_alias: bool | None = None,
) -> dict[str, object]:
    if PYDANTIC_V1 and not TYPE_CHECKING and not hasattr(model, "model_dump"):
        return model.dict(
            exclude=exclude, exclude_unset=exclude_unset, exclude_defaults=exclude_defaults, by_alias=bool(by_alias)
        )
    kwargs: _ModelDumpKwargs = {}
    if by_alias is not None:
        kwargs["by_alias"] = by_alias
    dumped: dict[str, object] = model.model_dump(
        mode=mode,
        exclude=exclude,
        exclude_unset=exclude_unset,
        exclude_defaults=exclude_defaults,
        warnings=True if PYDANTIC_V1 else warnings,
        **kwargs,
    )
    return dumped


if PYDANTIC_V1 and not TYPE_CHECKING:
    import pydantic.generics

    class GenericModel(pydantic.generics.GenericModel, pydantic.BaseModel): ...
else:

    class GenericModel(pydantic.BaseModel): ...
