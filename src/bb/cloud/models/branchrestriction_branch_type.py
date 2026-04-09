from enum import StrEnum


class BranchrestrictionBranchType(StrEnum):
    BUGFIX = "bugfix"
    DEVELOPMENT = "development"
    FEATURE = "feature"
    HOTFIX = "hotfix"
    PRODUCTION = "production"
    RELEASE = "release"
