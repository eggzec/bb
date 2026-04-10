from enum import Enum


class RestHookScriptType(str, Enum):
    POST = "POST"
    PRE = "PRE"

    def __str__(self) -> str:
        return str(self.value)
