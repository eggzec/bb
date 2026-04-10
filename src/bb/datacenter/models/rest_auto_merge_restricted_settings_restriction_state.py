from enum import Enum


class RestAutoMergeRestrictedSettingsRestrictionState(str, Enum):
    NONE = "NONE"
    RESTRICTED_MODIFIABLE = "RESTRICTED_MODIFIABLE"
    RESTRICTED_UNMODIFIABLE = "RESTRICTED_UNMODIFIABLE"

    def __str__(self) -> str:
        return str(self.value)
