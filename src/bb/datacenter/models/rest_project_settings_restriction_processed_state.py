from enum import Enum


class RestProjectSettingsRestrictionProcessedState(str, Enum):
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    PROCESSED = "PROCESSED"
    UNPROCESSED = "UNPROCESSED"

    def __str__(self) -> str:
        return str(self.value)
