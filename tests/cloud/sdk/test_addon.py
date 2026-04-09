"""Tests for bb.cloud.sdk.addon."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bb.cloud.sdk import addon
from bb.cloud.sdk._errors import AuthenticationError

_API = "bb.cloud.api.addon"


async def test_delete_returns_none(mock_client):
    with patch(f"{_API}.delete_addon.asyncio", new=AsyncMock(return_value=None)):
        result = await addon.delete(mock_client)
    assert result is None


async def test_update_returns_result(mock_client):
    value = MagicMock()
    with patch(f"{_API}.put_addon.asyncio", new=AsyncMock(return_value=value)):
        result = await addon.update(mock_client)
    assert result is value


async def test_update_returns_none(mock_client):
    with patch(f"{_API}.put_addon.asyncio", new=AsyncMock(return_value=None)):
        result = await addon.update(mock_client)
    assert result is None


async def test_linkers_returns_result(mock_client):
    value = MagicMock()
    with patch(f"{_API}.get_addon_linkers.asyncio", new=AsyncMock(return_value=value)):
        result = await addon.linkers(mock_client)
    assert result is value


async def test_get_linker_returns_result(mock_client):
    value = MagicMock()
    with patch(f"{_API}.get_addon_linkers_linker_key.asyncio", new=AsyncMock(return_value=value)):
        result = await addon.get_linker(mock_client, "key1")
    assert result is value


async def test_linker_values_returns_result(mock_client):
    value = MagicMock()
    with patch(f"{_API}.get_addon_linkers_linker_key_values.asyncio", new=AsyncMock(return_value=value)):
        result = await addon.linker_values(mock_client, "key1")
    assert result is value


async def test_get_linker_value_returns_result(mock_client):
    value = MagicMock()
    with patch(f"{_API}.get_addon_linkers_linker_key_values_value_id.asyncio", new=AsyncMock(return_value=value)):
        result = await addon.get_linker_value(mock_client, "key1", "val1")
    assert result is value


async def test_create_linker_value_returns_result(mock_client):
    value = MagicMock()
    with patch(f"{_API}.post_addon_linkers_linker_key_values.asyncio", new=AsyncMock(return_value=value)):
        result = await addon.create_linker_value(mock_client, "key1")
    assert result is value


async def test_set_linker_values_returns_result(mock_client):
    value = MagicMock()
    with patch(f"{_API}.put_addon_linkers_linker_key_values.asyncio", new=AsyncMock(return_value=value)):
        result = await addon.set_linker_values(mock_client, "key1")
    assert result is value


async def test_clear_linker_values_returns_none(mock_client):
    with patch(f"{_API}.delete_addon_linkers_linker_key_values.asyncio", new=AsyncMock(return_value=None)):
        result = await addon.clear_linker_values(mock_client, "key1")
    assert result is None


async def test_delete_linker_value_returns_none(mock_client):
    with patch(f"{_API}.delete_addon_linkers_linker_key_values_value_id.asyncio", new=AsyncMock(return_value=None)):
        result = await addon.delete_linker_value(mock_client, "key1", "val1")
    assert result is None


async def test_delete_raises_on_bad_auth(bad_auth_client):
    with pytest.raises(AuthenticationError):
        await addon.delete(bad_auth_client)
