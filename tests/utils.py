# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import os
import traceback
import contextlib
from typing import Tuple, TypeVar, Callable, Awaitable, Generator
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from x_twitter_scraper import XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper._types import Omit, NoneType, JsonValue
from x_twitter_scraper._utils import (
    is_dict,
    is_list,
    is_sequence,
    is_list_type,
    is_union_type,
    extract_type_arg,
    is_sequence_type,
    is_annotated_type,
    is_type_alias_type,
)
from x_twitter_scraper._compat import PYDANTIC_V1, field_outer_type, get_model_fields
from x_twitter_scraper._models import BaseModel
from x_twitter_scraper._utils._compat import get_args, is_class, get_origin

# The builtin getattr returns Any, and an attribute of an unknown object is an unknown object. https://docs.python.org/3/library/functions.html#getattr
get_attribute: Callable[[object, str], object] = getattr
get_attribute_or: Callable[[object, str, object], object] = getattr

BaseModelT = TypeVar("BaseModelT", bound=BaseModel)
T = TypeVar("T")


def json_response(status_code: int, *, json: JsonValue) -> httpx.Response:
    return httpx.Response(status_code, json=json)


def assert_matches_model(model: type[BaseModelT], value: BaseModelT, *, path: list[str]) -> bool:
    for name, field in get_model_fields(model).items():
        field_value = get_attribute(value, name)
        if PYDANTIC_V1:
            allow_none = bool(get_attribute_or(field, "allow_none", False))
        else:
            allow_none = False

        assert_matches_type(
            field_outer_type(field),
            field_value,
            path=[*path, name],
            allow_none=allow_none,
        )

    return True


def assert_matches_type(
    type_: object,
    value: object,
    *,
    path: list[str],
    allow_none: bool = False,
) -> None:
    if is_type_alias_type(type_):
        type_ = get_attribute(type_, "__value__")

    if is_annotated_type(type_):
        type_ = extract_type_arg(type_, 0)

    if allow_none and value is None:
        return

    if type_ is None or type_ is NoneType:
        assert value is None
        return

    origin = get_origin(type_) or type_

    if is_list_type(type_) or is_sequence_type(type_):
        assert is_sequence(value)
        if is_list_type(type_):
            assert is_list(value)
        inner_type = get_args(type_)[0]
        for index, entry in enumerate(value):
            assert_matches_type(inner_type, entry, path=[*path, str(index)])
        return

    if is_class(origin) and origin in (str, int, bool, float, bytes, datetime, date):
        assert isinstance(value, origin)
    elif origin == object:
        pass
    elif origin == Literal:
        assert any(type(value) is type(literal) and value == literal for literal in get_args(type_))
    elif origin == dict:
        assert is_dict(value)

        args = get_args(type_)
        key_type = args[0]
        items_type = args[1]

        for key, item in value.items():
            assert_matches_type(key_type, key, path=[*path, "<dict key>"])
            assert_matches_type(items_type, item, path=[*path, "<dict item>"])
    elif is_union_type(type_):
        variants = get_args(type_)

        if len(variants) == 2 and NoneType in variants:
            if value is None:
                return
            return assert_matches_type(variants[variants[0] is NoneType], value, path=path)

        for i, variant in enumerate(variants):
            try:
                assert_matches_type(variant, value, path=[*path, f"variant {i}"])
                return
            except AssertionError:
                traceback.print_exc()
                continue

        raise AssertionError("Did not match any variants")
    elif is_class(origin) and origin.__name__ == "HttpxBinaryResponseContent":
        assert value.__class__.__name__ == "HttpxBinaryResponseContent"
    elif is_class(origin) and issubclass(origin, BaseModel):
        assert is_class(type_) and issubclass(type_, BaseModel)
        assert isinstance(value, type_)
        assert assert_matches_model(type_, value, path=path)
    else:
        assert None, f"Unhandled field type: {type_}"


@contextlib.contextmanager
def update_env(**new_env: str | Omit) -> Generator[None, None, None]:
    old = os.environ.copy()

    try:
        for name, value in new_env.items():
            if isinstance(value, Omit):
                os.environ.pop(name, None)
            else:
                os.environ[name] = value

        yield None
    finally:
        os.environ.clear()
        os.environ.update(old)


async def send_with_mock_transport(
    sync_call: Callable[[XTwitterScraper], T],
    async_call: Callable[[AsyncXTwitterScraper], Awaitable[T]],
    payload: object,
    asynchronous: bool,
    method: str = "GET",
) -> Tuple[httpx.Request, T]:
    requests: list[httpx.Request] = []

    def respond(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json=payload)

    transport = httpx.MockTransport(respond)
    if asynchronous:
        async with AsyncXTwitterScraper(
            api_key="isolated-test",
            http_client=httpx.AsyncClient(transport=transport),
            _strict_response_validation=True,
        ) as client:
            result = await async_call(client)
    else:
        with XTwitterScraper(
            api_key="isolated-test",
            http_client=httpx.Client(transport=transport),
            _strict_response_validation=True,
        ) as sync_client:
            result = sync_call(sync_client)
    assert len(requests) == 1
    assert requests[0].method == method
    return requests[0], result
