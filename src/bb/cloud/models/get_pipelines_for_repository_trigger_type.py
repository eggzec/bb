from enum import StrEnum


class GetPipelinesForRepositoryTriggerType(StrEnum):
    MANUAL = "MANUAL"
    PARENT_STEP = "PARENT_STEP"
    PUSH = "PUSH"
    SCHEDULED = "SCHEDULED"
