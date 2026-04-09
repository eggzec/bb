from enum import StrEnum


class BranchingModelSettingsBranchTypesItemKind(StrEnum):
    BUGFIX = "bugfix"
    FEATURE = "feature"
    HOTFIX = "hotfix"
    RELEASE = "release"
