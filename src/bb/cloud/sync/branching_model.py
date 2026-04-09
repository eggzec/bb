from __future__ import annotations

import asyncio

from bb.cloud.models.branching_model import BranchingModel
from bb.cloud.models.branching_model_settings import BranchingModelSettings
from bb.cloud.models.effective_repo_branching_model import EffectiveRepoBranchingModel
from bb.cloud.sdk import branching_model as _async
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset

__all__ = [
    "get",
    "effective",
    "settings",
    "update_settings",
    "project_get",
    "project_settings",
    "update_project_settings",
]


def get(client: BBClient, workspace: str, repo_slug: str) -> BranchingModel | None:
    """Sync version of :func:`~bb.cloud.sdk.branching_model.get`."""
    return asyncio.run(_async.get(client, workspace, repo_slug))


def effective(client: BBClient, workspace: str, repo_slug: str) -> EffectiveRepoBranchingModel | None:
    """Sync version of :func:`~bb.cloud.sdk.branching_model.effective`."""
    return asyncio.run(_async.effective(client, workspace, repo_slug))


def settings(client: BBClient, workspace: str, repo_slug: str) -> BranchingModelSettings | None:
    """Sync version of :func:`~bb.cloud.sdk.branching_model.settings`."""
    return asyncio.run(_async.settings(client, workspace, repo_slug))


def update_settings(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: BranchingModelSettings | Unset = UNSET,
) -> BranchingModelSettings | None:
    """Sync version of :func:`~bb.cloud.sdk.branching_model.update_settings`."""
    return asyncio.run(_async.update_settings(client, workspace, repo_slug, body=body))


def project_get(client: BBClient, workspace: str, project_key: str) -> BranchingModel | None:
    """Sync version of :func:`~bb.cloud.sdk.branching_model.project_get`."""
    return asyncio.run(_async.project_get(client, workspace, project_key))


def project_settings(client: BBClient, workspace: str, project_key: str) -> BranchingModelSettings | None:
    """Sync version of :func:`~bb.cloud.sdk.branching_model.project_settings`."""
    return asyncio.run(_async.project_settings(client, workspace, project_key))


def update_project_settings(
    client: BBClient,
    workspace: str,
    project_key: str,
    *,
    body: BranchingModelSettings | Unset = UNSET,
) -> BranchingModelSettings | None:
    """Sync version of :func:`~bb.cloud.sdk.branching_model.update_project_settings`."""
    return asyncio.run(_async.update_project_settings(client, workspace, project_key, body=body))
