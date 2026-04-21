from __future__ import annotations

import asyncio

from bb.cloud.models.application_property import ApplicationProperty
from bb.cloud.models.error import Error
from bb.cloud.sdk import properties as _async
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset

__all__ = [
    "repo_get",
    "repo_set",
    "repo_delete",
    "commit_get",
    "commit_set",
    "commit_delete",
    "pr_get",
    "pr_set",
    "pr_delete",
    "user_get",
    "user_set",
    "user_delete",
]


def repo_get(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    app_key: str,
    property_name: str,
) -> ApplicationProperty | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.properties.repo_get`."""
    return asyncio.run(_async.repo_get(client, workspace, repo_slug, app_key, property_name))


def repo_set(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    app_key: str,
    property_name: str,
    *,
    body: ApplicationProperty | Unset = UNSET,
) -> None:
    """Sync version of :func:`~bb.cloud.sdk.properties.repo_set`."""
    return asyncio.run(_async.repo_set(client, workspace, repo_slug, app_key, property_name, body=body))


def repo_delete(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    app_key: str,
    property_name: str,
) -> None:
    """Sync version of :func:`~bb.cloud.sdk.properties.repo_delete`."""
    return asyncio.run(_async.repo_delete(client, workspace, repo_slug, app_key, property_name))


def commit_get(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    app_key: str,
    property_name: str,
) -> ApplicationProperty | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.properties.commit_get`."""
    return asyncio.run(_async.commit_get(client, workspace, repo_slug, commit, app_key, property_name))


def commit_set(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    app_key: str,
    property_name: str,
    *,
    body: ApplicationProperty | Unset = UNSET,
) -> None:
    """Sync version of :func:`~bb.cloud.sdk.properties.commit_set`."""
    return asyncio.run(_async.commit_set(client, workspace, repo_slug, commit, app_key, property_name, body=body))


def commit_delete(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    app_key: str,
    property_name: str,
) -> None:
    """Sync version of :func:`~bb.cloud.sdk.properties.commit_delete`."""
    return asyncio.run(_async.commit_delete(client, workspace, repo_slug, commit, app_key, property_name))


def pr_get(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    app_key: str,
    property_name: str,
) -> ApplicationProperty | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.properties.pr_get`."""
    return asyncio.run(_async.pr_get(client, workspace, repo_slug, pull_request_id, app_key, property_name))


def pr_set(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    app_key: str,
    property_name: str,
    *,
    body: ApplicationProperty | Unset = UNSET,
) -> None:
    """Sync version of :func:`~bb.cloud.sdk.properties.pr_set`."""
    return asyncio.run(_async.pr_set(client, workspace, repo_slug, pull_request_id, app_key, property_name, body=body))


def pr_delete(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    app_key: str,
    property_name: str,
) -> None:
    """Sync version of :func:`~bb.cloud.sdk.properties.pr_delete`."""
    return asyncio.run(_async.pr_delete(client, workspace, repo_slug, pull_request_id, app_key, property_name))


def user_get(
    client: BBClient,
    workspace: str,
    username: str,
    app_key: str,
    property_name: str,
) -> ApplicationProperty | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.properties.user_get`."""
    return asyncio.run(_async.user_get(client, workspace, username, app_key, property_name))


def user_set(
    client: BBClient,
    workspace: str,
    username: str,
    app_key: str,
    property_name: str,
    *,
    body: ApplicationProperty | Unset = UNSET,
) -> None:
    """Sync version of :func:`~bb.cloud.sdk.properties.user_set`."""
    return asyncio.run(_async.user_set(client, workspace, username, app_key, property_name, body=body))


def user_delete(
    client: BBClient,
    workspace: str,
    username: str,
    app_key: str,
    property_name: str,
) -> None:
    """Sync version of :func:`~bb.cloud.sdk.properties.user_delete`."""
    return asyncio.run(_async.user_delete(client, workspace, username, app_key, property_name))
