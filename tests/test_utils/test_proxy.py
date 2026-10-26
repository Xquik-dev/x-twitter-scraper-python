# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing_extensions import NoReturn, override

from tests.utils import get_attribute
from x_twitter_scraper._utils import LazyProxy


class RecursiveLazyProxy(LazyProxy["RecursiveLazyProxy"]):
    @override
    def __load__(self) -> "RecursiveLazyProxy":
        return self

    def __call__(self, *_args: object, **_kwds: object) -> NoReturn:
        raise RuntimeError("This should never be called!")


def test_recursive_proxy() -> None:
    proxy = RecursiveLazyProxy()
    assert repr(proxy) == "RecursiveLazyProxy"
    assert str(proxy) == "RecursiveLazyProxy"
    assert dir(proxy) == []
    assert type(proxy).__name__ == "RecursiveLazyProxy"
    value: object = proxy
    for name in ("name", "foo", "bar", "baz"):
        value = get_attribute(value, name)
    assert type(value).__name__ == "RecursiveLazyProxy"


def test_isinstance_does_not_error() -> None:
    class AlwaysErrorProxy(LazyProxy[object]):
        @override
        def __load__(self) -> object:
            raise RuntimeError("Mocking missing dependency")

    proxy = AlwaysErrorProxy()
    assert not isinstance(proxy, dict)
    assert isinstance(proxy, LazyProxy)


def test_proxy_forwards_to_loaded_object() -> None:
    class DictProxy(LazyProxy[dict[str, int]]):
        @override
        def __load__(self) -> dict[str, int]:
            return {"answer": 42}

    proxy = DictProxy()
    assert callable(proxy.keys)
    assert repr(proxy) == "{'answer': 42}"
    assert str(proxy) == "{'answer': 42}"
    assert "keys" in dir(proxy)
    proxied_class: object = proxy.__class__
    assert proxied_class is dict
    assert proxy.__get_proxied__() == {"answer": 42}
    assert proxy.__as_proxied__() is proxy


def test_repr_loads_once() -> None:
    values = iter(["first", "second"])

    class ChangingProxy(LazyProxy[str]):
        @override
        def __load__(self) -> str:
            return next(values)

    proxy = ChangingProxy()
    assert repr(proxy) == "'first'"
    assert repr(proxy) == "'second'"
