from .command import register_command


@register_command('--help', '-h')
def print_help():
    print("help text")
