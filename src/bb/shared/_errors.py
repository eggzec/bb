"""Shared SDK-level exceptions for Bitbucket SDK targets.

Both Cloud and Data Center SDKs expose an ``AuthenticationError`` class.
This module provides the shared base so the message structure is consistent
while each target can supply a target-specific hint.
"""

from __future__ import annotations


class AuthenticationError(Exception):
    """Raised when a Bitbucket SDK client's auth method is not accepted by an
    endpoint.

    The auth method is inferred from the ``prefix`` field of the underlying
    :class:`~bb.cloud.client.AuthenticatedClient` (or its DC equivalent) and
    must map to one of the allowed :class:`AuthMethod` members for the target.

    Attributes:
        allowed: :class:`frozenset` of :class:`AuthMethod` values accepted by
            the endpoint.
        actual:  String describing the inferred auth method
            (e.g. ``"oauth2"`` or ``"unknown (prefix='Digest')"``)

    Args:
        allowed: Frozenset of accepted auth methods.
        actual:  String describing what the client is actually using.
        hint:    Optional target-specific guidance appended to the message
                 (e.g. ``"Use APITokenAuth or OAuthTokenAuth to build a BBClient."``)
    """

    def __init__(self, *, allowed: frozenset, actual: str, hint: str = "") -> None:
        self.allowed = allowed
        self.actual = actual
        allowed_names = ", ".join(sorted(v.value if hasattr(v, "value") else str(v) for v in allowed))
        message = f"Auth method {actual!r} is not accepted by this endpoint. Accepted: {allowed_names}."
        if hint:
            message = f"{message} {hint}"
        super().__init__(message)
