from enum import StrEnum


class IssueChangeMessageMarkup(StrEnum):
    CREOLE = "creole"
    MARKDOWN = "markdown"
    PLAINTEXT = "plaintext"
