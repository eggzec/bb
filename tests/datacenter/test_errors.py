"""Tests for bb.datacenter.sdk._errors.AuthenticationError."""

from __future__ import annotations

from bb.datacenter.sdk._auth_validation import AuthMethod
from bb.datacenter.sdk._errors import AuthenticationError


class TestAuthenticationError:
    def test_message_contains_actual(self):
        err = AuthenticationError(
            allowed=frozenset({AuthMethod.BEARER, AuthMethod.BASIC}),
            actual="jwt",
        )
        msg = str(err)
        assert "jwt" in msg

    def test_message_contains_at_least_one_allowed(self):
        err = AuthenticationError(
            allowed=frozenset({AuthMethod.BEARER, AuthMethod.BASIC}),
            actual="jwt",
        )
        msg = str(err)
        assert "bearer" in msg or "basic" in msg

    def test_attributes_set_correctly(self):
        allowed = frozenset({AuthMethod.BEARER})
        err = AuthenticationError(allowed=allowed, actual="basic")
        assert err.allowed is allowed
        assert err.actual == "basic"

    def test_allowed_frozenset_preserved(self):
        allowed = frozenset({AuthMethod.BEARER, AuthMethod.BASIC})
        err = AuthenticationError(allowed=allowed, actual="unknown (prefix='Digest')")
        assert err.allowed == allowed

    def test_unknown_prefix_in_message(self):
        err = AuthenticationError(
            allowed=frozenset({AuthMethod.BEARER}),
            actual="unknown (prefix='Digest')",
        )
        assert "Digest" in str(err)
