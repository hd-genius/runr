#!/usr/bin/env python3

import sys
from runr.plugins import load_plugins
from runr.commands import is_program_command, run_command
from runr.search import find_script_with_name
from runr.errors import ApplicationError


def main():
    try:
        load_plugins()
        first_argument = sys.argv[1]
        if (is_program_command(first_argument)):
            run_command(first_argument)
        else:
            find_script_with_name(first_argument).execute()
    except ApplicationError as error:
        error.print()


if __name__ == "__main__":
    main()
