from enum import Enum


class RestLabelableLabelableType(str, Enum):
    REPOSITORY = "REPOSITORY"

    def __str__(self) -> str:
        return str(self.value)
