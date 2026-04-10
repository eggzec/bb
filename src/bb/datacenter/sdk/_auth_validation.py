"""Authentication validation for the Bitbucket Data Center SDK.

Bitbucket Data Center REST API endpoints accept two authentication schemes:

    bearer  – Personal Access Token sent as ``Authorization: Bearer <token>``
    basic   – HTTP Basic Auth (Base-64 of ``username:password``)

The SDK maps these to ``AuthenticatedClient.prefix`` values set by the auth
factories in ``_auth.py``:

    "Bearer" → bearer   (PersonalAccessTokenAuth)
    "Basic"  → basic    (BasicAuth)

Usage in SDK methods::

    from bb.datacenter.sdk._auth_validation import AuthMethod, require_auth

    @require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
    async def get(client: BBDCClient, ...) -> ...:
        ...
"""

from __future__ import annotations

from enum import StrEnum
from typing import TYPE_CHECKING

from bb.datacenter.sdk._errors import AuthenticationError
from bb.shared._auth_validation import make_require_auth

if TYPE_CHECKING:
    from bb.datacenter.client import AuthenticatedClient
    from bb.datacenter.sdk._client import BBDCClient


class AuthMethod(StrEnum):
    """Authentication methods recognised by the Bitbucket Data Center SDK.

    Values describe the wire-level auth mechanism used by each endpoint.
    """

    BEARER = "bearer"
    BASIC = "basic"


# All Bitbucket Data Center REST endpoints accept both methods.
BB_DC_AUTH_METHODS: frozenset[AuthMethod] = frozenset(
    {
        AuthMethod.BEARER,
        AuthMethod.BASIC,
    }
)

# Maps the ``prefix`` field of AuthenticatedClient → AuthMethod.
_PREFIX_TO_METHOD: dict[str, AuthMethod] = {
    "Bearer": AuthMethod.BEARER,
    "Basic": AuthMethod.BASIC,
}


def _infer_method(auth_client: AuthenticatedClient) -> AuthMethod | None:
    """Infer the :class:`AuthMethod` from *auth_client*.prefix.

    Returns ``None`` if the prefix is not recognised.
    """
    return _PREFIX_TO_METHOD.get(auth_client.prefix)


def _validate(client: BBDCClient, allowed: frozenset[AuthMethod]) -> None:
    """Validate *client* auth against *allowed* methods.

    Args:
        client: The :class:`~bb.datacenter.sdk._client.BBDCClient` to validate.
                ``client.auth`` is accessed here.
        allowed: Frozenset of :class:`AuthMethod` values accepted by the
                 endpoint.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If the
            underlying :class:`~bb.datacenter.client.AuthenticatedClient` has
            an unrecognised ``prefix``, or if the inferred method is not in
            *allowed*.
    """
    auth_client: AuthenticatedClient = client.auth
    method = _infer_method(auth_client)

    if method is None:
        raise AuthenticationError(
            allowed=allowed,
            actual=f"unknown (prefix={auth_client.prefix!r})",
        )

    if method not in allowed:
        raise AuthenticationError(allowed=allowed, actual=str(method))


# Bind the shared decorator factory to this target's validation function.
# ``require_auth`` has the same call signature and semantics as before;
# the decorator machinery lives in bb.shared.
require_auth = make_require_auth(_validate)
"""Decorator factory that declares and enforces accepted DC auth methods.

Apply to every SDK function that wraps an authenticated Bitbucket Data
Center endpoint.  Pass each :class:`AuthMethod` the endpoint accepts
individually.

``client`` (always the first positional argument in SDK functions) is
validated before the wrapped function body runs.

Args:
    *methods: One or more :class:`AuthMethod` values accepted by this
              endpoint.  For all Bitbucket Data Center endpoints pass::

                  AuthMethod.BEARER, AuthMethod.BASIC

Raises:
    :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: Raised *at call
        time* if the ``client`` argument does not carry a recognised,
        allowed auth method.

Example::

    from bb.datacenter.sdk._auth_validation import AuthMethod, require_auth

    @require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
    async def get(client: BBDCClient, project_key: str, repo_slug: str) -> RestRepository | None:
        result = await get_repository.asyncio(project_key, repo_slug, client=client.auth)
        return result if isinstance(result, RestRepository) else None
"""
