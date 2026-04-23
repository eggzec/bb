from __future__ import annotations
import asyncio
from bb.cloud.models.error import Error
from bb.cloud.models.get_hook_events_subject_type_subject_type import GetHookEventsSubjectTypeSubjectType
from bb.cloud.models.hook_event import HookEvent
from bb.cloud.models.webhook_subscription import WebhookSubscription
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset
from bb.cloud.sdk import webhooks as _async
__all__ = ['list_repo', 'get_repo', 'create_repo', 'update_repo', 'delete_repo', 'list_workspace', 'get_workspace', 'create_workspace', 'update_workspace', 'delete_workspace', 'events', 'HookSubjectType']
HookSubjectType = GetHookEventsSubjectTypeSubjectType

def list_repo(client: BBClient, workspace: str, repo_slug: str, *, pagelen: int=25) -> list[WebhookSubscription] | Error:
    """Return all webhook subscriptions for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.webhooks.list_repo`.

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
    hooks = webhooks.list_repo(client, workspace="myws", repo_slug="myrepo")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/hooks
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-hooks-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.webhooks.list_repo`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.list_repo(client, workspace, repo_slug, pagelen=pagelen))

def get_repo(client: BBClient, workspace: str, repo_slug: str, uid: str) -> WebhookSubscription | Error | None:
    """Return a single repository webhook by UID, or ``None`` if not found.

Synchronous wrapper around :func:`~bb.cloud.sdk.webhooks.get_repo`.

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
    hook = webhooks.get_repo(client, "myws", "myrepo", "{uid}")
    ```

References:
    `GET /2.0/repositories/{workspace}/{repo_slug}/hooks/{uid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-hooks-uid-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.webhooks.get_repo`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.get_repo(client, workspace, repo_slug, uid))

def create_repo(client: BBClient, workspace: str, repo_slug: str, *, body: WebhookSubscription | Unset=UNSET) -> WebhookSubscription | Error | None:
    """Create a webhook subscription for a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.webhooks.create_repo`.

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
    hook = webhooks.create_repo(client, "myws", "myrepo", body=WebhookSubscription(...))
    ```

References:
    `POST /2.0/repositories/{workspace}/{repo_slug}/hooks
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-hooks-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.webhooks.create_repo`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.create_repo(client, workspace, repo_slug, body=body))

def update_repo(client: BBClient, workspace: str, repo_slug: str, uid: str, *, body: WebhookSubscription | Unset=UNSET) -> WebhookSubscription | Error | None:
    """Update a repository webhook subscription.

Synchronous wrapper around :func:`~bb.cloud.sdk.webhooks.update_repo`.

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
    hook = webhooks.update_repo(client, "myws", "myrepo", "{uid}", body=WebhookSubscription(...))
    ```

References:
    `PUT /2.0/repositories/{workspace}/{repo_slug}/hooks/{uid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-hooks-uid-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.webhooks.update_repo`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.update_repo(client, workspace, repo_slug, uid, body=body))

def delete_repo(client: BBClient, workspace: str, repo_slug: str, uid: str) -> None:
    """Delete a repository webhook subscription.

Synchronous wrapper around :func:`~bb.cloud.sdk.webhooks.delete_repo`.

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
    webhooks.delete_repo(client, "myws", "myrepo", "{uid}")
    ```

References:
    `DELETE /2.0/repositories/{workspace}/{repo_slug}/hooks/{uid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-hooks-uid-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.webhooks.delete_repo`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.delete_repo(client, workspace, repo_slug, uid))

def list_workspace(client: BBClient, workspace: str, *, pagelen: int=25) -> list[WebhookSubscription] | Error:
    """Return all webhook subscriptions for a workspace.

Synchronous wrapper around :func:`~bb.cloud.sdk.webhooks.list_workspace`.

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
    hooks = webhooks.list_workspace(client, workspace="myws")
    ```

References:
    `GET /2.0/workspaces/{workspace}/hooks
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-workspace-hooks-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.webhooks.list_workspace`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.list_workspace(client, workspace, pagelen=pagelen))

def get_workspace(client: BBClient, workspace: str, uid: str) -> WebhookSubscription | Error | None:
    """Return a single workspace webhook by UID, or ``None`` if not found.

Synchronous wrapper around :func:`~bb.cloud.sdk.webhooks.get_workspace`.

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
    hook = webhooks.get_workspace(client, "myws", "{uid}")
    ```

References:
    `GET /2.0/workspaces/{workspace}/hooks/{uid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-workspace-hooks-uid-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.webhooks.get_workspace`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.get_workspace(client, workspace, uid))

def create_workspace(client: BBClient, workspace: str, *, body: WebhookSubscription | Unset=UNSET) -> WebhookSubscription | Error | None:
    """Create a webhook subscription for a workspace.

Synchronous wrapper around :func:`~bb.cloud.sdk.webhooks.create_workspace`.

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
    hook = webhooks.create_workspace(client, "myws", body=WebhookSubscription(...))
    ```

References:
    `POST /2.0/workspaces/{workspace}/hooks
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-workspace-hooks-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.webhooks.create_workspace`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.create_workspace(client, workspace, body=body))

def update_workspace(client: BBClient, workspace: str, uid: str, *, body: WebhookSubscription | Unset=UNSET) -> WebhookSubscription | Error | None:
    """Update a workspace webhook subscription.

Synchronous wrapper around :func:`~bb.cloud.sdk.webhooks.update_workspace`.

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
    hook = webhooks.update_workspace(client, "myws", "{uid}", body=WebhookSubscription(...))
    ```

References:
    `PUT /2.0/workspaces/{workspace}/hooks/{uid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-workspace-hooks-uid-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.webhooks.update_workspace`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.update_workspace(client, workspace, uid, body=body))

def delete_workspace(client: BBClient, workspace: str, uid: str) -> None:
    """Delete a workspace webhook subscription.

Synchronous wrapper around :func:`~bb.cloud.sdk.webhooks.delete_workspace`.

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
    webhooks.delete_workspace(client, "myws", "{uid}")
    ```

References:
    `DELETE /2.0/workspaces/{workspace}/hooks/{uid}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-workspaces/#api-workspaces-workspace-hooks-uid-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.webhooks.delete_workspace`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.delete_workspace(client, workspace, uid))

def events(client: BBClient, subject_type: GetHookEventsSubjectTypeSubjectType) -> list[HookEvent] | Error:
    """Return all event types available for a given webhook subject type.

Synchronous wrapper around :func:`~bb.cloud.sdk.webhooks.events`.

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
    ev = webhooks.events(client, webhooks.HookSubjectType.REPOSITORY)
    ```

References:
    `GET /2.0/hook_events/{subject_type}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-webhooks/#api-hook-events-subject-type-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.webhooks.events`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.events(client, subject_type))
