from enum import Enum


class ElevatePermissionsWithRecoveryCodeActionType(str, Enum):
    UNLOCK_USER_2SV_SETTINGS = "unlock-user-2sv-settings"

    def __str__(self) -> str:
        return str(self.value)
