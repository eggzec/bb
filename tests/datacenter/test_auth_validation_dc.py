"""Tests for bb.datacenter.sdk._auth_validation."""

from __future__ import annotations

import pytest

from bb.datacenter.client import AuthenticatedClient
from bb.datacenter.sdk._auth import BasicAuth, PersonalAccessTokenAuth
from bb.datacenter.sdk._auth_validation import (
    BB_DC_AUTH_METHODS,
    AuthMethod,
    _infer_method,
    _validate,
    require_auth,
)
from bb.datacenter.sdk._client import BBDCClient
from bb.datacenter.sdk._errors import AuthenticationError

# ---------------------------------------------------------------------------
# _infer_method
# ---------------------------------------------------------------------------


class TestInferMethod:
    def _client(self, prefix: str) -> AuthenticatedClient:
        return AuthenticatedClient(base_url="http://localhost:7990/rest", token="t", prefix=prefix)

    def test_bearer_returns_bearer(self):
        assert _infer_method(self._client("Bearer")) is AuthMethod.BEARER

    def test_basic_returns_basic(self):
        assert _infer_method(self._client("Basic")) is AuthMethod.BASIC

    def test_digest_returns_none(self):
        assert _infer_method(self._client("Digest")) is None

    def test_jwt_returns_none(self):
        assert _infer_method(self._client("JWT")) is None

    def test_empty_prefix_returns_none(self):
        assert _infer_method(self._client("")) is None


# ---------------------------------------------------------------------------
# _validate
# ---------------------------------------------------------------------------


def _make_bbdcclient(prefix: str) -> BBDCClient:
    """Build a BBDCClient whose underlying auth uses *prefix*."""
    if prefix == "Bearer":
        return BBDCClient(auth=PersonalAccessTokenAuth(token="tok"))
    if prefix == "Basic":
        return BBDCClient(auth=BasicAuth(username="user", password="pass"))

    # Unknown prefix: patch prefix on a real AuthenticatedClient
    auth = PersonalAccessTokenAuth(token="tok")
    ac = auth.get_authenticated_client()
    object.__setattr__(ac, "prefix", prefix)

    class _FakeBBDCClient:
        @property
        def auth(self) -> AuthenticatedClient:
            return ac

    return _FakeBBDCClient()  # type: ignore[return-value]


class TestValidate:
    def test_bearer_accepted_by_all_dc_methods(self):
        _validate(_make_bbdcclient("Bearer"), BB_DC_AUTH_METHODS)  # no raise

    def test_basic_accepted_by_all_dc_methods(self):
        _validate(_make_bbdcclient("Basic"), BB_DC_AUTH_METHODS)  # no raise

    def test_unknown_prefix_raises(self):
        with pytest.raises(AuthenticationError) as exc_info:
            _validate(_make_bbdcclient("Digest"), BB_DC_AUTH_METHODS)
        assert "unknown" in exc_info.value.actual
        assert "Digest" in exc_info.value.actual

    def test_disallowed_method_raises(self):
        """Bearer-only allowed set should reject Basic."""
        with pytest.raises(AuthenticationError) as exc_info:
            _validate(_make_bbdcclient("Basic"), frozenset({AuthMethod.BEARER}))
        assert exc_info.value.actual == AuthMethod.BASIC

    def test_error_allowed_attribute(self):
        allowed = frozenset({AuthMethod.BEARER})
        with pytest.raises(AuthenticationError) as exc_info:
            _validate(_make_bbdcclient("Basic"), allowed)
        assert exc_info.value.allowed == allowed

    def test_error_message_contains_basic(self):
        with pytest.raises(AuthenticationError) as exc_info:
            _validate(_make_bbdcclient("Basic"), frozenset({AuthMethod.BEARER}))
        assert "basic" in str(exc_info.value)


# ---------------------------------------------------------------------------
# require_auth decorator
# ---------------------------------------------------------------------------


class TestRequireAuthDecorator:
    def _make_decorated(self, *methods: AuthMethod):
        @require_auth(*methods)
        async def _fn(client: BBDCClient, x: int = 0) -> int:
            return x + 1

        return _fn

    async def test_passes_through_on_bearer(self):
        fn = self._make_decorated(AuthMethod.BEARER, AuthMethod.BASIC)
        result = await fn(_make_bbdcclient("Bearer"), x=5)
        assert result == 6

    async def test_passes_through_on_basic(self):
        fn = self._make_decorated(AuthMethod.BEARER, AuthMethod.BASIC)
        result = await fn(_make_bbdcclient("Basic"), x=3)
        assert result == 4

    async def test_raises_before_body_on_bad_auth(self):
        body_called = False

        @require_auth(AuthMethod.BEARER)
        async def _fn(client: BBDCClient) -> None:
            nonlocal body_called
            body_called = True

        with pytest.raises(AuthenticationError):
            await _fn(_make_bbdcclient("Basic"))
        assert not body_called

    async def test_unknown_prefix_raises(self):
        fn = self._make_decorated(AuthMethod.BEARER, AuthMethod.BASIC)
        with pytest.raises(AuthenticationError):
            await fn(_make_bbdcclient("Digest"))

    def test_preserves_name(self):
        @require_auth(AuthMethod.BEARER)
        async def my_dc_func(client: BBDCClient) -> None:
            """DC docstring."""

        assert my_dc_func.__name__ == "my_dc_func"

    def test_preserves_docstring(self):
        @require_auth(AuthMethod.BEARER)
        async def my_dc_func(client: BBDCClient) -> None:
            """DC docstring."""

        assert my_dc_func.__doc__ == "DC docstring."


# ---------------------------------------------------------------------------
# BB_DC_AUTH_METHODS constant
# ---------------------------------------------------------------------------


class TestBBDCAuthMethods:
    def test_contains_bearer(self):
        assert AuthMethod.BEARER in BB_DC_AUTH_METHODS

    def test_contains_basic(self):
        assert AuthMethod.BASIC in BB_DC_AUTH_METHODS

    def test_exactly_two_methods(self):
        assert len(BB_DC_AUTH_METHODS) == 2

    def test_is_frozen(self):
        with pytest.raises((AttributeError, TypeError)):
            BB_DC_AUTH_METHODS.add(AuthMethod.BEARER)  # type: ignore[union-attr]
