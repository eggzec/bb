"""Authentication validation for the Bitbucket Cloud SDK.

Per ``context/endpoint_security_index.md`` (generated from ``bb_cloud_fixed.openapi.json``),
every one of the 336 Bitbucket Cloud REST API endpoints accepts exactly three
authentication methods:

    oauth2   – OAuth 2.0 Bearer token
    basic    – HTTP Basic Auth (Base-64 of ``email:token`` or ``username:password``)
    api_key  – API Key; identical wire format to *basic* (Base-64 in Authorization header)

Additionally, Bitbucket Connect apps authenticate with JWT, which is not listed in
the OpenAPI spec but is a documented Bitbucket authentication mechanism.

The SDK maps these to ``AuthenticatedClient.prefix`` values set by the auth factories
in ``_auth.py``:

    "Bearer" → oauth2        (OAuthTokenAuth, OAuthClientCredsAuth)
    "Basic"  → basic/api_key (APITokenAuth, AppPasswordAuth)
    "JWT"    → jwt           (JWTAuth)

Usage in SDK methods::

    from bb.cloud.sdk._auth_validation import AuthMethod, require_auth

    @require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
    async def get(client: BBClient, ...) -> ...:
        ...

Each method's accepted auth methods are declared explicitly in its decorator so
that if a single endpoint's security scheme changes, only that decorator needs updating.
"""

from __future__ import annotations

from enum import StrEnum
from typing import TYPE_CHECKING

from bb.cloud.sdk._errors import AuthenticationError
from bb.shared._auth_validation import make_require_auth

if TYPE_CHECKING:
    from bb.cloud.client import AuthenticatedClient
    from bb.cloud.sdk._client import BBClient


class AuthMethod(StrEnum):
    """Authentication methods recognised by the SDK.

    Values match the security-scheme keys in the Bitbucket Cloud OpenAPI spec,
    plus ``jwt`` for Bitbucket Connect apps.
    """

    OAUTH2 = "oauth2"
    BASIC = "basic"
    API_KEY = "api_key"
    JWT = "jwt"


# Every Bitbucket Cloud REST endpoint accepts exactly these three methods.
BB_CLOUD_AUTH_METHODS: frozenset[AuthMethod] = frozenset(
    {
        AuthMethod.OAUTH2,
        AuthMethod.BASIC,
        AuthMethod.API_KEY,
    }
)

# Maps the ``prefix`` field of AuthenticatedClient → AuthMethod.
# "Basic" satisfies BOTH ``basic`` and ``api_key`` because both use the same
# wire format (Base-64 credentials in the Authorization header).
_PREFIX_TO_METHOD: dict[str, AuthMethod] = {
    "Bearer": AuthMethod.OAUTH2,
    "Basic": AuthMethod.BASIC,
    "JWT": AuthMethod.JWT,
}


def _infer_method(auth_client: AuthenticatedClient) -> AuthMethod | None:
    """Infer the :class:`AuthMethod` from *auth_client*.prefix.

    Returns ``None`` if the prefix is not recognised.
    """
    return _PREFIX_TO_METHOD.get(auth_client.prefix)


def _validate(client: BBClient, allowed: frozenset[AuthMethod]) -> None:
    """Validate *client* auth against *allowed* methods.

    This is the core validation logic called by the :func:`require_auth`
    decorator at function call time.

    Args:
        client: The :class:`~bb.cloud.sdk._client.BBClient` to validate.
                ``client.auth`` is accessed here, which auto-refreshes
                expiring OAuth CC / JWT tokens.
        allowed: Frozenset of :class:`AuthMethod` values accepted by the
                 endpoint.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If the underlying
            :class:`~bb.cloud.client.AuthenticatedClient` has an unrecognised
            ``prefix``, or if the inferred method is not in *allowed*.
    """
    auth_client: AuthenticatedClient = client.auth  # may refresh the token
    method = _infer_method(auth_client)

    if method is None:
        raise AuthenticationError(
            allowed=allowed,
            actual=f"unknown (prefix={auth_client.prefix!r})",
        )

    # "Basic" wire-format satisfies both ``basic`` and ``api_key``.
    satisfied: frozenset[AuthMethod] = (
        frozenset({AuthMethod.BASIC, AuthMethod.API_KEY}) if method is AuthMethod.BASIC else frozenset({method})
    )

    if not satisfied & allowed:
        raise AuthenticationError(allowed=allowed, actual=str(method))


# Bind the shared decorator factory to this target's validation function.
# ``require_auth`` has the same call signature and semantics as before;
# the only change is that the decorator machinery lives in bb.shared.
require_auth = make_require_auth(_validate)
"""Decorator factory that declares and enforces accepted Cloud auth methods.

Apply to every SDK function that wraps an authenticated Bitbucket Cloud
endpoint.  Pass each :class:`AuthMethod` the endpoint accepts individually
so that if a single endpoint's security scheme changes, only that function's
decorator needs updating — not a shared constant.

``client`` (always the first positional argument in SDK functions) is
validated before the wrapped function body runs.  ``"Basic"`` wire-format
satisfies both :attr:`AuthMethod.BASIC` and :attr:`AuthMethod.API_KEY`.

Args:
    *methods: One or more :class:`AuthMethod` values accepted by this
              endpoint.  For all current Bitbucket Cloud endpoints pass::

                  AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: Raised *at call
        time* if the ``client`` argument does not carry a recognised,
        allowed auth method.

Example::

    from bb.cloud.sdk._auth_validation import AuthMethod, require_auth

    @require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
    async def get(client: BBClient, workspace: str, repo_slug: str) -> Repository | None:
        result = await get_repositories_workspace_repo_slug.asyncio(
            workspace, repo_slug, client=client.auth
        )
        return result if isinstance(result, Repository) else None
"""
