# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("x_twitter_scraper.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
