from enum import Enum


class RestAutoMergeProjectSettingsRequestRestrictionAction(str, Enum):
    CREATE = "CREATE"
    DELETE = "DELETE"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
