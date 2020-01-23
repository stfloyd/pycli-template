import os
import sys
import warnings

from .__version__ import __version__


# -----------------------------------------------------------------------------
# Application Information

APP_NAME = 'app'
APP_NAME_VERBOSE = 'Python CLI Template'
APP_DESCRIPTION = 'A python command line utility.'
APP_VERSION = __version__

APP_CLI_HELP_TEXT = \
f"""
{APP_NAME_VERBOSE}
{APP_DESCRIPTION}

 _                 _    
| |               | |   
| |__   ___  _ __ | | __
| '_ \ / _ \| '_ \| |/ /
| | | | (_) | | | |   < 
|_| |_|\___/|_| |_|_|\_\ 
"""

APP_ROOT = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

APP_DEFAULT_CONFIG = {
    'test': 0
}

from .core import AppConfig
config = AppConfig()

from .cli import cli

if __name__ == "__main__":
    cli(sys.argv)