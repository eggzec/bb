from __future__ import annotations

from typing import Any

from bb.cloud.api.addon import (
    delete_addon,
    delete_addon_linkers_linker_key_values,
    delete_addon_linkers_linker_key_values_value_id,
    get_addon_linkers,
    get_addon_linkers_linker_key,
    get_addon_linkers_linker_key_values,
    get_addon_linkers_linker_key_values_value_id,
    post_addon_linkers_linker_key_values,
    put_addon,
    put_addon_linkers_linker_key_values,
)
from bb.cloud.sdk._auth_validation import AuthMethod, require_auth
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset

__all__ = [
    "delete",
    "update",
    "linkers",
    "get_linker",
    "linker_values",
    "get_linker_value",
    "create_linker_value",
    "set_linker_values",
    "clear_linker_values",
    "delete_linker_value",
]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete(client: BBClient) -> None:
    """Uninstall the addon.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.

    Returns:
        ``None``.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import addon

        client = BBClient.from_env()
        await addon.delete(client)
        ```

    References:
        `DELETE /2.0/addon
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-addon/#api-addon-delete>`_
    """
    await delete_addon.asyncio(client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update(client: BBClient, *, body: Unset = UNSET) -> Any | None:
    """Update the addon descriptor.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        body: Updated addon descriptor body.

    Returns:
        The updated addon object, or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import addon

        client = BBClient.from_env()
        result = await addon.update(client)
        ```

    References:
        `PUT /2.0/addon
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-addon/#api-addon-put>`_
    """
    return await put_addon.asyncio(client=client.auth, body=body)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def linkers(client: BBClient) -> Any | None:
    """List all addon linkers.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.

    Returns:
        The linkers object, or ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import addon

        client = BBClient.from_env()
        all_linkers = await addon.linkers(client)
        ```

    References:
        `GET /2.0/addon/linkers
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-addon/#api-addon-linkers-get>`_
    """
    return await get_addon_linkers.asyncio(client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_linker(client: BBClient, linker_key: str) -> Any | None:
    """Fetch a specific addon linker.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        linker_key: The linker's unique key identifier.

    Returns:
        The linker object, or ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import addon

        client = BBClient.from_env()
        linker = await addon.get_linker(client, linker_key="my-linker")
        ```

    References:
        `GET /2.0/addon/linkers/{linker_key}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-addon/#api-addon-linkers-linker-key-get>`_
    """
    return await get_addon_linkers_linker_key.asyncio(linker_key, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def linker_values(client: BBClient, linker_key: str) -> Any | None:
    """List all values for an addon linker.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        linker_key: The linker's unique key identifier.

    Returns:
        The linker values object, or ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import addon

        client = BBClient.from_env()
        values = await addon.linker_values(client, linker_key="my-linker")
        ```

    References:
        `GET /2.0/addon/linkers/{linker_key}/values
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-addon/#api-addon-linkers-linker-key-values-get>`_
    """
    return await get_addon_linkers_linker_key_values.asyncio(linker_key, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_linker_value(client: BBClient, linker_key: str, value_id: str) -> Any | None:
    """Fetch a specific value for an addon linker.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        linker_key: The linker's unique key identifier.
        value_id: The value's ID.

    Returns:
        The linker value object, or ``None`` if not found.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import addon

        client = BBClient.from_env()
        value = await addon.get_linker_value(client, linker_key="my-linker", value_id="42")
        ```

    References:
        `GET /2.0/addon/linkers/{linker_key}/values/{value_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-addon/#api-addon-linkers-linker-key-values-value-id-get>`_
    """
    return await get_addon_linkers_linker_key_values_value_id.asyncio(linker_key, value_id, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def create_linker_value(client: BBClient, linker_key: str, *, body: Unset = UNSET) -> Any | None:
    """Create a new value for an addon linker.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        linker_key: The linker's unique key identifier.
        body: Value body.

    Returns:
        The created linker value object, or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import addon

        client = BBClient.from_env()
        value = await addon.create_linker_value(client, linker_key="my-linker")
        ```

    References:
        `POST /2.0/addon/linkers/{linker_key}/values
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-addon/#api-addon-linkers-linker-key-values-post>`_
    """
    return await post_addon_linkers_linker_key_values.asyncio(linker_key, client=client.auth, body=body)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def set_linker_values(client: BBClient, linker_key: str, *, body: Unset = UNSET) -> Any | None:
    """Set (replace) all values for an addon linker.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        linker_key: The linker's unique key identifier.
        body: Replacement values body.

    Returns:
        The updated linker values object, or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import addon

        client = BBClient.from_env()
        result = await addon.set_linker_values(client, linker_key="my-linker")
        ```

    References:
        `PUT /2.0/addon/linkers/{linker_key}/values
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-addon/#api-addon-linkers-linker-key-values-put>`_
    """
    return await put_addon_linkers_linker_key_values.asyncio(linker_key, client=client.auth, body=body)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def clear_linker_values(client: BBClient, linker_key: str) -> None:
    """Delete all values for an addon linker.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        linker_key: The linker's unique key identifier.

    Returns:
        ``None``.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import addon

        client = BBClient.from_env()
        await addon.clear_linker_values(client, linker_key="my-linker")
        ```

    References:
        `DELETE /2.0/addon/linkers/{linker_key}/values
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-addon/#api-addon-linkers-linker-key-values-delete>`_
    """
    await delete_addon_linkers_linker_key_values.asyncio(linker_key, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete_linker_value(client: BBClient, linker_key: str, value_id: str) -> None:
    """Delete a specific value from an addon linker.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
        linker_key: The linker's unique key identifier.
        value_id: The value's ID.

    Returns:
        ``None``.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import addon

        client = BBClient.from_env()
        await addon.delete_linker_value(client, linker_key="my-linker", value_id="42")
        ```

    References:
        `DELETE /2.0/addon/linkers/{linker_key}/values/{value_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-addon/#api-addon-linkers-linker-key-values-value-id-delete>`_
    """
    await delete_addon_linkers_linker_key_values_value_id.asyncio(linker_key, value_id, client=client.auth)
