"""Bitbucket Data Center branch SDK wrappers.

Maps to the ``repository`` API tag for branch operations under
``/api/latest/projects/{projectKey}/repos/{repositorySlug}/branches`` and
``/branch-utils/latest/projects/{projectKey}/repos/{repositorySlug}/branches``.
"""

from __future__ import annotations

from bb.datacenter.api.project import get_default_branch_2, set_default_branch_2
from bb.datacenter.api.repository import delete_branch, get_branches
from bb.datacenter.models.rest_branch import RestBranch
from bb.datacenter.models.rest_branch_create_request import RestBranchCreateRequest
from bb.datacenter.models.rest_minimal_ref import RestMinimalRef
from bb.datacenter.sdk._auth_validation import AuthMethod, require_auth
from bb.datacenter.sdk._client import BBDCClient
from bb.datacenter.sdk._pagination import async_paginate
from bb.datacenter.types import UNSET, Unset

__all__ = [
    "list",
    "search",
    "get_by_commit",
    "get_default",
    "set_default",
    "create",
    "delete",
]


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def list(
    client: BBDCClient,
    project_key: str,
    repo_slug: str,
    *,
    filter_text: str | Unset = UNSET,
    base: str | Unset = UNSET,
    details: bool | Unset = UNSET,
    limit: int = 25,
) -> list[RestBranch]:
    """List all branches in a repository across all pages.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).
        repo_slug: Repository slug.
        filter_text: Branch name filter text.
        base: A commit or tag to compare branches against.
        details: Whether to include branch metadata (ahead/behind counts).
        limit: Number of results per page. Defaults to ``25``.

    Returns:
        All branches in the repository across all pages.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.datacenter import BBDCClient
        from bb.datacenter.sdk import branches

        client = BBDCClient.from_env()
        result = await branches.list(client, project_key="PRJ", repo_slug="myrepo")
        ```

    References:
        `GET /api/latest/projects/{projectKey}/repos/{repositorySlug}/branches
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-repository/#api-api-latest-projects-projectkey-repos-repositoryslug-branches-get>`_
    """
    return [
        b
        async for b in async_paginate(
            get_branches.asyncio,
            project_key,
            repo_slug,
            client=client.auth,
            filter_text=filter_text,
            base=base,
            details=details,
            limit=limit,
        )
        if isinstance(b, RestBranch)
    ]


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def search(
    client: BBDCClient,
    project_key: str,
    repo_slug: str,
    *,
    filter_text: str | Unset = UNSET,
    limit: int = 25,
) -> list[RestBranch]:  # pyrefly: ignore[unsupported-operation]
    """Search for branches by name prefix.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).
        repo_slug: Repository slug.
        filter_text: Branch name filter text.
        limit: Number of results per page. Defaults to ``25``.

    Returns:
        All matching branches across all pages.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.datacenter import BBDCClient
        from bb.datacenter.sdk import branches

        client = BBDCClient.from_env()
        result = await branches.search(client, project_key="PRJ", repo_slug="myrepo", filter_text="feat/")
        ```

    References:
        `GET /api/latest/projects/{projectKey}/repos/{repositorySlug}/branches
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-repository/#api-api-latest-projects-projectkey-repos-repositoryslug-branches-get>`_
    """
    return [
        b
        async for b in async_paginate(
            get_branches.asyncio,
            project_key,
            repo_slug,
            client=client.auth,
            filter_text=filter_text,
            limit=limit,
        )
        if isinstance(b, RestBranch)
    ]


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def get_by_commit(
    client: BBDCClient,
    project_key: str,
    repo_slug: str,
    commit_id: str,
    *,
    limit: int = 25,
) -> list[RestMinimalRef]:  # pyrefly: ignore[unsupported-operation]
    """List branches that contain a given commit.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).
        repo_slug: Repository slug.
        commit_id: The commit SHA to search for.
        limit: Number of results per page. Defaults to ``25``.

    Returns:
        All :class:`~bb.datacenter.models.rest_minimal_ref.RestMinimalRef` objects
        for branches containing the given commit, across all pages.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.datacenter import BBDCClient
        from bb.datacenter.sdk import branches

        client = BBDCClient.from_env()
        result = await branches.get_by_commit(client, project_key="PRJ", repo_slug="myrepo", commit_id="abc123")
        ```

    References:
        `GET /branch-utils/latest/projects/{projectKey}/repos/{repositorySlug}/branches/info/{commitId}
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-repository/#api-branch-utils-latest-projects-projectkey-repos-repositoryslug-branches-info-commitid-get>`_
    """
    from bb.datacenter.api.repository import find_by_commit

    return [
        b
        async for b in async_paginate(
            find_by_commit.asyncio,
            project_key,
            repo_slug,
            commit_id,
            client=client.auth,
            limit=limit,
        )
        if isinstance(b, RestMinimalRef)
    ]


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def get_default(
    client: BBDCClient,
    project_key: str,
    repo_slug: str,
) -> RestMinimalRef | None:
    """Get the default branch for a repository.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).
        repo_slug: Repository slug.

    Returns:
        The default :class:`~bb.datacenter.models.rest_minimal_ref.RestMinimalRef`,
        or ``None`` if not found.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.datacenter import BBDCClient
        from bb.datacenter.sdk import branches

        client = BBDCClient.from_env()
        default = await branches.get_default(client, project_key="PRJ", repo_slug="myrepo")
        ```

    References:
        `GET /api/latest/projects/{projectKey}/repos/{repositorySlug}/default-branch
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-project/#api-api-latest-projects-projectkey-repos-repositoryslug-default-branch-get>`_
    """
    result = await get_default_branch_2.asyncio(project_key, repo_slug, client=client.auth)
    return result if isinstance(result, RestMinimalRef) else None


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def set_default(
    client: BBDCClient,
    project_key: str,
    repo_slug: str,
    *,
    body: RestBranch | Unset = UNSET,
) -> None:
    """Set the default branch for a repository.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).
        repo_slug: Repository slug.
        body: Branch identifier body.
            Use :class:`~bb.datacenter.models.rest_branch.RestBranch` with at least ``id`` set.

    Returns:
        ``None``.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.datacenter import BBDCClient
        from bb.datacenter.models.rest_branch import RestBranch
        from bb.datacenter.sdk import branches

        client = BBDCClient.from_env()
        await branches.set_default(
            client,
            project_key="PRJ",
            repo_slug="myrepo",
            body=RestBranch(id="refs/heads/main"),
        )
        ```

    References:
        `PUT /api/latest/projects/{projectKey}/repos/{repositorySlug}/default-branch
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-project/#api-api-latest-projects-projectkey-repos-repositoryslug-default-branch-put>`_
    """
    await set_default_branch_2.asyncio(project_key, repo_slug, client=client.auth, body=body)


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def create(
    client: BBDCClient,
    project_key: str,
    repo_slug: str,
    *,
    body: RestBranchCreateRequest,
) -> RestBranch | None:
    """Create a new branch.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).
        repo_slug: Repository slug.
        body: Branch creation request with ``name`` and ``startPoint``.
            Use :class:`~bb.datacenter.models.rest_branch_create_request.RestBranchCreateRequest`.

    Returns:
        The created :class:`~bb.datacenter.models.rest_branch.RestBranch`,
        or ``None`` on error.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.datacenter import BBDCClient
        from bb.datacenter.models.rest_branch_create_request import RestBranchCreateRequest
        from bb.datacenter.sdk import branches

        client = BBDCClient.from_env()
        branch = await branches.create(
            client,
            project_key="PRJ",
            repo_slug="myrepo",
            body=RestBranchCreateRequest(name="feature/my-feature", start_point="main"),
        )
        ```

    References:
        `POST /branch-utils/latest/projects/{projectKey}/repos/{repositorySlug}/branches
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-repository/#api-branch-utils-latest-projects-projectkey-repos-repositoryslug-branches-post>`_
    """
    from bb.datacenter.api.repository import create_branch

    result = await create_branch.asyncio(project_key, repo_slug, client=client.auth, body=body)
    return result if isinstance(result, RestBranch) else None


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def delete(
    client: BBDCClient,
    project_key: str,
    repo_slug: str,
    *,
    branch_id: str,
    dry_run: bool | Unset = UNSET,
) -> None:
    """Delete a branch.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).
        repo_slug: Repository slug.
        branch_id: The fully-qualified branch ID to delete (e.g. ``"refs/heads/feature/my-branch"``).
        dry_run: If ``True``, validate the delete without executing it.

    Returns:
        ``None``.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.datacenter import BBDCClient
        from bb.datacenter.sdk import branches

        client = BBDCClient.from_env()
        await branches.delete(
            client,
            project_key="PRJ",
            repo_slug="myrepo",
            branch_id="refs/heads/feature/my-branch",
        )
        ```

    References:
        `DELETE /branch-utils/latest/projects/{projectKey}/repos/{repositorySlug}/branches
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-repository/#api-branch-utils-latest-projects-projectkey-repos-repositoryslug-branches-delete>`_
    """
    from bb.datacenter.models.rest_branch_delete_request import RestBranchDeleteRequest

    body = RestBranchDeleteRequest(name=branch_id, dry_run=dry_run)
    await delete_branch.asyncio(project_key, repo_slug, client=client.auth, body=body)
