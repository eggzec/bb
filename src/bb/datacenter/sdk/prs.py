"""Bitbucket Data Center pull request SDK wrappers.

Maps to the ``pull_requests`` API tag under
``/api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests``.
"""

from __future__ import annotations

from bb.datacenter.models.rest_pull_request import RestPullRequest
from bb.datacenter.models.rest_pull_request_merge_request import RestPullRequestMergeRequest
from bb.datacenter.sdk._auth_validation import AuthMethod, require_auth
from bb.datacenter.sdk._client import BBDCClient
from bb.datacenter.sdk._pagination import async_paginate
from bb.datacenter.types import UNSET, Unset

__all__ = [
    "list",
    "get",
    "create",
    "update",
    "merge",
    "decline",
    "approve",
    "unapprove",
]


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def list(
    client: BBDCClient,
    project_key: str,
    repo_slug: str,
    *,
    state: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    at: str | Unset = UNSET,
    order: str | Unset = UNSET,
    filter_text: str | Unset = UNSET,
    limit: int = 25,
) -> list[RestPullRequest]:
    """List all pull requests for a repository across all pages.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).
        repo_slug: Repository slug.
        state: Filter by pull request state. One of ``"OPEN"``, ``"MERGED"``,
            ``"DECLINED"``, or ``"ALL"``. Defaults to ``"OPEN"``.
        direction: Direction relative to the repository. ``"INCOMING"`` or ``"OUTGOING"``.
        at: Fully-qualified branch ID to filter pull requests targeting or leaving that branch.
        order: Sort order. ``"NEWEST"`` or ``"OLDEST"``.
        filter_text: Text to filter pull requests by title or description.
        limit: Number of results per page. Defaults to ``25``.

    Returns:
        All pull requests matching the filters across all pages.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.datacenter import BBDCClient
        from bb.datacenter.sdk import prs

        client = BBDCClient.from_env()
        open_prs = await prs.list(client, project_key="PRJ", repo_slug="myrepo")
        ```

    References:
        `GET /api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-pull-requests/#api-api-latest-projects-projectkey-repos-repositoryslug-pull-requests-get>`_
    """
    from bb.datacenter.api.pull_requests import get_page

    return [
        pr
        async for pr in async_paginate(
            get_page.asyncio,
            project_key,
            repo_slug,
            client=client.auth,
            state=state,
            direction=direction,
            at=at,
            order=order,
            filter_text=filter_text,
            limit=limit,
        )
        if isinstance(pr, RestPullRequest)
    ]


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def get(
    client: BBDCClient,
    project_key: str,
    repo_slug: str,
    pull_request_id: str,
) -> RestPullRequest | None:
    """Fetch a single pull request by ID.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).
        repo_slug: Repository slug.
        pull_request_id: The pull request ID.

    Returns:
        The :class:`~bb.datacenter.models.rest_pull_request.RestPullRequest`,
        or ``None`` if not found.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.datacenter import BBDCClient
        from bb.datacenter.sdk import prs

        client = BBDCClient.from_env()
        pr = await prs.get(client, project_key="PRJ", repo_slug="myrepo", pull_request_id="42")
        ```

    References:
        `GET /api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-pull-requests/#api-api-latest-projects-projectkey-repos-repositoryslug-pull-requests-pullrequestid-get>`_
    """
    from bb.datacenter.api.pull_requests import get_3

    result = await get_3.asyncio(project_key, repo_slug, pull_request_id, client=client.auth)
    return result if isinstance(result, RestPullRequest) else None


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def create(
    client: BBDCClient,
    project_key: str,
    repo_slug: str,
    *,
    body: RestPullRequest | Unset = UNSET,
) -> RestPullRequest | None:
    """Create a new pull request.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).
        repo_slug: Repository slug.
        body: Pull request body.
            Use :class:`~bb.datacenter.models.rest_pull_request.RestPullRequest`.

    Returns:
        The created :class:`~bb.datacenter.models.rest_pull_request.RestPullRequest`,
        or ``None`` on error.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.datacenter import BBDCClient
        from bb.datacenter.models.rest_pull_request import RestPullRequest
        from bb.datacenter.sdk import prs

        client = BBDCClient.from_env()
        pr = await prs.create(
            client,
            project_key="PRJ",
            repo_slug="myrepo",
            body=RestPullRequest(title="My PR", ...),
        )
        ```

    References:
        `POST /api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-pull-requests/#api-api-latest-projects-projectkey-repos-repositoryslug-pull-requests-post>`_
    """
    from bb.datacenter.api.pull_requests import create as _create_pr

    result = await _create_pr.asyncio(project_key, repo_slug, client=client.auth, body=body)
    return result if isinstance(result, RestPullRequest) else None


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def update(
    client: BBDCClient,
    project_key: str,
    repo_slug: str,
    pull_request_id: str,
    *,
    body: RestPullRequest | Unset = UNSET,
) -> RestPullRequest | None:
    """Update an existing pull request.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).
        repo_slug: Repository slug.
        pull_request_id: The pull request ID.
        body: Fields to update.
            Use :class:`~bb.datacenter.models.rest_pull_request.RestPullRequest`.

    Returns:
        The updated :class:`~bb.datacenter.models.rest_pull_request.RestPullRequest`,
        or ``None`` on error.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.datacenter import BBDCClient
        from bb.datacenter.sdk import prs

        client = BBDCClient.from_env()
        pr = await prs.update(
            client, project_key="PRJ", repo_slug="myrepo", pull_request_id="42",
            body=RestPullRequest(title="Updated title"),
        )
        ```

    References:
        `PUT /api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-pull-requests/#api-api-latest-projects-projectkey-repos-repositoryslug-pull-requests-pullrequestid-put>`_
    """
    from bb.datacenter.api.pull_requests import update as _update_pr

    result = await _update_pr.asyncio(project_key, repo_slug, pull_request_id, client=client.auth, body=body)
    return result if isinstance(result, RestPullRequest) else None


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def merge(
    client: BBDCClient,
    project_key: str,
    repo_slug: str,
    pull_request_id: str,
    *,
    body: RestPullRequestMergeRequest | Unset = UNSET,
    version: str | Unset = UNSET,
) -> RestPullRequest | None:
    """Merge a pull request.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).
        repo_slug: Repository slug.
        pull_request_id: The pull request ID.
        body: Optional merge configuration.
            Use :class:`~bb.datacenter.models.rest_pull_request_merge_request.RestPullRequestMergeRequest`.
        version: The current version of the pull request (for optimistic concurrency).

    Returns:
        The merged :class:`~bb.datacenter.models.rest_pull_request.RestPullRequest`,
        or ``None`` on error.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.datacenter import BBDCClient
        from bb.datacenter.sdk import prs

        client = BBDCClient.from_env()
        merged = await prs.merge(client, project_key="PRJ", repo_slug="myrepo", pull_request_id="42")
        ```

    References:
        `POST /api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/merge
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-pull-requests/#api-api-latest-projects-projectkey-repos-repositoryslug-pull-requests-pullrequestid-merge-post>`_
    """
    from bb.datacenter.api.pull_requests import merge as _merge_pr

    result = await _merge_pr.asyncio(
        project_key, repo_slug, pull_request_id, client=client.auth, body=body, version=version
    )
    return result if isinstance(result, RestPullRequest) else None


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def decline(
    client: BBDCClient,
    project_key: str,
    repo_slug: str,
    pull_request_id: str,
    *,
    version: str | Unset = UNSET,
) -> RestPullRequest | None:
    """Decline a pull request.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).
        repo_slug: Repository slug.
        pull_request_id: The pull request ID.
        version: The current version of the pull request (for optimistic concurrency).

    Returns:
        The declined :class:`~bb.datacenter.models.rest_pull_request.RestPullRequest`,
        or ``None`` on error.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.datacenter import BBDCClient
        from bb.datacenter.sdk import prs

        client = BBDCClient.from_env()
        await prs.decline(client, project_key="PRJ", repo_slug="myrepo", pull_request_id="42")
        ```

    References:
        `POST /api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/decline
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-pull-requests/#api-api-latest-projects-projectkey-repos-repositoryslug-pull-requests-pullrequestid-decline-post>`_
    """
    from bb.datacenter.api.pull_requests import decline as _decline_pr

    result = await _decline_pr.asyncio(project_key, repo_slug, pull_request_id, client=client.auth, version=version)
    return result if isinstance(result, RestPullRequest) else None


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def approve(
    client: BBDCClient,
    project_key: str,
    repo_slug: str,
    pull_request_id: str,
) -> None:
    """Approve a pull request.

    .. deprecated::
        This endpoint is part of the ``deprecated`` API group in the
        Bitbucket Data Center REST API.  It may be removed in a future
        server version.  No date-based removal guarantee is published.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).
        repo_slug: Repository slug.
        pull_request_id: The pull request ID.

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
        from bb.datacenter.sdk import prs

        client = BBDCClient.from_env()
        await prs.approve(client, project_key="PRJ", repo_slug="myrepo", pull_request_id="42")
        ```

    References:
        `POST /api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/approve
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-deprecated/#api-api-latest-projects-projectkey-repos-repositoryslug-pull-requests-pullrequestid-approve-post>`_
    """
    from bb.datacenter.api.pull_requests import approve as _approve_pr

    await _approve_pr.asyncio(project_key, repo_slug, pull_request_id, client=client.auth)


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def unapprove(
    client: BBDCClient,
    project_key: str,
    repo_slug: str,
    pull_request_id: str,
) -> None:
    """Withdraw approval from a pull request.

    .. deprecated::
        This endpoint is part of the ``deprecated`` API group in the
        Bitbucket Data Center REST API.  It may be removed in a future
        server version.  No date-based removal guarantee is published.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).
        repo_slug: Repository slug.
        pull_request_id: The pull request ID.

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
        from bb.datacenter.sdk import prs

        client = BBDCClient.from_env()
        await prs.unapprove(client, project_key="PRJ", repo_slug="myrepo", pull_request_id="42")
        ```

    References:
        `DELETE /api/latest/projects/{projectKey}/repos/{repositorySlug}/pull-requests/{pullRequestId}/approve
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-deprecated/#api-api-latest-projects-projectkey-repos-repositoryslug-pull-requests-pullrequestid-approve-delete>`_
    """
    from bb.datacenter.api.pull_requests import withdraw_approval

    await withdraw_approval.asyncio(project_key, repo_slug, pull_request_id, client=client.auth)
