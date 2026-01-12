from pathlib import Path
import shutil
import subprocess

from runr.api import register_script, Script


@register_script
class PythonScript(Script):
    @classmethod
    def can_handle(self, file: Path) -> bool:
        return file.suffix == ".py"

    def __init__(self, file: Path) -> None:
        super().__init__(file)

    def execute(self):
        python_executable = shutil.which('python')
        if not python_executable:
            python_executable = shutil.which('python3')
        if not python_executable:
            raise Exception('no Python executable could be found')
        subprocess.run([python_executable, self.path])
