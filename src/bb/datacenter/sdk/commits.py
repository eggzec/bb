"""Bitbucket Data Center commit SDK wrappers.

Maps to the ``repository`` API tag for commit operations under
``/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits``.
"""

from __future__ import annotations

from bb.datacenter.api.repository import get_commit, get_commits
from bb.datacenter.models.rest_commit import RestCommit
from bb.datacenter.sdk._auth_validation import AuthMethod, require_auth
from bb.datacenter.sdk._client import BBDCClient
from bb.datacenter.sdk._pagination import async_paginate
from bb.datacenter.types import UNSET, Unset

__all__ = [
    "list",
    "get",
]


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def list(
    client: BBDCClient,
    project_key: str,
    repo_slug: str,
    *,
    since: str | Unset = UNSET,
    until: str | Unset = UNSET,
    path: str | Unset = UNSET,
    follow_renames: str | Unset = UNSET,
    ignore_missing: str | Unset = UNSET,
    merges: str | Unset = UNSET,
    with_counts: str | Unset = UNSET,
    limit: int = 25,
) -> list[RestCommit]:
    """List commits in a repository across all pages.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).
        repo_slug: Repository slug.
        since: A commit ID or ``refs/`` branch/tag to exclude commits reachable from.
        until: A commit ID or ``refs/`` branch/tag to include; defaults to ``HEAD``.
        path: Filter commits by a file path.
        follow_renames: Whether to follow renames of the specified ``path``.
        ignore_missing: Whether to ignore any missing commits or refs.
        merges: Whether to include only merge commits (``"include"``), only
            non-merges (``"exclude"``), or all commits (``"only"``).
        with_counts: Whether to include the total number of commits.
        limit: Number of results per page. Defaults to ``25``.

    Returns:
        All commits matching the filters across all pages.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.datacenter import BBDCClient
        from bb.datacenter.sdk import commits

        client = BBDCClient.from_env()
        result = await commits.list(client, project_key="PRJ", repo_slug="myrepo")
        ```

    References:
        `GET /api/latest/projects/{projectKey}/repos/{repositorySlug}/commits
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-repository/#api-api-latest-projects-projectkey-repos-repositoryslug-commits-get>`_
    """
    return [
        c
        async for c in async_paginate(
            get_commits.asyncio,
            project_key,
            repo_slug,
            client=client.auth,
            since=since,
            until=until,
            path=path,
            follow_renames=follow_renames,
            ignore_missing=ignore_missing,
            merges=merges,
            with_counts=with_counts,
            limit=limit,
        )
        if isinstance(c, RestCommit)
    ]


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def get(
    client: BBDCClient,
    project_key: str,
    repo_slug: str,
    commit_id: str,
    *,
    path: str | Unset = UNSET,
) -> RestCommit | None:
    """Fetch a single commit by ID.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).
        repo_slug: Repository slug.
        commit_id: The full or abbreviated commit SHA.
        path: Limit the returned commit to changes affecting this path.

    Returns:
        The :class:`~bb.datacenter.models.rest_commit.RestCommit`,
        or ``None`` if not found.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.datacenter import BBDCClient
        from bb.datacenter.sdk import commits

        client = BBDCClient.from_env()
        commit = await commits.get(client, project_key="PRJ", repo_slug="myrepo", commit_id="abc123")
        ```

    References:
        `GET /api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-repository/#api-api-latest-projects-projectkey-repos-repositoryslug-commits-commitid-get>`_
    """
    result = await get_commit.asyncio(project_key, repo_slug, commit_id, client=client.auth, path=path)
    return result if isinstance(result, RestCommit) else None
