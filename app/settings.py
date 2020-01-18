import os
import sys


# -----------------------------------------------------------------------------
# Application Information

PROGRAM_NAME = 'app'
PROGRAM_NAME_VERBOSE = 'Python CLI Template'
PROGRAM_DESCRIPTION = 'A python command line utility.'
PROGRAM_VERSION = '0.1'


# -----------------------------------------------------------------------------
# Application Paths

BASE_DIR = os.getcwd()

CONFIG_DIR = os.path.join(BASE_DIR, 'config/')
CONFIG_FILE_PATH = os.path.join(CONFIG_DIR, 'config.json')

LOGGING_DIR = os.path.join(BASE_DIR, 'logs/')
DEFAULT_LOG_FILE_PATH = os.path.join(LOGGING_DIR, f'{PROGRAM_NAME}.log')
DEBUG_LOG_FILE_PATH = os.path.join(LOGGING_DIR, f'{PROGRAM_NAME}.debug.log')
ERROR_LOG_FILE_PATH = os.path.join(LOGGING_DIR, f'{PROGRAM_NAME}.error.log')


# -----------------------------------------------------------------------------
# Application Settings & Configuration

DEFAULT_CONFIG = {
    'value_a': 10
}

LOG_OUTPUT_FMT = '%(asctime)-8s %(name)-8s %(levelname)-8s %(message)s'

TIME_FMT = "%Y-%m-%d %H:%M:%S"