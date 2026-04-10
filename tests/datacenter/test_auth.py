"""Tests for bb.datacenter.sdk._auth — PersonalAccessTokenAuth, BasicAuth, auto_detect_auth."""

from __future__ import annotations

import base64

import pytest

from bb.datacenter.sdk._auth import (
    AuthMethod,
    BasicAuth,
    PersonalAccessTokenAuth,
    auto_detect_auth,
)


class TestPersonalAccessTokenAuth:
    def test_method_is_bearer(self):
        auth = PersonalAccessTokenAuth(token="mytoken")
        assert auth.method == AuthMethod.BEARER

    def test_default_base_url_is_localhost(self, monkeypatch):
        monkeypatch.delenv("BB_DC_BASE_URL", raising=False)
        auth = PersonalAccessTokenAuth(token="mytoken")
        assert auth.base_url == "http://localhost:7990/rest"

    def test_custom_base_url(self):
        auth = PersonalAccessTokenAuth(token="tok", base_url="https://bb.example.com/rest")
        assert auth.base_url == "https://bb.example.com/rest"

    def test_base_url_from_env(self, monkeypatch):
        monkeypatch.setenv("BB_DC_BASE_URL", "https://env.example.com/rest")
        auth = PersonalAccessTokenAuth(token="tok")
        assert auth.base_url == "https://env.example.com/rest"

    def test_explicit_url_overrides_env(self, monkeypatch):
        monkeypatch.setenv("BB_DC_BASE_URL", "https://env.example.com/rest")
        auth = PersonalAccessTokenAuth(token="tok", base_url="https://override.example.com/rest")
        assert auth.base_url == "https://override.example.com/rest"

    def test_get_authenticated_client_bearer_prefix(self):
        auth = PersonalAccessTokenAuth(token="mytoken")
        client = auth.get_authenticated_client()
        assert client.prefix == "Bearer"
        assert client.token == "mytoken"

    def test_is_expired_always_false(self):
        auth = PersonalAccessTokenAuth(token="tok")
        assert auth.is_expired() is False

    def test_to_dict_method(self):
        auth = PersonalAccessTokenAuth(token="abcdefgh")
        d = auth.to_dict()
        assert d["method"] == "bearer"
        assert d["token_last_4"] == "efgh"

    def test_to_dict_short_token_masked(self):
        auth = PersonalAccessTokenAuth(token="ab")
        d = auth.to_dict()
        assert d["token_last_4"] == "****"

    def test_to_dict_contains_base_url(self):
        auth = PersonalAccessTokenAuth(token="tok", base_url="https://bb.example.com/rest")
        assert auth.to_dict()["base_url"] == "https://bb.example.com/rest"

    def test_from_env_reads_bb_dc_token(self, monkeypatch):
        monkeypatch.setenv("BB_DC_TOKEN", "myenvtoken")
        auth = PersonalAccessTokenAuth.from_env()
        assert auth.token == "myenvtoken"

    def test_from_env_raises_if_token_missing(self, monkeypatch):
        monkeypatch.delenv("BB_DC_TOKEN", raising=False)
        with pytest.raises(RuntimeError, match="BB_DC_TOKEN"):
            PersonalAccessTokenAuth.from_env()

    def test_from_env_raises_if_token_blank(self, monkeypatch):
        monkeypatch.setenv("BB_DC_TOKEN", "   ")
        with pytest.raises(RuntimeError, match="BB_DC_TOKEN"):
            PersonalAccessTokenAuth.from_env()


class TestBasicAuth:
    def test_method_is_basic(self):
        auth = BasicAuth(username="user", password="pass")
        assert auth.method == AuthMethod.BASIC

    def test_default_base_url_is_localhost(self, monkeypatch):
        monkeypatch.delenv("BB_DC_BASE_URL", raising=False)
        auth = BasicAuth(username="user", password="pass")
        assert auth.base_url == "http://localhost:7990/rest"

    def test_custom_base_url(self):
        auth = BasicAuth(username="user", password="pass", base_url="https://bb.example.com/rest")
        assert auth.base_url == "https://bb.example.com/rest"

    def test_get_authenticated_client_basic_prefix(self):
        auth = BasicAuth(username="admin", password="secret")
        client = auth.get_authenticated_client()
        assert client.prefix == "Basic"

    def test_get_authenticated_client_base64_encoded(self):
        auth = BasicAuth(username="admin", password="secret")
        client = auth.get_authenticated_client()
        expected = base64.b64encode(b"admin:secret").decode()
        assert client.token == expected

    def test_is_expired_always_false(self):
        auth = BasicAuth(username="user", password="pass")
        assert auth.is_expired() is False

    def test_to_dict_shows_username_not_password(self):
        auth = BasicAuth(username="admin", password="secret")
        d = auth.to_dict()
        assert d["method"] == "basic"
        assert d["username"] == "admin"
        assert "password" not in d
        assert "secret" not in str(d)

    def test_from_env_reads_username_and_password(self, monkeypatch):
        monkeypatch.setenv("BB_DC_USERNAME", "admin")
        monkeypatch.setenv("BB_DC_PASSWORD", "s3cret")
        auth = BasicAuth.from_env()
        assert auth.username == "admin"
        assert auth.password == "s3cret"

    def test_from_env_raises_if_username_missing(self, monkeypatch):
        monkeypatch.delenv("BB_DC_USERNAME", raising=False)
        monkeypatch.setenv("BB_DC_PASSWORD", "pass")
        with pytest.raises(RuntimeError, match="BB_DC_USERNAME"):
            BasicAuth.from_env()

    def test_from_env_raises_if_password_missing(self, monkeypatch):
        monkeypatch.setenv("BB_DC_USERNAME", "user")
        monkeypatch.delenv("BB_DC_PASSWORD", raising=False)
        with pytest.raises(RuntimeError, match="BB_DC_PASSWORD"):
            BasicAuth.from_env()

    def test_from_env_raises_if_both_missing(self, monkeypatch):
        monkeypatch.delenv("BB_DC_USERNAME", raising=False)
        monkeypatch.delenv("BB_DC_PASSWORD", raising=False)
        with pytest.raises(RuntimeError):
            BasicAuth.from_env()


class TestAutoDetectAuth:
    def test_prefers_pat_over_basic(self, monkeypatch):
        monkeypatch.setenv("BB_DC_TOKEN", "mytoken")
        monkeypatch.setenv("BB_DC_USERNAME", "user")
        monkeypatch.setenv("BB_DC_PASSWORD", "pass")
        auth = auto_detect_auth()
        assert isinstance(auth, PersonalAccessTokenAuth)

    def test_falls_back_to_basic(self, monkeypatch):
        monkeypatch.delenv("BB_DC_TOKEN", raising=False)
        monkeypatch.setenv("BB_DC_USERNAME", "user")
        monkeypatch.setenv("BB_DC_PASSWORD", "pass")
        auth = auto_detect_auth()
        assert isinstance(auth, BasicAuth)

    def test_pat_token_propagated(self, monkeypatch):
        monkeypatch.setenv("BB_DC_TOKEN", "tok123")
        monkeypatch.delenv("BB_DC_USERNAME", raising=False)
        monkeypatch.delenv("BB_DC_PASSWORD", raising=False)
        auth = auto_detect_auth()
        assert isinstance(auth, PersonalAccessTokenAuth)
        assert auth.token == "tok123"

    def test_basic_credentials_propagated(self, monkeypatch):
        monkeypatch.delenv("BB_DC_TOKEN", raising=False)
        monkeypatch.setenv("BB_DC_USERNAME", "admin")
        monkeypatch.setenv("BB_DC_PASSWORD", "s3cret")
        auth = auto_detect_auth()
        assert isinstance(auth, BasicAuth)
        assert auth.username == "admin"

    def test_raises_if_nothing_set(self, monkeypatch):
        monkeypatch.delenv("BB_DC_TOKEN", raising=False)
        monkeypatch.delenv("BB_DC_USERNAME", raising=False)
        monkeypatch.delenv("BB_DC_PASSWORD", raising=False)
        with pytest.raises(RuntimeError):
            auto_detect_auth()

    def test_raises_if_only_username_set(self, monkeypatch):
        monkeypatch.delenv("BB_DC_TOKEN", raising=False)
        monkeypatch.setenv("BB_DC_USERNAME", "user")
        monkeypatch.delenv("BB_DC_PASSWORD", raising=False)
        with pytest.raises(RuntimeError):
            auto_detect_auth()
