import os
import sys
import logging
import json

from . import (
    APP_ROOT, APP_DEFAULT_CONFIG,
    env, config
)


def print_app_env():
    log_dir = env.APP_LOGGING_DIR
    conf_dir = env.APP_CONFIG_DIR

    app_env_str = f'Base: {APP_ROOT}\nLogging: {log_dir}\nConfig: {conf_dir}'
    print(app_env_str)


def print_config():
    print(config)