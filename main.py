#!/usr/bin/python3

import os
import sys
import errno
import json

import app
from app.logging import create_logger


# -----------------------------------------------------------------------------
# Application Definition

def main(argv):
    '''
    Main entry point into the program.
    '''

    # Get arguments and argument parser.
    (args, parser) = app.cli(argv)

    # Initialize logging and set verbosity level.
    logger = create_logger(__name__, args.verbose)

    logger.debug(f'Program arguments: {argv}')
    # Check if any command arguments have been passed.
    if (len(argv) <= 1):
        # No arguments passed.
        logger.warning(f'No command arguments passed')
        parser.print_help()
        sys.exit(errno.EAGAIN)

    # Initialize our app.
    try:
        app.init(args)
    except Exception as e:
        logger.exception(e)
        logger.failure(f'App initialization failed: {e.errno}')
        return os.EX_SOFTWARE
    
    # Load application configuration.
    try:
        config = app.load_config(args)
    except Exception as e:
        logger.exception(e)
        logger.failure(f'App configuration failed: {e.errno}')
        return os.EX_CONFIG

    # Do something with config before running main app logic.

    # Run main app logic
    try:
        exit_code = app.process(args, config)
    except Exception as e:
        logger.exception(e)
        logger.failure(f'App processing failed: {e.errno}')
        return os.EX_SOFTWARE

    # Handle anything else you need to, we're getting out of here.

    return exit_code


if __name__ == "__main__":
    sys.exit(main(sys.argv))
