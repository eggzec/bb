from enum import StrEnum


class PipelineRefTargetRefType(StrEnum):
    BOOKMARK = "bookmark"
    BRANCH = "branch"
    NAMED_BRANCH = "named_branch"
    TAG = "tag"
