from enum import Enum


class RestNodeConnectivitySummaryNodeType(str, Enum):
    BITBUCKET = "BITBUCKET"
    MESH = "MESH"

    def __str__(self) -> str:
        return str(self.value)
