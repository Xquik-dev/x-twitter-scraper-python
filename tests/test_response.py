# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

import json
from typing import Any, Dict, List, Union, Callable, cast
from typing_extensions import Annotated

import httpx
import pytest
import pydantic

from x_twitter_scraper import BaseModel, XTwitterScraper, AsyncXTwitterScraper
from x_twitter_scraper._response import (
    APIResponse,
    BaseAPIResponse,
    AsyncAPIResponse,
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    extract_response_type,
)
from x_twitter_scraper._streaming import Stream
from x_twitter_scraper._base_client import FinalRequestOptions, make_request_options


class ConcreteBaseAPIResponse(APIResponse[bytes]): ...


class ConcreteAPIResponse(APIResponse[List[str]]): ...


class ConcreteAsyncAPIResponse(APIResponse[httpx.Response]): ...


def test_extract_response_type_direct_classes() -> None:
    assert extract_response_type(BaseAPIResponse[str]) == str
    assert extract_response_type(APIResponse[str]) == str
    assert extract_response_type(AsyncAPIResponse[str]) == str


def test_extract_response_type_direct_class_missing_type_arg() -> None:
    with pytest.raises(
        RuntimeError,
        match="Expected type <class 'x_twitter_scraper._response.AsyncAPIResponse'> to have a type argument at index 0 but it did not",
    ):
        extract_response_type(AsyncAPIResponse)


def test_extract_response_type_concrete_subclasses() -> None:
    assert extract_response_type(ConcreteBaseAPIResponse) == bytes
    assert extract_response_type(ConcreteAPIResponse) == List[str]
    assert extract_response_type(ConcreteAsyncAPIResponse) == httpx.Response


def test_extract_response_type_binary_response() -> None:
    assert extract_response_type(BinaryAPIResponse) == bytes
    assert extract_response_type(AsyncBinaryAPIResponse) == bytes


ResponseFactory = Callable[[httpx.Response, bool], Union[APIResponse[str], AsyncAPIResponse[str]]]


@pytest.fixture(params=[False, True], ids=["sync", "async"])
def response_factory(
    request: pytest.FixtureRequest, client: XTwitterScraper, async_client: AsyncXTwitterScraper
) -> ResponseFactory:
    def create(raw: httpx.Response, stream: bool) -> Union[APIResponse[str], AsyncAPIResponse[str]]:
        response_type = AsyncAPIResponse[str] if request.param else APIResponse[str]
        return response_type(
            raw=raw,
            client=async_client if request.param else client,
            stream=stream,
            stream_cls=None,
            cast_to=str,
            options=FinalRequestOptions.construct(method="get", url="/foo"),
        )

    return create


class PydanticModel(pydantic.BaseModel): ...


async def test_response_caches_null_post_parser_result(response_factory: ResponseFactory) -> None:
    calls: list[object] = []

    def post_parser(value: object) -> None:
        calls.append(value)

    response = response_factory(httpx.Response(200, content=b"foo"), False)
    response._options = FinalRequestOptions.construct(
        method="get", url="/foo", **make_request_options(post_parser=post_parser)
    )
    for _ in range(2):
        result: object = await response.parse() if isinstance(response, AsyncAPIResponse) else response.parse()
        assert result is None
    assert calls == ["foo"]


async def test_response_parse_mismatched_basemodel(response_factory: ResponseFactory) -> None:
    response = response_factory(httpx.Response(200, content=b"foo"), False)
    with pytest.raises(
        TypeError,
        match="Pydantic models must subclass our base model type, e.g. `from x_twitter_scraper import BaseModel`",
    ):
        if isinstance(response, AsyncAPIResponse):
            await response.parse(to=PydanticModel)
        else:
            response.parse(to=PydanticModel)


async def test_response_parse_custom_stream(response_factory: ResponseFactory) -> None:
    response = response_factory(httpx.Response(200, content=b"foo"), True)
    stream = (
        await response.parse(to=Stream[int])
        if isinstance(response, AsyncAPIResponse)
        else response.parse(to=Stream[int])
    )
    assert stream._cast_to == int


class CustomModel(BaseModel):
    foo: str
    bar: int


@pytest.mark.parametrize(
    "model_type", [CustomModel, Annotated[CustomModel, "random metadata"]], ids=["model", "annotated"]
)
async def test_response_parse_custom_model(response_factory: ResponseFactory, model_type: object) -> None:
    response = response_factory(httpx.Response(200, content=json.dumps({"foo": "hello!", "bar": 2})), False)
    model = cast("type[CustomModel]", model_type)
    obj = await response.parse(to=model) if isinstance(response, AsyncAPIResponse) else response.parse(to=model)
    assert obj.foo == "hello!"
    assert obj.bar == 2


@pytest.mark.parametrize(
    "content, expected",
    [("false", False), ("true", True), ("False", False), ("True", True), ("TrUe", True), ("FalSe", False)],
)
async def test_response_parse_bool(response_factory: ResponseFactory, content: str, expected: bool) -> None:
    response = response_factory(httpx.Response(200, content=content), False)
    result = await response.parse(to=bool) if isinstance(response, AsyncAPIResponse) else response.parse(to=bool)
    assert result is expected


class OtherModel(BaseModel):
    a: str


@pytest.mark.parametrize("client, async_client", [(False, False)], indirect=True)
async def test_response_parse_expect_model_union_non_json_content(response_factory: ResponseFactory) -> None:
    response = response_factory(
        httpx.Response(200, content=b"foo", headers={"Content-Type": "application/text"}), False
    )
    model = cast(Any, Union[CustomModel, OtherModel])
    obj = await response.parse(to=model) if isinstance(response, AsyncAPIResponse) else response.parse(to=model)
    assert isinstance(obj, str)
    assert obj == "foo"


@pytest.mark.parametrize("client, async_client", [(False, False), (True, True)], indirect=True)
@pytest.mark.parametrize("mapping_type", [dict, Dict, dict[str, object]])
async def test_response_parse_dictionary(
    response_factory: ResponseFactory, mapping_type: type[dict[str, object]]
) -> None:
    data = {"nested": {"count": 2}, "items": [True, None], "empty": {}}
    response = response_factory(httpx.Response(200, json=data), False)
    result = (
        await response.parse(to=mapping_type)
        if isinstance(response, AsyncAPIResponse)
        else response.parse(to=mapping_type)
    )
    assert result == data
