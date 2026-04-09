from __future__ import annotations

from bb.cloud.api.reports import (
    bulk_create_or_update_annotations,
    create_or_update_annotation,
    create_or_update_report,
    delete_report,
    get_annotations_for_report,
    get_report,
    get_reports_for_commit,
)
from bb.cloud.api.reports import (
    delete_annotation as _delete_annotation,
)
from bb.cloud.api.reports import (
    get_annotation as _get_annotation,
)
from bb.cloud.models.report import Report
from bb.cloud.models.report_annotation import ReportAnnotation
from bb.cloud.sdk._auth_validation import AuthMethod, require_auth
from bb.cloud.sdk._client import BBClient
from bb.cloud.sdk._pagination import async_paginate
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


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def list(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    pagelen: int = 25,
) -> list[Report]:
    """List all reports for a commit.

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
        result = await reports.list(
            client, workspace="myws", repo_slug="myrepo", commit="abc123"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}/reports
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-reports/#api-repositories-workspace-repo-slug-commit-commit-reports-get>`_
    """
    return [
        r
        async for r in async_paginate(
            get_reports_for_commit.asyncio,
            workspace,
            repo_slug,
            commit,
            client=client.auth,
            pagelen=pagelen,
        )
        if isinstance(r, Report)
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get(client: BBClient, workspace: str, repo_slug: str, commit: str, report_id: str) -> Report | None:
    """Retrieve a single report by ID.

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
        report = await reports.get(
            client, workspace="myws", repo_slug="myrepo", commit="abc123", report_id="my-report"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-reports/#api-repositories-workspace-repo-slug-commit-commit-reports-reportid-get>`_
    """
    result = await get_report.asyncio(workspace, repo_slug, commit, report_id, client=client.auth)
    return result if isinstance(result, Report) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def create_or_update(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    report_id: str,
    *,
    body: Report | Unset = UNSET,
) -> Report | None:
    """Create or update a report for a commit.

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
        report = await reports.create_or_update(
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
    """
    result = await create_or_update_report.asyncio(
        workspace, repo_slug, commit, report_id, client=client.auth, body=body
    )
    return result if isinstance(result, Report) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete(client: BBClient, workspace: str, repo_slug: str, commit: str, report_id: str) -> None:
    """Delete a report from a commit.

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
        await reports.delete(
            client, workspace="myws", repo_slug="myrepo", commit="abc123", report_id="my-report"
        )
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-reports/#api-repositories-workspace-repo-slug-commit-commit-reports-reportid-delete>`_
    """
    await delete_report.asyncio(workspace, repo_slug, commit, report_id, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def annotations(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    report_id: str,
    *,
    pagelen: int = 25,
) -> list[ReportAnnotation]:
    """List all annotations for a report.

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
        result = await reports.annotations(
            client, workspace="myws", repo_slug="myrepo", commit="abc123", report_id="my-report"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-reports/#api-repositories-workspace-repo-slug-commit-commit-reports-reportid-annotations-get>`_
    """
    return [
        a
        async for a in async_paginate(
            get_annotations_for_report.asyncio,
            workspace,
            repo_slug,
            commit,
            report_id,
            client=client.auth,
            pagelen=pagelen,
        )
        if isinstance(a, ReportAnnotation)
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_annotation(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    report_id: str,
    annotation_id: str,
) -> ReportAnnotation | None:
    """Retrieve a single annotation by ID.

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
        annotation = await reports.get_annotation(
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
    """
    result = await _get_annotation.asyncio(workspace, repo_slug, commit, report_id, annotation_id, client=client.auth)
    return result if isinstance(result, ReportAnnotation) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def create_annotation(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    report_id: str,
    annotation_id: str,
    *,
    body: ReportAnnotation | Unset = UNSET,
) -> ReportAnnotation | None:
    """Create or update an annotation on a report.

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
        annotation = await reports.create_annotation(
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
    """
    result = await create_or_update_annotation.asyncio(
        workspace, repo_slug, commit, report_id, annotation_id, client=client.auth, body=body
    )
    return result if isinstance(result, ReportAnnotation) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def bulk_annotations(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    report_id: str,
    *,
    body: Unset = UNSET,
) -> list[ReportAnnotation]:
    """Bulk create or update annotations for a report.

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
        created = await reports.bulk_annotations(
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
    """
    result = await bulk_create_or_update_annotations.asyncio(
        workspace, repo_slug, commit, report_id, client=client.auth, body=body
    )
    if isinstance(result, list):
        return [a for a in result if isinstance(a, ReportAnnotation)]
    return []


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete_annotation(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    report_id: str,
    annotation_id: str,
) -> None:
    """Delete an annotation from a report.

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
        await reports.delete_annotation(
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
    """
    await _delete_annotation.asyncio(workspace, repo_slug, commit, report_id, annotation_id, client=client.auth)
