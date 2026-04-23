from __future__ import annotations
import asyncio
from bb.cloud.models.application_property import ApplicationProperty
from bb.cloud.models.error import Error
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset
from bb.cloud.sdk import properties as _async
__all__ = ['repo_get', 'repo_set', 'repo_delete', 'commit_get', 'commit_set', 'commit_delete', 'pr_get', 'pr_set', 'pr_delete', 'user_get', 'user_set', 'user_delete']

def repo_get(client: BBClient, workspace: str, repo_slug: str, app_key: str, property_name: str) -> ApplicationProperty | Error | None:
    """Retrieve a custom property value set on a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.properties.repo_get`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    app_key: Key of the Connect app that set the property.
    property_name: Name of the property.

Returns:
    An :class:`~bb.cloud.models.application_property.ApplicationProperty` object,
    or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import properties

    client = BBClient.from_env()
    prop = properties.repo_get(
        client, workspace="myws", repo_slug="myrepo", app_key="my-app", property_name="my-prop"
    )
    ```

References:
    `https://developer.atlassian.com/cloud/bitbucket/rest/api-group-properties/
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-properties/>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.properties.repo_get`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.repo_get(client, workspace, repo_slug, app_key, property_name))

def repo_set(client: BBClient, workspace: str, repo_slug: str, app_key: str, property_name: str, *, body: ApplicationProperty | Unset=UNSET) -> None:
    """Set a custom property value on a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.properties.repo_set`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    app_key: Key of the Connect app setting the property.
    property_name: Name of the property.
    body: Property value payload. Defaults to :data:`~bb.cloud.types.UNSET`.

Returns:
    None.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import properties
    from bb.cloud.models.application_property import ApplicationProperty

    client = BBClient.from_env()
    properties.repo_set(
        client,
        workspace="myws",
        repo_slug="myrepo",
        app_key="my-app",
        property_name="my-prop",
        body=ApplicationProperty(...),
    )
    ```

References:
    `https://developer.atlassian.com/cloud/bitbucket/rest/api-group-properties/
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-properties/>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.properties.repo_set`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.repo_set(client, workspace, repo_slug, app_key, property_name, body=body))

def repo_delete(client: BBClient, workspace: str, repo_slug: str, app_key: str, property_name: str) -> None:
    """Delete a custom property value from a repository.

Synchronous wrapper around :func:`~bb.cloud.sdk.properties.repo_delete`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    app_key: Key of the Connect app that owns the property.
    property_name: Name of the property to delete.

Returns:
    None.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import properties

    client = BBClient.from_env()
    properties.repo_delete(
        client, workspace="myws", repo_slug="myrepo", app_key="my-app", property_name="my-prop"
    )
    ```

References:
    `https://developer.atlassian.com/cloud/bitbucket/rest/api-group-properties/
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-properties/>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.properties.repo_delete`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.repo_delete(client, workspace, repo_slug, app_key, property_name))

def commit_get(client: BBClient, workspace: str, repo_slug: str, commit: str, app_key: str, property_name: str) -> ApplicationProperty | Error | None:
    """Retrieve a custom property value set on a commit.

Synchronous wrapper around :func:`~bb.cloud.sdk.properties.commit_get`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    commit: Full SHA1 of the commit.
    app_key: Key of the Connect app that set the property.
    property_name: Name of the property.

Returns:
    An :class:`~bb.cloud.models.application_property.ApplicationProperty` object,
    or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import properties

    client = BBClient.from_env()
    prop = properties.commit_get(
        client,
        workspace="myws",
        repo_slug="myrepo",
        commit="abc123",
        app_key="my-app",
        property_name="my-prop",
    )
    ```

References:
    `https://developer.atlassian.com/cloud/bitbucket/rest/api-group-properties/
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-properties/>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.properties.commit_get`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.commit_get(client, workspace, repo_slug, commit, app_key, property_name))

def commit_set(client: BBClient, workspace: str, repo_slug: str, commit: str, app_key: str, property_name: str, *, body: ApplicationProperty | Unset=UNSET) -> None:
    """Set a custom property value on a commit.

Synchronous wrapper around :func:`~bb.cloud.sdk.properties.commit_set`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    commit: Full SHA1 of the commit.
    app_key: Key of the Connect app setting the property.
    property_name: Name of the property.
    body: Property value payload. Defaults to :data:`~bb.cloud.types.UNSET`.

Returns:
    None.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import properties
    from bb.cloud.models.application_property import ApplicationProperty

    client = BBClient.from_env()
    properties.commit_set(
        client,
        workspace="myws",
        repo_slug="myrepo",
        commit="abc123",
        app_key="my-app",
        property_name="my-prop",
        body=ApplicationProperty(...),
    )
    ```

References:
    `https://developer.atlassian.com/cloud/bitbucket/rest/api-group-properties/
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-properties/>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.properties.commit_set`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.commit_set(client, workspace, repo_slug, commit, app_key, property_name, body=body))

def commit_delete(client: BBClient, workspace: str, repo_slug: str, commit: str, app_key: str, property_name: str) -> None:
    """Delete a custom property value from a commit.

Synchronous wrapper around :func:`~bb.cloud.sdk.properties.commit_delete`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    commit: Full SHA1 of the commit.
    app_key: Key of the Connect app that owns the property.
    property_name: Name of the property to delete.

Returns:
    None.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import properties

    client = BBClient.from_env()
    properties.commit_delete(
        client,
        workspace="myws",
        repo_slug="myrepo",
        commit="abc123",
        app_key="my-app",
        property_name="my-prop",
    )
    ```

References:
    `https://developer.atlassian.com/cloud/bitbucket/rest/api-group-properties/
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-properties/>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.properties.commit_delete`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.commit_delete(client, workspace, repo_slug, commit, app_key, property_name))

def pr_get(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, app_key: str, property_name: str) -> ApplicationProperty | Error | None:
    """Retrieve a custom property value set on a pull request.

Synchronous wrapper around :func:`~bb.cloud.sdk.properties.pr_get`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    pull_request_id: Numeric ID of the pull request.
    app_key: Key of the Connect app that set the property.
    property_name: Name of the property.

Returns:
    An :class:`~bb.cloud.models.application_property.ApplicationProperty` object,
    or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import properties

    client = BBClient.from_env()
    prop = properties.pr_get(
        client,
        workspace="myws",
        repo_slug="myrepo",
        pull_request_id=42,
        app_key="my-app",
        property_name="my-prop",
    )
    ```

References:
    `https://developer.atlassian.com/cloud/bitbucket/rest/api-group-properties/
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-properties/>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.properties.pr_get`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.pr_get(client, workspace, repo_slug, pull_request_id, app_key, property_name))

def pr_set(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, app_key: str, property_name: str, *, body: ApplicationProperty | Unset=UNSET) -> None:
    """Set a custom property value on a pull request.

Synchronous wrapper around :func:`~bb.cloud.sdk.properties.pr_set`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    pull_request_id: Numeric ID of the pull request.
    app_key: Key of the Connect app setting the property.
    property_name: Name of the property.
    body: Property value payload. Defaults to :data:`~bb.cloud.types.UNSET`.

Returns:
    None.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import properties
    from bb.cloud.models.application_property import ApplicationProperty

    client = BBClient.from_env()
    properties.pr_set(
        client,
        workspace="myws",
        repo_slug="myrepo",
        pull_request_id=42,
        app_key="my-app",
        property_name="my-prop",
        body=ApplicationProperty(...),
    )
    ```

References:
    `https://developer.atlassian.com/cloud/bitbucket/rest/api-group-properties/
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-properties/>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.properties.pr_set`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.pr_set(client, workspace, repo_slug, pull_request_id, app_key, property_name, body=body))

def pr_delete(client: BBClient, workspace: str, repo_slug: str, pull_request_id: int, app_key: str, property_name: str) -> None:
    """Delete a custom property value from a pull request.

Synchronous wrapper around :func:`~bb.cloud.sdk.properties.pr_delete`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    repo_slug: Repository slug or UUID.
    pull_request_id: Numeric ID of the pull request.
    app_key: Key of the Connect app that owns the property.
    property_name: Name of the property to delete.

Returns:
    None.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import properties

    client = BBClient.from_env()
    properties.pr_delete(
        client,
        workspace="myws",
        repo_slug="myrepo",
        pull_request_id=42,
        app_key="my-app",
        property_name="my-prop",
    )
    ```

References:
    `https://developer.atlassian.com/cloud/bitbucket/rest/api-group-properties/
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-properties/>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.properties.pr_delete`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.pr_delete(client, workspace, repo_slug, pull_request_id, app_key, property_name))

def user_get(client: BBClient, workspace: str, username: str, app_key: str, property_name: str) -> ApplicationProperty | Error | None:
    """Retrieve a custom property value set on a user.

Synchronous wrapper around :func:`~bb.cloud.sdk.properties.user_get`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    username: Account ID or username of the user.
    app_key: Key of the Connect app that set the property.
    property_name: Name of the property.

Returns:
    An :class:`~bb.cloud.models.application_property.ApplicationProperty` object,
    or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import properties

    client = BBClient.from_env()
    prop = properties.user_get(
        client,
        workspace="myws",
        username="jdoe",
        app_key="my-app",
        property_name="my-prop",
    )
    ```

References:
    `https://developer.atlassian.com/cloud/bitbucket/rest/api-group-properties/
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-properties/>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.properties.user_get`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.user_get(client, workspace, username, app_key, property_name))

def user_set(client: BBClient, workspace: str, username: str, app_key: str, property_name: str, *, body: ApplicationProperty | Unset=UNSET) -> None:
    """Set a custom property value on a user.

Synchronous wrapper around :func:`~bb.cloud.sdk.properties.user_set`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    username: Account ID or username of the user.
    app_key: Key of the Connect app setting the property.
    property_name: Name of the property.
    body: Property value payload. Defaults to :data:`~bb.cloud.types.UNSET`.

Returns:
    None.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import properties
    from bb.cloud.models.application_property import ApplicationProperty

    client = BBClient.from_env()
    properties.user_set(
        client,
        workspace="myws",
        username="jdoe",
        app_key="my-app",
        property_name="my-prop",
        body=ApplicationProperty(...),
    )
    ```

References:
    `https://developer.atlassian.com/cloud/bitbucket/rest/api-group-properties/
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-properties/>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.properties.user_set`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.user_set(client, workspace, username, app_key, property_name, body=body))

def user_delete(client: BBClient, workspace: str, username: str, app_key: str, property_name: str) -> None:
    """Delete a custom property value from a user.

Synchronous wrapper around :func:`~bb.cloud.sdk.properties.user_delete`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    username: Account ID or username of the user.
    app_key: Key of the Connect app that owns the property.
    property_name: Name of the property to delete.

Returns:
    None.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import properties

    client = BBClient.from_env()
    properties.user_delete(
        client,
        workspace="myws",
        username="jdoe",
        app_key="my-app",
        property_name="my-prop",
    )
    ```

References:
    `https://developer.atlassian.com/cloud/bitbucket/rest/api-group-properties/
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-properties/>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.properties.user_delete`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.user_delete(client, workspace, username, app_key, property_name))
