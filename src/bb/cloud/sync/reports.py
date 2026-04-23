from __future__ import annotations
import asyncio
from bb.cloud.models.error import Error
from bb.cloud.models.report import Report
from bb.cloud.models.report_annotation import ReportAnnotation
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset
from bb.cloud.sdk import reports as _async
__all__ = ['list', 'get', 'create_or_update', 'delete', 'annotations', 'get_annotation', 'create_annotation', 'bulk_annotations', 'delete_annotation']

def list(client: BBClient, workspace: str, repo_slug: str, commit: str, *, pagelen: int=25) -> list[Report] | Error:
    """List all reports for a commit.

Synchronous wrapper around :func:`~bb.cloud.sdk.reports.list`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    commit: Full SHA1 of the commit.
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    List of :class:`~bb.cloud.models.report.Report` objects.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import reports

    client = BBClient.from_env()
    result = reports.list(
        client, workspace="myws", repo_slug="myrepo", commit="abc123"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}/reports
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-reports/#api-repositories-workspace-repo-slug-commit-commit-reports-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.reports.list`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.list(client, workspace, repo_slug, commit, pagelen=pagelen))

def get(client: BBClient, workspace: str, repo_slug: str, commit: str, report_id: str) -> Report | Error | None:
    """Retrieve a single report by ID.

Synchronous wrapper around :func:`~bb.cloud.sdk.reports.get`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    commit: Full SHA1 of the commit.
    report_id: Unique ID of the report.

Returns:
    A :class:`~bb.cloud.models.report.Report` object, or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import reports

    client = BBClient.from_env()
    report = reports.get(
        client, workspace="myws", repo_slug="myrepo", commit="abc123", report_id="my-report"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-reports/#api-repositories-workspace-repo-slug-commit-commit-reports-reportid-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.reports.get`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.get(client, workspace, repo_slug, commit, report_id))

def create_or_update(client: BBClient, workspace: str, repo_slug: str, commit: str, report_id: str, *, body: Report | Unset=UNSET) -> Report | Error | None:
    """Create or update a report for a commit.

Synchronous wrapper around :func:`~bb.cloud.sdk.reports.create_or_update`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    commit: Full SHA1 of the commit.
    report_id: Unique ID for the report.
    body: Report payload. Defaults to :data:`~bb.cloud.types.UNSET`.

Returns:
    The created or updated :class:`~bb.cloud.models.report.Report`, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import reports
    from bb.cloud.models.report import Report

    client = BBClient.from_env()
    report = reports.create_or_update(
        client,
        workspace="myws",
        repo_slug="myrepo",
        commit="abc123",
        report_id="my-report",
        body=Report(...),
    )
    ```

References:
    `PUT /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-reports/#api-repositories-workspace-repo-slug-commit-commit-reports-reportid-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.reports.create_or_update`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.create_or_update(client, workspace, repo_slug, commit, report_id, body=body))

def delete(client: BBClient, workspace: str, repo_slug: str, commit: str, report_id: str) -> None:
    """Delete a report from a commit.

Synchronous wrapper around :func:`~bb.cloud.sdk.reports.delete`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    commit: Full SHA1 of the commit.
    report_id: Unique ID of the report to delete.

Returns:
    None.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import reports

    client = BBClient.from_env()
    reports.delete(
        client, workspace="myws", repo_slug="myrepo", commit="abc123", report_id="my-report"
    )
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-reports/#api-repositories-workspace-repo-slug-commit-commit-reports-reportid-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.reports.delete`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.delete(client, workspace, repo_slug, commit, report_id))

def annotations(client: BBClient, workspace: str, repo_slug: str, commit: str, report_id: str, *, pagelen: int=25) -> list[ReportAnnotation] | Error:
    """List all annotations for a report.

Synchronous wrapper around :func:`~bb.cloud.sdk.reports.annotations`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    commit: Full SHA1 of the commit.
    report_id: Unique ID of the report.
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    List of :class:`~bb.cloud.models.report_annotation.ReportAnnotation` objects.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import reports

    client = BBClient.from_env()
    result = reports.annotations(
        client, workspace="myws", repo_slug="myrepo", commit="abc123", report_id="my-report"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-reports/#api-repositories-workspace-repo-slug-commit-commit-reports-reportid-annotations-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.reports.annotations`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.annotations(client, workspace, repo_slug, commit, report_id, pagelen=pagelen))

def get_annotation(client: BBClient, workspace: str, repo_slug: str, commit: str, report_id: str, annotation_id: str) -> ReportAnnotation | Error | None:
    """Retrieve a single annotation by ID.

Synchronous wrapper around :func:`~bb.cloud.sdk.reports.get_annotation`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    commit: Full SHA1 of the commit.
    report_id: Unique ID of the report.
    annotation_id: Unique ID of the annotation.

Returns:
    A :class:`~bb.cloud.models.report_annotation.ReportAnnotation` object, or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import reports

    client = BBClient.from_env()
    annotation = reports.get_annotation(
        client,
        workspace="myws",
        repo_slug="myrepo",
        commit="abc123",
        report_id="my-report",
        annotation_id="ann-1",
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-reports/#api-repositories-workspace-repo-slug-commit-commit-reports-reportid-annotations-annotationid-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.reports.get_annotation`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.get_annotation(client, workspace, repo_slug, commit, report_id, annotation_id))

def create_annotation(client: BBClient, workspace: str, repo_slug: str, commit: str, report_id: str, annotation_id: str, *, body: ReportAnnotation | Unset=UNSET) -> ReportAnnotation | Error | None:
    """Create or update an annotation on a report.

Synchronous wrapper around :func:`~bb.cloud.sdk.reports.create_annotation`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    commit: Full SHA1 of the commit.
    report_id: Unique ID of the report.
    annotation_id: Unique ID for the annotation.
    body: Annotation payload. Defaults to :data:`~bb.cloud.types.UNSET`.

Returns:
    The created or updated :class:`~bb.cloud.models.report_annotation.ReportAnnotation`,
    or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import reports
    from bb.cloud.models.report_annotation import ReportAnnotation

    client = BBClient.from_env()
    annotation = reports.create_annotation(
        client,
        workspace="myws",
        repo_slug="myrepo",
        commit="abc123",
        report_id="my-report",
        annotation_id="ann-1",
        body=ReportAnnotation(...),
    )
    ```

References:
    `PUT /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-reports/#api-repositories-workspace-repo-slug-commit-commit-reports-reportid-annotations-annotationid-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.reports.create_annotation`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.create_annotation(client, workspace, repo_slug, commit, report_id, annotation_id, body=body))

def bulk_annotations(client: BBClient, workspace: str, repo_slug: str, commit: str, report_id: str, *, body: Unset=UNSET) -> list[ReportAnnotation] | Error:
    """Bulk create or update annotations for a report.

Synchronous wrapper around :func:`~bb.cloud.sdk.reports.bulk_annotations`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    commit: Full SHA1 of the commit.
    report_id: Unique ID of the report.
    body: List of annotation payloads. Defaults to :data:`~bb.cloud.types.UNSET`.

Returns:
    List of created or updated :class:`~bb.cloud.models.report_annotation.ReportAnnotation` objects.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import reports

    client = BBClient.from_env()
    created = reports.bulk_annotations(
        client,
        workspace="myws",
        repo_slug="myrepo",
        commit="abc123",
        report_id="my-report",
        body=...,
    )
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-reports/#api-repositories-workspace-repo-slug-commit-commit-reports-reportid-annotations-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.reports.bulk_annotations`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.bulk_annotations(client, workspace, repo_slug, commit, report_id, body=body))

def delete_annotation(client: BBClient, workspace: str, repo_slug: str, commit: str, report_id: str, annotation_id: str) -> None:
    """Delete an annotation from a report.

Synchronous wrapper around :func:`~bb.cloud.sdk.reports.delete_annotation`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    commit: Full SHA1 of the commit.
    report_id: Unique ID of the report.
    annotation_id: Unique ID of the annotation to delete.

Returns:
    None.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import reports

    client = BBClient.from_env()
    reports.delete_annotation(
        client,
        workspace="myws",
        repo_slug="myrepo",
        commit="abc123",
        report_id="my-report",
        annotation_id="ann-1",
    )
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-reports/#api-repositories-workspace-repo-slug-commit-commit-reports-reportid-annotations-annotationid-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.reports.delete_annotation`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.delete_annotation(client, workspace, repo_slug, commit, report_id, annotation_id))
