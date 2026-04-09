from enum import StrEnum


class GetPipelinesForRepositoryTargetSelectorType(StrEnum):
    BRANCH = "BRANCH"
    CUSTOM = "CUSTOM"
    DEFAULT = "DEFAULT"
    PULLREQUESTS = "PULLREQUESTS"
    TAG = "TAG"
