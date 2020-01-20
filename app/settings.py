import os
import sys
import logging


# -----------------------------------------------------------------------------
# Application Information

PROGRAM_NAME = 'app'
PROGRAM_NAME_VERBOSE = 'Python CLI Template'
PROGRAM_DESCRIPTION = 'A python command line utility.'
PROGRAM_VERSION = '0.1'

CLI_HELP_TEXT = \
f"""
{PROGRAM_NAME_VERBOSE}
{PROGRAM_DESCRIPTION}

 _                 _    
| |               | |   
| |__   ___  _ __ | | __
| '_ \ / _ \| '_ \| |/ /
| | | | (_) | | | |   < 
|_| |_|\___/|_| |_|_|\_\ 
"""


# -----------------------------------------------------------------------------
# Application Paths

BASE_DIR = os.getcwd()

LOGS_DIR = os.path.join(BASE_DIR, 'logs/')
DEFAULT_LOG_FILE = os.path.join(LOGS_DIR, f'{PROGRAM_NAME}.log')
DEBUG_LOG_FILE = os.path.join(LOGS_DIR, f'{PROGRAM_NAME}.debug.log')
ERROR_LOG_FILE = os.path.join(LOGS_DIR, f'{PROGRAM_NAME}.error.log')

CONFIG_DIR = os.path.join(BASE_DIR, 'config/')
CONFIG_FILE = os.path.join(CONFIG_DIR, 'config.json')


# -----------------------------------------------------------------------------
# Application Settings & Configuration

DEBUG = True

# SMTP (for logging)
# If this is enabled, then an email will be sent from `SMTP_FROM_ADDR` to
# `SMTP_TO_ADDR` with the subject of `SMTP_SUBJECT`.
# Make sure to have valid credentials in the tuple `SMTP_CREDENTIALS`.
SMTP_LOGGING_ENABLED = False
SMTP_MAILHOST = ("smtp.example.com", 587)
SMTP_CREDENTIALS = ('<address>', '<password>')
SMTP_FROM_ADDR = '<address>'
SMTP_TO_ADDR = '<address>'

# format:
# 0         1 
# level     filepath
FILE_LOGGERS = [
    (logging.INFO, DEFAULT_LOG_FILE),
    (logging.DEBUG, DEBUG_LOG_FILE),
    (logging.ERROR, ERROR_LOG_FILE)
]

# format:
# 0         1 
# level     stream
STREAM_LOGGERS = [
    (logging.INFO, sys.stdout)
]

# format:
# 0         1           2               3               4           5
# level     mailhost    credentials     from address    to address  subject
SMTP_LOGGERS = [
    (logging.ERROR, SMTP_MAILHOST, SMTP_CREDENTIALS, SMTP_FROM_ADDR, SMTP_TO_ADDR, 'App Error')
]


# General logging settings/customization
LOG_BACKUP_COUNT = 10
LOG_FILE_MAX_KB = 5000
LOG_FMT = '%(asctime)-8s %(name)-16s %(levelname)-8s %(message)s'
LOG_TIME_FMT = '%Y-%m-%d %H:%M:%S'


# 12-hour: %I:%M %p
# 24-hour: %H:%M
TIME_FMT = '%I:%M %p'
TIMEZONE = 'America/New_York'


DEFAULT_CONFIG = {
    'value_a': 10
}
