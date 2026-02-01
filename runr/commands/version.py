from .command import register_command

@register_command('--version', '-v')
def print_version():
    print("runr version: 0.1.0")