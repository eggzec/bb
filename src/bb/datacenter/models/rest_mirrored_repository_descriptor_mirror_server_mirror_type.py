from enum import Enum


class RestMirroredRepositoryDescriptorMirrorServerMirrorType(str, Enum):
    FARM = "FARM"
    SINGLE = "SINGLE"

    def __str__(self) -> str:
        return str(self.value)
