# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Any, Dict, List, Tuple
from functools import reduce

import httpx
import pytest

from tests.utils import send_with_mock_transport

IMAGE = "https://example.com/a.png"

Write = Tuple[str, Tuple[str, ...], Dict[str, str]]
WRITES: List[Tuple[str, str, Write]] = [
    ("POST", "/x/tweets", ("tweets.create", (), {"text": "hi"})),
    ("DELETE", "/x/tweets/1", ("tweets.delete", ("1",), {})),
    ("POST", "/x/tweets/1/like", ("tweets.like.create", ("1",), {})),
    ("DELETE", "/x/tweets/1/like", ("tweets.like.delete", ("1",), {})),
    ("POST", "/x/tweets/1/bookmark", ("tweets.bookmark.create", ("1",), {})),
    ("DELETE", "/x/tweets/1/bookmark", ("tweets.bookmark.delete", ("1",), {})),
    ("POST", "/x/tweets/1/retweet", ("tweets.retweet.create", ("1",), {})),
    ("DELETE", "/x/tweets/1/retweet", ("tweets.retweet.delete", ("1",), {})),
    ("POST", "/x/users/1/follow", ("users.follow.create", ("1",), {})),
    ("DELETE", "/x/users/1/follow", ("users.follow.delete_all", ("1",), {})),
    ("POST", "/x/users/1/block", ("users.block.create", ("1",), {})),
    ("DELETE", "/x/users/1/block", ("users.block.delete", ("1",), {})),
    ("POST", "/x/users/1/mute", ("users.mute.create", ("1",), {})),
    ("DELETE", "/x/users/1/mute", ("users.mute.delete", ("1",), {})),
    ("POST", "/x/users/1/remove-follower", ("users.remove_follower", ("1",), {})),
    ("POST", "/x/dm/1", ("dm.send", ("1",), {"text": "hi"})),
    ("DELETE", "/x/dm/1/messages/2", ("dm.delete_message", ("2",), {"user_id": "1"})),
    ("POST", "/x/media", ("media.upload", (), {"url": IMAGE})),
    ("PATCH", "/x/profile", ("profile.update", (), {"name": "a"})),
    ("PATCH", "/x/profile/avatar", ("profile.update_avatar", (), {"url": IMAGE})),
    ("PATCH", "/x/profile/banner", ("profile.update_banner", (), {"url": IMAGE})),
    ("POST", "/x/communities", ("communities.create", (), {"name": "a"})),
    ("DELETE", "/x/communities/1", ("communities.delete", ("1",), {"community_name": "a"})),
    ("POST", "/x/communities/1/join", ("communities.join.create", ("1",), {})),
    ("DELETE", "/x/communities/1/join", ("communities.join.delete_all", ("1",), {})),
]
each_write = pytest.mark.parametrize(
    "method,path,write", WRITES, ids=[f"{method} {path}" for method, path, _ in WRITES]
)
each_client = pytest.mark.parametrize("asynchronous", [False, True])


def call(client: Any, write: Write, headers: Dict[str, str]) -> Any:
    target, arguments, fields = write
    method = reduce(getattr, f"x.{target}".split("."), client)
    return method(*arguments, account="@a", idempotency_key="key", **fields, **headers)


async def send(write: Write, method: str, asynchronous: bool, **headers: str) -> httpx.Request:
    request, _ = await send_with_mock_transport(
        lambda client: call(client, write, headers),
        lambda client: call(client, write, headers),
        {},
        asynchronous,
        method,
        strict_response_validation=False,
    )
    return request


@each_client
@each_write
async def test_a_write_sends_prefer_beside_its_idempotency_key(
    method: str, path: str, write: Write, asynchronous: bool
) -> None:
    request = await send(write, method, asynchronous, prefer="wait=50")

    assert request.url.path == f"/api/v1{path}"
    assert request.headers["Prefer"] == "wait=50"
    assert request.headers["Idempotency-Key"] == "key"


@each_client
@each_write
async def test_a_write_leaves_prefer_out_unless_the_caller_sets_it(
    method: str, path: str, write: Write, asynchronous: bool
) -> None:
    request = await send(write, method, asynchronous)

    assert request.url.path == f"/api/v1{path}"
    assert "Prefer" not in request.headers
