from enum import Enum


class RestJobState(str, Enum):
    ABORTED = "ABORTED"
    CANCELED = "CANCELED"
    CANCELING = "CANCELING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    FINALISING = "FINALISING"
    INITIALISING = "INITIALISING"
    READY = "READY"
    RUNNING = "RUNNING"
    TIMED_OUT = "TIMED_OUT"

    def __str__(self) -> str:
        return str(self.value)
