"""Live tests for ``BBClient.from_env()`` and auth method detection.

These tests verify the end-to-end auth flow: the credentials in ``.env`` are
correctly detected, the resulting ``AuthenticatedClient`` carries a sensible
scheme/token prefix, and a trivial authenticated request succeeds.
"""

from __future__ import annotations

import os

import pytest

from bb.cloud.client import AuthenticatedClient
from bb.cloud.sdk import users
from bb.cloud.sdk._auth import (
    APITokenAuth,
    AppPasswordAuth,
    AuthMethod,
    JWTAuth,
    OAuthClientCredsAuth,
    OAuthTokenAuth,
    auto_detect_auth,
)
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live


def _expected_auth_method() -> AuthMethod:
    """Return the auth method ``auto_detect_auth`` should pick given the env."""
    if os.environ.get("BB_EMAIL") and os.environ.get("BB_TOKEN"):
        return AuthMethod.API_TOKEN
    if os.environ.get("BB_OAUTH_CLIENT_ID") and os.environ.get("BB_OAUTH_CLIENT_SECRET"):
        return AuthMethod.OAUTH_CLIENT_CREDS
    if os.environ.get("BB_OAUTH_TOKEN"):
        return AuthMethod.OAUTH_CODE
    if os.environ.get("BB_JWT_CLIENT_KEY") and os.environ.get("BB_JWT_CLIENT_SECRET"):
        return AuthMethod.JWT
    if os.environ.get("BB_USERNAME") and os.environ.get("BB_APP_PASSWORD"):
        return AuthMethod.APP_PASSWORD
    pytest.fail("no recognised auth env vars set but live tests are running")


def test_auto_detect_auth_matches_env() -> None:
    expected = _expected_auth_method()
    auth = auto_detect_auth()
    assert auth.method is expected, (
        f"auto_detect_auth returned {auth.method!r}, expected {expected!r} given the current .env"
    )


def test_auto_detect_auth_instance_type() -> None:
    expected = _expected_auth_method()
    auth = auto_detect_auth()
    expected_cls = {
        AuthMethod.API_TOKEN: APITokenAuth,
        AuthMethod.OAUTH_CLIENT_CREDS: OAuthClientCredsAuth,
        AuthMethod.OAUTH_CODE: OAuthTokenAuth,
        AuthMethod.JWT: JWTAuth,
        AuthMethod.APP_PASSWORD: AppPasswordAuth,
    }[expected]
    assert isinstance(auth, expected_cls), (
        f"auto_detect_auth returned {type(auth).__name__}, expected {expected_cls.__name__}"
    )


def test_bbclient_from_env_builds_authenticated_client(client: BBClient) -> None:
    assert isinstance(client.auth, AuthenticatedClient), (
        f"BBClient.auth must be AuthenticatedClient, got {type(client.auth).__name__}"
    )
    assert client.workspace == os.environ.get("BB_WORKSPACE"), (
        f"BBClient.workspace must echo BB_WORKSPACE; got {client.workspace!r} vs {os.environ.get('BB_WORKSPACE')!r}"
    )


def test_bbclient_auth_prefix_matches_method(client: BBClient) -> None:
    method = _expected_auth_method()
    expected_prefix = {
        AuthMethod.API_TOKEN: "Basic",
        AuthMethod.OAUTH_CLIENT_CREDS: "Bearer",
        AuthMethod.OAUTH_CODE: "Bearer",
        AuthMethod.JWT: "JWT",
        AuthMethod.APP_PASSWORD: "Basic",
    }[method]
    assert client.auth.prefix == expected_prefix, (
        f"auth prefix for {method.value} should be {expected_prefix!r}, got {client.auth.prefix!r}"
    )
    assert client.auth.token, "AuthenticatedClient.token must be populated"


async def test_authenticated_request_succeeds(client: BBClient) -> None:
    """The simplest sanity check: GET /user with the configured auth returns a
    real account. If this fails, every other live test is doomed."""
    from bb.cloud.models.account import Account
    from bb.cloud.models.error import Error

    me = await users.me(client)
    assert me is not None, "users.me returned None — auth likely failed before reaching the API"
    assert not isinstance(me, Error), (
        f"users.me returned Error instead of Account — auth failure: "
        f"{me.error.message if me.error else me!r}"
    )
    assert isinstance(me, Account), f"expected Account, got {type(me).__name__}"


@pytest.mark.live
async def test_bad_token_does_not_return_account(workspace: str) -> None:
    """SDK must not return a valid Account for invalid credentials.

    Uses users.me() which requires a valid session. On a 401, Bitbucket may
    return a non-JSON body; the content-type guard (BUG-GENERATOR-001 fix) then
    returns None rather than Error — both outcomes are acceptable.
    What is NOT acceptable is the SDK returning an Account object for bad creds.
    """
    from bb.cloud.models.account import Account
    from bb.cloud.sdk import users

    bad_client = BBClient(
        auth=APITokenAuth(email="nobody@example.com", token="invalid-token-xyz-000"),
        workspace=workspace,
    )
    result = await users.me(bad_client)
    assert not isinstance(result, Account), (
        f"SDK returned Account for invalid credentials — auth was not enforced. "
        f"Got: {result!r}"
    )
