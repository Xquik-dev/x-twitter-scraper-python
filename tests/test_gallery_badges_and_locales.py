# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import json
from typing import Dict, Type
from datetime import datetime, timezone
from typing_extensions import Literal

import pytest

from tests.utils import send_with_mock_transport
from tests.mock_api_schema import model_payloads
from x_twitter_scraper._models import BaseModel
from x_twitter_scraper.types.x import TweetGetRepliesResponse
from x_twitter_scraper.types.extraction_retrieve_response import Result, ExtractionRetrieveResponse

GALLERY_ITEM = {
    "id": "42",
    "tweetId": "1234567890",
    "mediaType": "photo",
    "mediaUrl": "https://media.xquik.com/tweet_1234567890/0.jpg",
    "fileSize": None,
    "createdAt": "2026-10-16T11:00:00.000Z",
    "authorUsername": "NASA",
    "authorDisplayName": "NASA",
    "authorAvatar": None,
    "tweetText": "Launch day.",
    "likes": 1200,
    "retweets": 340,
    "views": None,
}


def minimal(model: Type[BaseModel]) -> Dict[str, object]:
    payload: Dict[str, object] = json.loads(model_payloads({model})[model])
    return payload


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_downloads_list_the_files_saved_to_the_gallery(asynchronous: bool) -> None:
    _, download = await send_with_mock_transport(
        lambda client: client.x.media.download(tweet_id="1234567890"),
        lambda client: client.x.media.download(tweet_id="1234567890"),
        {"tweetId": "1234567890", "galleryUrl": "https://xquik.com/gallery/abc123", "items": [GALLERY_ITEM]},
        asynchronous,
        method="POST",
    )

    assert download.items is not None
    item = download.items[0]
    assert (item.id, item.media_type, item.media_url) == (
        "42",
        "photo",
        "https://media.xquik.com/tweet_1234567890/0.jpg",
    )
    assert item.created_at == datetime(2026, 10, 16, 11, tzinfo=timezone.utc)
    assert (item.file_size, item.author_avatar, item.views) == (None, None, None)
    assert (item.likes, item.retweets) == (1200, 340)


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_replies_count_the_replies_the_read_has_not_reached(asynchronous: bool) -> None:
    _, replies = await send_with_mock_transport(
        lambda client: client.x.tweets.get_replies("1"),
        lambda client: client.x.tweets.get_replies("1"),
        {**minimal(TweetGetRepliesResponse), "unreachedReplies": 120},
        asynchronous,
    )

    assert replies.unreached_replies == 120


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_flat_extraction_rows_carry_the_badge_type(asynchronous: bool) -> None:
    payload = minimal(ExtractionRetrieveResponse)
    payload["results"] = [{**minimal(Result), "verifiedType": "Business"}]
    _, extraction = await send_with_mock_transport(
        lambda client: client.extractions.retrieve("77"),
        lambda client: client.extractions.retrieve("77"),
        payload,
        asynchronous,
    )

    assert extraction.results[0].verified_type == "Business"


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize("locale", ["ja", "ko", "zh"])
async def test_account_locale_takes_japanese_korean_and_chinese(
    locale: Literal["ja", "ko", "zh"], asynchronous: bool
) -> None:
    request, _ = await send_with_mock_transport(
        lambda client: client.account.update_locale(locale=locale),
        lambda client: client.account.update_locale(locale=locale),
        {"success": True},
        asynchronous,
        method="PATCH",
    )

    assert json.loads(request.content) == {"locale": locale}
