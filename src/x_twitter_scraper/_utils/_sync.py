# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import asyncio
import functools
from typing import TypeVar, Callable, Awaitable
from typing_extensions import ParamSpec

import anyio
import sniffio
import anyio.to_thread

T_Retval = TypeVar("T_Retval")
T_ParamSpec = ParamSpec("T_ParamSpec")


async def to_thread(
    func: Callable[T_ParamSpec, T_Retval], /, *args: T_ParamSpec.args, **kwargs: T_ParamSpec.kwargs
) -> T_Retval:
    if sniffio.current_async_library() == "asyncio":
        return await asyncio.to_thread(func, *args, **kwargs)

    return await anyio.to_thread.run_sync(
        functools.partial(func, *args, **kwargs),
    )


def asyncify(function: Callable[T_ParamSpec, T_Retval]) -> Callable[T_ParamSpec, Awaitable[T_Retval]]:
    async def wrapper(*args: T_ParamSpec.args, **kwargs: T_ParamSpec.kwargs) -> T_Retval:
        return await to_thread(function, *args, **kwargs)

    return wrapper
