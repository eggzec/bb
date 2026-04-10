from enum import Enum


class RestMailConfigurationProtocol(str, Enum):
    SMTP = "SMTP"
    SMTPS = "SMTPS"

    def __str__(self) -> str:
        return str(self.value)
