from enum import Enum


class RestGitTagCreateRequestType(str, Enum):
    ANNOTATED = "ANNOTATED"
    LIGHTWEIGHT = "LIGHTWEIGHT"

    def __str__(self) -> str:
        return str(self.value)
