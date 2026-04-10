from enum import Enum


class RestScopeType(str, Enum):
    GLOBAL = "GLOBAL"
    PROJECT = "PROJECT"
    REPOSITORY = "REPOSITORY"

    def __str__(self) -> str:
        return str(self.value)
