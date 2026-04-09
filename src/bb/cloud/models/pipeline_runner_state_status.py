from enum import StrEnum


class PipelineRunnerStateStatus(StrEnum):
    DISABLED = "DISABLED"
    ENABLED = "ENABLED"
    OFFLINE = "OFFLINE"
    ONLINE = "ONLINE"
    UNHEALTHY = "UNHEALTHY"
    UNREGISTERED = "UNREGISTERED"
