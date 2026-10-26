# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from types import ModuleType
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[ModuleType]):
    @override
    def __load__(self) -> ModuleType:
        import importlib

        mod = importlib.import_module("x_twitter_scraper.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
