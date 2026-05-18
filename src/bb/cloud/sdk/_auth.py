"""Authentication methods for Bitbucket Cloud API.

Supports:
1. API Token (Basic Auth) - Email + Token
2. OAuth 2.0 - Authorization Code Grant / Refresh Token
3. OAuth 2.0 - Client Credentials Grant (server-to-server)
4. JWT - For Bitbucket Connect apps
5. App Password (deprecated, until June 2026)

References:
- https://support.atlassian.com/bitbucket-cloud/docs/using-api-tokens/
- https://support.atlassian.com/bitbucket-cloud/docs/use-oauth-on-bitbucket-cloud/
- https://developer.atlassian.com/cloud/bitbucket/authentication-for-apps/
"""

import base64
import os
import time
from abc import ABC, abstractmethod
from datetime import UTC, datetime
from enum import StrEnum

import httpx

from bb.cloud.client import AuthenticatedClient

BASE_URL = "https://api.bitbucket.org/2.0"
OAUTH_URL = "https://bitbucket.org/site/oauth2"


class AuthMethod(StrEnum):
    """Supported authentication methods."""

    API_TOKEN = "api_token"  # Email + API Token (Basic Auth)
    OAUTH_CODE = "oauth_code"  # OAuth 2.0 Authorization Code / Refresh Token
    OAUTH_CLIENT_CREDS = "oauth_client_creds"  # OAuth 2.0 Client Credentials
    JWT = "jwt"  # JWT for Bitbucket Connect apps
    APP_PASSWORD = "app_password"  # Deprecated (until June 2026)


class BaseAuth(ABC):
    """Base class for authentication methods."""

    method: AuthMethod

    @abstractmethod
    def get_authenticated_client(self) -> AuthenticatedClient:
        """Return a fully configured AuthenticatedClient for the generated API."""

    def is_expired(self) -> bool:
        """Override in subclasses that hold expiring tokens."""
        return False


class APITokenAuth(BaseAuth):
    """Authenticate using Email + API Token (Basic Auth).

    References:
    https://support.atlassian.com/bitbucket-cloud/docs/using-api-tokens/
    """

    method = AuthMethod.API_TOKEN

    def __init__(self, email: str, token: str) -> None:
        self.email = email
        self.token = token

    def get_authenticated_client(self) -> AuthenticatedClient:
        credentials = f"{self.email}:{self.token}"
        encoded = base64.b64encode(credentials.encode()).decode()
        return AuthenticatedClient(base_url=BASE_URL, token=encoded, prefix="Basic", follow_redirects=True)

    def to_dict(self) -> dict:
        return {
            "method": self.method.value,
            "email": self.email,
            "token_last_4": self.token[-4:] if len(self.token) >= 4 else "****",
        }

    @classmethod
    def from_env(cls) -> "APITokenAuth":
        """Load from environment variables: BB_EMAIL, BB_TOKEN."""
        email = os.environ.get("BB_EMAIL", "").strip()
        token = os.environ.get("BB_TOKEN", "").strip()
        if not email or not token:
            raise RuntimeError("APITokenAuth requires BB_EMAIL and BB_TOKEN environment variables")
        return cls(email=email, token=token)


class OAuthTokenAuth(BaseAuth):
    """Authenticate using an OAuth 2.0 access token (Bearer).

    The token must be obtained via one of the OAuth 2.0 grant flows:
    - Authorization Code Grant (user login)
    - Refresh Token Grant

    References:
    https://support.atlassian.com/bitbucket-cloud/docs/use-oauth-on-bitbucket-cloud/
    """

    method = AuthMethod.OAUTH_CODE

    def __init__(
        self,
        access_token: str,
        token_type: str = "bearer",
        expires_in: int | None = None,
        refresh_token: str | None = None,
    ) -> None:
        self.access_token = access_token
        self.token_type = token_type
        self.expires_in = expires_in
        self.refresh_token = refresh_token
        self.created_at = datetime.now(UTC)

    def get_authenticated_client(self) -> AuthenticatedClient:
        return AuthenticatedClient(
            base_url=BASE_URL,
            token=self.access_token,
            prefix=self.token_type.capitalize(),
            follow_redirects=True,
        )

    def is_expired(self) -> bool:
        if self.expires_in is None:
            return False
        age = datetime.now(UTC) - self.created_at
        return age.total_seconds() > self.expires_in

    def to_dict(self) -> dict:
        return {
            "method": self.method.value,
            "token_type": self.token_type,
            "expires_in": self.expires_in,
            "token_last_4": self.access_token[-4:] if len(self.access_token) >= 4 else "****",
            "has_refresh_token": self.refresh_token is not None,
        }

    @classmethod
    def from_env(cls) -> "OAuthTokenAuth":
        """Load from environment: BB_OAUTH_TOKEN, BB_OAUTH_EXPIRES, BB_OAUTH_REFRESH."""
        token = os.environ.get("BB_OAUTH_TOKEN", "").strip()
        if not token:
            raise RuntimeError("OAuthTokenAuth requires BB_OAUTH_TOKEN environment variable")
        expires_in = None
        if expires_str := os.environ.get("BB_OAUTH_EXPIRES", "").strip():
            try:
                expires_in = int(expires_str)
            except ValueError:
                pass
        return cls(
            access_token=token,
            expires_in=expires_in,
            refresh_token=os.environ.get("BB_OAUTH_REFRESH", "").strip() or None,
        )


class OAuthClientCredsAuth(BaseAuth):
    """Authenticate using OAuth 2.0 Client Credentials Grant (server-to-server).

    References:
    https://support.atlassian.com/bitbucket-cloud/docs/use-oauth-on-bitbucket-cloud/
    """

    method = AuthMethod.OAUTH_CLIENT_CREDS

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        access_token: str | None = None,
        expires_in: int | None = None,
    ) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token
        self.expires_in = expires_in
        self.created_at: datetime | None = datetime.now(UTC) if access_token else None

    def _fetch_access_token(self) -> tuple[str, int]:
        credentials = f"{self.client_id}:{self.client_secret}"
        encoded = base64.b64encode(credentials.encode()).decode()
        response = httpx.post(
            f"{OAUTH_URL}/access_token",
            headers={"Authorization": f"Basic {encoded}"},
            data={"grant_type": "client_credentials"},
        )
        response.raise_for_status()
        data = response.json()
        return data["access_token"], data.get("expires_in", 3600)

    def get_access_token(self) -> str:
        """Return a valid access token, fetching/refreshing as needed."""
        if self.access_token is None or self.is_expired():
            self.access_token, self.expires_in = self._fetch_access_token()
            self.created_at = datetime.now(UTC)
        return self.access_token

    def is_expired(self) -> bool:
        if self.created_at is None or self.expires_in is None:
            return True
        return (datetime.now(UTC) - self.created_at).total_seconds() > self.expires_in

    def get_authenticated_client(self) -> AuthenticatedClient:
        return AuthenticatedClient(base_url=BASE_URL, token=self.get_access_token(), prefix="Bearer", follow_redirects=True)

    def to_dict(self) -> dict:
        return {
            "method": self.method.value,
            "client_id": self.client_id,
            "client_id_last_4": self.client_id[-4:] if len(self.client_id) >= 4 else "****",
            "has_token": self.access_token is not None,
            "token_expired": self.is_expired(),
        }

    @classmethod
    def from_env(cls) -> "OAuthClientCredsAuth":
        """Load from environment: BB_OAUTH_CLIENT_ID, BB_OAUTH_CLIENT_SECRET."""
        client_id = os.environ.get("BB_OAUTH_CLIENT_ID", "").strip()
        client_secret = os.environ.get("BB_OAUTH_CLIENT_SECRET", "").strip()
        if not client_id or not client_secret:
            raise RuntimeError("OAuthClientCredsAuth requires BB_OAUTH_CLIENT_ID and BB_OAUTH_CLIENT_SECRET")
        return cls(client_id=client_id, client_secret=client_secret)


class JWTAuth(BaseAuth):
    """Authenticate using JWT for Bitbucket Connect apps.

    Generates a session-level JWT token (10-min TTL) at client creation time.
    BBClient.auth auto-refreshes via is_expired().

    References:
    https://developer.atlassian.com/cloud/bitbucket/authentication-for-apps/
    """

    method = AuthMethod.JWT

    def __init__(self, client_key: str, client_secret: str, installation_host: str = "bitbucket.org") -> None:
        self.client_key = client_key
        self.client_secret = client_secret
        self.installation_host = installation_host
        self._issued_at: int = 0

    def _create_jwt_token(self) -> str:
        import hashlib

        try:
            import jwt
        except ImportError:
            raise RuntimeError("JWT auth requires 'PyJWT' package: pip install PyJWT")

        now = int(time.time())
        self._issued_at = now
        qsh = hashlib.sha256(b"GET+/").hexdigest()
        payload = {
            "iss": self.client_key,
            "sub": self.client_key,
            "aud": self.installation_host,
            "iat": now,
            "exp": now + 600,  # 10 minutes
            "qsh": qsh,
        }
        return jwt.encode(payload, self.client_secret, algorithm="HS256")

    def is_expired(self) -> bool:
        return (int(time.time()) - self._issued_at) > 540  # refresh 1 min before expiry

    def get_authenticated_client(self) -> AuthenticatedClient:
        return AuthenticatedClient(base_url=BASE_URL, token=self._create_jwt_token(), prefix="JWT", follow_redirects=True)

    def to_dict(self) -> dict:
        return {
            "method": self.method.value,
            "client_key": self.client_key,
            "client_key_last_4": self.client_key[-4:] if len(self.client_key) >= 4 else "****",
            "installation_host": self.installation_host,
        }

    @classmethod
    def from_env(cls) -> "JWTAuth":
        """Load from environment: BB_JWT_CLIENT_KEY, BB_JWT_CLIENT_SECRET, BB_JWT_HOST."""
        client_key = os.environ.get("BB_JWT_CLIENT_KEY", "").strip()
        client_secret = os.environ.get("BB_JWT_CLIENT_SECRET", "").strip()
        if not client_key or not client_secret:
            raise RuntimeError("JWTAuth requires BB_JWT_CLIENT_KEY and BB_JWT_CLIENT_SECRET environment variables")
        return cls(
            client_key=client_key,
            client_secret=client_secret,
            installation_host=os.environ.get("BB_JWT_HOST", "bitbucket.org").strip(),
        )


class AppPasswordAuth(BaseAuth):
    """Authenticate using App Password (DEPRECATED - support ends June 9, 2026).

    Use APITokenAuth instead.
    """

    method = AuthMethod.APP_PASSWORD

    def __init__(self, username: str, app_password: str) -> None:
        self.username = username
        self.app_password = app_password

    def get_authenticated_client(self) -> AuthenticatedClient:
        credentials = f"{self.username}:{self.app_password}"
        encoded = base64.b64encode(credentials.encode()).decode()
        return AuthenticatedClient(base_url=BASE_URL, token=encoded, prefix="Basic", follow_redirects=True)

    def to_dict(self) -> dict:
        return {
            "method": self.method.value,
            "username": self.username,
            "note": "DEPRECATED - use API Tokens instead. Support ends June 9, 2026.",
        }

    @classmethod
    def from_env(cls) -> "AppPasswordAuth":
        """Load from environment: BB_USERNAME, BB_APP_PASSWORD."""
        username = os.environ.get("BB_USERNAME", "").strip()
        password = os.environ.get("BB_APP_PASSWORD", "").strip()
        if not username or not password:
            raise RuntimeError("AppPasswordAuth requires BB_USERNAME and BB_APP_PASSWORD (DEPRECATED)")
        return cls(username=username, app_password=password)


def auto_detect_auth() -> BaseAuth:
    """Auto-detect available authentication method from environment variables.

    Priority order:
    1. API Token: BB_EMAIL + BB_TOKEN
    2. OAuth Client Credentials: BB_OAUTH_CLIENT_ID + BB_OAUTH_CLIENT_SECRET
    3. OAuth Token: BB_OAUTH_TOKEN
    4. JWT: BB_JWT_CLIENT_KEY + BB_JWT_CLIENT_SECRET
    5. App Password: BB_USERNAME + BB_APP_PASSWORD (deprecated)

    Raises RuntimeError if no valid method is found.
    """
    if os.environ.get("BB_EMAIL") and os.environ.get("BB_TOKEN"):
        return APITokenAuth.from_env()
    if os.environ.get("BB_OAUTH_CLIENT_ID") and os.environ.get("BB_OAUTH_CLIENT_SECRET"):
        return OAuthClientCredsAuth.from_env()
    if os.environ.get("BB_OAUTH_TOKEN"):
        return OAuthTokenAuth.from_env()
    if os.environ.get("BB_JWT_CLIENT_KEY") and os.environ.get("BB_JWT_CLIENT_SECRET"):
        return JWTAuth.from_env()
    if os.environ.get("BB_USERNAME") and os.environ.get("BB_APP_PASSWORD"):
        return AppPasswordAuth.from_env()
    raise RuntimeError(
        "No valid auth found. Set one of: "
        "BB_EMAIL+BB_TOKEN, "
        "BB_OAUTH_CLIENT_ID+BB_OAUTH_CLIENT_SECRET, "
        "BB_OAUTH_TOKEN, "
        "BB_JWT_CLIENT_KEY+BB_JWT_CLIENT_SECRET, "
        "BB_USERNAME+BB_APP_PASSWORD (deprecated)"
    )
