import asyncio
import os
from collections.abc import Coroutine
from typing import Any, TypeVar

from bb.cloud.client import AuthenticatedClient
from bb.cloud.sdk._auth import BaseAuth, auto_detect_auth

_T = TypeVar("_T")


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
        self._runner: asyncio.Runner | None = None

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

    # ------------------------------------------------------------------
    # Context manager support
    # ------------------------------------------------------------------

    def __enter__(self) -> "BBClient":
        """Open a sync context: starts a persistent asyncio.Runner.

        Use this when making multiple sequential sync SDK calls on the same
        client.  The runner keeps its event loop open between calls, allowing
        the underlying async httpx client to reuse connections.

        Example::

            with BBClient.from_env() as client:
                repos_list = sync.repos.list(client, workspace)
                branches   = sync.branches.list(client, workspace, repo_slug)
        """
        self._runner = asyncio.Runner()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: object,
    ) -> None:
        """Close the runner and reset the cached async httpx client."""
        if self._runner is not None:
            self._runner.close()
            self._runner = None
        self._client._async_client = None  # type: ignore[attr-defined]

    async def __aenter__(self) -> "BBClient":
        """Open an async context (no-op — async SDK manages its own loop).

        Primarily useful for ensuring ``__aexit__`` cleanup runs.

        Example::

            async with BBClient.from_env() as client:
                result = await repos.list(client, workspace)
        """
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: object,
    ) -> None:
        """Close and clean up the cached async httpx client."""
        async_client = self._client._async_client  # type: ignore[attr-defined]
        if async_client is not None:
            await async_client.aclose()
            self._client._async_client = None  # type: ignore[attr-defined]

    def run_sync(self, coro: Coroutine[Any, Any, _T]) -> _T:
        """Run a coroutine synchronously.

        When ``BBClient`` is used as a sync context manager the persistent
        ``asyncio.Runner`` is reused across calls — the event loop stays open
        and the underlying httpx connection pool is shared.

        Outside a context manager a fresh ``asyncio.run()`` is used per call
        and the cached async httpx client is reset afterwards to prevent
        ``RuntimeError: Event loop is closed`` on subsequent calls.

        Args:
            coro: Coroutine to run (typically ``_async.some_function(client, ...)``).

        Returns:
            Whatever the coroutine returns.
        """
        if self._runner is not None:
            return self._runner.run(coro)
        try:
            return asyncio.run(coro)
        finally:
            self._client._async_client = None  # type: ignore[attr-defined]
