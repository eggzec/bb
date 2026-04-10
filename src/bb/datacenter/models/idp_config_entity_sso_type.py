from enum import Enum


class IdpConfigEntitySsoType(str, Enum):
    NONE = "NONE"
    OIDC = "OIDC"
    SAML = "SAML"

    def __str__(self) -> str:
        return str(self.value)
