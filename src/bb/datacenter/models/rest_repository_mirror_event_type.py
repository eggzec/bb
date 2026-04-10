from enum import Enum


class RestRepositoryMirrorEventType(str, Enum):
    SYNCHRONIZATION_FAILED = "SYNCHRONIZATION_FAILED"
    SYNCHRONIZED = "SYNCHRONIZED"

    def __str__(self) -> str:
        return str(self.value)
