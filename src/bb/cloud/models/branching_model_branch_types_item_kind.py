from enum import StrEnum


class BranchingModelBranchTypesItemKind(StrEnum):
    BUGFIX = "bugfix"
    FEATURE = "feature"
    HOTFIX = "hotfix"
    RELEASE = "release"
