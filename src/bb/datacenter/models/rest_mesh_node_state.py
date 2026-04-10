from enum import Enum


class RestMeshNodeState(str, Enum):
    AVAILABLE = "AVAILABLE"
    DELETING = "DELETING"
    DISABLED = "DISABLED"
    DRAINING = "DRAINING"
    OFFLINE = "OFFLINE"

    def __str__(self) -> str:
        return str(self.value)
