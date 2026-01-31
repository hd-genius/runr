from pathlib import Path
import subprocess
from runr.api import register_script, Script


@register_script
class PowerShellScript(Script):
    @classmethod
    def can_handle(self, file: Path) -> bool:
        return file.suffix == ".ps1"

    def __init__(self, file: Path) -> None:
        super().__init__(file)

    def execute(self):
        subprocess.run(['powershell', self.path])
