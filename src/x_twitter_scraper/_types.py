# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from os import PathLike
from typing import (
    IO,
    TYPE_CHECKING,
    Dict,
    List,
    Type,
    Tuple,
    Union,
    Mapping,
    TypeVar,
    Callable,
    Iterable,
    Iterator,
    Optional,
    Sequence,
    AsyncIterable,
)
from typing_extensions import (
    Set,
    Literal,
    Protocol,
    TypeAlias,
    TypedDict,
    SupportsIndex,
    overload,
    override,
    runtime_checkable,
)

import httpx
import pydantic
from httpx import URL, Proxy, Timeout as Timeout, Response, BaseTransport, AsyncBaseTransport

if TYPE_CHECKING:
    from ._models import SecurityOptions

Transport = BaseTransport
AsyncTransport = AsyncBaseTransport
Query = Mapping[str, object]
Body = object
AnyMapping = Mapping[str, object]
ModelT = TypeVar("ModelT", bound=pydantic.BaseModel)
_T = TypeVar("_T")

ArrayFormat = Literal["comma", "repeat", "indices", "brackets"]
NestedFormat = Literal["dots", "brackets"]


ProxiesDict = Dict["str | URL", Union[None, str, URL, Proxy]]
ProxiesTypes = Union[str, Proxy, ProxiesDict]
Base64FileInput = Union[IO[bytes], PathLike[str]]
FileContent = Union[IO[bytes], bytes, PathLike[str]]


BinaryTypes = Union[bytes, bytearray, IO[bytes], Iterable[bytes]]
AsyncBinaryTypes = Union[bytes, bytearray, IO[bytes], AsyncIterable[bytes]]

FileTypes = Union[
    FileContent,
    Tuple[Optional[str], FileContent],
    Tuple[Optional[str], FileContent, Optional[str]],
    Tuple[Optional[str], FileContent, Optional[str], Mapping[str, str]],
]
RequestFiles = Union[Mapping[str, FileTypes], Sequence[Tuple[str, FileTypes]]]

HttpxFileContent = Union[IO[bytes], bytes]
HttpxFileTypes = Union[
    HttpxFileContent,
    Tuple[Optional[str], HttpxFileContent],
    Tuple[Optional[str], HttpxFileContent, Optional[str]],
    Tuple[Optional[str], HttpxFileContent, Optional[str], Mapping[str, str]],
]
HttpxRequestFiles = Union[Mapping[str, HttpxFileTypes], Sequence[Tuple[str, HttpxFileTypes]]]

if TYPE_CHECKING:
    NoneType: Type[None]
else:
    NoneType = type(None)


class RequestOptions(TypedDict, total=False):
    headers: Headers
    max_retries: int
    timeout: float | Timeout | None
    params: Query
    extra_json: AnyMapping
    idempotency_key: str
    follow_redirects: bool
    post_parser: PostParser
    security: SecurityOptions


class NotGiven:
    """
    Distinguishes a parameter the user did not pass from an explicit None.

    User code shouldn't need to use not_given directly.

    For example:

    ```py
    def create(timeout: Timeout | None | NotGiven = not_given): ...


    create(timeout=1)  # 1s timeout
    create(timeout=None)  # No timeout
    create()  # Default timeout behavior
    ```
    """

    def __bool__(self) -> Literal[False]:
        return False

    @override
    def __repr__(self) -> str:
        return "NOT_GIVEN"


not_given = NotGiven()
NOT_GIVEN = NotGiven()


class Omit:
    """
    To explicitly omit something from being sent in a request, use `omit`.

    ```py
    client.post(..., headers={"Content-Type": omit})
    ```
    """

    def __bool__(self) -> Literal[False]:
        return False


omit = Omit()


@runtime_checkable
class ModelBuilderProtocol(Protocol):
    @classmethod
    def build(
        cls: type[_T],
        *,
        response: Response,
        data: object,
    ) -> _T: ...


Headers = Mapping[str, Union[str, Omit]]


class HeadersLikeProtocol(Protocol):
    def get(self, __key: str) -> str | None: ...


HeadersLike = Union[Headers, HeadersLikeProtocol]

ResponseT = TypeVar("ResponseT")

StrBytesIntFloat = Union[str, bytes, int, float]

JsonValue: TypeAlias = Union[str, int, float, bool, List["JsonValue"], Dict[str, "JsonValue"], None]

IncEx: TypeAlias = Union[Set[int], Set[str], Mapping[int, Union["IncEx", bool]], Mapping[str, Union["IncEx", bool]]]

PostParser = Callable[[object], object]


class HttpxSendArgs(TypedDict, total=False, closed=True):
    auth: httpx.Auth
    follow_redirects: bool


_T_co = TypeVar("_T_co", covariant=True)


if TYPE_CHECKING:
    # str fails this protocol because its __contains__ accepts only str.
    # https://github.com/hauntsaninja/useful_types/blob/5e9710f3875107d068e7679fd7fec9cfab0eff3b/useful_types/__init__.py#L285
    class SequenceNotStr(Protocol[_T_co]):
        @overload
        def __getitem__(self, index: SupportsIndex, /) -> _T_co: ...
        @overload
        def __getitem__(self, index: slice, /) -> Sequence[_T_co]: ...
        def __contains__(self, value: object, /) -> bool: ...
        def __len__(self) -> int: ...
        def __iter__(self) -> Iterator[_T_co]: ...
        def __reversed__(self) -> Iterator[_T_co]: ...
else:
    SequenceNotStr = Sequence
