from enum import StrEnum


class ProjectBranchingModelBranchTypesItemKind(StrEnum):
    BUGFIX = "bugfix"
    FEATURE = "feature"
    HOTFIX = "hotfix"
    RELEASE = "release"
