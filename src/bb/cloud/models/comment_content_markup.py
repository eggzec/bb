from enum import StrEnum


class CommentContentMarkup(StrEnum):
    CREOLE = "creole"
    MARKDOWN = "markdown"
    PLAINTEXT = "plaintext"
