import os

from bb.cloud.client import AuthenticatedClient
from bb.cloud.sdk._auth import BaseAuth, auto_detect_auth


class BBClient:
    """Bitbucket Cloud SDK client.

    Wraps an AuthenticatedClient from the generated API layer and handles
    token refresh for auth methods with expiring tokens (OAuth CC, JWT).

    Usage::

        # Auto-detect auth from environment variables
        client = BBClient.from_env()

        # Or provide auth explicitly
        from bb.cloud.sdk._auth import APITokenAuth
        client = BBClient(auth=APITokenAuth(email="...", token="..."))

    References:
    - https://support.atlassian.com/bitbucket-cloud/docs/using-api-tokens/
    - https://support.atlassian.com/bitbucket-cloud/docs/use-oauth-on-bitbucket-cloud/
    - https://developer.atlassian.com/cloud/bitbucket/authentication-for-apps/
    """

    def __init__(self, auth: BaseAuth, workspace: str | None = None) -> None:
        self._auth_method = auth
        self._client: AuthenticatedClient = auth.get_authenticated_client()
        self.workspace = workspace or os.environ.get("BB_WORKSPACE")

    @classmethod
    def from_env(cls) -> "BBClient":
        """Build a BBClient from environment variables.

        Auto-detects auth method in this order:
        1. API Token: BB_EMAIL + BB_TOKEN
        2. OAuth Client Credentials: BB_OAUTH_CLIENT_ID + BB_OAUTH_CLIENT_SECRET
        3. OAuth Token: BB_OAUTH_TOKEN
        4. JWT: BB_JWT_CLIENT_KEY + BB_JWT_CLIENT_SECRET
        5. App Password: BB_USERNAME + BB_APP_PASSWORD (deprecated)

        Optional: BB_WORKSPACE sets the default workspace slug.

        Raises RuntimeError if no valid auth method is found.
        """
        return cls(auth=auto_detect_auth(), workspace=os.environ.get("BB_WORKSPACE"))

    @property
    def auth(self) -> AuthenticatedClient:
        """The AuthenticatedClient to pass to generated asyncio() functions.

        Auto-refreshes the underlying token for OAuth CC and JWT auth.
        """
        if self._auth_method.is_expired():
            self._client = self._auth_method.get_authenticated_client()
        return self._client
