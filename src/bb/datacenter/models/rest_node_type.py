from enum import Enum


class RestNodeType(str, Enum):
    BITBUCKET = "BITBUCKET"
    MESH = "MESH"

    def __str__(self) -> str:
        return str(self.value)
