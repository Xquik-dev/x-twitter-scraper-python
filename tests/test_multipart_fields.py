# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

import pytest

from x_twitter_scraper import XTwitterScraper
from x_twitter_scraper._models import FinalRequestOptions


@pytest.mark.parametrize(
    "fields,expected",
    [
        ({}, {}),
        ({"name": "one", "count": 1}, {"name": "one", "count": "1"}),
        ({"names": ["one", "two", "three"]}, {"names[]": ["one", "two", "three"]}),
        ({"nested": {"flags": [True, False]}}, {"nested[flags][]": ["true", "false"]}),
        ({"zero": 0, "empty": "", "missing": None, "nulls": [None]}, {"zero": "0"}),
    ],
)
def test_multipart_field_grouping(
    fields: dict[object, object], expected: dict[str, object], client: XTwitterScraper
) -> None:
    assert client._serialize_multipartform(fields) == expected


@pytest.mark.parametrize("key", [1, None, ("field",)])
def test_multipart_rejects_non_string_field_names(key: object) -> None:
    with XTwitterScraper(api_key="isolated-test") as client:
        with pytest.raises(TypeError, match="Multipart field names must be strings"):
            client._build_request(
                FinalRequestOptions.construct(
                    method="post",
                    url="/upload",
                    headers={"Content-Type": "multipart/form-data"},
                    json_data={key: "value"},
                )
            )
