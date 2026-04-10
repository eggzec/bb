from enum import Enum


class IdpConfigEntitySignatureAlgorithm(str, Enum):
    RSA_SHA256 = "RSA_SHA256"
    RSA_SHA384 = "RSA_SHA384"
    RSA_SHA512 = "RSA_SHA512"

    def __str__(self) -> str:
        return str(self.value)
