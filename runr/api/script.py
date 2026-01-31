from abc import ABC, abstractmethod
from pathlib import Path


class Script(ABC):
    """The base class representing a script that can be executed"""
    name: str
    path: Path

    @classmethod
    @abstractmethod
    def can_handle(self, file: Path) -> bool:
        """Returns True if this script type can handle the given file, returns False if it cannot."""
        pass

    def __init__(self, file: Path) -> None:
        self.name = file.stem
        self.path = file

    @abstractmethod
    def execute(self):
        """Runs the script file that this object represents"""
        pass
