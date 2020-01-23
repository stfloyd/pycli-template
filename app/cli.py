import os
import sys
import logging
from argparse import ArgumentParser, RawTextHelpFormatter

from . import (
    APP_CLI_HELP_TEXT,
    env,
    commands,
    config
)

from .__version__ import __version__


# -----------------------------------------------------------------------------
# CLI Definition

def cli(argv):
    """
    Initialize our argument parser given arguments and
    return the parsed args & parser.
    """

    # Get our parser.
    parser = _create_parser(argv)

    # Parse the arguments via our argument parser.
    args = parser.parse_args(argv[1:])

    commands.print_config()
    config.load(args)
    commands.print_config()

    # Return our args and the parser for parser.print_help(), etc.
    return (args, parser)


def _create_parser(argv):
    # argv[0] is always the filename being executed.
    # In this case it is the name of our program/entry point.
    program_name = argv[0]

    # Create an argument parser to handle our command line arguments.
    parser = ArgumentParser(
        prog=program_name,
        description=APP_CLI_HELP_TEXT,
        formatter_class=RawTextHelpFormatter
    )

    # Verbose mode switch
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='enable verbose output'
    )

    # Output program version information.
    parser.add_argument(
        '--version',
        action='version',
        version=__version__
    )

    return parser