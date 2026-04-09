from enum import StrEnum


class EffectiveRepoBranchingModelBranchTypesItemKind(StrEnum):
    BUGFIX = "bugfix"
    FEATURE = "feature"
    HOTFIX = "hotfix"
    RELEASE = "release"
