# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from typing_extensions import Iterator, AsyncIterator


def consume_sync_iterator(iterator: Iterator[object]) -> None:
    for _ in iterator:
        ...


async def consume_async_iterator(iterator: AsyncIterator[object]) -> None:
    async for _ in iterator:
        ...
