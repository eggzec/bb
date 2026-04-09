"""Tests for authentication validation: AuthMethod enum, require_auth(), AuthenticationError."""

import pytest

from bb.cloud.client import AuthenticatedClient
from bb.cloud.sdk._auth import APITokenAuth, OAuthTokenAuth
from bb.cloud.sdk._auth_validation import (
    BB_CLOUD_AUTH_METHODS,
    AuthMethod,
    _infer_method,
    _validate,
    require_auth,
)
from bb.cloud.sdk._client import BBClient
from bb.cloud.sdk._errors import AuthenticationError

# ---------------------------------------------------------------------------
# _infer_method
# ---------------------------------------------------------------------------


class TestInferMethod:
    def _client(self, prefix: str) -> AuthenticatedClient:
        return AuthenticatedClient(base_url="https://api.bitbucket.org/2.0", token="t", prefix=prefix)

    def test_bearer_returns_oauth2(self):
        assert _infer_method(self._client("Bearer")) is AuthMethod.OAUTH2

    def test_basic_returns_basic(self):
        assert _infer_method(self._client("Basic")) is AuthMethod.BASIC

    def test_jwt_returns_jwt(self):
        assert _infer_method(self._client("JWT")) is AuthMethod.JWT

    def test_unknown_returns_none(self):
        assert _infer_method(self._client("Digest")) is None
        assert _infer_method(self._client("")) is None


# ---------------------------------------------------------------------------
# _validate (core validation logic, testable without decorator overhead)
# ---------------------------------------------------------------------------


def _make_bbclient(prefix: str) -> BBClient:
    """Build a BBClient whose underlying token uses *prefix*."""
    if prefix == "Basic":
        auth = APITokenAuth(email="x@x.com", token="tok")
        return BBClient(auth=auth)
    if prefix == "Bearer":
        auth = OAuthTokenAuth(access_token="tok")
        return BBClient(auth=auth)

    # For JWT and unknown prefixes: build an OAuth client then patch the prefix,
    # avoiding the PyJWT import and any real token generation.
    auth = OAuthTokenAuth(access_token="tok")
    ac = auth.get_authenticated_client()
    object.__setattr__(ac, "prefix", prefix)

    class _FakeBBClient:
        @property
        def auth(self) -> AuthenticatedClient:
            return ac

    return _FakeBBClient()  # type: ignore[return-value]


class TestValidate:
    def test_oauth2_accepted_by_all_methods(self):
        _validate(_make_bbclient("Bearer"), BB_CLOUD_AUTH_METHODS)  # no raise

    def test_basic_accepted_by_all_methods(self):
        _validate(_make_bbclient("Basic"), BB_CLOUD_AUTH_METHODS)  # no raise

    def test_jwt_raises_when_not_in_allowed(self):
        # BB_CLOUD_AUTH_METHODS doesn't include JWT; JWT prefix must raise.
        with pytest.raises(AuthenticationError):
            _validate(_make_bbclient("JWT"), BB_CLOUD_AUTH_METHODS)

    def test_unknown_prefix_raises(self):
        with pytest.raises(AuthenticationError) as exc_info:
            _validate(_make_bbclient("Digest"), BB_CLOUD_AUTH_METHODS)
        assert "unknown" in exc_info.value.actual
        assert "Digest" in exc_info.value.actual

    def test_disallowed_method_raises(self):
        """JWT-only allowed set should reject Basic."""
        with pytest.raises(AuthenticationError) as exc_info:
            _validate(_make_bbclient("Basic"), frozenset({AuthMethod.JWT}))
        assert exc_info.value.actual == AuthMethod.BASIC

    def test_basic_satisfies_api_key(self):
        """BASIC and API_KEY share wire format; Basic prefix must satisfy api_key-only."""
        # Should NOT raise because BASIC & {API_KEY} overlaps
        _validate(_make_bbclient("Basic"), frozenset({AuthMethod.API_KEY}))

    def test_error_attributes(self):
        allowed = frozenset({AuthMethod.OAUTH2})
        with pytest.raises(AuthenticationError) as exc_info:
            _validate(_make_bbclient("Basic"), allowed)
        err = exc_info.value
        assert err.allowed == allowed
        assert err.actual == AuthMethod.BASIC
        assert "basic" in str(err)


# ---------------------------------------------------------------------------
# require_auth decorator integration
# ---------------------------------------------------------------------------


class TestRequireAuthDecorator:
    """Test that @require_auth wraps async functions and validates client."""

    def _make_decorated(self, *methods: AuthMethod):
        """Return an async function decorated with require_auth(*methods)."""

        @require_auth(*methods)
        async def _fn(client: BBClient, x: int = 0) -> int:
            return x + 1

        return _fn

    @pytest.mark.asyncio
    async def test_passes_through_on_valid_auth(self):
        fn = self._make_decorated(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
        result = await fn(_make_bbclient("Bearer"), x=5)
        assert result == 6

    @pytest.mark.asyncio
    async def test_raises_before_body_on_invalid_auth(self):
        """With JWT-only allowed, Basic client must raise before the body runs."""
        fn = self._make_decorated(AuthMethod.JWT)
        with pytest.raises(AuthenticationError):
            await fn(_make_bbclient("Basic"))

    @pytest.mark.asyncio
    async def test_unknown_prefix_raises(self):
        fn = self._make_decorated(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
        with pytest.raises(AuthenticationError):
            await fn(_make_bbclient("Digest"))

    def test_preserves_function_metadata(self):
        """functools.wraps must preserve __name__ and __doc__."""

        @require_auth(AuthMethod.OAUTH2)
        async def my_func(client: BBClient) -> None:
            """My docstring."""

        assert my_func.__name__ == "my_func"
        assert my_func.__doc__ == "My docstring."

    @pytest.mark.asyncio
    async def test_basic_satisfies_api_key_via_decorator(self):
        fn = self._make_decorated(AuthMethod.API_KEY)
        result = await fn(_make_bbclient("Basic"), x=10)
        assert result == 11


# ---------------------------------------------------------------------------
# AuthenticationError
# ---------------------------------------------------------------------------


class TestAuthenticationError:
    def test_message_contains_allowed_and_actual(self):
        err = AuthenticationError(
            allowed=frozenset({AuthMethod.OAUTH2, AuthMethod.BASIC}),
            actual="jwt",
        )
        msg = str(err)
        assert "jwt" in msg
        assert "oauth2" in msg or "basic" in msg

    def test_attributes_set_correctly(self):
        allowed = frozenset({AuthMethod.JWT})
        err = AuthenticationError(allowed=allowed, actual="oauth2")
        assert err.allowed is allowed
        assert err.actual == "oauth2"


# ---------------------------------------------------------------------------
# BB_CLOUD_AUTH_METHODS constant
# ---------------------------------------------------------------------------


class TestBBCloudAuthMethods:
    def test_contains_all_three_oas_methods(self):
        assert AuthMethod.OAUTH2 in BB_CLOUD_AUTH_METHODS
        assert AuthMethod.BASIC in BB_CLOUD_AUTH_METHODS
        assert AuthMethod.API_KEY in BB_CLOUD_AUTH_METHODS

    def test_is_frozen(self):
        with pytest.raises((AttributeError, TypeError)):
            BB_CLOUD_AUTH_METHODS.add(AuthMethod.JWT)  # type: ignore[union-attr]
