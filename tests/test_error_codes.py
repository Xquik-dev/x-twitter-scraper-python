# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import pytest

from x_twitter_scraper._compat import parse_obj
from x_twitter_scraper.types.shared.error import Error, ErrorValueStructuredError


@pytest.mark.parametrize(
    "code",
    [
        "api_key_expired",
        "api_key_paused",
        "api_key_budget_reached",
        "api_key_revoked",
        "ip_not_allowed",
        "insufficient_scope",
        "media_unavailable",
        "extraction_terminal",
        "post_unavailable",
        "price_changed",
        "x_community_creation_closed",
    ],
)
def test_an_error_reads_each_code_the_api_added(code: str) -> None:
    assert parse_obj(Error, {"error": code}).error == code

    structured = parse_obj(Error, {"error": {"code": code, "message": "m", "type": "api_error"}}).error
    assert isinstance(structured, ErrorValueStructuredError)
    assert structured.code == code


@pytest.mark.parametrize("scope", ["write", "monitors", "exports", "billing", "full"])
def test_an_insufficient_scope_error_names_the_scope_it_needs(scope: str) -> None:
    error = parse_obj(Error, {"error": "insufficient_scope", "requiredScope": scope})

    assert error.required_scope == scope


def test_an_error_rejects_a_scope_the_api_does_not_list() -> None:
    with pytest.raises(ValueError):
        parse_obj(Error, {"error": "insufficient_scope", "requiredScope": "admin"})
