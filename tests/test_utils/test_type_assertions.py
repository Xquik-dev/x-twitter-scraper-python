# SPDX-FileCopyrightText: 2026 Xquik contributors
# SPDX-License-Identifier: Apache-2.0

from typing import Union, Literal, Sequence

import pytest

from tests.utils import assert_matches_type


@pytest.mark.parametrize(
    "annotation, valid, invalid",
    [
        (Union[int, None], 1, "bad"),
        (Union[None, int], None, "bad"),
        (Literal[1], 1, True),
        (Literal[True], True, 1),
        (Literal["x"], "x", "y"),
        (list[int], [1], ["bad"]),
        (Sequence[int], (1,), ("bad",)),
        (list[dict[str, int]], [{"key": 1}], [{"key": "bad"}]),
    ],
)
def test_assertions_reject_mismatched_values(annotation: object, valid: object, invalid: object) -> None:
    assert_matches_type(annotation, valid, path=["response"])
    with pytest.raises(AssertionError):
        assert_matches_type(annotation, invalid, path=["response"])
