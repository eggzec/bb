from __future__ import annotations

import asyncio
from typing import Any

from bb.cloud.models.error import Error
from bb.cloud.sdk import addon as _async
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset

__all__ = [
    "delete",
    "update",
    "linkers",
    "get_linker",
    "linker_values",
    "get_linker_value",
    "create_linker_value",
    "set_linker_values",
    "clear_linker_values",
    "delete_linker_value",
]


def delete(client: BBClient) -> None:
    """Sync version of :func:`~bb.cloud.sdk.addon.delete`."""
    return asyncio.run(_async.delete(client))


def update(client: BBClient, *, body: Unset = UNSET) -> Any | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.addon.update`."""
    return asyncio.run(_async.update(client, body=body))


def linkers(client: BBClient) -> Any | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.addon.linkers`."""
    return asyncio.run(_async.linkers(client))


def get_linker(client: BBClient, linker_key: str) -> Any | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.addon.get_linker`."""
    return asyncio.run(_async.get_linker(client, linker_key))


def linker_values(client: BBClient, linker_key: str) -> Any | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.addon.linker_values`."""
    return asyncio.run(_async.linker_values(client, linker_key))


def get_linker_value(client: BBClient, linker_key: str, value_id: str) -> Any | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.addon.get_linker_value`."""
    return asyncio.run(_async.get_linker_value(client, linker_key, value_id))


def create_linker_value(client: BBClient, linker_key: str, *, body: Unset = UNSET) -> Any | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.addon.create_linker_value`."""
    return asyncio.run(_async.create_linker_value(client, linker_key, body=body))


def set_linker_values(client: BBClient, linker_key: str, *, body: Unset = UNSET) -> Any | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.addon.set_linker_values`."""
    return asyncio.run(_async.set_linker_values(client, linker_key, body=body))


def clear_linker_values(client: BBClient, linker_key: str) -> None:
    """Sync version of :func:`~bb.cloud.sdk.addon.clear_linker_values`."""
    return asyncio.run(_async.clear_linker_values(client, linker_key))


def delete_linker_value(client: BBClient, linker_key: str, value_id: str) -> None:
    """Sync version of :func:`~bb.cloud.sdk.addon.delete_linker_value`."""
    return asyncio.run(_async.delete_linker_value(client, linker_key, value_id))
