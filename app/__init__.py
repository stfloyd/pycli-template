import os
from logging import getLogger
from argparse import ArgumentParser
import json

from app import settings, logging
from app.cli import cli


logger = logging.get_logger(__name__)


def init(args):
    # If the config directory doesn't exist, create it.
    if not os.path.exists(settings.CONFIG_DIR):
        logger.warning(f'Config directory does not exist at: {settings.CONFIG_DIR}')
        try:
            os.makedirs(settings.CONFIG_DIR)
            logger.success('Created config directory')
        except IOError as ioe:
            logger.error(ioe)
            logger.failure('Unable to create config directory')
            raise ioe

    # If the config file doesn't exist, write the default config to it.
    if not os.path.exists(settings.CONFIG_FILE):
        logger.warning(f'Default config file does not exist at: {settings.CONFIG_FILE_PATH}')
        try:
            with open(settings.CONFIG_FILE, 'w+') as config_file:
                json.dump(settings.DEFAULT_CONFIG, config_file)
            logger.success('Created default config file')
        except IOError as ioe:
            logger.error(ioe)
            logger.failure('Unable to create default config file')
            raise ioe

    logger.success('App initialized')
    
    return True


def load_config(args):
    '''
    Load app configuration from JSON file.
    If JSON file cannot be found, it will return the default configuration
    from settings.py.
    '''

    config_path = args.config

    try:
        logger.info(f'Loading configuration from file: {config_path}')
        with open(config_path) as config_file:
            # Attempt to open the configuration file if it exists.
            config = json.load(config_file)
        logger.success('Configuration loaded')
    except (IOError, OSError) as e:
        # Configuration file does not exist, use default config.
        logger.error(e)
        logger.failure(f'Failed to load configuration from file')
        logger.info(f'Using default configuration')
        config = settings.DEFAULT_CONFIG
    
    logger.debug(f'Configuration: {config}')
    return config


def process(args, config):
    # Get value A.
    value_a = config['value_a']
    logger.info(f'A: {value_a}')

    # Get value B.
    # Test for value not in default config.
    if 'value_b' in config:
        # The value exists from loaded configuration, proceed.
        value_b = config['value_b']
        logger.debug(f'\'value_b\' found in config ({args.config}): {value_b}')
        logger.info(f'B: {value_b}')
        
        # Let's add our values in this case.
        sums = value_a + value_b
        logger.info(f'A + B = {sums}')

    logger.success('App finished processing')

    # Return successfully
    return os.EX_OK