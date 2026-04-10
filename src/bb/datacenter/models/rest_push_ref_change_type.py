from enum import Enum


class RestPushRefChangeType(str, Enum):
    ADD = "ADD"
    DELETE = "DELETE"
    UPDATE = "UPDATE"

    def __str__(self) -> str:
        return str(self.value)
