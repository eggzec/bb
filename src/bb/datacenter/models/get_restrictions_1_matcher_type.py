from enum import Enum


class GetRestrictions1MatcherType(str, Enum):
    BRANCH = "BRANCH"
    MODEL_BRANCH = "MODEL_BRANCH"
    MODEL_CATEGORY = "MODEL_CATEGORY"
    PATTERN = "PATTERN"

    def __str__(self) -> str:
        return str(self.value)
