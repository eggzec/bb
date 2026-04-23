"""Bitbucket Data Center builds and required-builds synchronous SDK wrappers.

Synchronous wrappers around :mod:`bb.datacenter.sdk.builds` using :func:`asyncio.run`.


Covers build status reporting and required-build merge-check conditions under:
  ``/api/latest/projects/{projectKey}/repos/{repositorySlug}/commits/{commitId}/builds``
  ``/required-builds/latest/projects/{projectKey}/repos/{repositorySlug}/condition``"""
from __future__ import annotations
import asyncio
from bb.datacenter.models.rest_required_build_condition import RestRequiredBuildCondition
from bb.datacenter.models.rest_required_build_condition_set_request import RestRequiredBuildConditionSetRequest
from bb.datacenter.sdk._client import BBDCClient
from bb.datacenter.types import UNSET, Unset
from bb.datacenter.sdk import builds as _async
__all__ = ['add_build_status', 'list_required_builds', 'create_required_build', 'update_required_build', 'delete_required_build']

def add_build_status(client: BBDCClient, project_key: str, repo_slug: str, commit_id: str, *, body: Unset=UNSET) -> None:
    """Report a build status for a commit.

Synchronous wrapper around :func:`~bb.datacenter.sdk.builds.add_build_status`.

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
    builds.add_build_status(
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

Note:
    This synchronous wrapper executes :func:`~bb.datacenter.sdk.builds.add_build_status`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.add_build_status(client, project_key, repo_slug, commit_id, body=body))

def list_required_builds(client: BBDCClient, project_key: str, repo_slug: str, *, limit: int=25) -> list[RestRequiredBuildCondition]:
    """List all required-build merge-check conditions for a repository.

Synchronous wrapper around :func:`~bb.datacenter.sdk.builds.list_required_builds`.

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
    conditions = builds.list_required_builds(client, project_key="PRJ", repo_slug="myrepo")
    ```

References:
    `GET /required-builds/latest/projects/{projectKey}/repos/{repositorySlug}/condition
    <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-builds-and-deployments/#api-required-builds-latest-projects-projectkey-repos-repositoryslug-condition-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.datacenter.sdk.builds.list_required_builds`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.list_required_builds(client, project_key, repo_slug, limit=limit))

def create_required_build(client: BBDCClient, project_key: str, repo_slug: str, *, body: RestRequiredBuildConditionSetRequest | Unset=UNSET) -> RestRequiredBuildCondition | None:
    """Create a required-build merge-check condition for a repository.

Synchronous wrapper around :func:`~bb.datacenter.sdk.builds.create_required_build`.

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
    condition = builds.create_required_build(
        client, project_key="PRJ", repo_slug="myrepo", body=...
    )
    ```

References:
    `POST /required-builds/latest/projects/{projectKey}/repos/{repositorySlug}/condition
    <https://developer.atlassian.com/server/bitbucket/rest/v1002/api-group-builds-and-deployments/#api-required-builds-latest-projects-projectkey-repos-repositoryslug-condition-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.datacenter.sdk.builds.create_required_build`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.create_required_build(client, project_key, repo_slug, body=body))

def update_required_build(client: BBDCClient, project_key: str, repo_slug: str, condition_id: int, *, body: RestRequiredBuildConditionSetRequest | Unset=UNSET) -> RestRequiredBuildCondition | None:
    """Update an existing required-build merge-check condition.

Synchronous wrapper around :func:`~bb.datacenter.sdk.builds.update_required_build`.

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

Note:
    This synchronous wrapper executes :func:`~bb.datacenter.sdk.builds.update_required_build`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.update_required_build(client, project_key, repo_slug, condition_id, body=body))

def delete_required_build(client: BBDCClient, project_key: str, repo_slug: str, condition_id: int) -> None:
    """Delete a required-build merge-check condition.

Synchronous wrapper around :func:`~bb.datacenter.sdk.builds.delete_required_build`.

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

Note:
    This synchronous wrapper executes :func:`~bb.datacenter.sdk.builds.delete_required_build`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.delete_required_build(client, project_key, repo_slug, condition_id))
