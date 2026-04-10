"""BBDCClient — high-level Bitbucket Data Center SDK client."""

from __future__ import annotations

from bb.datacenter.client import AuthenticatedClient
from bb.datacenter.sdk._auth import BaseAuth, auto_detect_auth


class BBDCClient:
    """Bitbucket Data Center SDK client.

    Wraps an :class:`~bb.datacenter.client.AuthenticatedClient` from the
    generated API layer and provides a clean interface for the hand-written SDK
    wrappers.

    Bitbucket Data Center is a self-hosted product so the ``base_url`` is
    always user-supplied.  Set ``BB_DC_BASE_URL`` to the REST root of your
    instance, e.g. ``https://bitbucket.example.com/rest``.

    Usage::

        # Auto-detect auth from environment variables
        client = BBDCClient.from_env()

        # Or provide auth explicitly
        from bb.datacenter.sdk._auth import PersonalAccessTokenAuth
        client = BBDCClient(
            auth=PersonalAccessTokenAuth(token="your-pat", base_url="https://bitbucket.example.com/rest")
        )

    References:
    - https://confluence.atlassian.com/bitbucketserver/personal-access-tokens-939515499.html
    - https://confluence.atlassian.com/bitbucketserver/rest-api-67473606.html
    """

    def __init__(self, auth: BaseAuth) -> None:
        self._auth_method = auth
        self._client: AuthenticatedClient = auth.get_authenticated_client()

    @classmethod
    def from_env(cls) -> BBDCClient:
        """Build a BBDCClient from environment variables.

        Auto-detects auth method in this order:
        1. Personal Access Token: BB_DC_TOKEN
        2. Basic Auth: BB_DC_USERNAME + BB_DC_PASSWORD

        ``BB_DC_BASE_URL`` must also be set to the REST root of your Bitbucket
        instance (e.g. ``https://bitbucket.example.com/rest``).

        Raises RuntimeError if no valid auth method is found.
        """
        return cls(auth=auto_detect_auth())

    @property
    def auth(self) -> AuthenticatedClient:
        """The AuthenticatedClient to pass to generated asyncio() functions.

        Auto-refreshes the underlying token for auth methods with expiring
        tokens (not applicable currently for DC auth, but kept for symmetry
        with the Cloud SDK).
        """
        if self._auth_method.is_expired():
            self._client = self._auth_method.get_authenticated_client()
        return self._client
