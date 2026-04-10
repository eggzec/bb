"""Tests for bb.datacenter.sdk._client.BBDCClient."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from bb.datacenter.sdk._auth import BasicAuth, PersonalAccessTokenAuth
from bb.datacenter.sdk._client import BBDCClient


class TestBBDCClientInit:
    def test_stores_auth_method(self):
        auth = PersonalAccessTokenAuth(token="tok")
        client = BBDCClient(auth=auth)
        assert client._auth_method is auth

    def test_creates_authenticated_client_on_init(self):
        auth = PersonalAccessTokenAuth(token="tok")
        client = BBDCClient(auth=auth)
        assert client._client is not None

    def test_bearer_client_prefix(self):
        auth = PersonalAccessTokenAuth(token="tok")
        client = BBDCClient(auth=auth)
        assert client.auth.prefix == "Bearer"

    def test_basic_client_prefix(self):
        auth = BasicAuth(username="user", password="pass")
        client = BBDCClient(auth=auth)
        assert client.auth.prefix == "Basic"


class TestBBDCClientAuthProperty:
    def test_returns_same_client_when_not_expired(self):
        auth = PersonalAccessTokenAuth(token="tok")
        client = BBDCClient(auth=auth)
        first = client.auth
        second = client.auth
        assert first is second

    def test_refreshes_client_when_expired(self):
        auth = PersonalAccessTokenAuth(token="tok")
        auth.is_expired = MagicMock(return_value=True)
        client = BBDCClient(auth=auth)
        old = client._client
        _ = client.auth
        assert client._client is not old

    def test_no_refresh_when_not_expired(self):
        auth = PersonalAccessTokenAuth(token="tok")
        auth.is_expired = MagicMock(return_value=False)
        client = BBDCClient(auth=auth)
        first = client._client
        _ = client.auth
        assert client._client is first


class TestBBDCClientFromEnv:
    def test_from_env_with_token(self, monkeypatch):
        monkeypatch.setenv("BB_DC_TOKEN", "envtok")
        client = BBDCClient.from_env()
        assert isinstance(client._auth_method, PersonalAccessTokenAuth)
        assert client._auth_method.token == "envtok"

    def test_from_env_with_basic(self, monkeypatch):
        monkeypatch.delenv("BB_DC_TOKEN", raising=False)
        monkeypatch.setenv("BB_DC_USERNAME", "admin")
        monkeypatch.setenv("BB_DC_PASSWORD", "s3cret")
        client = BBDCClient.from_env()
        assert isinstance(client._auth_method, BasicAuth)
        assert client._auth_method.username == "admin"

    def test_from_env_prefers_token_over_basic(self, monkeypatch):
        monkeypatch.setenv("BB_DC_TOKEN", "tok")
        monkeypatch.setenv("BB_DC_USERNAME", "user")
        monkeypatch.setenv("BB_DC_PASSWORD", "pass")
        client = BBDCClient.from_env()
        assert isinstance(client._auth_method, PersonalAccessTokenAuth)

    def test_from_env_raises_if_no_auth(self, monkeypatch):
        monkeypatch.delenv("BB_DC_TOKEN", raising=False)
        monkeypatch.delenv("BB_DC_USERNAME", raising=False)
        monkeypatch.delenv("BB_DC_PASSWORD", raising=False)
        with pytest.raises(RuntimeError):
            BBDCClient.from_env()
