from enum import Enum


class RestRepositoryRefChangeActivityRefChangeRefType(str, Enum):
    BRANCH = "BRANCH"
    TAG = "TAG"

    def __str__(self) -> str:
        return str(self.value)
