from enum import Enum


class RepositoryHookDetailsType(str, Enum):
    POST_RECEIVE = "POST_RECEIVE"
    PRE_PULL_REQUEST_MERGE = "PRE_PULL_REQUEST_MERGE"
    PRE_RECEIVE = "PRE_RECEIVE"

    def __str__(self) -> str:
        return str(self.value)
