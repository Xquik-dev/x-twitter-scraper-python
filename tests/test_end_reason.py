# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from typing import Any, Dict, List, Tuple, Optional

import pytest

from tests.utils import send_with_mock_transport

TWEETS_PAGE: Dict[str, object] = {"has_next_page": False, "next_cursor": "", "tweets": []}
USERS_PAGE: Dict[str, object] = {"has_next_page": False, "next_cursor": "", "users": []}
READS: List[Tuple[str, Dict[str, object], Dict[str, object]]] = [
    ("x.tweets.search", {"q": "rust"}, TWEETS_PAGE),
    ("x.bookmarks.list", {}, TWEETS_PAGE),
    ("x.users.retrieve_followers", {"id": "44"}, USERS_PAGE),
    ("x.communities.retrieve_members", {"id": "9"}, USERS_PAGE),
]


def call(client: object, method: str, arguments: Dict[str, object]) -> Any:
    target: Any = client
    for name in method.split("."):
        target = getattr(target, name)
    return target(**arguments)


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize(("method", "arguments", "page"), READS)
@pytest.mark.parametrize(("ending", "expected"), [({"endReason": "stalled"}, "stalled"), ({}, None)])
async def test_a_last_page_says_when_x_cut_it_short(
    method: str,
    arguments: Dict[str, object],
    page: Dict[str, object],
    ending: Dict[str, object],
    expected: Optional[str],
    asynchronous: bool,
) -> None:
    _, result = await send_with_mock_transport(
        lambda client: call(client, method, arguments),
        lambda client: call(client, method, arguments),
        {**page, **ending},
        asynchronous,
    )

    assert result.end_reason == expected
