from enum import StrEnum


class RepositoryForkPolicy(StrEnum):
    ALLOW_FORKS = "allow_forks"
    NO_FORKS = "no_forks"
    NO_PUBLIC_FORKS = "no_public_forks"
