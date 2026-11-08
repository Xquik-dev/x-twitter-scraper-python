# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import json
from typing import Any, Dict, List, Tuple

import httpx
import pytest

from tests.utils import send_with_mock_transport
from x_twitter_scraper.types import PaginatedTweets, ImageFilteredTweets, TopicFilteredTweets

POST: Dict[str, object] = {
    "id": "7",
    "bookmarkCount": 0,
    "likeCount": 3,
    "quoteCount": 0,
    "replyCount": 1,
    "retweetCount": 2,
    "text": "Rust 1.91 ships today",
    "viewCount": 40,
}
PAGE: Dict[str, object] = {"has_next_page": False, "next_cursor": "", "tweets": [POST]}
ESTIMATE: Dict[str, object] = {
    "allowed": True,
    "creditsAvailable": "100",
    "creditsRequired": "20",
    "estimatedResults": 10,
    "source": "resultsLimit",
}
TOPIC_FILTER: Dict[str, object] = {
    "topic": "the Rust programming language",
    "question": "Is this post about the Rust programming language?",
    "cutoff": 0.5,
    "checked": 3,
    "kept": 1,
    "unchecked": [{"id": "9", "reason": "no_answer"}],
}
IMAGE_FILTER: Dict[str, object] = {
    "imageShows": "charts",
    "question": "Does a picture attached to this post show a chart or graph that plots data?",
    "cutoff": 0.5,
    "checked": 2,
    "kept": 1,
    "unchecked": [{"id": "8", "reason": "no_safe_photos"}],
}
FILTERS: Dict[str, object] = {"topic": "the Rust programming language", "image_shows": "charts"}
SENT_FILTERS: Dict[str, object] = {"topic": "the Rust programming language", "imageShows": "charts"}
PAGE_READS: List[Tuple[str, Dict[str, object]]] = [("x.tweets.search", {}), ("x.users.retrieve_tweets", {"id": "44"})]


def call(client: object, method: str, arguments: Dict[str, object]) -> Any:
    target: Any = client
    for name in method.split("."):
        target = getattr(target, name)
    return target(**arguments)


def sent(request: httpx.Request) -> object:
    if request.method == "GET":
        return dict(request.url.params)
    return json.loads(request.content)


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize(
    ("method", "arguments", "verb", "payload", "expected"),
    [
        ("x.tweets.search", FILTERS, "GET", PAGE, SENT_FILTERS),
        ("x.users.retrieve_tweets", {"id": "44", **FILTERS}, "GET", PAGE, SENT_FILTERS),
        ("x.users.retrieve_replies", {"id": "44", **FILTERS}, "GET", PAGE, SENT_FILTERS),
        ("x.users.retrieve_media", {"id": "44", **FILTERS}, "GET", PAGE, SENT_FILTERS),
        (
            "extractions.run",
            {"tool_type": "tweet_search_extractor", **FILTERS},
            "POST",
            ESTIMATE,
            {"toolType": "tweet_search_extractor", **SENT_FILTERS},
        ),
        (
            "extractions.estimate_cost",
            {"tool_type": "tweet_search_extractor", **FILTERS},
            "POST",
            ESTIMATE,
            {"toolType": "tweet_search_extractor", **SENT_FILTERS},
        ),
        (
            "x.media.download",
            {"tweet_ids": ["7"], "image_shows": "charts"},
            "POST",
            {},
            {"tweetIds": ["7"], "imageShows": "charts"},
        ),
    ],
)
async def test_filters_go_out_under_their_api_names(
    method: str,
    arguments: Dict[str, object],
    verb: str,
    payload: object,
    expected: object,
    asynchronous: bool,
) -> None:
    request, _ = await send_with_mock_transport(
        lambda client: call(client, method, arguments),
        lambda client: call(client, method, arguments),
        payload,
        asynchronous,
        verb,
    )

    assert sent(request) == expected


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize(("method", "arguments"), PAGE_READS)
async def test_a_topic_filtered_page_reads_its_scores(
    method: str, arguments: Dict[str, object], asynchronous: bool
) -> None:
    _, page = await send_with_mock_transport(
        lambda client: call(client, method, {**arguments, "topic": "the Rust programming language"}),
        lambda client: call(client, method, {**arguments, "topic": "the Rust programming language"}),
        {**PAGE, "tweets": [{**POST, "topicScore": 0.91}], "topicFilter": TOPIC_FILTER},
        asynchronous,
    )

    assert type(page) is TopicFilteredTweets
    assert page.tweets[0].topic_score == 0.91
    assert page.topic_filter.kept == 1


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize(("method", "arguments"), PAGE_READS)
async def test_an_image_filtered_page_reads_its_scores(
    method: str, arguments: Dict[str, object], asynchronous: bool
) -> None:
    _, page = await send_with_mock_transport(
        lambda client: call(client, method, {**arguments, "image_shows": "charts"}),
        lambda client: call(client, method, {**arguments, "image_shows": "charts"}),
        {**PAGE, "tweets": [{**POST, "imageScore": 0.88}], "imageFilter": IMAGE_FILTER},
        asynchronous,
    )

    assert type(page) is ImageFilteredTweets
    assert page.tweets[0].image_score == 0.88
    assert page.image_filter.kept == 1


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize(("method", "arguments"), PAGE_READS)
async def test_an_unfiltered_page_stays_a_plain_page(
    method: str, arguments: Dict[str, object], asynchronous: bool
) -> None:
    _, page = await send_with_mock_transport(
        lambda client: call(client, method, arguments),
        lambda client: call(client, method, arguments),
        PAGE,
        asynchronous,
    )

    assert type(page) is PaginatedTweets


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_an_extraction_job_reads_both_filter_summaries(asynchronous: bool) -> None:
    job = {
        "id": "77",
        "createdAt": "2026-11-08T10:00:00.000Z",
        "status": "completed",
        "toolType": "tweet_search_extractor",
        "totalResults": 1,
        "url": "https://xquik.com/extractions/77",
        "imageFilter": IMAGE_FILTER,
        "topicFilter": TOPIC_FILTER,
    }
    _, extraction = await send_with_mock_transport(
        lambda client: client.extractions.retrieve("77"),
        lambda client: client.extractions.retrieve("77"),
        {"hasMore": False, "job": job, "pollAfterMs": 0, "results": [], "waitUrl": "/extractions/77/wait"},
        asynchronous,
    )

    assert extraction.job.image_filter is not None
    assert extraction.job.image_filter.unchecked[0].reason == "no_safe_photos"
    assert extraction.job.topic_filter is not None
    assert extraction.job.topic_filter.cutoff == 0.5


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_a_media_download_reads_the_image_filter(asynchronous: bool) -> None:
    _, download = await send_with_mock_transport(
        lambda client: client.x.media.download(tweet_ids=["7"], image_shows="charts"),
        lambda client: client.x.media.download(tweet_ids=["7"], image_shows="charts"),
        {"totalTweets": 0, "totalMedia": 0, "imageFilter": {**IMAGE_FILTER, "kept": 0}},
        asynchronous,
        "POST",
    )

    assert download.image_filter is not None
    assert download.image_filter.image_shows == "charts"
    assert download.image_filter.kept == 0
