commands = {}


def register_command(*aliases: list[str]):
    def add_command(command: callable):
        for alias in aliases:
            commands[alias] = command
        return command
    return add_command


def is_program_command(value: str) -> bool:
    return value in commands


def run_command(command: str):
    if command in commands:
        command_to_execute = commands[command]
        command_to_execute()
    else:
        raise UnrecognizedCommandError(command)


class UnrecognizedCommandError(Exception):
    def __init__(self, command):
        super()
        self.command = command
