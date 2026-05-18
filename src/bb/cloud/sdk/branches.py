from __future__ import annotations

from bb.cloud.api.refs import (
    delete_repositories_workspace_repo_slug_refs_branches_name,
    delete_repositories_workspace_repo_slug_refs_tags_name,
    get_repositories_workspace_repo_slug_refs_branches,
    get_repositories_workspace_repo_slug_refs_branches_name,
    get_repositories_workspace_repo_slug_refs_tags,
    get_repositories_workspace_repo_slug_refs_tags_name,
    post_repositories_workspace_repo_slug_refs_tags,
)
from bb.cloud.models.branch import Branch
from bb.cloud.models.error import Error
from bb.cloud.models.tag import Tag
from bb.cloud.sdk._auth_validation import AuthMethod, require_auth
from bb.cloud.sdk._client import BBClient
from bb.cloud.sdk._pagination import async_paginate
from bb.cloud.types import UNSET, Unset

__all__ = ["list", "get", "create", "delete", "tags", "get_tag", "create_tag", "delete_tag"]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def list(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagelen: int = 25,
) -> list[Branch] | Error:
    """List all branches for a repository across all pages.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        q: Optional query filter string (Bitbucket query syntax, e.g. ``name ~ "feature"``).
        sort: Optional sort field (e.g. ``-target.date`` for newest first).
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All :class:`~bb.cloud.models.branch.Branch` objects across all pages.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import branches

        client = BBClient.from_env()
        result = await branches.list(client, workspace="myworkspace", repo_slug="myrepo")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/refs/branches
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-refs/#api-repositories-workspace-repo-slug-refs-branches-get>`_
    """
    result = await async_paginate(
        get_repositories_workspace_repo_slug_refs_branches.asyncio,
        workspace,
        repo_slug,
        client=client.auth,
        q=q,
        sort=sort,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [item for item in result if isinstance(item, Branch)]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get(client: BBClient, workspace: str, repo_slug: str, name: str) -> Branch | Error | None:
    """Fetch a single branch by name.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        name: Branch name (e.g. ``main`` or ``feature/my-feature``).

    Returns:
        The :class:`~bb.cloud.models.branch.Branch`, or ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import branches

        client = BBClient.from_env()
        branch = await branches.get(
            client, workspace="myworkspace", repo_slug="myrepo", name="main"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/refs/branches/{name}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-refs/#api-repositories-workspace-repo-slug-refs-branches-name-get>`_
    """
    result = await get_repositories_workspace_repo_slug_refs_branches_name.asyncio(
        workspace, repo_slug, name, client=client.auth
    )
    if isinstance(result, (Branch, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def create(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    name: str,
    target_hash: str,
) -> Branch | Error | None:
    """Create a branch pointing at a target commit hash.

    The Bitbucket Cloud spec omits ``requestBody`` for this endpoint so the generated
    wrapper has no body parameter. This function sends the JSON body directly via the
    underlying async httpx client.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        name: Name of the new branch.
        target_hash: Full commit hash that the new branch should point to.

    Returns:
        The created :class:`~bb.cloud.models.branch.Branch`, or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import branches

        client = BBClient.from_env()
        branch = await branches.create(
            client,
            workspace="myworkspace",
            repo_slug="myrepo",
            name="feature/new-branch",
            target_hash="a1b2c3d4e5f6",
        )
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/refs/branches
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-refs/#api-repositories-workspace-repo-slug-refs-branches-post>`_
    """
    http = client.auth.get_async_httpx_client()
    resp = await http.post(
        f"/repositories/{workspace}/{repo_slug}/refs/branches",
        json={"name": name, "target": {"hash": target_hash}},
    )
    if resp.status_code == 201:
        return Branch.from_dict(resp.json())
    if "application/json" in resp.headers.get("content-type", ""):
        try:
            return Error.from_dict(resp.json())
        except Exception:
            pass
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete(client: BBClient, workspace: str, repo_slug: str, name: str) -> None:
    """Delete a branch.

    Does not raise on 404 or other non-success status codes.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        name: Branch name to delete.

    Returns:
        None.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import branches

        client = BBClient.from_env()
        await branches.delete(
            client, workspace="myworkspace", repo_slug="myrepo", name="feature/old-branch"
        )
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/refs/branches/{name}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-refs/#api-repositories-workspace-repo-slug-refs-branches-name-delete>`_
    """
    await delete_repositories_workspace_repo_slug_refs_branches_name.asyncio(
        workspace, repo_slug, name, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def tags(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagelen: int = 25,
) -> list[Tag] | Error:
    """List all tags for a repository across all pages.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        q: Optional query filter string (Bitbucket query syntax).
        sort: Optional sort field (e.g. ``-target.date`` for newest first).
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        All :class:`~bb.cloud.models.tag.Tag` objects across all pages.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import branches

        client = BBClient.from_env()
        result = await branches.tags(client, workspace="myworkspace", repo_slug="myrepo")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/refs/tags
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-refs/#api-repositories-workspace-repo-slug-refs-tags-get>`_
    """
    result = await async_paginate(
        get_repositories_workspace_repo_slug_refs_tags.asyncio,
        workspace,
        repo_slug,
        client=client.auth,
        q=q,
        sort=sort,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [item for item in result if isinstance(item, Tag)]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_tag(client: BBClient, workspace: str, repo_slug: str, name: str) -> Tag | Error | None:
    """Fetch a single tag by name.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        name: Tag name.

    Returns:
        The :class:`~bb.cloud.models.tag.Tag`, or ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import branches

        client = BBClient.from_env()
        tag = await branches.get_tag(
            client, workspace="myworkspace", repo_slug="myrepo", name="v1.0.0"
        )
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/refs/tags/{name}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-refs/#api-repositories-workspace-repo-slug-refs-tags-name-get>`_
    """
    result = await get_repositories_workspace_repo_slug_refs_tags_name.asyncio(
        workspace, repo_slug, name, client=client.auth
    )
    if isinstance(result, (Tag, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def create_tag(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: Tag | Unset = UNSET,
) -> Tag | Error | None:
    """Create a tag in a repository.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        body: Tag payload. Use :class:`~bb.cloud.models.tag.Tag` populated with at minimum
            ``name`` and ``target``.

    Returns:
        The created :class:`~bb.cloud.models.tag.Tag`, or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import branches
        from bb.cloud.models.tag import Tag

        client = BBClient.from_env()
        tag = await branches.create_tag(
            client, workspace="myworkspace", repo_slug="myrepo", body=Tag(name="v1.0.0", ...)
        )
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/refs/tags
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-refs/#api-repositories-workspace-repo-slug-refs-tags-post>`_
    """
    result = await post_repositories_workspace_repo_slug_refs_tags.asyncio(
        workspace, repo_slug, client=client.auth, body=body
    )
    if isinstance(result, (Tag, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete_tag(client: BBClient, workspace: str, repo_slug: str, name: str) -> None:
    """Delete a tag from a repository.

    Does not raise on 404 or other non-success status codes.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID (with surrounding braces, e.g. ``{abc-123}``).
        repo_slug: Repository slug or UUID.
        name: Tag name to delete.

    Returns:
        None.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import branches

        client = BBClient.from_env()
        await branches.delete_tag(
            client, workspace="myworkspace", repo_slug="myrepo", name="v0.9.0"
        )
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/refs/tags/{name}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-refs/#api-repositories-workspace-repo-slug-refs-tags-name-delete>`_
    """
    await delete_repositories_workspace_repo_slug_refs_tags_name.asyncio(workspace, repo_slug, name, client=client.auth)
