from __future__ import annotations

import logging

import pytest

from x_twitter_scraper._utils import _logs


def test_setup_logging_supports_debug_and_info(monkeypatch: pytest.MonkeyPatch) -> None:
    old_logger_level = _logs.logger.level
    old_httpx_level = _logs.httpx_logger.level

    try:
        monkeypatch.setenv("X_TWITTER_SCRAPER_LOG", "debug")
        _logs.setup_logging()
        assert _logs.logger.level == logging.DEBUG
        assert _logs.httpx_logger.level == logging.DEBUG

        monkeypatch.setenv("X_TWITTER_SCRAPER_LOG", "info")
        _logs.setup_logging()
        assert _logs.logger.level == logging.INFO
        assert _logs.httpx_logger.level == logging.INFO

        monkeypatch.setenv("X_TWITTER_SCRAPER_LOG", "disabled")
        _logs.setup_logging()
        assert _logs.logger.level == logging.INFO
        assert _logs.httpx_logger.level == logging.INFO
    finally:
        _logs.logger.setLevel(old_logger_level)
        _logs.httpx_logger.setLevel(old_httpx_level)
