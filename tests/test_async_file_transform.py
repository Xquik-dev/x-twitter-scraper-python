# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

import io
import threading
from typing_extensions import Annotated, TypedDict, override

import pytest

from x_twitter_scraper._utils import PropertyInfo, async_transform

EncodedFile = Annotated[io.BytesIO, PropertyInfo(format="base64")]


class FileInput(TypedDict):
    file: EncodedFile


@pytest.mark.asyncio
@pytest.mark.parametrize("expected_type", [FileInput, dict[str, EncodedFile]])
@pytest.mark.parametrize("fail", [False, True])
async def test_file_reads_run_outside_event_loop(expected_type: object, fail: bool) -> None:
    reader_threads: list[int] = []
    event_loop_thread = threading.get_ident()

    class RecordingFile(io.BytesIO):
        @override
        def read(self, size: int | None = -1) -> bytes:
            reader_threads.append(threading.get_ident())
            if fail:
                raise OSError("File read failed")
            return super().read(size)

    with RecordingFile(b"hello") as file:
        if fail:
            with pytest.raises(OSError, match="File read failed"):
                await async_transform({"file": file}, expected_type)
        else:
            result: object = await async_transform({"file": file}, expected_type)
            assert result == {"file": "aGVsbG8="}
        assert not file.closed
    assert len(reader_threads) == 1
    assert reader_threads[0] != event_loop_thread
