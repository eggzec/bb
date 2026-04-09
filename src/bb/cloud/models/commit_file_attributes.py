from enum import StrEnum


class CommitFileAttributes(StrEnum):
    BINARY = "binary"
    EXECUTABLE = "executable"
    LFS = "lfs"
    LINK = "link"
    SUBREPOSITORY = "subrepository"
