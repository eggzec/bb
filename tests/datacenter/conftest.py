"""Shared fixtures for all tests/datacenter/ tests."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from bb.datacenter.client import AuthenticatedClient
from bb.datacenter.sdk._client import BBDCClient


@pytest.fixture
def mock_dc_client() -> BBDCClient:
    """BBDCClient mock that passes require_auth via Bearer (Personal Access Token)."""
    auth_client = MagicMock(spec=AuthenticatedClient)
    auth_client.prefix = "Bearer"
    client = MagicMock(spec=BBDCClient)
    client.auth = auth_client
    return client


@pytest.fixture
def basic_mock_dc_client() -> BBDCClient:
    """BBDCClient mock that passes require_auth via Basic auth."""
    auth_client = MagicMock(spec=AuthenticatedClient)
    auth_client.prefix = "Basic"
    client = MagicMock(spec=BBDCClient)
    client.auth = auth_client
    return client


@pytest.fixture
def bad_auth_dc_client() -> BBDCClient:
    """BBDCClient mock with an unrecognised auth prefix — triggers AuthenticationError."""
    auth_client = MagicMock(spec=AuthenticatedClient)
    auth_client.prefix = "Digest"
    client = MagicMock(spec=BBDCClient)
    client.auth = auth_client
    return client
