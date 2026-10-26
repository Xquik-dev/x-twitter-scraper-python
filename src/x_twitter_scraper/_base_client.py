# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import sys
import time
import uuid
import email
import asyncio
import inspect
import logging
import platform
import warnings
import email.utils
from types import TracebackType
from random import random
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Type,
    Union,
    Generic,
    Mapping,
    TypeVar,
    Iterable,
    Iterator,
    Optional,
    Generator,
    AsyncIterator,
    cast,
    overload,
)
from typing_extensions import Literal, override, get_origin

import anyio
import httpx
import distro
import pydantic
from httpx import URL
from pydantic import PrivateAttr

from . import _exceptions
from ._qs import Querystring
from ._files import to_httpx_files, async_to_httpx_files
from ._types import (
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    ResponseT,
    AnyMapping,
    PostParser,
    BinaryTypes,
    RequestFiles,
    HttpxResponse,
    HttpxSendArgs,
    RequestOptions,
    AsyncBinaryTypes,
    HttpxRequestFiles,
    ModelBuilderProtocol,
    not_given,
)
from ._utils import is_dict, is_list, memoize, asyncify, is_given, is_tuple, get_header, is_mapping
from ._compat import PYDANTIC_V1, model_copy, model_dump
from ._models import GenericModel, SecurityOptions, FinalRequestOptions, validate_type, construct_type
from ._response import (
    APIResponse,
    BaseAPIResponse,
    AsyncAPIResponse,
    extract_response_type,
)
from ._constants import (
    DEFAULT_TIMEOUT,
    MAX_RETRY_DELAY,
    DEFAULT_MAX_RETRIES,
    INITIAL_RETRY_DELAY,
    RAW_RESPONSE_HEADER,
    OVERRIDE_CAST_TO_HEADER,
    DEFAULT_CONNECTION_LIMITS,
)
from ._streaming import Stream, SSEDecoder, AsyncStream, SSEBytesDecoder
from ._exceptions import (
    APIStatusError,
    APITimeoutError,
    APIConnectionError,
    APIResponseValidationError,
)
from ._utils._json import json_loads, openapi_dumps

log: logging.Logger = logging.getLogger(__name__)

SyncPageT = TypeVar("SyncPageT", bound="BaseSyncPage[object]")
AsyncPageT = TypeVar("AsyncPageT", bound="BaseAsyncPage[object]")


_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_ItemT_co = TypeVar("_ItemT_co", covariant=True)

_StreamT = TypeVar("_StreamT", bound=Stream[object])
_AsyncStreamT = TypeVar("_AsyncStreamT", bound=AsyncStream[object])

if TYPE_CHECKING:
    from httpx._config import (
        DEFAULT_TIMEOUT_CONFIG,  # pyright: ignore[reportPrivateImportUsage]
    )

    HTTPX_DEFAULT_TIMEOUT = DEFAULT_TIMEOUT_CONFIG
else:
    try:
        from httpx._config import DEFAULT_TIMEOUT_CONFIG as HTTPX_DEFAULT_TIMEOUT
    except ImportError:
        HTTPX_DEFAULT_TIMEOUT = Timeout(5.0)


class PageInfo:
    url: URL | NotGiven
    params: Query | NotGiven
    json: Body | NotGiven

    @overload
    def __init__(
        self,
        *,
        url: URL,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        params: Query,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        json: Body,
    ) -> None: ...

    def __init__(
        self,
        *,
        url: URL | NotGiven = not_given,
        json: Body | NotGiven = not_given,
        params: Query | NotGiven = not_given,
    ) -> None:
        self.url = url
        self.json = json
        self.params = params

    @override
    def __repr__(self) -> str:
        if self.url:
            return f"{self.__class__.__name__}(url={self.url})"
        if self.json:
            return f"{self.__class__.__name__}(json={self.json})"
        return f"{self.__class__.__name__}(params={self.params})"


class BasePage(GenericModel, Generic[_ItemT_co]):
    _options: FinalRequestOptions = PrivateAttr()
    _model: Type[object] = PrivateAttr()

    def has_next_page(self) -> bool:
        items = self._get_page_items()
        if not items:
            return False
        return self.next_page_info() is not None

    def next_page_info(self) -> Optional[PageInfo]: ...

    def _get_page_items(self) -> Iterable[_ItemT_co]:
        raise NotImplementedError("Page items unavailable. Implement _get_page_items in the page subclass.")

    def _params_from_url(self, url: URL) -> httpx.QueryParams:
        return httpx.QueryParams(_query_param_pairs(self._options.params)).merge(url.params)

    def _info_to_options(self, info: PageInfo) -> FinalRequestOptions:
        options = model_copy(self._options)
        options._strip_raw_response_header()

        if not isinstance(info.params, NotGiven):
            options.params = {**options.params, **info.params}
            return options

        if not isinstance(info.url, NotGiven):
            params = self._params_from_url(info.url)
            url = info.url.copy_with(params=params)
            options.params = dict(url.params)
            options.url = str(url)
            return options

        if not isinstance(info.json, NotGiven):
            if not is_mapping(info.json):
                raise TypeError("Pagination is only supported with mappings")

            json_data: object = options.json_data or {}
            if not is_mapping(json_data):
                raise TypeError("Pagination is only supported with mappings")
            options.json_data = {**json_data, **info.json}
            return options

        raise ValueError("Unexpected PageInfo state")


class BaseSyncPage(BasePage[_ItemT_co], Generic[_ItemT_co]):
    _client: SyncAPIClient = pydantic.PrivateAttr()

    def _set_private_attributes(
        self,
        client: SyncAPIClient,
        model: Type[object],
        options: FinalRequestOptions,
    ) -> None:
        if (not PYDANTIC_V1) and getattr(self, "__pydantic_private__", None) is None:
            self.__pydantic_private__ = {}

        self._model = model
        self._client = client
        self._options = options

    @override
    def __iter__(self) -> Iterator[_ItemT_co]:  # type: ignore
        for page in self.iter_pages():
            yield from page._get_page_items()

    def iter_pages(self: SyncPageT) -> Iterator[SyncPageT]:
        page = self
        while True:
            yield page
            if page.has_next_page():
                page = page.get_next_page()
            else:
                return

    def get_next_page(self: SyncPageT) -> SyncPageT:
        info = self.next_page_info()
        if not info:
            raise RuntimeError(
                "No next page expected; please check `.has_next_page()` before calling `.get_next_page()`."
            )

        options = self._info_to_options(info)
        return self._client._request_api_list(self._model, page=self.__class__, options=options)


class AsyncPaginator(Generic[_T, AsyncPageT]):
    def __init__(
        self,
        client: AsyncAPIClient,
        options: FinalRequestOptions,
        page_cls: Type[AsyncPageT],
        model: Type[_T],
    ) -> None:
        self._model = model
        self._client = client
        self._options = options
        self._page_cls = page_cls

    def __await__(self) -> Generator[object, None, AsyncPageT]:
        return self._get_page().__await__()

    async def _get_page(self) -> AsyncPageT:
        page_cls = self._page_cls

        def _parser(resp: object) -> object:
            if not isinstance(resp, page_cls):
                raise TypeError(f"Expected a {page_cls} page but received {type(resp)}")
            resp._set_private_attributes(
                model=self._model,
                options=self._options,
                client=self._client,
            )
            return resp

        self._options.post_parser = _parser

        return await self._client.request(self._page_cls, self._options)

    async def __aiter__(self) -> AsyncIterator[_T]:
        page = await self
        async for item in page:
            if not isinstance(item, self._model):
                raise TypeError(f"Expected a {self._model} page item but received {type(item)}")
            yield item


class BaseAsyncPage(BasePage[_ItemT_co], Generic[_ItemT_co]):
    _client: AsyncAPIClient = pydantic.PrivateAttr()

    def _set_private_attributes(
        self,
        model: Type[object],
        client: AsyncAPIClient,
        options: FinalRequestOptions,
    ) -> None:
        if (not PYDANTIC_V1) and getattr(self, "__pydantic_private__", None) is None:
            self.__pydantic_private__ = {}

        self._model = model
        self._client = client
        self._options = options

    async def __aiter__(self) -> AsyncIterator[_ItemT_co]:
        async for page in self.iter_pages():
            for item in page._get_page_items():
                yield item

    async def iter_pages(self: AsyncPageT) -> AsyncIterator[AsyncPageT]:
        page = self
        while True:
            yield page
            if page.has_next_page():
                page = await page.get_next_page()
            else:
                return

    async def get_next_page(self: AsyncPageT) -> AsyncPageT:
        info = self.next_page_info()
        if not info:
            raise RuntimeError(
                "No next page expected; please check `.has_next_page()` before calling `.get_next_page()`."
            )

        options = self._info_to_options(info)
        return await self._client._request_api_list(self._model, page=self.__class__, options=options)


_HttpxClientT = TypeVar("_HttpxClientT", bound=Union[httpx.Client, httpx.AsyncClient])
_DefaultStreamT = TypeVar("_DefaultStreamT", bound=Union[Stream[object], AsyncStream[object]])


class BaseClient(Generic[_HttpxClientT, _DefaultStreamT]):
    _client: _HttpxClientT
    _version: str
    _base_url: URL
    max_retries: int
    timeout: Union[float, Timeout, None]
    _strict_response_validation: bool
    _idempotency_header: str | None
    _default_stream_cls: type[_DefaultStreamT] | None = None

    def __init__(
        self,
        *,
        version: str,
        base_url: str | URL,
        _strict_response_validation: bool,
        max_retries: int = DEFAULT_MAX_RETRIES,
        timeout: float | Timeout | None = DEFAULT_TIMEOUT,
        custom_headers: Mapping[str, str] | None = None,
        custom_query: Mapping[str, object] | None = None,
    ) -> None:
        self._version = version
        self._base_url = self._enforce_trailing_slash(URL(base_url))
        self.max_retries = max_retries
        self.timeout = timeout
        self._custom_headers: Mapping[str, str] = custom_headers or {}
        self._custom_query: Mapping[str, object] = custom_query or {}
        self._strict_response_validation = _strict_response_validation
        self._idempotency_header = None
        self._platform: Platform | None = None

        if max_retries is None:  # pyright: ignore[reportUnnecessaryComparison]
            raise TypeError(
                "max_retries cannot be None. If you want to disable retries, pass `0`; if you want unlimited retries, pass `math.inf` or a very high number; if you want the default behavior, pass `x_twitter_scraper.DEFAULT_MAX_RETRIES`"
            )

    def _enforce_trailing_slash(self, url: URL) -> URL:
        if url.raw_path.endswith(b"/"):
            return url
        return url.copy_with(raw_path=url.raw_path + b"/")

    def _make_status_error_from_response(
        self,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.is_closed and not response.is_stream_consumed:
            body = None
            err_msg = f"Error code: {response.status_code}"
        else:
            err_text = response.text.strip()
            body = err_text

            try:
                body = json_loads(err_text)
                err_msg = f"Error code: {response.status_code} - {body}"
            except Exception:
                err_msg = err_text or f"Error code: {response.status_code}"

        return self._make_status_error(err_msg, body=body, response=response)

    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> _exceptions.APIStatusError:
        raise NotImplementedError()

    def _auth_headers(self, _security: SecurityOptions, /) -> dict[str, str]:
        return {}

    def _auth_query(self, _security: SecurityOptions, /) -> dict[str, str]:
        return {}

    def _custom_auth(self, _security: SecurityOptions, /) -> httpx.Auth | None:
        return None

    def _build_headers(self, options: FinalRequestOptions, *, retries_taken: int = 0) -> httpx.Headers:
        custom_headers = options.headers or {}
        headers_dict = _merge_mappings({**self._auth_headers(options.security), **self.default_headers}, custom_headers)
        self._validate_headers(headers_dict, custom_headers)

        headers = httpx.Headers(headers_dict)

        idempotency_header = self._idempotency_header
        if idempotency_header and options.idempotency_key and idempotency_header not in headers:
            headers[idempotency_header] = options.idempotency_key

        lower_custom_headers = [header.lower() for header in custom_headers]
        if "x-stainless-retry-count" not in lower_custom_headers:
            headers["x-stainless-retry-count"] = str(retries_taken)
        if "x-stainless-read-timeout" not in lower_custom_headers:
            timeout = self.timeout if isinstance(options.timeout, NotGiven) else options.timeout
            if isinstance(timeout, Timeout):
                timeout = timeout.read
            if timeout is not None:
                headers["x-stainless-read-timeout"] = str(timeout)

        return headers

    def _prepare_url(self, url: str) -> URL:
        merge_url = URL(url)
        if merge_url.is_relative_url:
            merge_raw_path = self.base_url.raw_path + merge_url.raw_path.lstrip(b"/")
            return self.base_url.copy_with(raw_path=merge_raw_path)

        return merge_url

    def _make_sse_decoder(self) -> SSEDecoder | SSEBytesDecoder:
        return SSEDecoder()

    def _build_request(
        self,
        options: FinalRequestOptions,
        *,
        retries_taken: int = 0,
    ) -> httpx.Request:
        if log.isEnabledFor(logging.DEBUG):
            log.debug(
                "Request options: %s",
                model_dump(
                    options,
                    exclude_unset=True,
                    exclude={
                        "content",
                    }
                    if PYDANTIC_V1
                    else {},
                ),
            )
        kwargs: dict[str, Any] = {}

        json_data = options.json_data
        if options.extra_json is not None:
            if json_data is None:
                json_data = cast(Body, options.extra_json)
            elif is_mapping(json_data):
                json_data = _merge_mappings(json_data, options.extra_json)
            else:
                raise RuntimeError(f"Unexpected JSON data type, {type(json_data)}, cannot merge with `extra_body`")

        headers = self._build_headers(options, retries_taken=retries_taken)
        params = _merge_mappings({**self._auth_query(options.security), **self.default_query}, options.params)
        content_type = get_header(headers, "Content-Type")
        files = options.files

        if content_type is not None and content_type.startswith("multipart/form-data"):
            if "boundary" not in content_type:
                headers.pop("Content-Type")

            if json_data:
                if not is_dict(json_data):
                    raise TypeError(
                        f"Expected query input to be a dictionary for multipart requests but got {type(json_data)} instead."
                    )
                kwargs["data"] = self._serialize_multipartform(json_data)

            # httpx sends multipart only when `files` is truthy.
            # https://github.com/encode/httpx/blob/0.28.1/httpx/_content.py#L211
            if not files:
                files = cast(HttpxRequestFiles, ForceMultipartDict())

        prepared_url = self._prepare_url(options.url)
        if params and prepared_url.query:
            existing = tuple((key, value) for key, value in prepared_url.params.multi_items() if key not in params)
            query = str(httpx.QueryParams(existing))
            extra = self.qs.stringify(params)
            prepared_url = prepared_url.copy_with(query="&".join(filter(None, (query, extra))).encode())
            params = {}
        if "_" in prepared_url.host:
            kwargs["extensions"] = {"sni_hostname": prepared_url.host.replace("_", "-")}

        is_body_allowed = options.method.lower() != "get"

        if is_body_allowed:
            if options.content is not None and json_data is not None:
                raise TypeError("Passing both `content` and `json_data` is not supported")
            if options.content is not None and files is not None:
                raise TypeError("Passing both `content` and `files` is not supported")
            if options.content is not None:
                kwargs["content"] = options.content
            elif isinstance(json_data, bytes):
                kwargs["content"] = json_data
            elif not files:
                kwargs["content"] = openapi_dumps(json_data) if is_given(json_data) and json_data is not None else None
            kwargs["files"] = files
        else:
            headers.pop("Content-Type", None)
            kwargs.pop("data", None)

        return self._client.build_request(  # pyright: ignore[reportUnknownMemberType]
            headers=headers,
            timeout=self.timeout if isinstance(options.timeout, NotGiven) else options.timeout,
            method=options.method,
            url=prepared_url,
            params=self.qs.stringify(params) if params else None,
            **kwargs,
        )

    def _serialize_multipartform(self, data: Mapping[object, object]) -> dict[str, object]:
        fields: dict[str, object] = {}
        for key, value in data.items():
            if not isinstance(key, str):
                raise TypeError("Multipart field names must be strings")
            fields[key] = value
        items = self.qs.stringify_items(fields, array_format="brackets")
        serialized: dict[str, list[str]] = {}
        for key, value in items:
            serialized.setdefault(key, []).append(value)
        return {key: values[0] if len(values) == 1 else values for key, values in serialized.items()}

    def _maybe_override_cast_to(self, cast_to: type[ResponseT], options: FinalRequestOptions) -> type[ResponseT]:
        if not is_given(options.headers):
            return cast_to

        headers = dict(options.headers)

        override_cast_to = headers.pop(OVERRIDE_CAST_TO_HEADER, not_given)
        if is_given(override_cast_to):
            options.headers = headers
            return cast(Type[ResponseT], override_cast_to)

        return cast_to

    def _should_stream_response_body(self, request: httpx.Request) -> bool:
        return bool(get_header(request.headers, RAW_RESPONSE_HEADER) == "stream")

    def _process_response_data(
        self,
        *,
        data: object,
        cast_to: type[ResponseT],
        response: httpx.Response,
    ) -> ResponseT:
        if data is None:
            return cast(ResponseT, None)

        if cast_to is object:
            return cast(ResponseT, data)

        try:
            origin = get_origin(cast_to) or cast_to
            if inspect.isclass(origin) and issubclass(origin, ModelBuilderProtocol):
                return cast(ResponseT, origin.build(response=response, data=data))

            if self._strict_response_validation:
                return validate_type(type_=cast_to, value=data)

            return cast(ResponseT, construct_type(type_=cast_to, value=data))
        except pydantic.ValidationError as err:
            raise APIResponseValidationError(response=response, body=data) from err

    @property
    def qs(self) -> Querystring:
        return Querystring()

    @property
    def custom_auth(self) -> httpx.Auth | None:
        return None

    @property
    def auth_headers(self) -> dict[str, str]:
        return {}

    @property
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": self.user_agent,
            **self.platform_headers(),
            **self._custom_headers,
        }

    @property
    def default_query(self) -> dict[str, object]:
        return {
            **self._custom_query,
        }

    def _validate_headers(self, _headers: Headers, _custom_headers: Headers, /) -> None:
        return

    @property
    def user_agent(self) -> str:
        return f"{self.__class__.__name__}/Python {self._version}"

    @property
    def base_url(self) -> URL:
        return self._base_url

    @base_url.setter
    def base_url(self, url: URL | str) -> None:
        self._base_url = self._enforce_trailing_slash(url if isinstance(url, URL) else URL(url))

    def platform_headers(self) -> Dict[str, str]:
        # A cache on a method keeps every instance alive.
        # https://github.com/python/cpython/issues/88476
        return platform_headers(self._version, platform=self._platform)

    def _parse_retry_after_header(self, response_headers: Optional[httpx.Headers] = None) -> float | None:
        if response_headers is None:
            return None

        for header, scale in (("retry-after-ms", 1000), ("retry-after", 1)):
            value = get_header(response_headers, header)
            if value is None:
                continue
            try:
                return float(value) / scale
            except ValueError:
                pass

        retry_date_tuple = email.utils.parsedate_tz(get_header(response_headers, "retry-after"))
        if retry_date_tuple is None:
            return None

        retry_date = email.utils.mktime_tz(retry_date_tuple)
        return float(retry_date - time.time())

    def _calculate_retry_timeout(
        self,
        remaining_retries: int,
        options: FinalRequestOptions,
        response_headers: Optional[httpx.Headers] = None,
    ) -> float:
        max_retries = options.get_max_retries(self.max_retries)

        retry_after = self._parse_retry_after_header(response_headers)
        if retry_after is not None and 0 < retry_after <= 60:
            return retry_after

        nb_retries = min(max_retries - remaining_retries, 1000)

        sleep_seconds = min(INITIAL_RETRY_DELAY * pow(2.0, nb_retries), MAX_RETRY_DELAY)

        jitter = 1 - 0.25 * random()
        timeout = sleep_seconds * jitter
        return timeout if timeout >= 0 else 0

    def _retry_delay(
        self, remaining_retries: int, options: FinalRequestOptions, response: httpx.Response | None
    ) -> float:
        if remaining_retries == 1:
            log.debug("1 retry left")
        else:
            log.debug("%i retries left", remaining_retries)

        timeout = self._calculate_retry_timeout(remaining_retries, options, response.headers if response else None)
        log.info("Retrying request to %s in %f seconds", options.url, timeout)

        return timeout

    def _should_retry(self, response: httpx.Response) -> bool:
        should_retry_header = get_header(response.headers, "x-should-retry")

        if should_retry_header == "true":
            log.debug("Retrying as header `x-should-retry` is set to `true`")
            return True
        if should_retry_header == "false":
            log.debug("Not retrying as header `x-should-retry` is set to `false`")
            return False

        if response.status_code in (408, 409, 429) or response.status_code >= 500:
            log.debug("Retrying due to status code %i", response.status_code)
            return True

        log.debug("Not retrying")
        return False

    def _idempotency_key(self) -> str:
        return f"stainless-python-retry-{uuid.uuid4()}"


class _DefaultHttpxClient(httpx.Client):
    def __init__(self, **kwargs: Any) -> None:
        kwargs.setdefault("timeout", DEFAULT_TIMEOUT)
        kwargs.setdefault("limits", DEFAULT_CONNECTION_LIMITS)
        kwargs.setdefault("follow_redirects", True)
        super().__init__(**kwargs)


if TYPE_CHECKING:
    DefaultHttpxClient = httpx.Client
    """An alias to `httpx.Client` that provides the same defaults that this SDK
    uses internally.
    """
else:
    DefaultHttpxClient = _DefaultHttpxClient


class SyncHttpxClientWrapper(DefaultHttpxClient):
    def __del__(self) -> None:
        if self.is_closed:
            return

        try:
            self.close()
        except Exception:
            pass


class SyncAPIClient(BaseClient[httpx.Client, Stream[object]]):
    _client: httpx.Client
    _default_stream_cls: type[Stream[object]] | None = None

    def __init__(
        self,
        *,
        version: str,
        base_url: str | URL,
        max_retries: int = DEFAULT_MAX_RETRIES,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        custom_headers: Mapping[str, str] | None = None,
        custom_query: Mapping[str, object] | None = None,
        _strict_response_validation: bool,
    ) -> None:
        if not is_given(timeout):
            if http_client and http_client.timeout != HTTPX_DEFAULT_TIMEOUT:
                timeout = http_client.timeout
            else:
                timeout = DEFAULT_TIMEOUT

        if http_client is not None and not isinstance(http_client, httpx.Client):  # pyright: ignore[reportUnnecessaryIsInstance]
            raise TypeError(
                f"Invalid `http_client` argument; Expected an instance of `httpx.Client` but got {type(http_client)}"
            )

        super().__init__(
            version=version,
            timeout=cast(Timeout, timeout),
            base_url=base_url,
            max_retries=max_retries,
            custom_query=custom_query,
            custom_headers=custom_headers,
            _strict_response_validation=_strict_response_validation,
        )
        self._client = http_client or SyncHttpxClientWrapper(
            base_url=base_url,
            timeout=cast(Timeout, timeout),
        )

    def is_closed(self) -> bool:
        return self._client.is_closed

    def close(self) -> None:
        """Close the underlying HTTPX client.

        The client will *not* be usable after this.
        """
        if hasattr(self, "_client"):
            self._client.close()

    def __enter__(self: _T) -> _T:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        self.close()

    def _prepare_options(
        self,
        options: FinalRequestOptions,
    ) -> FinalRequestOptions:
        return options

    def _prepare_request(self, _request: httpx.Request, /) -> None:
        return None

    @overload
    def request(
        self,
        cast_to: Type[ResponseT],
        options: FinalRequestOptions,
        *,
        stream: Literal[True],
        stream_cls: Type[_StreamT],
    ) -> _StreamT: ...

    @overload
    def request(
        self,
        cast_to: Type[ResponseT],
        options: FinalRequestOptions,
        *,
        stream: Literal[False] = False,
    ) -> ResponseT: ...

    @overload
    def request(
        self,
        cast_to: Type[ResponseT],
        options: FinalRequestOptions,
        *,
        stream: bool = False,
        stream_cls: Type[_StreamT] | None = None,
    ) -> ResponseT | _StreamT: ...

    def request(
        self,
        cast_to: Type[ResponseT],
        options: FinalRequestOptions,
        *,
        stream: bool = False,
        stream_cls: type[_StreamT] | None = None,
    ) -> ResponseT | _StreamT:
        cast_to = self._maybe_override_cast_to(cast_to, options)

        input_options = model_copy(options)
        if input_options.idempotency_key is None and input_options.method.lower() != "get":
            input_options.idempotency_key = self._idempotency_key()

        response: httpx.Response | None = None
        max_retries = input_options.get_max_retries(self.max_retries)

        retries_taken = 0
        for retries_taken in range(max_retries + 1):
            options = model_copy(input_options)
            options = self._prepare_options(options)

            remaining_retries = max_retries - retries_taken
            request = self._build_request(options, retries_taken=retries_taken)
            self._prepare_request(request)

            kwargs: HttpxSendArgs = {}
            custom_auth = self._custom_auth(options.security)
            if custom_auth is not None:
                kwargs["auth"] = custom_auth

            if options.follow_redirects is not None:
                kwargs["follow_redirects"] = options.follow_redirects

            log.debug("Sending HTTP Request: %s %s", request.method, request.url)

            response = None
            try:
                response = self._client.send(
                    request,
                    stream=stream or self._should_stream_response_body(request=request),
                    **kwargs,
                )
            except Exception as err:
                is_timeout = isinstance(err, httpx.TimeoutException)
                log.debug(
                    "Encountered httpx.TimeoutException" if is_timeout else "Encountered Exception", exc_info=True
                )
                if remaining_retries > 0:
                    self._sleep_for_retry(
                        retries_taken=retries_taken,
                        max_retries=max_retries,
                        options=input_options,
                        response=None,
                    )
                    continue

                log.debug("Raising timeout error" if is_timeout else "Raising connection error")
                error_type = APITimeoutError if is_timeout else APIConnectionError
                raise error_type(request=request) from err

            log.debug(
                'HTTP Response: %s %s "%i %s" %s',
                request.method,
                request.url,
                response.status_code,
                response.reason_phrase,
                response.headers,
            )

            try:
                response.raise_for_status()
            except httpx.HTTPStatusError as err:
                log.debug("Encountered httpx.HTTPStatusError", exc_info=True)

                if remaining_retries > 0 and self._should_retry(err.response):
                    err.response.close()
                    self._sleep_for_retry(
                        retries_taken=retries_taken,
                        max_retries=max_retries,
                        options=input_options,
                        response=response,
                    )
                    continue

                if not err.response.is_closed:
                    err.response.read()

                log.debug("Re-raising status error")
                raise self._make_status_error_from_response(err.response) from None

            break

        assert response is not None, "could not resolve response (should never happen)"
        return self._process_response(
            cast_to=cast_to,
            options=options,
            response=response,
            stream=stream,
            stream_cls=stream_cls,
            retries_taken=retries_taken,
        )

    def _sleep_for_retry(
        self, *, retries_taken: int, max_retries: int, options: FinalRequestOptions, response: httpx.Response | None
    ) -> None:
        time.sleep(self._retry_delay(max_retries - retries_taken, options, response))

    def _process_response(
        self,
        *,
        cast_to: Type[ResponseT],
        options: FinalRequestOptions,
        response: httpx.Response,
        stream: bool,
        stream_cls: type[Stream[object]] | type[AsyncStream[object]] | None,
        retries_taken: int = 0,
    ) -> ResponseT:
        origin = get_origin(cast_to) or cast_to
        custom_response = (
            inspect.isclass(origin)
            and issubclass(origin, BaseAPIResponse)
            and (not stream or bool(get_header(response.request.headers, RAW_RESPONSE_HEADER)))
        )
        if custom_response:
            if not issubclass(origin, APIResponse):
                raise TypeError(f"API Response types must subclass {APIResponse}; Received {origin}")
            response_cls = cast("type[APIResponse[ResponseT]]", cast_to)
            cast_to = cast("type[ResponseT]", extract_response_type(response_cls))
        elif cast_to == HttpxResponse:
            return cast(ResponseT, response)
        else:
            response_cls = APIResponse

        api_response = response_cls(
            raw=response,
            client=self,
            cast_to=cast_to,
            stream=stream,
            stream_cls=stream_cls,
            options=options,
            retries_taken=retries_taken,
        )
        if custom_response or bool(get_header(response.request.headers, RAW_RESPONSE_HEADER)):
            return cast(ResponseT, api_response)

        return api_response.parse()

    def _request_api_list(
        self,
        model: Type[object],
        page: Type[SyncPageT],
        options: FinalRequestOptions,
    ) -> SyncPageT:
        def _parser(resp: object) -> object:
            if not isinstance(resp, page):
                raise TypeError(f"Expected a {page} page but received {type(resp)}")
            resp._set_private_attributes(
                client=self,
                model=model,
                options=options,
            )
            return resp

        options.post_parser = _parser

        return self.request(page, options, stream=False)

    @overload
    def get(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        options: RequestOptions = {},
        stream: Literal[False] = False,
    ) -> ResponseT: ...

    @overload
    def get(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        options: RequestOptions = {},
        stream: Literal[True],
        stream_cls: type[_StreamT],
    ) -> _StreamT: ...

    @overload
    def get(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        options: RequestOptions = {},
        stream: bool,
        stream_cls: type[_StreamT] | None = None,
    ) -> ResponseT | _StreamT: ...

    def get(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        options: RequestOptions = {},
        stream: bool = False,
        stream_cls: type[_StreamT] | None = None,
    ) -> ResponseT | _StreamT:
        opts = FinalRequestOptions.construct(method="get", url=path, **options)
        return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))

    @overload
    def post(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        body: Body | None = None,
        content: BinaryTypes | None = None,
        options: RequestOptions = {},
        files: RequestFiles | None = None,
        stream: Literal[False] = False,
    ) -> ResponseT: ...

    @overload
    def post(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        body: Body | None = None,
        content: BinaryTypes | None = None,
        options: RequestOptions = {},
        files: RequestFiles | None = None,
        stream: Literal[True],
        stream_cls: type[_StreamT],
    ) -> _StreamT: ...

    @overload
    def post(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        body: Body | None = None,
        content: BinaryTypes | None = None,
        options: RequestOptions = {},
        files: RequestFiles | None = None,
        stream: bool,
        stream_cls: type[_StreamT] | None = None,
    ) -> ResponseT | _StreamT: ...

    def post(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        body: Body | None = None,
        content: BinaryTypes | None = None,
        options: RequestOptions = {},
        files: RequestFiles | None = None,
        stream: bool = False,
        stream_cls: type[_StreamT] | None = None,
    ) -> ResponseT | _StreamT:
        _validate_request_body(body, content, files)
        opts = FinalRequestOptions.construct(
            method="post", url=path, json_data=body, content=content, files=to_httpx_files(files), **options
        )
        return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))

    def patch(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        body: Body | None = None,
        content: BinaryTypes | None = None,
        files: RequestFiles | None = None,
        options: RequestOptions = {},
    ) -> ResponseT:
        _validate_request_body(body, content, files)
        opts = FinalRequestOptions.construct(
            method="patch", url=path, json_data=body, content=content, files=to_httpx_files(files), **options
        )
        return self.request(cast_to, opts)

    def put(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        body: Body | None = None,
        content: BinaryTypes | None = None,
        files: RequestFiles | None = None,
        options: RequestOptions = {},
    ) -> ResponseT:
        _validate_request_body(body, content, files)
        opts = FinalRequestOptions.construct(
            method="put", url=path, json_data=body, content=content, files=to_httpx_files(files), **options
        )
        return self.request(cast_to, opts)

    def delete(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        body: Body | None = None,
        content: BinaryTypes | None = None,
        options: RequestOptions = {},
    ) -> ResponseT:
        _validate_request_body(body, content)
        opts = FinalRequestOptions.construct(method="delete", url=path, json_data=body, content=content, **options)
        return self.request(cast_to, opts)

    def get_api_list(
        self,
        path: str,
        *,
        model: Type[object],
        page: Type[SyncPageT],
        body: Body | None = None,
        options: RequestOptions = {},
        method: str = "get",
    ) -> SyncPageT:
        opts = FinalRequestOptions.construct(method=method, url=path, json_data=body, **options)
        return self._request_api_list(model, page, opts)


class _DefaultAsyncHttpxClient(httpx.AsyncClient):
    def __init__(self, **kwargs: Any) -> None:
        kwargs.setdefault("timeout", DEFAULT_TIMEOUT)
        kwargs.setdefault("limits", DEFAULT_CONNECTION_LIMITS)
        kwargs.setdefault("follow_redirects", True)
        super().__init__(**kwargs)


try:
    import httpx_aiohttp
except ImportError:

    class _DefaultAioHttpClient(httpx.AsyncClient):
        def __init__(self, **_kwargs: Any) -> None:
            raise RuntimeError("To use the aiohttp client you must have installed the package with the `aiohttp` extra")
else:

    class _DefaultAioHttpClient(httpx_aiohttp.HttpxAiohttpClient):  # type: ignore
        def __init__(self, **kwargs: Any) -> None:
            kwargs.setdefault("timeout", DEFAULT_TIMEOUT)
            kwargs.setdefault("limits", DEFAULT_CONNECTION_LIMITS)
            kwargs.setdefault("follow_redirects", True)

            super().__init__(**kwargs)


if TYPE_CHECKING:
    DefaultAsyncHttpxClient = httpx.AsyncClient
    """An alias to `httpx.AsyncClient` that provides the same defaults that this SDK
    uses internally.
    """

    DefaultAioHttpClient = httpx.AsyncClient
    """An alias to `httpx.AsyncClient` that changes the default HTTP transport to `aiohttp`."""
else:
    DefaultAsyncHttpxClient = _DefaultAsyncHttpxClient
    DefaultAioHttpClient = _DefaultAioHttpClient


class AsyncHttpxClientWrapper(DefaultAsyncHttpxClient):
    def __del__(self) -> None:
        if self.is_closed:
            return

        try:
            asyncio.get_running_loop().create_task(self.aclose())
        except Exception:
            pass


class AsyncAPIClient(BaseClient[httpx.AsyncClient, AsyncStream[object]]):
    _client: httpx.AsyncClient
    _default_stream_cls: type[AsyncStream[object]] | None = None

    def __init__(
        self,
        *,
        version: str,
        base_url: str | URL,
        _strict_response_validation: bool,
        max_retries: int = DEFAULT_MAX_RETRIES,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        custom_headers: Mapping[str, str] | None = None,
        custom_query: Mapping[str, object] | None = None,
    ) -> None:
        if not is_given(timeout):
            if http_client and http_client.timeout != HTTPX_DEFAULT_TIMEOUT:
                timeout = http_client.timeout
            else:
                timeout = DEFAULT_TIMEOUT

        if http_client is not None and not isinstance(http_client, httpx.AsyncClient):  # pyright: ignore[reportUnnecessaryIsInstance]
            raise TypeError(
                f"Invalid `http_client` argument; Expected an instance of `httpx.AsyncClient` but got {type(http_client)}"
            )

        super().__init__(
            version=version,
            base_url=base_url,
            timeout=cast(Timeout, timeout),
            max_retries=max_retries,
            custom_query=custom_query,
            custom_headers=custom_headers,
            _strict_response_validation=_strict_response_validation,
        )
        self._client = http_client or AsyncHttpxClientWrapper(
            base_url=base_url,
            timeout=cast(Timeout, timeout),
        )

    def is_closed(self) -> bool:
        return self._client.is_closed

    async def close(self) -> None:
        """Close the underlying HTTPX client.

        The client will *not* be usable after this.
        """
        await self._client.aclose()

    async def __aenter__(self: _T) -> _T:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.close()

    async def _prepare_options(
        self,
        options: FinalRequestOptions,
    ) -> FinalRequestOptions:
        return options

    async def _prepare_request(self, _request: httpx.Request, /) -> None:
        return None

    @overload
    async def request(
        self,
        cast_to: Type[ResponseT],
        options: FinalRequestOptions,
        *,
        stream: Literal[False] = False,
    ) -> ResponseT: ...

    @overload
    async def request(
        self,
        cast_to: Type[ResponseT],
        options: FinalRequestOptions,
        *,
        stream: Literal[True],
        stream_cls: type[_AsyncStreamT],
    ) -> _AsyncStreamT: ...

    @overload
    async def request(
        self,
        cast_to: Type[ResponseT],
        options: FinalRequestOptions,
        *,
        stream: bool,
        stream_cls: type[_AsyncStreamT] | None = None,
    ) -> ResponseT | _AsyncStreamT: ...

    async def request(
        self,
        cast_to: Type[ResponseT],
        options: FinalRequestOptions,
        *,
        stream: bool = False,
        stream_cls: type[_AsyncStreamT] | None = None,
    ) -> ResponseT | _AsyncStreamT:
        if self._platform is None:
            self._platform = await asyncify(get_platform)()

        cast_to = self._maybe_override_cast_to(cast_to, options)

        input_options = model_copy(options)
        if input_options.idempotency_key is None and input_options.method.lower() != "get":
            input_options.idempotency_key = self._idempotency_key()

        response: httpx.Response | None = None
        max_retries = input_options.get_max_retries(self.max_retries)

        retries_taken = 0
        for retries_taken in range(max_retries + 1):
            options = model_copy(input_options)
            options = await self._prepare_options(options)

            remaining_retries = max_retries - retries_taken
            request = self._build_request(options, retries_taken=retries_taken)
            await self._prepare_request(request)

            kwargs: HttpxSendArgs = {}
            if self.custom_auth is not None:
                kwargs["auth"] = self.custom_auth

            if options.follow_redirects is not None:
                kwargs["follow_redirects"] = options.follow_redirects

            log.debug("Sending HTTP Request: %s %s", request.method, request.url)

            response = None
            try:
                response = await self._client.send(
                    request,
                    stream=stream or self._should_stream_response_body(request=request),
                    **kwargs,
                )
            except Exception as err:
                is_timeout = isinstance(err, httpx.TimeoutException)
                log.debug(
                    "Encountered httpx.TimeoutException" if is_timeout else "Encountered Exception", exc_info=True
                )
                if remaining_retries > 0:
                    await self._sleep_for_retry(
                        retries_taken=retries_taken,
                        max_retries=max_retries,
                        options=input_options,
                        response=None,
                    )
                    continue

                log.debug("Raising timeout error" if is_timeout else "Raising connection error")
                error_type = APITimeoutError if is_timeout else APIConnectionError
                raise error_type(request=request) from err

            log.debug(
                'HTTP Response: %s %s "%i %s" %s',
                request.method,
                request.url,
                response.status_code,
                response.reason_phrase,
                response.headers,
            )

            try:
                response.raise_for_status()
            except httpx.HTTPStatusError as err:
                log.debug("Encountered httpx.HTTPStatusError", exc_info=True)

                if remaining_retries > 0 and self._should_retry(err.response):
                    await err.response.aclose()
                    await self._sleep_for_retry(
                        retries_taken=retries_taken,
                        max_retries=max_retries,
                        options=input_options,
                        response=response,
                    )
                    continue

                if not err.response.is_closed:
                    await err.response.aread()

                log.debug("Re-raising status error")
                raise self._make_status_error_from_response(err.response) from None

            break

        assert response is not None, "could not resolve response (should never happen)"
        return await self._process_response(
            cast_to=cast_to,
            options=options,
            response=response,
            stream=stream,
            stream_cls=stream_cls,
            retries_taken=retries_taken,
        )

    async def _sleep_for_retry(
        self, *, retries_taken: int, max_retries: int, options: FinalRequestOptions, response: httpx.Response | None
    ) -> None:
        await anyio.sleep(self._retry_delay(max_retries - retries_taken, options, response))

    async def _process_response(
        self,
        *,
        cast_to: Type[ResponseT],
        options: FinalRequestOptions,
        response: httpx.Response,
        stream: bool,
        stream_cls: type[Stream[object]] | type[AsyncStream[object]] | None,
        retries_taken: int = 0,
    ) -> ResponseT:
        origin = get_origin(cast_to) or cast_to
        custom_response = (
            inspect.isclass(origin)
            and issubclass(origin, BaseAPIResponse)
            and (not stream or bool(get_header(response.request.headers, RAW_RESPONSE_HEADER)))
        )
        if custom_response:
            if not issubclass(origin, AsyncAPIResponse):
                raise TypeError(f"API Response types must subclass {AsyncAPIResponse}; Received {origin}")
            response_cls = cast("type[AsyncAPIResponse[ResponseT]]", cast_to)
            cast_to = cast("type[ResponseT]", extract_response_type(response_cls))
        elif cast_to == HttpxResponse:
            return cast(ResponseT, response)
        else:
            response_cls = AsyncAPIResponse

        api_response = response_cls(
            raw=response,
            client=self,
            cast_to=cast_to,
            stream=stream,
            stream_cls=stream_cls,
            options=options,
            retries_taken=retries_taken,
        )
        if custom_response or bool(get_header(response.request.headers, RAW_RESPONSE_HEADER)):
            return cast(ResponseT, api_response)

        return await api_response.parse()

    def _request_api_list(
        self,
        model: Type[_T],
        page: Type[AsyncPageT],
        options: FinalRequestOptions,
    ) -> AsyncPaginator[_T, AsyncPageT]:
        return AsyncPaginator(client=self, options=options, page_cls=page, model=model)

    @overload
    async def get(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        options: RequestOptions = {},
        stream: Literal[False] = False,
    ) -> ResponseT: ...

    @overload
    async def get(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        options: RequestOptions = {},
        stream: Literal[True],
        stream_cls: type[_AsyncStreamT],
    ) -> _AsyncStreamT: ...

    @overload
    async def get(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        options: RequestOptions = {},
        stream: bool,
        stream_cls: type[_AsyncStreamT] | None = None,
    ) -> ResponseT | _AsyncStreamT: ...

    async def get(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        options: RequestOptions = {},
        stream: bool = False,
        stream_cls: type[_AsyncStreamT] | None = None,
    ) -> ResponseT | _AsyncStreamT:
        opts = FinalRequestOptions.construct(method="get", url=path, **options)
        return await self.request(cast_to, opts, stream=stream, stream_cls=stream_cls)

    @overload
    async def post(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        body: Body | None = None,
        content: AsyncBinaryTypes | None = None,
        files: RequestFiles | None = None,
        options: RequestOptions = {},
        stream: Literal[False] = False,
    ) -> ResponseT: ...

    @overload
    async def post(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        body: Body | None = None,
        content: AsyncBinaryTypes | None = None,
        files: RequestFiles | None = None,
        options: RequestOptions = {},
        stream: Literal[True],
        stream_cls: type[_AsyncStreamT],
    ) -> _AsyncStreamT: ...

    @overload
    async def post(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        body: Body | None = None,
        content: AsyncBinaryTypes | None = None,
        files: RequestFiles | None = None,
        options: RequestOptions = {},
        stream: bool,
        stream_cls: type[_AsyncStreamT] | None = None,
    ) -> ResponseT | _AsyncStreamT: ...

    async def post(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        body: Body | None = None,
        content: AsyncBinaryTypes | None = None,
        files: RequestFiles | None = None,
        options: RequestOptions = {},
        stream: bool = False,
        stream_cls: type[_AsyncStreamT] | None = None,
    ) -> ResponseT | _AsyncStreamT:
        _validate_request_body(body, content, files)
        opts = FinalRequestOptions.construct(
            method="post", url=path, json_data=body, content=content, files=await async_to_httpx_files(files), **options
        )
        return await self.request(cast_to, opts, stream=stream, stream_cls=stream_cls)

    async def patch(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        body: Body | None = None,
        content: AsyncBinaryTypes | None = None,
        files: RequestFiles | None = None,
        options: RequestOptions = {},
    ) -> ResponseT:
        _validate_request_body(body, content, files)
        opts = FinalRequestOptions.construct(
            method="patch",
            url=path,
            json_data=body,
            content=content,
            files=await async_to_httpx_files(files),
            **options,
        )
        return await self.request(cast_to, opts)

    async def put(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        body: Body | None = None,
        content: AsyncBinaryTypes | None = None,
        files: RequestFiles | None = None,
        options: RequestOptions = {},
    ) -> ResponseT:
        _validate_request_body(body, content, files)
        opts = FinalRequestOptions.construct(
            method="put", url=path, json_data=body, content=content, files=await async_to_httpx_files(files), **options
        )
        return await self.request(cast_to, opts)

    async def delete(
        self,
        path: str,
        *,
        cast_to: Type[ResponseT],
        body: Body | None = None,
        content: AsyncBinaryTypes | None = None,
        options: RequestOptions = {},
    ) -> ResponseT:
        _validate_request_body(body, content)
        opts = FinalRequestOptions.construct(method="delete", url=path, json_data=body, content=content, **options)
        return await self.request(cast_to, opts)

    def get_api_list(
        self,
        path: str,
        *,
        model: Type[_T],
        page: Type[AsyncPageT],
        body: Body | None = None,
        options: RequestOptions = {},
        method: str = "get",
    ) -> AsyncPaginator[_T, AsyncPageT]:
        opts = FinalRequestOptions.construct(method=method, url=path, json_data=body, **options)
        return self._request_api_list(model, page, opts)


def _validate_request_body(
    body: Body | None, content: BinaryTypes | AsyncBinaryTypes | None, files: RequestFiles | None = None
) -> None:
    if body is not None and content is not None:
        raise TypeError("Passing both `body` and `content` is not supported")
    if files is not None and content is not None:
        raise TypeError("Passing both `files` and `content` is not supported")
    if isinstance(body, bytes):
        warnings.warn(
            "Passing raw bytes as `body` is deprecated and will be removed in a future version. "
            "Please pass raw bytes via the `content` parameter instead.",
            DeprecationWarning,
            stacklevel=3,
        )


def make_request_options(
    *,
    query: Query | None = None,
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    idempotency_key: str | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = not_given,
    post_parser: PostParser | NotGiven = not_given,
    security: SecurityOptions | None = None,
) -> RequestOptions:
    options: RequestOptions = {}
    if extra_headers is not None:
        options["headers"] = extra_headers

    if extra_body is not None:
        options["extra_json"] = cast(AnyMapping, extra_body)

    if query is not None:
        options["params"] = query

    if extra_query is not None:
        options["params"] = {**options.get("params", {}), **extra_query}

    if not isinstance(timeout, NotGiven):
        options["timeout"] = timeout

    if idempotency_key is not None:
        options["idempotency_key"] = idempotency_key

    if is_given(post_parser):
        options["post_parser"] = post_parser

    if security is not None:
        options["security"] = security

    return options


class ForceMultipartDict(Dict[str, None]):
    def __bool__(self) -> bool:
        return True


class OtherPlatform:
    def __init__(self, name: str) -> None:
        self.name = name

    @override
    def __str__(self) -> str:
        return f"Other:{self.name}"


Platform = Union[
    OtherPlatform,
    Literal[
        "MacOS",
        "Linux",
        "Windows",
        "FreeBSD",
        "OpenBSD",
        "iOS",
        "Android",
        "Unknown",
    ],
]


def get_platform() -> Platform:
    try:
        system = platform.system().lower()
        platform_name = platform.platform().lower()
    except Exception:
        return "Unknown"

    if "iphone" in platform_name or "ipad" in platform_name:
        return "iOS"

    if system == "darwin":
        return "MacOS"

    if system == "windows":
        return "Windows"

    if "android" in platform_name:
        return "Android"

    if system == "linux":
        distro_id = distro.id()
        if distro_id == "freebsd":
            return "FreeBSD"

        if distro_id == "openbsd":
            return "OpenBSD"

        return "Linux"

    if platform_name:
        return OtherPlatform(platform_name)

    return "Unknown"


@memoize
def platform_headers(version: str, *, platform: Platform | None) -> Dict[str, str]:
    return {
        "X-Xquik-SDK": "python",
        "X-Stainless-Lang": "python",
        "X-Stainless-Package-Version": version,
        "X-Stainless-OS": str(platform or get_platform()),
        "X-Stainless-Arch": str(get_architecture()),
        "X-Stainless-Runtime": get_python_runtime(),
        "X-Stainless-Runtime-Version": get_python_version(),
    }


class OtherArch:
    def __init__(self, name: str) -> None:
        self.name = name

    @override
    def __str__(self) -> str:
        return f"other:{self.name}"


Arch = Union[OtherArch, Literal["x32", "x64", "arm", "arm64", "unknown"]]


def get_python_runtime() -> str:
    try:
        return platform.python_implementation()
    except Exception:
        return "unknown"


def get_python_version() -> str:
    try:
        return platform.python_version()
    except Exception:
        return "unknown"


def get_architecture() -> Arch:
    try:
        machine = platform.machine().lower()
    except Exception:
        return "unknown"

    if machine in ("arm64", "aarch64"):
        return "arm64"

    if machine == "arm":
        return "arm"

    if machine == "x86_64":
        return "x64"

    if sys.maxsize <= 2**32:
        return "x32"

    if machine:
        return OtherArch(machine)

    return "unknown"


def _merge_mappings(
    obj1: Mapping[_T_co, Union[_T, Omit]],
    obj2: Mapping[_T_co, Union[_T, Omit]],
) -> Dict[_T_co, _T]:
    merged = {**obj1, **obj2}
    return {key: value for key, value in merged.items() if not isinstance(value, Omit)}


_QueryValue = Union[str, int, float, bool, None]


def _query_param_pairs(params: Mapping[str, object]) -> list[tuple[str, _QueryValue]]:
    pairs: list[tuple[str, _QueryValue]] = []
    for key, value in params.items():
        values: Iterable[object] = value if is_list(value) or is_tuple(value) else (value,)
        for item in values:
            if item is not None and not isinstance(item, (str, int, float, bool)):
                raise TypeError(f"Expected a primitive query value for {key!r} but received {type(item)}")
            pairs.append((key, item))
    return pairs
