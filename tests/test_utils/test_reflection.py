from __future__ import annotations

import pytest

from x_twitter_scraper._utils import function_has_argument, assert_signatures_in_sync


def source_function(alpha: str, beta: int) -> None:
    del alpha, beta


def matching_function(alpha: str, beta: int) -> None:
    del alpha, beta


def missing_function(alpha: str) -> None:
    del alpha


def mismatched_function(alpha: int, beta: int) -> None:
    del alpha, beta


def test_function_has_argument() -> None:
    assert function_has_argument(source_function, "alpha")
    assert not function_has_argument(source_function, "gamma")


def test_assert_signatures_in_sync() -> None:
    assert_signatures_in_sync(source_function, matching_function)
    assert_signatures_in_sync(source_function, missing_function, exclude_params={"beta"})


def test_assert_signatures_in_sync_reports_missing_parameters() -> None:
    with pytest.raises(AssertionError, match=r"(?s)1 errors encountered.*`beta` param is missing"):
        assert_signatures_in_sync(source_function, missing_function)


def test_assert_signatures_in_sync_reports_mismatched_types() -> None:
    with pytest.raises(AssertionError, match=r"types for the `alpha` param are do not match"):
        assert_signatures_in_sync(source_function, mismatched_function)
