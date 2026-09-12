# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

import io
import os
from copy import deepcopy
from typing import cast
from pathlib import Path
from typing_extensions import override

import anyio
import pytest
from dirty_equals import IsDict, IsList, IsBytes, IsTuple

from x_twitter_scraper._files import (
    to_httpx_files,
    read_file_content,
    deepcopy_with_paths,
    async_to_httpx_files,
    assert_is_file_content,
    async_read_file_content,
)
from x_twitter_scraper._types import FileContent, RequestFiles
from x_twitter_scraper._utils import extract_files


class BytesPath(os.PathLike[bytes]):
    @override
    def __fspath__(self) -> bytes:
        return b"invalid-byte-path"


readme_path = Path(__file__).parent.parent.joinpath("README.md")


@pytest.mark.parametrize("use_async", [False, True], ids=["sync", "async"])
@pytest.mark.parametrize(
    "files, expected",
    [
        ({"file": readme_path}, IsDict({"file": IsTuple("README.md", IsBytes())})),
        ({"file": anyio.Path(readme_path)}, IsDict({"file": IsTuple("README.md", IsBytes())})),
        ([("file", readme_path)], IsList(IsTuple("file", IsTuple("README.md", IsBytes())))),
        (None, None),
        ({"f": (None, b"x")}, {"f": (None, b"x")}),
        ({"f": ("x", b"x", "text/plain", {"x": "y"})}, {"f": ("x", b"x", "text/plain", {"x": "y"})}),
        ({"file": b"contents"}, {"file": b"contents"}),
        (
            {"file": ("custom.md", readme_path, "text/markdown")},
            IsDict({"file": IsTuple("custom.md", IsBytes(), "text/markdown")}),
        ),
    ],
    ids=["path", "anyio-path", "sequence", "none", "unnamed-tuple", "headers-tuple", "bytes", "named-tuple"],
)
@pytest.mark.asyncio
async def test_upload_files(files: RequestFiles | None, expected: object, use_async: bool) -> None:
    result = await async_to_httpx_files(files) if use_async else to_httpx_files(files)
    print(result)
    if expected is None:
        assert result is None
    else:
        assert result == expected


@pytest.mark.parametrize("use_async", [False, True], ids=["sync", "async"])
@pytest.mark.parametrize(
    "files, error",
    [
        ("invalid", "Unexpected file type input"),
        ({"file": BytesPath()}, "File paths must resolve to strings"),
        ({"file": "foo"}, "Expected file types input to be a FileContent type or to be a tuple"),
    ],
    ids=["container", "byte-path", "content"],
)
@pytest.mark.asyncio
async def test_invalid_upload_files(files: object, error: str, use_async: bool) -> None:
    with pytest.raises(TypeError, match=error):
        if use_async:
            await async_to_httpx_files(cast(RequestFiles, files))
        else:
            to_httpx_files(cast(RequestFiles, files))


@pytest.mark.parametrize("use_async", [False, True], ids=["sync", "async"])
@pytest.mark.parametrize("file, expected", [(b"contents", b"contents"), (readme_path, readme_path.read_bytes())])
@pytest.mark.asyncio
async def test_read_file_content(file: FileContent, expected: bytes, use_async: bool) -> None:
    result = await async_read_file_content(file) if use_async else read_file_content(file)
    assert result == expected


def test_accepts_file_content() -> None:
    assert_is_file_content(io.BytesIO(b"contents"))


@pytest.mark.parametrize("key, error", [(None, "Expected file input"), ("upload", "Expected entry at `upload`")])
def test_invalid_file_content(key: str | None, error: str) -> None:
    with pytest.raises(RuntimeError, match=error):
        assert_is_file_content("invalid", key=key)


def assert_different_identities(obj1: object, obj2: object) -> None:
    assert obj1 == obj2
    assert obj1 is not obj2


class TestDeepcopyWithPaths:
    @pytest.mark.parametrize(
        "original, paths",
        [
            ({"file": b"data", "other": "value"}, [["file"]]),
            ({"file": b"contents"}, [["file"]]),
            ({"a": b"file1", "b": b"file2", "c": "unchanged"}, [["a"], ["b"]]),
            ({"foo": {"bar": 1}}, [["foo"]]),
            ({"foo": [{"bar": 1}]}, [["foo", "bar"]]),
            ({"foo": "bar"}, [["missing", "file"]]),
        ],
        ids=["top-level", "file-reference", "multiple-paths", "nested-dict", "list-without-array", "missing-key"],
    )
    def test_copies_mapping_preserving_values(self, original: dict[str, object], paths: list[list[str]]) -> None:
        result = deepcopy_with_paths(original, paths)
        assert_different_identities(result, original)
        for key, value in original.items():
            assert result[key] is value

    def test_list_popped_wholesale(self) -> None:
        files = [b"f1", b"f2"]
        original = {"files": files, "title": "t"}
        result = deepcopy_with_paths(original, [["files", "<array>"]])
        assert_different_identities(result, original)
        result_files = result["files"]
        assert isinstance(result_files, list)
        assert_different_identities(result_files, files)

    def test_nested_array_path_copies_list_and_elements(self) -> None:
        elem1 = {"file": b"f1", "extra": 1}
        elem2 = {"file": b"f2", "extra": 2}
        original = {"items": [elem1, elem2]}
        result = deepcopy_with_paths(original, [["items", "<array>", "file"]])
        assert_different_identities(result, original)
        result_items = result["items"]
        assert isinstance(result_items, list)
        assert_different_identities(result_items, original["items"])
        assert_different_identities(result_items[0], elem1)
        assert_different_identities(result_items[1], elem2)

    def test_empty_paths_returns_same_object(self) -> None:
        original = {"foo": "bar"}
        result = deepcopy_with_paths(original, [])
        assert result is original

    @pytest.mark.parametrize(
        "original, paths, expected_files, remaining",
        [
            (
                {"file": b"contents", "other": "value"},
                [["file"]],
                [("file", b"contents")],
                {"other": "value"},
            ),
            (
                {"items": [{"file": b"f1", "extra": 1}, {"file": b"f2", "extra": 2}], "title": "example"},
                [["items", "<array>", "file"]],
                [("items[][file]", b"f1"), ("items[][file]", b"f2")],
                {"items": [{"extra": 1}, {"extra": 2}], "title": "example"},
            ),
        ],
        ids=["top-level", "nested-array"],
    )
    def test_extract_files_preserves_original(
        self, original: dict[str, object], paths: list[list[str]], expected_files: object, remaining: object
    ) -> None:
        before = deepcopy(original)
        copied = deepcopy_with_paths(original, paths)
        assert extract_files(copied, paths=paths) == expected_files
        assert original == before
        assert copied == remaining
