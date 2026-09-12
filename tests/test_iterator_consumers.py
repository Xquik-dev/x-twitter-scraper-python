# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from contextlib import nullcontext
from collections.abc import Iterator, AsyncIterator

import pytest

from x_twitter_scraper._utils._streams import consume_sync_iterator, consume_async_iterator


@pytest.mark.parametrize("use_async", [False, True])
@pytest.mark.parametrize("values", [[], [1, 2]])
@pytest.mark.parametrize("fail", [False, True])
async def test_iterator_consumers(use_async: bool, values: list[int], fail: bool) -> None:
    consumed: list[int] = []

    def source() -> Iterator[int]:
        for value in values:
            consumed.append(value)
            yield value
        if fail:
            raise ValueError("Source failed")

    async def async_source() -> AsyncIterator[int]:
        for value in source():
            yield value

    with pytest.raises(ValueError, match="Source failed") if fail else nullcontext():
        result = await consume_async_iterator(async_source()) if use_async else consume_sync_iterator(source())
        assert result is None
    assert consumed == values
