import os
import sys
import logging
from argparse import ArgumentParser, RawTextHelpFormatter

from app import settings


# -----------------------------------------------------------------------------
# CLI Definition

def cli(argv):
    """
    Initialize our argument parser given arguments and
    return the parsed args & parser.
    """

    # argv[0] is always the filename being executed.
    # In this case it is the name of our program/entry point.
    program_name = argv[0]

    # Create an argument parser to handle our command line arguments.
    parser = ArgumentParser(
        prog=program_name,
        description=settings.CLI_HELP_TEXT,
        formatter_class=RawTextHelpFormatter
    )

    # Configuration File Path (Optional)
    parser.add_argument(
        '--config',
        type=str,
        required=False,
        metavar='FILE',
        default=settings.CONFIG_FILE,
        help='specify config file path'
    )

    # List available configs
    parser.add_argument(
        '-l', '--list-configs',
        action='store_true',
        help='print a list of available configs'
    )

    # Verbose mode switch
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='enable verbose console'
    )

    # Output program version information.
    parser.add_argument(
        '--version',
        action='version',
        version=f'{settings.PROGRAM_NAME_VERBOSE} {settings.PROGRAM_VERSION}'
    )

    # Parse the arguments via our argument parser.
    args = parser.parse_args(argv[1:])

    if args.verbose is not None and args.verbose:
        settings.STREAM_LOGGERS.append((logging.DEBUG, sys.stdout))

    # Return our args and the parser for parser.print_help(), etc.
    return (args, parser)