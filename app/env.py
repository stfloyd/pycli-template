import os
import sys
import logging

from . import APP_NAME


APP_ENV_CONFIG_DIR = 'APP_CONFIG_DIR'
APP_ENV_LOGGING_DIR = 'APP_LOGGING_DIR'

APP_CONFIG_DIR = os.path.abspath(os.environ.get(APP_ENV_CONFIG_DIR, '/etc/'))
APP_CONFIG_FILE = os.path.join(APP_CONFIG_DIR, f"{APP_NAME}.json")

APP_LOGGING_DIR = os.path.abspath(os.environ.get(APP_ENV_LOGGING_DIR, '/var/log/app/'))
APP_DEFAULT_LOG_FILE = os.path.join(APP_LOGGING_DIR, f"{APP_NAME}.log")
APP_DEBUG_LOG_FILE = os.path.join(APP_LOGGING_DIR, f"{APP_NAME}.debug.log")
APP_ERROR_LOG_FILE = os.path.join(APP_LOGGING_DIR, f"{APP_NAME}.error.log")

APP_DEBUG = False

FILE_LOGGERS = [
    (logging.INFO, APP_DEFAULT_LOG_FILE), (logging.DEBUG, APP_DEBUG_LOG_FILE), (logging.ERROR, APP_ERROR_LOG_FILE)
]

STREAM_LOGGERS = [
    (logging.INFO, sys.stdout)
]

LOG_BACKUP_COUNT = 10
LOG_FILE_MAX_KB = 5000
LOG_FMT = '%(asctime)-8s %(name)-16s %(levelname)-8s %(message)s'
LOG_TIME_FMT = '%Y-%m-%d %H:%M:%S'