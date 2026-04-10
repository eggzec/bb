from enum import Enum


class RestUpstreamServerState(str, Enum):
    INITIALIZING = "INITIALIZING"
    INSTALLED = "INSTALLED"
    PENDING = "PENDING"
    REMOVED = "REMOVED"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
