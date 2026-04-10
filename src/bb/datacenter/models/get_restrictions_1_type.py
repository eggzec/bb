from enum import Enum


class GetRestrictions1Type(str, Enum):
    FAST_FORWARD_ONLY = "fast-forward-only"
    NO_CREATES = "no-creates"
    NO_DELETES = "no-deletes"
    PULL_REQUEST_ONLY = "pull-request-only"
    READ_ONLY = "read-only"

    def __str__(self) -> str:
        return str(self.value)
