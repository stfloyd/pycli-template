'''
Helper functions and definitions for the app module. 
'''

import sys
import logging

import app.settings as settings


# -----------------------------------------------------------------------------
# Logging Configuration


def create_log_file_handler(filename, level, formatter):
    '''
    Helper function for create_logger.
    Creates a file handler for file logging output.
    '''

    handler = logging.FileHandler(
        filename=filename,
        encoding="utf-8", mode="w"
    )
    handler.setFormatter(formatter)
    handler.setLevel(level)
    return handler


def create_log_stream_handler(level, formatter, stream=sys.stdout):
    '''
    Helper function for create_logger.
    Creates a stream handler for console logging output.
    '''

    handler = logging.StreamHandler(stream)
    handler.setFormatter(formatter)
    handler.setLevel(level)
    return handler


def create_logger(name, verbose=False):
    '''
    Create a logger of a given name and verbosity.
    '''

    # Get our logger.
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Create our log formatter.
    formatter = logging.Formatter(
        settings.LOG_OUTPUT_FMT,
        settings.TIME_FMT
    )

    # Handler for all debug messages
    debug_handler = create_log_file_handler(
        settings.DEBUG_LOG_FILE_PATH,
        logging.DEBUG,
        formatter
    )

    # Handler for all info messages
    default_handler = create_log_file_handler(
        settings.DEFAULT_LOG_FILE_PATH,
        logging.INFO,
        formatter
    )

    # Handler for all error messages
    error_handler = create_log_file_handler(
        settings.ERROR_LOG_FILE_PATH,
        logging.ERROR,
        formatter
    )

    # Add all our file handlers
    logger.addHandler(default_handler)
    logger.addHandler(error_handler)
    logger.addHandler(debug_handler)

    # Handle verbosity
    if verbose: console_level = logging.DEBUG
    else:       console_level = logging.INFO

    # Enable console stream logging.
    console_handler = create_log_stream_handler(
        console_level,
        formatter
    )

    # Add our console stream handler.
    logger.addHandler(console_handler)

    # Add a new level to the logger: success
    logging.SUCCESS = 25  # between INFO and WARNING
    logging.addLevelName(
        logging.SUCCESS,
        'SUCCESS'
    )

    # Add a new level to the logger: failure
    logging.FAILURE = 35  # between WARNING and ERROR
    logging.addLevelName(
        logging.FAILURE,
        'FAILURE'
    )

    # Bind a success attr to the logger to log with success level.
    setattr(
        logger,
        'success',
        lambda message, *args: logger._log(logging.SUCCESS, message, args)
    )

    # Bind a failure attr to the logger to log with failure level.
    setattr(
        logger,
        'failure',
        lambda message, *args: logger._log(logging.FAILURE, message, args)
    )

    return logger