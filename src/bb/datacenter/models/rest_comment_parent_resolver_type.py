from enum import Enum


class RestCommentParentResolverType(str, Enum):
    NORMAL = "NORMAL"
    SERVICE = "SERVICE"

    def __str__(self) -> str:
        return str(self.value)
