from enum import Enum


class RestIndexingThreadStateCode(str, Enum):
    BROKEN = "BROKEN"
    IDLE = "IDLE"
    PROCESSING = "PROCESSING"
    STOPPED = "STOPPED"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
