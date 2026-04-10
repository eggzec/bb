from enum import Enum


class MethodStateDTOType(str, Enum):
    TOTP = "TOTP"

    def __str__(self) -> str:
        return str(self.value)
