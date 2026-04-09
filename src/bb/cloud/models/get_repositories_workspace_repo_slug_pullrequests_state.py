from enum import StrEnum


class GetRepositoriesWorkspaceRepoSlugPullrequestsState(StrEnum):
    DECLINED = "DECLINED"
    MERGED = "MERGED"
    OPEN = "OPEN"
    SUPERSEDED = "SUPERSEDED"
