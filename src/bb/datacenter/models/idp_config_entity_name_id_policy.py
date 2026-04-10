from enum import Enum


class IdpConfigEntityNameIdPolicy(str, Enum):
    EMAIL_ADDRESS = "EMAIL_ADDRESS"
    ENCRYPTED = "ENCRYPTED"
    ENTITY = "ENTITY"
    KERBEROS = "KERBEROS"
    NONE = "NONE"
    PERSISTENT = "PERSISTENT"
    TRANSIENT = "TRANSIENT"
    UNSPECIFIED = "UNSPECIFIED"
    WINDOWS_DOMAIN_QUALIFIED_NAME = "WINDOWS_DOMAIN_QUALIFIED_NAME"
    X509_SUBJECT_NAME = "X509_SUBJECT_NAME"

    def __str__(self) -> str:
        return str(self.value)
