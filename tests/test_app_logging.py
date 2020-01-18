import os
import sys
import logging

from app.logging import (
    create_log_file_handler,
    create_log_stream_handler,
    create_logger
)


TEST_LOG_LEVEL = logging.NOTSET
TEST_LOG_FORMATTER = None
TEST_LOG_OUT = os.devnull


def test_create_log_file_handler():
    handler = create_log_file_handler(
        TEST_LOG_OUT,
        TEST_LOG_LEVEL,
        TEST_LOG_FORMATTER
    )
    assert handler is not None
    assert isinstance(handler, logging.FileHandler)


def test_create_log_stream_handler():
    handler = create_log_stream_handler(
        TEST_LOG_LEVEL,
        TEST_LOG_FORMATTER,
        TEST_LOG_OUT
    )
    assert handler is not None
    assert isinstance(handler, logging.StreamHandler)


def test_create_logger():
    logger = create_logger(__name__)
    assert logging.SUCCESS == 25
    assert logging.FAILURE == 35