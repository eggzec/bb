from enum import StrEnum


class BranchMergeStrategiesItem(StrEnum):
    FAST_FORWARD = "fast_forward"
    MERGE_COMMIT = "merge_commit"
    REBASE_FAST_FORWARD = "rebase_fast_forward"
    REBASE_MERGE = "rebase_merge"
    SQUASH = "squash"
    SQUASH_FAST_FORWARD = "squash_fast_forward"
