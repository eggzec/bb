from enum import Enum


class RestJobMessageSeverity(str, Enum):
    ERROR = "ERROR"
    INFO = "INFO"
    WARN = "WARN"

    def __str__(self) -> str:
        return str(self.value)
