from enum import Enum


class RestMailConfigurationAuthType(str, Enum):
    BASIC = "BASIC"
    OAUTH2 = "OAUTH2"

    def __str__(self) -> str:
        return str(self.value)
