from enum import Enum


class RestCommentParentAnchorFileType(str, Enum):
    FROM = "FROM"
    TO = "TO"

    def __str__(self) -> str:
        return str(self.value)
