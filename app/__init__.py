import os
from logging import getLogger
from argparse import ArgumentParser
import json

import app.settings as settings
from app.logging import create_logger


# -----------------------------------------------------------------------------
# CLI Definition

def cli(argv):
    '''
    Initialize our argument parser given arguments and
    return the parsed args & parser.
    '''

    # argv[0] is always the filename being executed.
    # In this case it is the name of our program/entry point.
    program_name = argv[0]

    # Create an argument parser to handle our command line arguments.
    parser = ArgumentParser(
        prog=program_name,
        description=settings.PROGRAM_DESCRIPTION
    )

    # Configuration File Path (Optional)
    parser.add_argument(
        '-c', '--config',
        type=str,
        required=False,
        metavar='json_file',
        default=settings.CONFIG_FILE_PATH,
        help='specify config file path'
    )

    # Verbose mode switch
    parser.add_argument(
        '-v', '--verbose',
        action='store_true'
    )

    # Output program version information.
    parser.add_argument(
        '--version',
        action='version',
        version=f'{settings.PROGRAM_NAME_VERBOSE} {settings.PROGRAM_VERSION}'
    )

    # Parse the arguments via our argument parser.
    args = parser.parse_args(argv[1:])

    # Return our args and the parser for parser.print_help(), etc.
    return (args, parser)


def init(args):
    logger = create_logger(__name__, args.verbose)

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
    if not os.path.exists(settings.CONFIG_FILE_PATH):
        logger.warning(f'Default config file does not exist at: {settings.CONFIG_FILE_PATH}')
        try:
            with open(settings.CONFIG_FILE_PATH, 'w+') as config_file:
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

    logger = getLogger(__name__)

    config_path = args.config

    try:
        logger.info(f'Loading configuration from file: {config_path}')
        with open(config_path) as config_file:
            # Attempt to open the configuration file if it exists.
            config = json.load(config_file)
        logger.success('Configuration loaded')
    except (IOError, OSError) as e:
        # Configuration file does not exist, use default config.
        logger.error(e.args[1])
        logger.failure(f'Failed to load configuration from file')
        logger.info(f'Using default configuration')
        config = settings.DEFAULT_CONFIG
    
    logger.debug(f'Configuration: {config}')
    return config


def process(args, config):
    logger = getLogger(__name__)

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

    # Return successfully
    return os.EX_OK