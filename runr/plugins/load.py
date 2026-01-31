import os
from pathlib import Path
import sys
from importlib import import_module
import logging

from runr.utils import get_program_home


logger = logging.getLogger(__name__)

def load_plugins():
    sys.path.append(str(get_program_home()))
    for plugin in _find_all_plugins():
        _load_plugin(plugin)


def _load_plugin(plugin: Path):
    import_module("plugins." + plugin.stem)
    logger.info(f'The plugin {plugin} was loaded.')


def _find_all_plugins():
    plugin_dir = _get_plugins_directory()
    logger.info(f'The directory {plugin_dir} is assumed to be the plugin install location.')
    files = [Path(os.path.join(plugin_dir, x)) for x in os.listdir(plugin_dir)]
    return [x for x in files if _is_plugin(x)]


def _is_plugin(file: Path):
    return file.suffix == ".py"


def _get_plugins_directory():
    return get_program_home().joinpath('plugins')
