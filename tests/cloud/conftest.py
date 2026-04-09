"""Shared fixtures for all tests/cloud/ tests."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from bb.cloud.client import AuthenticatedClient
from bb.cloud.sdk._client import BBClient


@pytest.fixture
def mock_client() -> BBClient:
    """BBClient mock that passes require_auth (Bearer / OAuth2)."""
    auth_client = MagicMock(spec=AuthenticatedClient)
    auth_client.prefix = "Bearer"
    client = MagicMock(spec=BBClient)
    client.auth = auth_client
    return client


@pytest.fixture
def bad_auth_client() -> BBClient:
    """BBClient mock with an unrecognised auth prefix — triggers AuthenticationError."""
    auth_client = MagicMock(spec=AuthenticatedClient)
    auth_client.prefix = "Digest"
    client = MagicMock(spec=BBClient)
    client.auth = auth_client
    return client
