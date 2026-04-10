from enum import Enum


class RestMirroringRequestMirrorType(str, Enum):
    FARM = "FARM"
    SINGLE = "SINGLE"

    def __str__(self) -> str:
        return str(self.value)
