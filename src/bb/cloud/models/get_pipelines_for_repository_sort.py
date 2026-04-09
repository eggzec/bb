from enum import StrEnum


class GetPipelinesForRepositorySort(StrEnum):
    CREATED_ON = "created_on"
    CREATOR_UUID = "creator.uuid"
    RUN_CREATION_DATE = "run_creation_date"
