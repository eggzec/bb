from enum import Enum


class SetMailConfigBodyProtocol(str, Enum):
    SMTP = "SMTP"
    SMTPS = "SMTPS"

    def __str__(self) -> str:
        return str(self.value)
