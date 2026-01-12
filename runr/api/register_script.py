from .script import Script

script_classes: list[type] = []


def register_script(script_class):
    """A decorator that registers a class as a script handler."""
    script_classes.append(script_class)
    return script_class
