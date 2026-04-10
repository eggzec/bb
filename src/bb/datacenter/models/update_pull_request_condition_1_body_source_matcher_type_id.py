from enum import Enum


class UpdatePullRequestCondition1BodySourceMatcherTypeId(str, Enum):
    ANY_REF = "ANY_REF"
    BRANCH = "BRANCH"
    MODEL_BRANCH = "MODEL_BRANCH"
    MODEL_CATEGORY = "MODEL_CATEGORY"
    PATTERN = "PATTERN"

    def __str__(self) -> str:
        return str(self.value)
