from pathlib import Path
import subprocess
import os

from runr.api import register_script, Script


@register_script
class PowerShellScript(Script):
    @classmethod
    def can_handle(self, file: Path) -> bool:
        return file.suffix == ".sh"

    def __init__(self, file: Path) -> None:
        super().__init__(file)

    def execute(self):
        subprocess.run([self.path])
