from enum import Enum


class ElevatePermissionsWithPasswordActionType(str, Enum):
    UNLOCK_USER_2SV_SETTINGS = "unlock-user-2sv-settings"

    def __str__(self) -> str:
        return str(self.value)
