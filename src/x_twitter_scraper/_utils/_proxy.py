# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Callable, Iterable
from typing_extensions import Self, override

T = TypeVar("T")

# The builtin getattr returns Any, and an attribute of an unknown object is an unknown object. https://docs.python.org/3/library/functions.html#getattr
_get_attribute: Callable[[object, str], object] = getattr


class LazyProxy(Generic[T], ABC):
    def __getattr__(self, attr: str) -> object:
        proxied = self.__get_proxied__()
        if issubclass(type(proxied), LazyProxy):
            return proxied
        return _get_attribute(proxied, attr)

    @override
    def __repr__(self) -> str:
        proxied = self.__get_proxied__()
        if isinstance(proxied, LazyProxy):
            return proxied.__class__.__name__
        return repr(proxied)

    @override
    def __str__(self) -> str:
        proxied = self.__get_proxied__()
        if isinstance(proxied, LazyProxy):
            return proxied.__class__.__name__
        return str(proxied)

    @override
    def __dir__(self) -> Iterable[str]:
        proxied = self.__get_proxied__()
        if isinstance(proxied, LazyProxy):
            return list[str]()
        return proxied.__dir__()

    @property
    @override
    def __class__(self) -> type:
        try:
            proxied = self.__get_proxied__()
        except Exception:
            return type(self)
        if issubclass(type(proxied), LazyProxy):
            return type(proxied)
        return proxied.__class__

    @__class__.setter
    def __class__(self, value: type) -> None:
        raise AttributeError(f"cannot set __class__ of {type(self).__name__} to {value.__name__}")

    def __get_proxied__(self) -> T:
        return self.__load__()

    def __as_proxied__(self) -> Self:
        return self

    @abstractmethod
    def __load__(self) -> T: ...
