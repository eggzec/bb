from __future__ import annotations
import asyncio
from bb.cloud.models.base_commit import BaseCommit
from bb.cloud.models.commit import Commit
from bb.cloud.models.error import Error
from bb.cloud.models.pullrequest import Pullrequest
from bb.cloud.sdk._client import BBClient
from bb.cloud.sdk import commits as _async
__all__ = ['list', 'get', 'prs']

def list(client: BBClient, workspace: str, repo_slug: str, *, pagelen: int=25) -> list[BaseCommit] | Error:
    """List all commits for a repository across all pages.

Synchronous wrapper around :func:`~bb.cloud.sdk.commits.list`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
    repo_slug: Repository slug or UUID.
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    All :class:`~bb.cloud.models.base_commit.BaseCommit` objects across all pages.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import commits

    client = BBClient.from_env()
    result = commits.list(client, workspace="myworkspace", repo_slug="myrepo")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/commits
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-commits/#api-repositories-workspace-repo-slug-commits-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.commits.list`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.list(client, workspace, repo_slug, pagelen=pagelen))

def get(client: BBClient, workspace: str, repo_slug: str, commit: str) -> Commit | Error | None:
    """Fetch a single commit by hash.

Synchronous wrapper around :func:`~bb.cloud.sdk.commits.get`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
    repo_slug: Repository slug or UUID.
    commit: Full or abbreviated commit hash.

Returns:
    The :class:`~bb.cloud.models.commit.Commit`, or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import commits

    client = BBClient.from_env()
    commit = commits.get(
        client, workspace="myworkspace", repo_slug="myrepo", commit="a1b2c3d4"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-commits/#api-repositories-workspace-repo-slug-commit-commit-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.commits.get`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.get(client, workspace, repo_slug, commit))

def prs(client: BBClient, workspace: str, repo_slug: str, commit: str, *, pagelen: int=25) -> list[Pullrequest] | Error:
    """List all pull requests that include a given commit across all pages.

Synchronous wrapper around :func:`~bb.cloud.sdk.commits.prs`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
    repo_slug: Repository slug or UUID.
    commit: Full or abbreviated commit hash.
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    All :class:`~bb.cloud.models.pullrequest.Pullrequest` objects that contain the
    commit across all pages.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import commits

    client = BBClient.from_env()
    result = commits.prs(
        client, workspace="myworkspace", repo_slug="myrepo", commit="a1b2c3d4"
    )
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/commit/{commit}/pullrequests
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-commits/#api-repositories-workspace-repo-slug-commit-commit-pullrequests-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.commits.prs`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.prs(client, workspace, repo_slug, commit, pagelen=pagelen))
