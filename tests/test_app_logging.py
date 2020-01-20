import os
import sys

import logging
from logging import StreamHandler
from logging.handlers import RotatingFileHandler

from app.logging import (
    create_file_handler,
    create_stream_handler,
    get_logger
)


TEST_LOG_LEVEL = logging.NOTSET
TEST_LOG_FORMATTER = None
TEST_LOG_OUT = os.devnull


def test_create_log_file_handler():
    handler = create_file_handler(
        TEST_LOG_LEVEL,
        TEST_LOG_OUT,
        TEST_LOG_FORMATTER
    )
    assert handler is not None
    assert isinstance(handler, RotatingFileHandler)


def test_create_log_stream_handler():
    handler = create_stream_handler(
        TEST_LOG_LEVEL,
        TEST_LOG_OUT,
        TEST_LOG_FORMATTER,
    )
    assert handler is not None
    assert isinstance(handler, StreamHandler)


def test_get_logger():
    logger = get_logger(__name__)
    assert logging.SUCCESS == 25
    assert logging.FAILURE == 35