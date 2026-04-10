from enum import Enum


class RestRepositoryRefChangeActivityRefChangeUpdatedType(str, Enum):
    FORCED = "FORCED"
    NOT_FORCED = "NOT_FORCED"
    UNKNOWN = "UNKNOWN"
    UNRESOLVED = "UNRESOLVED"

    def __str__(self) -> str:
        return str(self.value)
