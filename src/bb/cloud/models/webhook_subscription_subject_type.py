from enum import StrEnum


class WebhookSubscriptionSubjectType(StrEnum):
    REPOSITORY = "repository"
    WORKSPACE = "workspace"
