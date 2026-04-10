from enum import Enum


class RestCommentParentThreadResolverType(str, Enum):
    NORMAL = "NORMAL"
    SERVICE = "SERVICE"

    def __str__(self) -> str:
        return str(self.value)
