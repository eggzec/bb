from enum import Enum


class GetBranchesOrderBy(str, Enum):
    ALPHABETICAL = "ALPHABETICAL"
    MODIFICATION = "MODIFICATION"

    def __str__(self) -> str:
        return str(self.value)
