from enum import Enum


class RestFarmSynchronizationRequestType(str, Enum):
    INCREMENTAL = "incremental"
    SNAPSHOT = "snapshot"

    def __str__(self) -> str:
        return str(self.value)
