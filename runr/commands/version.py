from .command import register_command

@register_command('--version', '-v')
def print_version():
    print("runr version: 1.0.0")