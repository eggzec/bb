"""Bitbucket Data Center builds and required-builds SDK wrappers.

Covers build status reporting and required-build merge-check conditions under:
  ``/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/builds``
  ``/required-builds/latest/projects/{projectKey}/repos/{repositorySlug}/condition``
"""

from __future__ import annotations

from bb.datacenter.api.builds_and_deployments import (
    create_required_builds_merge_check,
    delete_required_builds_merge_check,
    get_page_of_required_builds_merge_checks,
    update_required_builds_merge_check,
)
from bb.datacenter.models.rest_required_build_condition import RestRequiredBuildCondition
from bb.datacenter.models.rest_required_build_condition_set_request import RestRequiredBuildConditionSetRequest
from bb.datacenter.sdk._auth_validation import AuthMethod, require_auth
from bb.datacenter.sdk._client import BBDCClient
from bb.datacenter.sdk._pagination import async_paginate
from bb.datacenter.types import UNSET, Unset

__all__ = [
    "add_build_status",
    "list_required_builds",
    "create_required_build",
    "update_required_build",
    "delete_required_build",
]


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def add_build_status(
    client: BBDCClient,
    project_key: str,
    repo_slug: str,
    commit_id: str,
    *,
    body: Unset = UNSET,
) -> None:
    """Report a build status for a commit.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).
        repo_slug: Repository slug.
        commit_id: The full commit SHA.
        body: :class:`~bb.datacenter.models.rest_build_status_set_request.RestBuildStatusSetRequest`
            with ``state``, ``key``, and ``url`` fields.

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
        from bb.datacenter.models.rest_build_status_set_request import RestBuildStatusSetRequest
        from bb.datacenter.sdk import builds

        client = BBDCClient.from_env()
        await builds.add_build_status(
            client,
            project_key="PRJ",
            repo_slug="myrepo",
            commit_id="abc123",
            body=RestBuildStatusSetRequest(state="SUCCESSFUL", key="ci/mycheck", url="https://ci.example.com/1"),
        )
        ```

    References:
        `POST /api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/builds
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-builds-and-deployments/#api-api-latest-projects-projectkey-repos-repositoryslug-commits-commitid-builds-post>`_
    """
    from bb.datacenter.api.builds_and_deployments import add

    await add.asyncio(project_key, repo_slug, commit_id, client=client.auth, body=body)


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def list_required_builds(
    client: BBDCClient,
    project_key: str,
    repo_slug: str,
    *,
    limit: int = 25,
) -> list[RestRequiredBuildCondition]:
    """List all required-build merge-check conditions for a repository.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).
        repo_slug: Repository slug.
        limit: Number of results per page. Defaults to ``25``.

    Returns:
        All :class:`~bb.datacenter.models.rest_required_build_condition.RestRequiredBuildCondition`
        objects across all pages.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.datacenter import BBDCClient
        from bb.datacenter.sdk import builds

        client = BBDCClient.from_env()
        conditions = await builds.list_required_builds(client, project_key="PRJ", repo_slug="myrepo")
        ```

    References:
        `GET /required-builds/latest/projects/{projectKey}/repos/{repositorySlug}/condition
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-builds-and-deployments/#api-required-builds-latest-projects-projectkey-repos-repositoryslug-condition-get>`_
    """
    return [
        c
        async for c in async_paginate(
            get_page_of_required_builds_merge_checks.asyncio,
            project_key,
            repo_slug,
            client=client.auth,
            limit=limit,
        )
        if isinstance(c, RestRequiredBuildCondition)
    ]


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def create_required_build(
    client: BBDCClient,
    project_key: str,
    repo_slug: str,
    *,
    body: RestRequiredBuildConditionSetRequest | Unset = UNSET,
) -> RestRequiredBuildCondition | None:
    """Create a required-build merge-check condition for a repository.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).
        repo_slug: Repository slug.
        body: :class:`~bb.datacenter.models.rest_required_build_condition_set_request.RestRequiredBuildConditionSetRequest`
            describing the required build keys and exempt ref matcher.

    Returns:
        The created :class:`~bb.datacenter.models.rest_required_build_condition.RestRequiredBuildCondition`,
        or ``None`` on error.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.datacenter import BBDCClient
        from bb.datacenter.sdk import builds

        client = BBDCClient.from_env()
        condition = await builds.create_required_build(
            client, project_key="PRJ", repo_slug="myrepo", body=...
        )
        ```

    References:
        `POST /required-builds/latest/projects/{projectKey}/repos/{repositorySlug}/condition
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-builds-and-deployments/#api-required-builds-latest-projects-projectkey-repos-repositoryslug-condition-post>`_
    """
    result = await create_required_builds_merge_check.asyncio(project_key, repo_slug, client=client.auth, body=body)
    return result if isinstance(result, RestRequiredBuildCondition) else None


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def update_required_build(
    client: BBDCClient,
    project_key: str,
    repo_slug: str,
    condition_id: int,
    *,
    body: RestRequiredBuildConditionSetRequest | Unset = UNSET,
) -> RestRequiredBuildCondition | None:
    """Update an existing required-build merge-check condition.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).
        repo_slug: Repository slug.
        condition_id: The numeric ID of the condition to update.
        body: Updated condition details.

    Returns:
        The updated :class:`~bb.datacenter.models.rest_required_build_condition.RestRequiredBuildCondition`,
        or ``None`` on error.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    References:
        `PUT /required-builds/latest/projects/{projectKey}/repos/{repositorySlug}/condition/{id}
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-builds-and-deployments/#api-required-builds-latest-projects-projectkey-repos-repositoryslug-condition-id-put>`_
    """
    result = await update_required_builds_merge_check.asyncio(
        project_key, repo_slug, condition_id, client=client.auth, body=body
    )
    return result if isinstance(result, RestRequiredBuildCondition) else None


@require_auth(AuthMethod.BEARER, AuthMethod.BASIC)
async def delete_required_build(
    client: BBDCClient,
    project_key: str,
    repo_slug: str,
    condition_id: int,
) -> None:
    """Delete a required-build merge-check condition.

    Args:
        client: Authenticated :class:`~bb.datacenter.sdk._client.BBDCClient` instance.
        project_key: The project key (e.g. ``"PRJ"``).
        repo_slug: Repository slug.
        condition_id: The numeric ID of the condition to delete.

    Returns:
        ``None``.

    Raises:
        :exc:`~bb.datacenter.sdk._errors.AuthenticationError`: If ``client`` uses an
            unrecognised or unsupported auth method.
        :exc:`~bb.datacenter.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    References:
        `DELETE /required-builds/latest/projects/{projectKey}/repos/{repositorySlug}/condition/{id}
        <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-builds-and-deployments/#api-required-builds-latest-projects-projectkey-repos-repositoryslug-condition-id-delete>`_
    """
    await delete_required_builds_merge_check.asyncio(project_key, repo_slug, condition_id, client=client.auth)
