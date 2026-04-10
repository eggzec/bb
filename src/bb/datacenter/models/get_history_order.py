from enum import Enum


class GetHistoryOrder(str, Enum):
    FREQUENCY = "FREQUENCY"
    NEWEST = "NEWEST"

    def __str__(self) -> str:
        return str(self.value)
