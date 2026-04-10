from enum import Enum


class NextLoginStepDTONextLoginStep(str, Enum):
    ENROLLMENT = "ENROLLMENT"
    TOTP_CODE_VERIFICATION = "TOTP_CODE_VERIFICATION"

    def __str__(self) -> str:
        return str(self.value)
