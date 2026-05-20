from __future__ import annotations
from bb.cloud.models.commitstatus import Commitstatus
from bb.cloud.models.error import Error
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset
from bb.cloud.sdk import commit_statuses as _async
__all__ = ['list', 'get', 'create', 'update']

def list(client: BBClient, workspace: str, repo_slug: str, commit: str, *, pagelen: int=25) -> list[Commitstatus] | Error:
    """List all commit statuses for a given commit.

Synchronous wrapper around :func:`~bb.cloud.sdk.commit_statuses.list`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    commit: Full SHA1 of the commit.
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    List of :class:`~bb.cloud.models.commitstatus.Commitstatus` objects.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import commit_statuses

    client = BBClient.from_env()
    statuses = commit_statuses.list(
        client, workspace="myws", repo_slug="myrepo", commit="abc123"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}/statuses
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-commit-statuses/#api-repositories-workspace-repo-slug-commit-commit-statuses-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.commit_statuses.list`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.list(client, workspace, repo_slug, commit, pagelen=pagelen))

def get(client: BBClient, workspace: str, repo_slug: str, commit: str, key: str) -> Commitstatus | Error | None:
    """Retrieve a single commit status by build key.

Synchronous wrapper around :func:`~bb.cloud.sdk.commit_statuses.get`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    commit: Full SHA1 of the commit.
    key: Unique key identifying the build status.

Returns:
    A :class:`~bb.cloud.models.commitstatus.Commitstatus` object, or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import commit_statuses

    client = BBClient.from_env()
    status = commit_statuses.get(
        client, workspace="myws", repo_slug="myrepo", commit="abc123", key="my-build"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build/{key}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-commit-statuses/#api-repositories-workspace-repo-slug-commit-commit-statuses-build-key-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.commit_statuses.get`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get(client, workspace, repo_slug, commit, key))

def create(client: BBClient, workspace: str, repo_slug: str, commit: str, *, body: Commitstatus | Unset=UNSET) -> Commitstatus | Error | None:
    """Create a commit status (build result) for a commit.

Synchronous wrapper around :func:`~bb.cloud.sdk.commit_statuses.create`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    commit: Full SHA1 of the commit.
    body: Commit status payload. Defaults to :data:`~bb.cloud.types.UNSET`.

Returns:
    The created :class:`~bb.cloud.models.commitstatus.Commitstatus`, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import commit_statuses
    from bb.cloud.models.commitstatus import Commitstatus

    client = BBClient.from_env()
    status = commit_statuses.create(
        client, workspace="myws", repo_slug="myrepo", commit="abc123", body=Commitstatus(...)
    )
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-commit-statuses/#api-repositories-workspace-repo-slug-commit-commit-statuses-build-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.commit_statuses.create`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.create(client, workspace, repo_slug, commit, body=body))

def update(client: BBClient, workspace: str, repo_slug: str, commit: str, key: str, *, body: Commitstatus | Unset=UNSET) -> Commitstatus | Error | None:
    """Update an existing commit status by build key.

Synchronous wrapper around :func:`~bb.cloud.sdk.commit_statuses.update`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    commit: Full SHA1 of the commit.
    key: Unique key identifying the build status to update.
    body: Updated commit status payload. Defaults to :data:`~bb.cloud.types.UNSET`.

Returns:
    The updated :class:`~bb.cloud.models.commitstatus.Commitstatus`, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import commit_statuses
    from bb.cloud.models.commitstatus import Commitstatus

    client = BBClient.from_env()
    status = commit_statuses.update(
        client,
        workspace="myws",
        repo_slug="myrepo",
        commit="abc123",
        key="my-build",
        body=Commitstatus(...),
    )
    ```

References:
    `PUT /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build/{key}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-commit-statuses/#api-repositories-workspace-repo-slug-commit-commit-statuses-build-key-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.commit_statuses.update`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.update(client, workspace, repo_slug, commit, key, body=body))
