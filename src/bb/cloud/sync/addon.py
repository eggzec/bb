from __future__ import annotations
import asyncio
from typing import Any
from bb.cloud.models.error import Error
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset
from bb.cloud.sdk import addon as _async
__all__ = ['delete', 'update', 'linkers', 'get_linker', 'linker_values', 'get_linker_value', 'create_linker_value', 'set_linker_values', 'clear_linker_values', 'delete_linker_value']

def delete(client: BBClient) -> None:
    """Uninstall the addon.

Synchronous wrapper around :func:`~bb.cloud.sdk.addon.delete`.

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
    addon.delete(client)
    ```

References:
    `DELETE /2.0/addon
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-addon/#api-addon-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.addon.delete`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.delete(client))

def update(client: BBClient, *, body: Unset=UNSET) -> Any | Error | None:
    """Update the addon descriptor.

Synchronous wrapper around :func:`~bb.cloud.sdk.addon.update`.

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
    result = addon.update(client)
    ```

References:
    `PUT /2.0/addon
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-addon/#api-addon-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.addon.update`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.update(client, body=body))

def linkers(client: BBClient) -> Any | Error | None:
    """List all addon linkers.

Synchronous wrapper around :func:`~bb.cloud.sdk.addon.linkers`.

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
    all_linkers = addon.linkers(client)
    ```

References:
    `GET /2.0/addon/linkers
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-addon/#api-addon-linkers-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.addon.linkers`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.linkers(client))

def get_linker(client: BBClient, linker_key: str) -> Any | Error | None:
    """Fetch a specific addon linker.

Synchronous wrapper around :func:`~bb.cloud.sdk.addon.get_linker`.

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
    linker = addon.get_linker(client, linker_key="my-linker")
    ```

References:
    `GET /2.0/addon/linkers/{linker_key}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-addon/#api-addon-linkers-linker-key-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.addon.get_linker`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.get_linker(client, linker_key))

def linker_values(client: BBClient, linker_key: str) -> Any | Error | None:
    """List all values for an addon linker.

Synchronous wrapper around :func:`~bb.cloud.sdk.addon.linker_values`.

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
    values = addon.linker_values(client, linker_key="my-linker")
    ```

References:
    `GET /2.0/addon/linkers/{linker_key}/values
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-addon/#api-addon-linkers-linker-key-values-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.addon.linker_values`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.linker_values(client, linker_key))

def get_linker_value(client: BBClient, linker_key: str, value_id: str) -> Any | Error | None:
    """Fetch a specific value for an addon linker.

Synchronous wrapper around :func:`~bb.cloud.sdk.addon.get_linker_value`.

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
    value = addon.get_linker_value(client, linker_key="my-linker", value_id="42")
    ```

References:
    `GET /2.0/addon/linkers/{linker_key}/values/{value_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-addon/#api-addon-linkers-linker-key-values-value-id-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.addon.get_linker_value`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.get_linker_value(client, linker_key, value_id))

def create_linker_value(client: BBClient, linker_key: str, *, body: Unset=UNSET) -> Any | Error | None:
    """Create a new value for an addon linker.

Synchronous wrapper around :func:`~bb.cloud.sdk.addon.create_linker_value`.

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
    value = addon.create_linker_value(client, linker_key="my-linker")
    ```

References:
    `POST /2.0/addon/linkers/{linker_key}/values
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-addon/#api-addon-linkers-linker-key-values-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.addon.create_linker_value`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.create_linker_value(client, linker_key, body=body))

def set_linker_values(client: BBClient, linker_key: str, *, body: Unset=UNSET) -> Any | Error | None:
    """Set (replace) all values for an addon linker.

Synchronous wrapper around :func:`~bb.cloud.sdk.addon.set_linker_values`.

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
    result = addon.set_linker_values(client, linker_key="my-linker")
    ```

References:
    `PUT /2.0/addon/linkers/{linker_key}/values
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-addon/#api-addon-linkers-linker-key-values-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.addon.set_linker_values`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.set_linker_values(client, linker_key, body=body))

def clear_linker_values(client: BBClient, linker_key: str) -> None:
    """Delete all values for an addon linker.

Synchronous wrapper around :func:`~bb.cloud.sdk.addon.clear_linker_values`.

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
    addon.clear_linker_values(client, linker_key="my-linker")
    ```

References:
    `DELETE /2.0/addon/linkers/{linker_key}/values
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-addon/#api-addon-linkers-linker-key-values-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.addon.clear_linker_values`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.clear_linker_values(client, linker_key))

def delete_linker_value(client: BBClient, linker_key: str, value_id: str) -> None:
    """Delete a specific value from an addon linker.

Synchronous wrapper around :func:`~bb.cloud.sdk.addon.delete_linker_value`.

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
    addon.delete_linker_value(client, linker_key="my-linker", value_id="42")
    ```

References:
    `DELETE /2.0/addon/linkers/{linker_key}/values/{value_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-addon/#api-addon-linkers-linker-key-values-value-id-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.addon.delete_linker_value`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return asyncio.run(_async.delete_linker_value(client, linker_key, value_id))
