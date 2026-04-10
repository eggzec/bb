from enum import Enum


class RestBuildStatusSetRequestState(str, Enum):
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    INPROGRESS = "INPROGRESS"
    SUCCESSFUL = "SUCCESSFUL"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
