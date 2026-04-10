from enum import Enum


class RestMirrorServerMirrorType(str, Enum):
    FARM = "FARM"
    SINGLE = "SINGLE"

    def __str__(self) -> str:
        return str(self.value)
