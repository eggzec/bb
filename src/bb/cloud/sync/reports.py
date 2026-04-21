from __future__ import annotations

import asyncio

from bb.cloud.models.error import Error
from bb.cloud.models.report import Report
from bb.cloud.models.report_annotation import ReportAnnotation
from bb.cloud.sdk import reports as _async
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset

__all__ = [
    "list",
    "get",
    "create_or_update",
    "delete",
    "annotations",
    "get_annotation",
    "create_annotation",
    "bulk_annotations",
    "delete_annotation",
]


def list(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    pagelen: int = 25,
) -> list[Report] | Error:
    """Sync version of :func:`~bb.cloud.sdk.reports.list`."""
    return asyncio.run(_async.list(client, workspace, repo_slug, commit, pagelen=pagelen))


def get(client: BBClient, workspace: str, repo_slug: str, commit: str, report_id: str) -> Report | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.reports.get`."""
    return asyncio.run(_async.get(client, workspace, repo_slug, commit, report_id))


def create_or_update(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    report_id: str,
    *,
    body: Report | Unset = UNSET,
) -> Report | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.reports.create_or_update`."""
    return asyncio.run(_async.create_or_update(client, workspace, repo_slug, commit, report_id, body=body))


def delete(client: BBClient, workspace: str, repo_slug: str, commit: str, report_id: str) -> None:
    """Sync version of :func:`~bb.cloud.sdk.reports.delete`."""
    return asyncio.run(_async.delete(client, workspace, repo_slug, commit, report_id))


def annotations(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    report_id: str,
    *,
    pagelen: int = 25,
) -> list[ReportAnnotation] | Error:
    """Sync version of :func:`~bb.cloud.sdk.reports.annotations`."""
    return asyncio.run(_async.annotations(client, workspace, repo_slug, commit, report_id, pagelen=pagelen))


def get_annotation(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    report_id: str,
    annotation_id: str,
) -> ReportAnnotation | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.reports.get_annotation`."""
    return asyncio.run(_async.get_annotation(client, workspace, repo_slug, commit, report_id, annotation_id))


def create_annotation(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    report_id: str,
    annotation_id: str,
    *,
    body: ReportAnnotation | Unset = UNSET,
) -> ReportAnnotation | Error | None:
    """Sync version of :func:`~bb.cloud.sdk.reports.create_annotation`."""
    return asyncio.run(
        _async.create_annotation(client, workspace, repo_slug, commit, report_id, annotation_id, body=body)
    )


def bulk_annotations(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    report_id: str,
    *,
    body: Unset = UNSET,
) -> list[ReportAnnotation] | Error:
    """Sync version of :func:`~bb.cloud.sdk.reports.bulk_annotations`."""
    return asyncio.run(_async.bulk_annotations(client, workspace, repo_slug, commit, report_id, body=body))


def delete_annotation(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    report_id: str,
    annotation_id: str,
) -> None:
    """Sync version of :func:`~bb.cloud.sdk.reports.delete_annotation`."""
    return asyncio.run(_async.delete_annotation(client, workspace, repo_slug, commit, report_id, annotation_id))
