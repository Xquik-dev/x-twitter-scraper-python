from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `x_twitter_scraper.resources` module.

    This is used so that we can lazily import `x_twitter_scraper.resources` only when
    needed *and* so that users can just import `x_twitter_scraper` and reference `x_twitter_scraper.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("x_twitter_scraper.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
