from enum import StrEnum


class GetPipelinesForRepositoryTargetRefType(StrEnum):
    ANNOTATED_TAG = "ANNOTATED_TAG"
    BRANCH = "BRANCH"
    TAG = "TAG"
