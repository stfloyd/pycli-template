import os
import logging
import json

from . import (
    APP_DEFAULT_CONFIG,
    env
)


class AppConfig(object):
    def __init__(self):
        self._config = APP_DEFAULT_CONFIG
        self._args = None
    
    def load(self, args=None):
        self._args = args
        self._config = _load_config(check=True)

    @property
    def args(self):
        return self._args

    @property
    def test(self):
        return self._config.get('test', None)
    
    def __str__(self):
        return f'args:{self.args}\ncfg:{{{self.test}}}'


def _check_config(create=False):
    config_dir = env.APP_CONFIG_DIR
    config_file = env.APP_CONFIG_FILE

    if not os.path.exists(config_dir):
        logging.warning(f'Config directory does not exist at: {config_dir}')

        if create:
            _create_config_dir()
        else:
            return False
    
    if not os.path.exists(config_file):
        logging.warning(f'Config file does not exist at: {config_file}')
        
        if create:
            _create_config_file()
        else:
            return False
    
    return True


def _load_config(check=False):
    config_file = env.APP_CONFIG_FILE
    config_data = None

    if check:
        _check_config(create=True)
    
    try:
        logging.debug(f'Loading configuration from file: {config_file}')

        with open(config_file) as cf:
            config_data = json.load(cf)

        logging.debug('Configuration loaded')
    except (IOError, OSError) as e:
        logging.exception(e)
        logging.error('Failed to load config.')
        raise e
    
    return config_data


def _create_config_dir():
    config_dir = env.APP_CONFIG_DIR

    try:
        os.makedirs(config_dir)
        logging.info('Created config directory')
    except IOError as ioe:
        logging.exception(ioe)
        logging.error('Unable to create config directory')
        raise ioe


def _create_config_file():
    config_file = env.APP_CONFIG_FILE

    try:
        with open(config_file, 'w+') as cf:
            json.dump(APP_DEFAULT_CONFIG, cf)
        logging.info('Created default config file')
    except IOError as ioe:
        logging.exception(ioe)
        logging.error('Unable to create default config file')
        raise ioe

# import os
# from logging import getLogger
# from argparse import ArgumentParser
# import json

# from .cli import cli


# logger = logging.get_logger(__name__)


# def init(args):
#     # If the config directory doesn't exist, create it.
#     if not os.path.exists(settings.CONFIG_DIR):
#         logger.warning(f'Config directory does not exist at: {settings.CONFIG_DIR}')
#         try:
#             os.makedirs(settings.CONFIG_DIR)
#             logger.success('Created config directory')
#         except IOError as ioe:
#             logger.error(ioe)
#             logger.failure('Unable to create config directory')
#             raise ioe

#     # If the config file doesn't exist, write the default config to it.
#     if not os.path.exists(settings.CONFIG_FILE):
#         logger.warning(f'Default config file does not exist at: {settings.CONFIG_FILE_PATH}')
#         try:
#             with open(settings.CONFIG_FILE, 'w+') as config_file:
#                 json.dump(settings.DEFAULT_CONFIG, config_file)
#             logger.success('Created default config file')
#         except IOError as ioe:
#             logger.error(ioe)
#             logger.failure('Unable to create default config file')
#             raise ioe

#     logger.success('App initialized')
    
#     return True


# def load_config(args):
#     '''
#     Load app configuration from JSON file.
#     If JSON file cannot be found, it will return the default configuration
#     from settings.py.
#     '''

#     config_path = args.config

#     try:
#         logger.info(f'Loading configuration from file: {config_path}')
#         with open(config_path) as config_file:
#             # Attempt to open the configuration file if it exists.
#             config = json.load(config_file)
#         logger.success('Configuration loaded')
#     except (IOError, OSError) as e:
#         # Configuration file does not exist, use default config.

#         logger.failure(f'Failed to load configuration from file')

#         # See if it's in config directory if that wasn't already specified.
#         appended_path = os.path.join('config/', config_path)
#         try:
#             logger.info(f'Attempt #2: Loading configuration from file: {appended_path}')
#             with open(appended_path) as config_file:
#                 config = json.load(config_file)
#             logger.success('Configuration loaded')
#         except (IOError, OSError) as e2:
#             logger.error(e)
#             logger.error(e2)
#             logger.info(f'Using default configuration')
#             config = settings.DEFAULT_CONFIG
    
#     logger.debug(f'Configuration: {config}')
#     return config


# def process(args, config):
#     # Get value A.
#     value_a = config['value_a']
#     logger.info(f'A: {value_a}')

#     # Get value B.
#     # Test for value not in default config.
#     if 'value_b' in config:
#         # The value exists from loaded configuration, proceed.
#         value_b = config['value_b']
#         logger.debug(f'\'value_b\' found in config ({args.config}): {value_b}')
#         logger.info(f'B: {value_b}')
        
#         # Let's add our values in this case.
#         sums = value_a + value_b
#         logger.info(f'A + B = {sums}')

#     logger.success('App finished processing')

#     # Return successfully
#     return os.EX_OK