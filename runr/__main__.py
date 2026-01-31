#!/usr/bin/env python3

import sys
import logging

from runr.plugins import load_plugins
from runr.commands import is_program_command, run_command
from runr.search import find_script_with_name
from runr.errors import ApplicationError

def main():
    logging.basicConfig(filename='runr.log', level=logging.INFO)
    try:
        load_plugins()
        try:
            first_argument = sys.argv[1]
        except IndexError:
            print('No argument was provided to runr. Please provide a script name or another argument.'
                  'Use "runr --help for help."')
        if (is_program_command(first_argument)):
            run_command(first_argument)
        else:
            script_arguments = sys.argv[2:]
            find_script_with_name(first_argument).execute()
    except Exception as error:
        error.print()


if __name__ == "__main__":
    main()
