from enum import Enum


class GetRepositoryHooksType(str, Enum):
    POST_RECEIVE = "POST_RECEIVE"
    PRE_RECEIVE = "PRE_RECEIVE"

    def __str__(self) -> str:
        return str(self.value)
