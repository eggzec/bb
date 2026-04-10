from enum import Enum


class IdpConfigEntityIdpType(str, Enum):
    CROWD = "CROWD"
    GENERIC = "GENERIC"

    def __str__(self) -> str:
        return str(self.value)
