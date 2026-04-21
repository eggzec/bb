from __future__ import annotations

from bb.cloud.api.properties import (
    delete_commit_hosted_property_value,
    delete_pull_request_hosted_property_value,
    delete_repository_hosted_property_value,
    delete_user_hosted_property_value,
    get_commit_hosted_property_value,
    get_pull_request_hosted_property_value,
    get_repository_hosted_property_value,
    retrieve_user_hosted_property_value,
    update_commit_hosted_property_value,
    update_pull_request_hosted_property_value,
    update_repository_hosted_property_value,
    update_user_hosted_property_value,
)
from bb.cloud.models.application_property import ApplicationProperty
from bb.cloud.models.error import Error
from bb.cloud.sdk._auth_validation import AuthMethod, require_auth
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset

__all__ = [
    "repo_get",
    "repo_set",
    "repo_delete",
    "commit_get",
    "commit_set",
    "commit_delete",
    "pr_get",
    "pr_set",
    "pr_delete",
    "user_get",
    "user_set",
    "user_delete",
]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def repo_get(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    app_key: str,
    property_name: str,
) -> ApplicationProperty | Error | None:
    """Retrieve a custom property value set on a repository.

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
        prop = await properties.repo_get(
            client, workspace="myws", repo_slug="myrepo", app_key="my-app", property_name="my-prop"
        )
        ```

    References:
        `https://developer.atlassian.com/cloud/bitbucket/rest/api-group-properties/
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-properties/>`_
    """
    result = await get_repository_hosted_property_value.asyncio(
        workspace, repo_slug, app_key, property_name, client=client.auth
    )
    if isinstance(result, (ApplicationProperty, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def repo_set(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    app_key: str,
    property_name: str,
    *,
    body: ApplicationProperty | Unset = UNSET,
) -> None:
    """Set a custom property value on a repository.

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
        await properties.repo_set(
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
    """
    await update_repository_hosted_property_value.asyncio(
        workspace, repo_slug, app_key, property_name, client=client.auth, body=body
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def repo_delete(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    app_key: str,
    property_name: str,
) -> None:
    """Delete a custom property value from a repository.

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
        await properties.repo_delete(
            client, workspace="myws", repo_slug="myrepo", app_key="my-app", property_name="my-prop"
        )
        ```

    References:
        `https://developer.atlassian.com/cloud/bitbucket/rest/api-group-properties/
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-properties/>`_
    """
    await delete_repository_hosted_property_value.asyncio(
        workspace, repo_slug, app_key, property_name, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def commit_get(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    app_key: str,
    property_name: str,
) -> ApplicationProperty | Error | None:
    """Retrieve a custom property value set on a commit.

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
        prop = await properties.commit_get(
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
    """
    result = await get_commit_hosted_property_value.asyncio(
        workspace, repo_slug, commit, app_key, property_name, client=client.auth
    )
    if isinstance(result, (ApplicationProperty, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def commit_set(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    app_key: str,
    property_name: str,
    *,
    body: ApplicationProperty | Unset = UNSET,
) -> None:
    """Set a custom property value on a commit.

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
        await properties.commit_set(
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
    """
    await update_commit_hosted_property_value.asyncio(
        workspace, repo_slug, commit, app_key, property_name, client=client.auth, body=body
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def commit_delete(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    commit: str,
    app_key: str,
    property_name: str,
) -> None:
    """Delete a custom property value from a commit.

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
        await properties.commit_delete(
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
    """
    await delete_commit_hosted_property_value.asyncio(
        workspace, repo_slug, commit, app_key, property_name, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def pr_get(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    app_key: str,
    property_name: str,
) -> ApplicationProperty | Error | None:
    """Retrieve a custom property value set on a pull request.

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
        prop = await properties.pr_get(
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
    """
    result = await get_pull_request_hosted_property_value.asyncio(
        workspace, repo_slug, pull_request_id, app_key, property_name, client=client.auth
    )
    if isinstance(result, (ApplicationProperty, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def pr_set(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    app_key: str,
    property_name: str,
    *,
    body: ApplicationProperty | Unset = UNSET,
) -> None:
    """Set a custom property value on a pull request.

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
        await properties.pr_set(
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
    """
    await update_pull_request_hosted_property_value.asyncio(
        workspace, repo_slug, pull_request_id, app_key, property_name, client=client.auth, body=body
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def pr_delete(
    client: BBClient,
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    app_key: str,
    property_name: str,
) -> None:
    """Delete a custom property value from a pull request.

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
        await properties.pr_delete(
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
    """
    await delete_pull_request_hosted_property_value.asyncio(
        workspace, repo_slug, pull_request_id, app_key, property_name, client=client.auth
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def user_get(
    client: BBClient,
    workspace: str,
    username: str,
    app_key: str,
    property_name: str,
) -> ApplicationProperty | Error | None:
    """Retrieve a custom property value set on a user.

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
        prop = await properties.user_get(
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
    """
    result = await retrieve_user_hosted_property_value.asyncio(
        workspace, username, app_key, property_name, client=client.auth
    )
    if isinstance(result, (ApplicationProperty, Error)):
        return result
    return None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def user_set(
    client: BBClient,
    workspace: str,
    username: str,
    app_key: str,
    property_name: str,
    *,
    body: ApplicationProperty | Unset = UNSET,
) -> None:
    """Set a custom property value on a user.

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
        await properties.user_set(
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
    """
    await update_user_hosted_property_value.asyncio(
        workspace, username, app_key, property_name, client=client.auth, body=body
    )


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def user_delete(
    client: BBClient,
    workspace: str,
    username: str,
    app_key: str,
    property_name: str,
) -> None:
    """Delete a custom property value from a user.

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
        await properties.user_delete(
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
    """
    await delete_user_hosted_property_value.asyncio(workspace, username, app_key, property_name, client=client.auth)
