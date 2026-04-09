from enum import StrEnum


class WorkspaceForkingMode(StrEnum):
    ALLOW_FORKS = "allow_forks"
    INTERNAL_ONLY = "internal_only"
