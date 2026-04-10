from enum import Enum


class ElevationMethodRestDTOElevationMethodsItem(str, Enum):
    PASSWORD = "PASSWORD"
    TOTP = "TOTP"

    def __str__(self) -> str:
        return str(self.value)
