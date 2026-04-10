from enum import Enum


class RestDeploymentSetRequestState(str, Enum):
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    PENDING = "PENDING"
    ROLLED_BACK = "ROLLED_BACK"
    SUCCESSFUL = "SUCCESSFUL"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
