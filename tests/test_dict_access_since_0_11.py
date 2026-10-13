# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

"""Values that were plain dictionaries in 0.11 still read like dictionaries."""

from __future__ import annotations

import json
from typing import Any, Dict, Callable, cast

import pytest

from x_twitter_scraper._models import validate_type, construct_type_unchecked
from x_twitter_scraper.types.x import TweetDetail
from x_twitter_scraper.types.shared import SearchTweet, EmbeddedTweet
from x_twitter_scraper.types.extraction_retrieve_response import ExtractionRetrieveResponse

ENTITIES = json.loads(
    """{
      "hashtags": [{"indices": [0, 6], "text": "xquik"}],
      "urls": [
        {"display_url": "xquik.com", "expanded_url": "https://xquik.com", "indices": [7, 30], "url": "https://t.co/a"}
      ],
      "user_mentions": [{"id_str": "44196397", "indices": [31, 37], "name": "Xquik", "screen_name": "xquik"}]
    }"""
)
COUNTS = {"bookmarkCount": 1, "likeCount": 42, "quoteCount": 0, "replyCount": 3, "retweetCount": 5, "viewCount": 900}
QUOTED = {"id": "1900000000000000009", "text": "Quoted", "entities": ENTITIES, **COUNTS}
TWEET = {
    "id": "1900000000000000001",
    "text": "#xquik https://t.co/a @xquik",
    "entities": ENTITIES,
    "noteTweet": {"text": "Long form", "entities": ENTITIES},
    "quoted_tweet": QUOTED,
    **COUNTS,
}
EXTRACTION = json.loads(
    """{
      "hasMore": false,
      "pollAfterMs": 0,
      "waitUrl": "https://xquik.com/api/v1/extractions/77/wait",
      "job": {
        "id": "77",
        "createdAt": "2026-10-13T12:00:00.000Z",
        "completedAt": "2026-10-13T12:00:09.250Z",
        "status": "completed",
        "toolType": "follower_explorer",
        "totalResults": 1
      },
      "results": [
        {
          "id": "1",
          "createdAt": "2026-10-13T12:00:05.000Z",
          "xUserId": "44196397",
          "xUsername": "xquik",
          "xFollowersCount": 1200,
          "xVerified": true,
          "legacyColumn": "kept"
        }
      ]
    }"""
)
PARSERS = [
    pytest.param(construct_type_unchecked, id="loose"),
    pytest.param(validate_type, id="strict"),
]


def message(owner: str) -> str:
    return rf"Dict access on {owner} is deprecated & goes away in a later minor version\. Use attribute access or to_dict\(\)\."


def assert_reads_like(value: Any, expected: Dict[str, Any], owner: str) -> None:
    """Every read a 0.11 caller made on the dictionary returns what the dictionary held, and warns."""
    warning = message(owner)
    for key, item in expected.items():
        with pytest.warns(DeprecationWarning, match=warning) as record:
            assert value[key] == item
        assert record[0].filename == __file__
        with pytest.warns(DeprecationWarning, match=warning):
            assert value.get(key) == item
        with pytest.warns(DeprecationWarning, match=warning):
            assert key in value
    # The keys come in the model's field order, which can differ from the order in the response.
    with pytest.warns(DeprecationWarning, match=warning) as record:
        assert sorted(value.keys()) == sorted(expected.keys())
    assert record[0].filename == __file__
    with pytest.warns(DeprecationWarning, match=warning):
        assert len(value.values()) == len(expected)
    with pytest.warns(DeprecationWarning, match=warning):
        assert dict(value.items()) == expected
    with pytest.warns(DeprecationWarning, match=warning):
        assert value.get("missing", "fallback") == "fallback"
    with pytest.warns(DeprecationWarning, match=warning):
        assert "missing" not in value
    with pytest.warns(DeprecationWarning, match=warning), pytest.raises(KeyError, match="missing"):
        value["missing"]


@pytest.mark.parametrize("parse", PARSERS)
def test_extraction_rows_and_job_keep_dict_access(parse: Callable[..., Any]) -> None:
    response = cast(ExtractionRetrieveResponse, parse(type_=ExtractionRetrieveResponse, value=EXTRACTION))

    assert response.results[0].x_username == "xquik"
    assert response.job.total_results == 1
    assert_reads_like(response.results[0], EXTRACTION["results"][0], "an extraction result row")
    assert_reads_like(response.job, EXTRACTION["job"], "an extraction job")
    with pytest.warns(DeprecationWarning):
        assert [row["xUsername"] for row in response.results] == ["xquik"]


@pytest.mark.parametrize("parse", PARSERS)
@pytest.mark.parametrize("model", [SearchTweet, TweetDetail, EmbeddedTweet])
def test_tweet_entities_keep_dict_access(model: Any, parse: Callable[..., Any]) -> None:
    tweet = parse(type_=model, value=TWEET)

    assert tweet.entities.urls[0].expanded_url == "https://xquik.com"
    assert_reads_like(tweet.entities, ENTITIES, "tweet entities")
    assert_reads_like(tweet.note_tweet.entities, ENTITIES, "tweet entities")
    assert_reads_like(tweet.quoted_tweet.entities, ENTITIES, "tweet entities")
    with pytest.warns(DeprecationWarning):
        assert tweet.entities["urls"][0]["expanded_url"] == "https://xquik.com"
