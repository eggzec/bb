from enum import Enum


class LoginOptionEntityType(str, Enum):
    IDP = "IDP"
    LEGACY_LOGIN_FORM = "LEGACY_LOGIN_FORM"
    LOGIN_FORM = "LOGIN_FORM"

    def __str__(self) -> str:
        return str(self.value)
