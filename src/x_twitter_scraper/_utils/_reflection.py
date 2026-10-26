# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import inspect
from typing import Callable
from typing_extensions import Protocol, ParamSpec

_P = ParamSpec("_P")
_Q = ParamSpec("_Q")


class _AnnotatedParameter(Protocol):
    # inspect.Parameter declares its annotation as Any, and an annotation can be any object. https://docs.python.org/3/library/inspect.html#inspect.Parameter.annotation
    @property
    def annotation(self) -> object: ...


def function_has_argument(func: Callable[_P, object], arg_name: str) -> bool:
    sig = inspect.signature(func)
    return arg_name in sig.parameters


def assert_signatures_in_sync(
    source_func: Callable[_P, object],
    check_func: Callable[_Q, object],
    *,
    exclude_params: set[str] = set(),
) -> None:
    check_sig = inspect.signature(check_func)
    source_sig = inspect.signature(source_func)

    errors: list[str] = []

    for name, source_param in source_sig.parameters.items():
        if name in exclude_params:
            continue

        custom_param = check_sig.parameters.get(name)
        if not custom_param:
            errors.append(f"the `{name}` param is missing")
            continue

        custom_parameter: _AnnotatedParameter = custom_param
        source_parameter: _AnnotatedParameter = source_param
        custom_annotation = custom_parameter.annotation
        source_annotation = source_parameter.annotation
        if custom_annotation != source_annotation:
            errors.append(
                f"types for the `{name}` param are do not match; source={repr(source_annotation)} checking={repr(custom_annotation)}"
            )
            continue

    if errors:
        raise AssertionError(f"{len(errors)} errors encountered when comparing signatures:\n\n" + "\n\n".join(errors))
