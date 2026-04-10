from enum import Enum


class RestRefSyncRequestAction(str, Enum):
    DISCARD = "DISCARD"
    MERGE = "MERGE"
    REBASE = "REBASE"

    def __str__(self) -> str:
        return str(self.value)
