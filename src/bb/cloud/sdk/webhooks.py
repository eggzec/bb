from __future__ import annotations

from bb.cloud.api.webhooks import (
    delete_repositories_workspace_repo_slug_hooks_uid,
    delete_workspaces_workspace_hooks_uid,
    get_hook_events_subject_type,
    get_repositories_workspace_repo_slug_hooks,
    get_repositories_workspace_repo_slug_hooks_uid,
    get_workspaces_workspace_hooks,
    get_workspaces_workspace_hooks_uid,
    post_repositories_workspace_repo_slug_hooks,
    post_workspaces_workspace_hooks,
    put_repositories_workspace_repo_slug_hooks_uid,
    put_workspaces_workspace_hooks_uid,
)
from bb.cloud.models.error import Error
from bb.cloud.models.get_hook_events_subject_type_subject_type import GetHookEventsSubjectTypeSubjectType
from bb.cloud.models.hook_event import HookEvent
from bb.cloud.models.webhook_subscription import WebhookSubscription
from bb.cloud.sdk._auth_validation import AuthMethod, require_auth
from bb.cloud.sdk._client import BBClient
from bb.cloud.sdk._pagination import async_paginate
from bb.cloud.types import UNSET, Unset

__all__ = [
    "list_repo",
    "get_repo",
    "create_repo",
    "update_repo",
    "delete_repo",
    "list_workspace",
    "get_workspace",
    "create_workspace",
    "update_workspace",
    "delete_workspace",
    "events",
    "HookSubjectType",
]

HookSubjectType = GetHookEventsSubjectTypeSubjectType


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def list_repo(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    pagelen: int = 25,
) -> list[WebhookSubscription] | Error:
    """Return all webhook subscriptions for a repository.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        List of :class:`~bb.cloud.models.webhook_subscription.WebhookSubscription` objects.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import webhooks

        client = BBClient.from_env()
        hooks = await webhooks.list_repo(client, workspace="myws", repo_slug="myrepo")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/hooks
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-hooks-get>`_
    """
    result = await async_paginate(
        get_repositories_workspace_repo_slug_hooks.asyncio,
        workspace,
        repo_slug,
        client=client.auth,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [item for item in result if isinstance(item, WebhookSubscription)]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_repo(client: BBClient, workspace: str, repo_slug: str, uid: str) -> WebhookSubscription | Error | None:
    """Return a single repository webhook by UID, or ``None`` if not found.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug.
        uid: Webhook subscription UID.

    Returns:
        :class:`~bb.cloud.models.webhook_subscription.WebhookSubscription`, or ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import webhooks

        client = BBClient.from_env()
        hook = await webhooks.get_repo(client, "myws", "myrepo", "{uid}")
        ```

    References:
        `GET /2.0/repositories/{workspace}/{repo_slug}/hooks/{uid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-hooks-uid-get>`_
    """
    result = await get_repositories_workspace_repo_slug_hooks_uid.asyncio(workspace, repo_slug, uid, client=client.auth)
    if isinstance(result, (WebhookSubscription, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def create_repo(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    *,
    body: WebhookSubscription | Unset = UNSET,
) -> WebhookSubscription | Error | None:
    """Create a webhook subscription for a repository.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug.
        body: Webhook subscription payload.

    Returns:
        Created :class:`~bb.cloud.models.webhook_subscription.WebhookSubscription`, or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import webhooks
        from bb.cloud.models.webhook_subscription import WebhookSubscription

        client = BBClient.from_env()
        hook = await webhooks.create_repo(client, "myws", "myrepo", body=WebhookSubscription(...))
        ```

    References:
        `POST /2.0/repositories/{workspace}/{repo_slug}/hooks
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-hooks-post>`_
    """
    result = await post_repositories_workspace_repo_slug_hooks.asyncio(
        workspace, repo_slug, client=client.auth, body=body
    )
    if isinstance(result, (WebhookSubscription, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update_repo(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    uid: str,
    *,
    body: WebhookSubscription | Unset = UNSET,
) -> WebhookSubscription | Error | None:
    """Update a repository webhook subscription.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug.
        uid: Webhook subscription UID.
        body: Updated webhook subscription payload.

    Returns:
        Updated :class:`~bb.cloud.models.webhook_subscription.WebhookSubscription`, or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import webhooks
        from bb.cloud.models.webhook_subscription import WebhookSubscription

        client = BBClient.from_env()
        hook = await webhooks.update_repo(client, "myws", "myrepo", "{uid}", body=WebhookSubscription(...))
        ```

    References:
        `PUT /2.0/repositories/{workspace}/{repo_slug}/hooks/{uid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-hooks-uid-put>`_
    """
    result = await put_repositories_workspace_repo_slug_hooks_uid.asyncio(
        workspace, repo_slug, uid, client=client.auth, body=body
    )
    if isinstance(result, (WebhookSubscription, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete_repo(client: BBClient, workspace: str, repo_slug: str, uid: str) -> None:
    """Delete a repository webhook subscription.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        repo_slug: Repository slug.
        uid: Webhook subscription UID.

    Returns:
        None.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import webhooks

        client = BBClient.from_env()
        await webhooks.delete_repo(client, "myws", "myrepo", "{uid}")
        ```

    References:
        `DELETE /2.0/repositories/{workspace}/{repo_slug}/hooks/{uid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-hooks-uid-delete>`_
    """
    await delete_repositories_workspace_repo_slug_hooks_uid.asyncio(workspace, repo_slug, uid, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def list_workspace(
    client: BBClient,
    workspace: str,
    *,
    pagelen: int = 25,
) -> list[WebhookSubscription] | Error:
    """Return all webhook subscriptions for a workspace.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        pagelen: Number of results per page. Defaults to ``25``.

    Returns:
        List of :class:`~bb.cloud.models.webhook_subscription.WebhookSubscription` objects.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import webhooks

        client = BBClient.from_env()
        hooks = await webhooks.list_workspace(client, workspace="myws")
        ```

    References:
        `GET /2.0/workspaces/{workspace}/hooks
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-workspace-hooks-get>`_
    """
    result = await async_paginate(
        get_workspaces_workspace_hooks.asyncio,
        workspace,
        client=client.auth,
        pagelen=pagelen,
    )

    if isinstance(result, Error):
        return result

    return [item for item in result if isinstance(item, WebhookSubscription)]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_workspace(client: BBClient, workspace: str, uid: str) -> WebhookSubscription | Error | None:
    """Return a single workspace webhook by UID, or ``None`` if not found.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        uid: Webhook subscription UID.

    Returns:
        :class:`~bb.cloud.models.webhook_subscription.WebhookSubscription`, or ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import webhooks

        client = BBClient.from_env()
        hook = await webhooks.get_workspace(client, "myws", "{uid}")
        ```

    References:
        `GET /2.0/workspaces/{workspace}/hooks/{uid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-workspace-hooks-uid-get>`_
    """
    result = await get_workspaces_workspace_hooks_uid.asyncio(workspace, uid, client=client.auth)
    if isinstance(result, (WebhookSubscription, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def create_workspace(
    client: BBClient,
    workspace: str,
    *,
    body: WebhookSubscription | Unset = UNSET,
) -> WebhookSubscription | Error | None:
    """Create a webhook subscription for a workspace.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        body: Webhook subscription payload.

    Returns:
        Created :class:`~bb.cloud.models.webhook_subscription.WebhookSubscription`, or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import webhooks
        from bb.cloud.models.webhook_subscription import WebhookSubscription

        client = BBClient.from_env()
        hook = await webhooks.create_workspace(client, "myws", body=WebhookSubscription(...))
        ```

    References:
        `POST /2.0/workspaces/{workspace}/hooks
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-workspace-hooks-post>`_
    """
    result = await post_workspaces_workspace_hooks.asyncio(workspace, client=client.auth, body=body)
    if isinstance(result, (WebhookSubscription, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update_workspace(
    client: BBClient,
    workspace: str,
    uid: str,
    *,
    body: WebhookSubscription | Unset = UNSET,
) -> WebhookSubscription | Error | None:
    """Update a workspace webhook subscription.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        uid: Webhook subscription UID.
        body: Updated webhook subscription payload.

    Returns:
        Updated :class:`~bb.cloud.models.webhook_subscription.WebhookSubscription`, or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import webhooks
        from bb.cloud.models.webhook_subscription import WebhookSubscription

        client = BBClient.from_env()
        hook = await webhooks.update_workspace(client, "myws", "{uid}", body=WebhookSubscription(...))
        ```

    References:
        `PUT /2.0/workspaces/{workspace}/hooks/{uid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-workspace-hooks-uid-put>`_
    """
    result = await put_workspaces_workspace_hooks_uid.asyncio(workspace, uid, client=client.auth, body=body)
    if isinstance(result, (WebhookSubscription, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete_workspace(client: BBClient, workspace: str, uid: str) -> None:
    """Delete a workspace webhook subscription.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        workspace: Workspace slug or UUID.
        uid: Webhook subscription UID.

    Returns:
        None.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import webhooks

        client = BBClient.from_env()
        await webhooks.delete_workspace(client, "myws", "{uid}")
        ```

    References:
        `DELETE /2.0/workspaces/{workspace}/hooks/{uid}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-workspace-hooks-uid-delete>`_
    """
    await delete_workspaces_workspace_hooks_uid.asyncio(workspace, uid, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def events(
    client: BBClient,
    subject_type: GetHookEventsSubjectTypeSubjectType,
) -> list[HookEvent] | Error:
    """Return all event types available for a given webhook subject type.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        subject_type: The subject type to list available events for (e.g. ``repository``,
            ``workspace``). Use :data:`HookSubjectType` for valid values.

    Returns:
        List of :class:`~bb.cloud.models.hook_event.HookEvent` objects.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import webhooks

        client = BBClient.from_env()
        ev = await webhooks.events(client, webhooks.HookSubjectType.REPOSITORY)
        ```

    References:
        `GET /2.0/hook_events/{subject_type}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-webhooks/#api-hook-events-subject-type-get>`_
    """
    result = await async_paginate(
        get_hook_events_subject_type.asyncio,
        subject_type,
        client=client.auth,
    )

    if isinstance(result, Error):
        return result

    return list(result)
