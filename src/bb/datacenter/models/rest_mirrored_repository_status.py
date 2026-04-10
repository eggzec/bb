from enum import Enum


class RestMirroredRepositoryStatus(str, Enum):
    AVAILABLE = "AVAILABLE"
    ERROR_AVAILABLE = "ERROR_AVAILABLE"
    ERROR_INITIALIZING = "ERROR_INITIALIZING"
    INITIALIZING = "INITIALIZING"
    NOT_MIRRORED = "NOT_MIRRORED"

    def __str__(self) -> str:
        return str(self.value)
