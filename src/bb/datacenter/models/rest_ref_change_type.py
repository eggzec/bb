from enum import Enum


class RestRefChangeType(str, Enum):
    ADD = "ADD"
    DELETE = "DELETE"
    UPDATE = "UPDATE"

    def __str__(self) -> str:
        return str(self.value)
