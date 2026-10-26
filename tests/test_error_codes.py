# SPDX-FileCopyrightText: 2026 Xquik contributors
#
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import httpx
import pytest

from tests.utils import json_response
from x_twitter_scraper import ConflictError, XTwitterScraper
from x_twitter_scraper.types import Error
from x_twitter_scraper._types import JsonValue
from x_twitter_scraper._models import validate_type
from x_twitter_scraper.types.shared.error import ErrorValueStructuredError

MESSAGE = "A top-up is already running. Check your balance before you try again."


def conflict_error(body: JsonValue) -> Error:
    def respond(_request: httpx.Request) -> httpx.Response:
        return json_response(409, json=body)

    transport = httpx.MockTransport(respond)
    http_client = httpx.Client(transport=transport)
    with XTwitterScraper(api_key="isolated-test", http_client=http_client, max_retries=0) as client:
        with pytest.raises(ConflictError) as raised:
            client.credits.topup_balance(dollars=10)
    return validate_type(type_=Error, value=raised.value.body)


@pytest.mark.parametrize(
    "code",
    [
        "contributor_not_found",
        "invalid_contributor_alias",
        "invalid_news_id",
        "news_not_found",
        "session_required",
        "topup_in_progress",
        "x_video_too_large",
    ],
)
def test_error_body_reads_each_code_the_api_documents(code: str) -> None:
    legacy = conflict_error({"error": code, "message": MESSAGE})
    structured = conflict_error({"error": {"code": code, "message": MESSAGE, "type": "invalid_request_error"}})

    assert legacy.error == code
    assert legacy.message == MESSAGE
    assert isinstance(structured.error, ErrorValueStructuredError)
    assert structured.error.code == code
    assert structured.error.message == MESSAGE
