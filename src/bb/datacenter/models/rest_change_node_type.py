from enum import Enum


class RestChangeNodeType(str, Enum):
    DIRECTORY = "DIRECTORY"
    FILE = "FILE"
    SUBMODULE = "SUBMODULE"

    def __str__(self) -> str:
        return str(self.value)
