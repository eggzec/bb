"""Tests for bb.cloud.sdk.users."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from bb.cloud.models.account import Account
from bb.cloud.models.gpg_account_key import GPGAccountKey as GpgAccountKey
from bb.cloud.models.ssh_account_key import SshAccountKey
from bb.cloud.models.user import User
from bb.cloud.sdk import users
from bb.cloud.sdk._errors import AuthenticationError

_USERS = "bb.cloud.api.users"
_SSH = "bb.cloud.api.ssh"
_GPG = "bb.cloud.api.gpg"


async def test_me_returns_user(mock_client):
    user = MagicMock(spec=User)
    with patch(f"{_USERS}.get_user.asyncio", new=AsyncMock(return_value=user)):
        result = await users.me(mock_client)
    assert result is user


async def test_me_returns_none(mock_client):
    with patch(f"{_USERS}.get_user.asyncio", new=AsyncMock(return_value=None)):
        result = await users.me(mock_client)
    assert result is None


async def test_get_returns_account(mock_client):
    account = MagicMock(spec=Account)
    with patch(f"{_USERS}.get_users_selected_user.asyncio", new=AsyncMock(return_value=account)):
        result = await users.get(mock_client, "user1")
    assert result is account


async def test_get_returns_none(mock_client):
    with patch(f"{_USERS}.get_users_selected_user.asyncio", new=AsyncMock(return_value=None)):
        result = await users.get(mock_client, "user1")
    assert result is None


async def test_emails_returns_list(mock_client, make_page):
    item = MagicMock()
    with patch(f"{_USERS}.get_user_emails.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await users.emails(mock_client)
    assert result == [item]


async def test_get_email_returns_email(mock_client):
    email = MagicMock()
    with patch(f"{_USERS}.get_user_emails_email.asyncio", new=AsyncMock(return_value=email)):
        result = await users.get_email(mock_client, "user@example.com")
    assert result is email


async def test_ssh_keys_returns_list(mock_client, make_page):
    item = MagicMock(spec=SshAccountKey)
    with patch(f"{_SSH}.get_users_selected_user_ssh_keys.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await users.ssh_keys(mock_client, "user1")
    assert result == [item]


async def test_get_ssh_key_returns_key(mock_client):
    key = MagicMock(spec=SshAccountKey)
    with patch(f"{_SSH}.get_users_selected_user_ssh_keys_key_id.asyncio", new=AsyncMock(return_value=key)):
        result = await users.get_ssh_key(mock_client, "user1", 42)
    assert result is key


async def test_add_ssh_key_returns_key(mock_client):
    key = MagicMock(spec=SshAccountKey)
    with patch(f"{_SSH}.post_users_selected_user_ssh_keys.asyncio", new=AsyncMock(return_value=key)):
        result = await users.add_ssh_key(mock_client, "user1")
    assert result is key


async def test_delete_ssh_key_returns_none(mock_client):
    with patch(f"{_SSH}.delete_users_selected_user_ssh_keys_key_id.asyncio", new=AsyncMock(return_value=None)):
        result = await users.delete_ssh_key(mock_client, "user1", 42)
    assert result is None


async def test_gpg_keys_returns_list(mock_client, make_page):
    item = MagicMock(spec=GpgAccountKey)
    with patch(f"{_GPG}.get_users_selected_user_gpg_keys.asyncio", new=AsyncMock(return_value=make_page([item]))):
        result = await users.gpg_keys(mock_client, "user1")
    assert result == [item]


async def test_get_gpg_key_returns_key(mock_client):
    key = MagicMock(spec=GpgAccountKey)
    with patch(f"{_GPG}.get_users_selected_user_gpg_keys_fingerprint.asyncio", new=AsyncMock(return_value=key)):
        result = await users.get_gpg_key(mock_client, "user1", "FINGER")
    assert result is key


async def test_add_gpg_key_returns_key(mock_client):
    key = MagicMock(spec=GpgAccountKey)
    with patch(f"{_GPG}.post_users_selected_user_gpg_keys.asyncio", new=AsyncMock(return_value=key)):
        result = await users.add_gpg_key(mock_client, "user1")
    assert result is key


async def test_delete_gpg_key_returns_none(mock_client):
    with patch(f"{_GPG}.delete_users_selected_user_gpg_keys_fingerprint.asyncio", new=AsyncMock(return_value=None)):
        result = await users.delete_gpg_key(mock_client, "user1", "FINGER")
    assert result is None


async def test_me_raises_on_bad_auth(bad_auth_client):
    with pytest.raises(AuthenticationError):
        await users.me(bad_auth_client)
