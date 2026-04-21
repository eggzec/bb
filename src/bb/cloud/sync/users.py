from __future__ import annotations

import asyncio
from typing import Any

from bb.cloud.models.account import Account
from bb.cloud.models.error import Error
from bb.cloud.models.gpg_account_key import GPGAccountKey as GpgAccountKey
from bb.cloud.models.ssh_account_key import SshAccountKey
from bb.cloud.sdk import users as _async
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset

__all__ = [
    "me",
    "get",
    "emails",
    "get_email",
    "ssh_keys",
    "get_ssh_key",
    "add_ssh_key",
    "update_ssh_key",
    "delete_ssh_key",
    "gpg_keys",
    "get_gpg_key",
    "add_gpg_key",
    "delete_gpg_key",
]


def me(client: BBClient) -> Account | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.users.me`."""
    return asyncio.run(_async.me(client))


def get(client: BBClient, selected_user: str) -> Account | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.users.get`."""
    return asyncio.run(_async.get(client, selected_user))


def emails(client: BBClient) -> list[Any] | Error:
    """Sync version of :func:`~bb.cloud.sdk.users.emails`."""
    return asyncio.run(_async.emails(client))


def get_email(client: BBClient, email: str) -> object | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.users.get_email`."""
    return asyncio.run(_async.get_email(client, email))


def ssh_keys(client: BBClient, selected_user: str, *, pagelen: int = 25) -> list[SshAccountKey] | Error:
    """Sync version of :func:`~bb.cloud.sdk.users.ssh_keys`."""
    return asyncio.run(_async.ssh_keys(client, selected_user, pagelen=pagelen))


def get_ssh_key(client: BBClient, selected_user: str, key_id: int) -> SshAccountKey | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.users.get_ssh_key`."""
    return asyncio.run(_async.get_ssh_key(client, selected_user, key_id))


def add_ssh_key(
    client: BBClient,
    selected_user: str,
    *,
    body: SshAccountKey | Unset = UNSET,
) -> SshAccountKey | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.users.add_ssh_key`."""
    return asyncio.run(_async.add_ssh_key(client, selected_user, body=body))


def update_ssh_key(
    client: BBClient,
    selected_user: str,
    key_id: int,
    *,
    body: SshAccountKey | Unset = UNSET,
) -> SshAccountKey | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.users.update_ssh_key`."""
    return asyncio.run(_async.update_ssh_key(client, selected_user, key_id, body=body))


def delete_ssh_key(client: BBClient, selected_user: str, key_id: int) -> None:
    """Sync version of :func:`~bb.cloud.sdk.users.delete_ssh_key`."""
    asyncio.run(_async.delete_ssh_key(client, selected_user, key_id))


def gpg_keys(client: BBClient, selected_user: str, *, pagelen: int = 25) -> list[GpgAccountKey] | Error:
    """Sync version of :func:`~bb.cloud.sdk.users.gpg_keys`."""
    return asyncio.run(_async.gpg_keys(client, selected_user, pagelen=pagelen))


def get_gpg_key(client: BBClient, selected_user: str, fingerprint: str) -> GpgAccountKey | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.users.get_gpg_key`."""
    return asyncio.run(_async.get_gpg_key(client, selected_user, fingerprint))


def add_gpg_key(
    client: BBClient,
    selected_user: str,
    *,
    body: GpgAccountKey | Unset = UNSET,
) -> GpgAccountKey | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.users.add_gpg_key`."""
    return asyncio.run(_async.add_gpg_key(client, selected_user, body=body))


def delete_gpg_key(client: BBClient, selected_user: str, fingerprint: str) -> None:
    """Sync version of :func:`~bb.cloud.sdk.users.delete_gpg_key`."""
    asyncio.run(_async.delete_gpg_key(client, selected_user, fingerprint))
