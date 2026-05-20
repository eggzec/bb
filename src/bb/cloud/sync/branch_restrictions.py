from __future__ import annotations
from bb.cloud.models.branchrestriction import Branchrestriction
from bb.cloud.models.error import Error
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset
from bb.cloud.sdk import branch_restrictions as _async
__all__ = ['list', 'get', 'create', 'update', 'delete']

def list(client: BBClient, workspace: str, repo_slug: str, *, pagelen: int=25) -> list[Branchrestriction] | Error:
    """List all branch restrictions for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.branch_restrictions.list`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    List of :class:`~bb.cloud.models.branchrestriction.Branchrestriction` objects.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import branch_restrictions

    client = BBClient.from_env()
    result = branch_restrictions.list(client, workspace="myws", repo_slug="myrepo")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/branch-restrictions
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branch-restrictions/#api-repositories-workspace-repo-slug-branch-restrictions-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.branch_restrictions.list`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.list(client, workspace, repo_slug, pagelen=pagelen))

def get(client: BBClient, workspace: str, repo_slug: str, id: int) -> Branchrestriction | Error | None:
    """Retrieve a single branch restriction by ID.

Synchronous wrapper around :func:`~bb.cloud.sdk.branch_restrictions.get`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    id: Numeric ID of the branch restriction.

Returns:
    A :class:`~bb.cloud.models.branchrestriction.Branchrestriction` object, or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import branch_restrictions

    client = BBClient.from_env()
    restriction = branch_restrictions.get(client, workspace="myws", repo_slug="myrepo", id=1)
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/branch-restrictions/{id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branch-restrictions/#api-repositories-workspace-repo-slug-branch-restrictions-id-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.branch_restrictions.get`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get(client, workspace, repo_slug, id))

def create(client: BBClient, workspace: str, repo_slug: str, *, body: Branchrestriction | Unset=UNSET) -> Branchrestriction | Error | None:
    """Create a branch restriction on a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.branch_restrictions.create`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    body: Branch restriction payload. Defaults to :data:`~bb.cloud.types.UNSET`.

Returns:
    The created :class:`~bb.cloud.models.branchrestriction.Branchrestriction`, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import branch_restrictions
    from bb.cloud.models.branchrestriction import Branchrestriction

    client = BBClient.from_env()
    restriction = branch_restrictions.create(
        client, workspace="myws", repo_slug="myrepo", body=Branchrestriction(...)
    )
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/branch-restrictions
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branch-restrictions/#api-repositories-workspace-repo-slug-branch-restrictions-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.branch_restrictions.create`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.create(client, workspace, repo_slug, body=body))

def update(client: BBClient, workspace: str, repo_slug: str, id: int, *, body: Branchrestriction | Unset=UNSET) -> Branchrestriction | Error | None:
    """Update a branch restriction on a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.branch_restrictions.update`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    id: Numeric ID of the branch restriction to update.
    body: Updated branch restriction payload. Defaults to :data:`~bb.cloud.types.UNSET`.

Returns:
    The updated :class:`~bb.cloud.models.branchrestriction.Branchrestriction`, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import branch_restrictions
    from bb.cloud.models.branchrestriction import Branchrestriction

    client = BBClient.from_env()
    restriction = branch_restrictions.update(
        client, workspace="myws", repo_slug="myrepo", id=1, body=Branchrestriction(...)
    )
    ```

References:
    `PUT /2.0/repositories/{workspace}/{repo_slug}/branch-restrictions/{id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branch-restrictions/#api-repositories-workspace-repo-slug-branch-restrictions-id-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.branch_restrictions.update`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.update(client, workspace, repo_slug, id, body=body))

def delete(client: BBClient, workspace: str, repo_slug: str, id: int) -> None:
    """Delete a branch restriction from a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.branch_restrictions.delete`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    id: Numeric ID of the branch restriction to delete.

Returns:
    None.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import branch_restrictions

    client = BBClient.from_env()
    branch_restrictions.delete(client, workspace="myws", repo_slug="myrepo", id=1)
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/branch-restrictions/{id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branch-restrictions/#api-repositories-workspace-repo-slug-branch-restrictions-id-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.branch_restrictions.delete`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.delete(client, workspace, repo_slug, id))
