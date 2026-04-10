"""Authentication methods for Bitbucket Data Center API.

Supports:
1. Personal Access Token (Bearer) - single token string
2. Basic Auth - username + password

Bitbucket Data Center is a self-hosted product. The ``base_url`` is therefore
always user-supplied; set ``BB_DC_BASE_URL`` to point at your instance, e.g.
``https://bitbucket.example.com/rest``.

References:
- https://confluence.atlassian.com/bitbucketserver/personal-access-tokens-939515499.html
- https://confluence.atlassian.com/bitbucketserver/basic-authentication-776640346.html
"""

from __future__ import annotations

import base64
import os
from abc import ABC, abstractmethod
from enum import StrEnum

from bb.datacenter.client import AuthenticatedClient


class AuthMethod(StrEnum):
    """Supported authentication methods for Bitbucket Data Center."""

    BEARER = "bearer"  # Personal Access Token
    BASIC = "basic"  # Username + Password


class BaseAuth(ABC):
    """Base class for Bitbucket Data Center authentication methods."""

    method: AuthMethod

    @abstractmethod
    def get_authenticated_client(self) -> AuthenticatedClient:
        """Return a fully configured AuthenticatedClient for the generated API."""

    def is_expired(self) -> bool:
        """Override in subclasses that hold expiring tokens."""
        return False


class PersonalAccessTokenAuth(BaseAuth):
    """Authenticate using a Bitbucket Data Center Personal Access Token.

    The token is sent as ``Authorization: Bearer <token>``.

    References:
    https://confluence.atlassian.com/bitbucketserver/personal-access-tokens-939515499.html

    Usage::

        from bb.datacenter.sdk._auth import PersonalAccessTokenAuth
        auth = PersonalAccessTokenAuth(token="your-pat")
        # or from environment variable BB_DC_TOKEN:
        auth = PersonalAccessTokenAuth.from_env()
    """

    method = AuthMethod.BEARER

    def __init__(self, token: str, base_url: str | None = None) -> None:
        self.token = token
        self.base_url = base_url or os.environ.get("BB_DC_BASE_URL", "http://localhost:7990/rest")

    def get_authenticated_client(self) -> AuthenticatedClient:
        return AuthenticatedClient(base_url=self.base_url, token=self.token, prefix="Bearer")

    def to_dict(self) -> dict:
        return {
            "method": self.method.value,
            "base_url": self.base_url,
            "token_last_4": self.token[-4:] if len(self.token) >= 4 else "****",
        }

    @classmethod
    def from_env(cls) -> PersonalAccessTokenAuth:
        """Load from environment variables: BB_DC_TOKEN, BB_DC_BASE_URL.

        Raises RuntimeError if BB_DC_TOKEN is not set.
        """
        token = os.environ.get("BB_DC_TOKEN", "").strip()
        if not token:
            raise RuntimeError("PersonalAccessTokenAuth requires BB_DC_TOKEN environment variable")
        return cls(token=token)


class BasicAuth(BaseAuth):
    """Authenticate using HTTP Basic Auth (username + password).

    The credentials are sent as ``Authorization: Basic base64(username:password)``.

    References:
    https://confluence.atlassian.com/bitbucketserver/basic-authentication-776640346.html

    Usage::

        from bb.datacenter.sdk._auth import BasicAuth
        auth = BasicAuth(username="admin", password="secret")
        # or from environment variables BB_DC_USERNAME + BB_DC_PASSWORD:
        auth = BasicAuth.from_env()
    """

    method = AuthMethod.BASIC

    def __init__(self, username: str, password: str, base_url: str | None = None) -> None:
        self.username = username
        self.password = password
        self.base_url = base_url or os.environ.get("BB_DC_BASE_URL", "http://localhost:7990/rest")

    def get_authenticated_client(self) -> AuthenticatedClient:
        credentials = f"{self.username}:{self.password}"
        encoded = base64.b64encode(credentials.encode()).decode()
        return AuthenticatedClient(base_url=self.base_url, token=encoded, prefix="Basic")

    def to_dict(self) -> dict:
        return {
            "method": self.method.value,
            "base_url": self.base_url,
            "username": self.username,
        }

    @classmethod
    def from_env(cls) -> BasicAuth:
        """Load from environment variables: BB_DC_USERNAME, BB_DC_PASSWORD, BB_DC_BASE_URL.

        Raises RuntimeError if BB_DC_USERNAME or BB_DC_PASSWORD is not set.
        """
        username = os.environ.get("BB_DC_USERNAME", "").strip()
        password = os.environ.get("BB_DC_PASSWORD", "").strip()
        if not username or not password:
            raise RuntimeError("BasicAuth requires BB_DC_USERNAME and BB_DC_PASSWORD environment variables")
        return cls(username=username, password=password)


def auto_detect_auth() -> BaseAuth:
    """Auto-detect available authentication method from environment variables.

    Priority order:
    1. Personal Access Token: BB_DC_TOKEN
    2. Basic Auth: BB_DC_USERNAME + BB_DC_PASSWORD

    Raises RuntimeError if no valid method is found.
    """
    if os.environ.get("BB_DC_TOKEN"):
        return PersonalAccessTokenAuth.from_env()
    if os.environ.get("BB_DC_USERNAME") and os.environ.get("BB_DC_PASSWORD"):
        return BasicAuth.from_env()
    raise RuntimeError(
        "No valid Bitbucket DC auth found. Set one of: "
        "BB_DC_TOKEN (Personal Access Token), "
        "BB_DC_USERNAME + BB_DC_PASSWORD (Basic Auth). "
        "Also set BB_DC_BASE_URL to point at your Bitbucket instance."
    )
