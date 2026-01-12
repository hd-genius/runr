import os
from pathlib import Path

from runr.errors import ConfigurationError

PROGRAM_HOME_VAR = 'RUNR_HOME'

def get_program_home():
    if PROGRAM_HOME_VAR not in os.environ:
        raise ConfigurationError(f'The environment variable "{PROGRAM_HOME_VAR}" is not set.')
    home_path = Path(os.environ[PROGRAM_HOME_VAR])
    if not home_path.exists():
        raise ConfigurationError(f'The value of "{PROGRAM_HOME_VAR}" is "{home_path}" but the path does not exist.')
    if not home_path.is_dir():
        raise ConfigurationError(f'The value of "{PROGRAM_HOME_VAR}" is "{home_path}" but the path is not a directory.')
    return home_path