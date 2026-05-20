from __future__ import annotations
from typing import Any
from bb.cloud.models.account import Account
from bb.cloud.models.error import Error
from bb.cloud.models.gpg_account_key import GPGAccountKey as GpgAccountKey
from bb.cloud.models.ssh_account_key import SshAccountKey
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset
from bb.cloud.sdk import users as _async
__all__ = ['me', 'get', 'emails', 'get_email', 'ssh_keys', 'get_ssh_key', 'add_ssh_key', 'update_ssh_key', 'delete_ssh_key', 'gpg_keys', 'get_gpg_key', 'add_gpg_key', 'delete_gpg_key']

def me(client: BBClient) -> Account | Error | None:
    """Return the currently authenticated user.

Synchronous wrapper around :func:`~bb.cloud.sdk.users.me`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.

Returns:
    :class:`~bb.cloud.models.account.Account` for the authenticated account, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import users

    client = BBClient.from_env()
    user = users.me(client)
    ```

References:
    `GET /2.0/user
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-users/#api-user-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.users.me`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.me(client))

def get(client: BBClient, selected_user: str) -> Account | Error | None:
    """Return a user by account ID or username, or ``None`` if not found.

Synchronous wrapper around :func:`~bb.cloud.sdk.users.get`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    selected_user: The account UUID or username of the user to retrieve.

Returns:
    :class:`~bb.cloud.models.account.Account` for the specified user, or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import users

    client = BBClient.from_env()
    account = users.get(client, "{account-uuid}")
    ```

References:
    `GET /2.0/users/{selected_user}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-users/#api-users-selected-user-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.users.get`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get(client, selected_user))

def emails(client: BBClient) -> list[Any] | Error:
    """Return all email addresses of the authenticated user.

Synchronous wrapper around :func:`~bb.cloud.sdk.users.emails`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.

Returns:
    List of email address objects for the authenticated user.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import users

    client = BBClient.from_env()
    addrs = users.emails(client)
    ```

References:
    `GET /2.0/user/emails
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-users/#api-user-emails-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.users.emails`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.emails(client))

def get_email(client: BBClient, email: str) -> object | Error | None:
    """Return a specific email address of the authenticated user.

Synchronous wrapper around :func:`~bb.cloud.sdk.users.get_email`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    email: The email address to look up.

Returns:
    Email address object, or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import users

    client = BBClient.from_env()
    addr = users.get_email(client, "me@example.com")
    ```

References:
    `GET /2.0/user/emails/{email}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-users/#api-user-emails-email-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.users.get_email`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get_email(client, email))

def ssh_keys(client: BBClient, selected_user: str, *, pagelen: int=25) -> list[SshAccountKey] | Error:
    """Return all SSH keys for a user.

Synchronous wrapper around :func:`~bb.cloud.sdk.users.ssh_keys`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    selected_user: The account UUID or username of the target user.
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    List of :class:`~bb.cloud.models.ssh_account_key.SshAccountKey` objects.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import users

    client = BBClient.from_env()
    keys = users.ssh_keys(client, "{account-uuid}")
    ```

References:
    `GET /2.0/users/{selected_user}/ssh-keys
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-ssh/#api-users-selected-user-ssh-keys-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.users.ssh_keys`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.ssh_keys(client, selected_user, pagelen=pagelen))

def get_ssh_key(client: BBClient, selected_user: str, key_id: int) -> SshAccountKey | Error | None:
    """Return a single SSH key by ID, or ``None`` if not found.

Synchronous wrapper around :func:`~bb.cloud.sdk.users.get_ssh_key`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    selected_user: The account UUID or username of the target user.
    key_id: Numeric ID of the SSH key.

Returns:
    :class:`~bb.cloud.models.ssh_account_key.SshAccountKey`, or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import users

    client = BBClient.from_env()
    key = users.get_ssh_key(client, "{account-uuid}", 123)
    ```

References:
    `GET /2.0/users/{selected_user}/ssh-keys/{key_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-ssh/#api-users-selected-user-ssh-keys-key-id-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.users.get_ssh_key`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get_ssh_key(client, selected_user, key_id))

def add_ssh_key(client: BBClient, selected_user: str, *, body: SshAccountKey | Unset=UNSET) -> SshAccountKey | Error | None:
    """Add an SSH key to a user account.

Synchronous wrapper around :func:`~bb.cloud.sdk.users.add_ssh_key`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    selected_user: The account UUID or username of the target user.
    body: SSH key payload.

Returns:
    Created :class:`~bb.cloud.models.ssh_account_key.SshAccountKey`, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import users
    from bb.cloud.models.ssh_account_key import SshAccountKey

    client = BBClient.from_env()
    key = users.add_ssh_key(client, "{account-uuid}", body=SshAccountKey(...))
    ```

References:
    `POST /2.0/users/{selected_user}/ssh-keys
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-ssh/#api-users-selected-user-ssh-keys-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.users.add_ssh_key`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.add_ssh_key(client, selected_user, body=body))

def update_ssh_key(client: BBClient, selected_user: str, key_id: int, *, body: SshAccountKey | Unset=UNSET) -> SshAccountKey | Error | None:
    """Update an SSH key on a user account.

Synchronous wrapper around :func:`~bb.cloud.sdk.users.update_ssh_key`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    selected_user: The account UUID or username of the target user.
    key_id: Numeric ID of the SSH key to update.
    body: Updated SSH key payload.

Returns:
    Updated :class:`~bb.cloud.models.ssh_account_key.SshAccountKey`, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import users
    from bb.cloud.models.ssh_account_key import SshAccountKey

    client = BBClient.from_env()
    key = users.update_ssh_key(client, "{account-uuid}", 123, body=SshAccountKey(...))
    ```

References:
    `PUT /2.0/users/{selected_user}/ssh-keys/{key_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-ssh/#api-users-selected-user-ssh-keys-key-id-put>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.users.update_ssh_key`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.update_ssh_key(client, selected_user, key_id, body=body))

def delete_ssh_key(client: BBClient, selected_user: str, key_id: int) -> None:
    """Delete an SSH key from a user account.

Synchronous wrapper around :func:`~bb.cloud.sdk.users.delete_ssh_key`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    selected_user: The account UUID or username of the target user.
    key_id: Numeric ID of the SSH key to delete.

Returns:
    None.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import users

    client = BBClient.from_env()
    users.delete_ssh_key(client, "{account-uuid}", 123)
    ```

References:
    `DELETE /2.0/users/{selected_user}/ssh-keys/{key_id}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-ssh/#api-users-selected-user-ssh-keys-key-id-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.users.delete_ssh_key`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.delete_ssh_key(client, selected_user, key_id))

def gpg_keys(client: BBClient, selected_user: str, *, pagelen: int=25) -> list[GpgAccountKey] | Error:
    """Return all GPG keys for a user.

Synchronous wrapper around :func:`~bb.cloud.sdk.users.gpg_keys`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    selected_user: The account UUID or username of the target user.
    pagelen: Number of results per page. Defaults to ``25``.

Returns:
    List of :class:`~bb.cloud.models.gpg_account_key.GPGAccountKey` objects.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import users

    client = BBClient.from_env()
    keys = users.gpg_keys(client, "{account-uuid}")
    ```

References:
    `GET /2.0/users/{selected_user}/gpg-keys
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-gpg/#api-users-selected-user-gpg-keys-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.users.gpg_keys`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.gpg_keys(client, selected_user, pagelen=pagelen))

def get_gpg_key(client: BBClient, selected_user: str, fingerprint: str) -> GpgAccountKey | Error | None:
    """Return a single GPG key by fingerprint, or ``None`` if not found.

Synchronous wrapper around :func:`~bb.cloud.sdk.users.get_gpg_key`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    selected_user: The account UUID or username of the target user.
    fingerprint: GPG key fingerprint.

Returns:
    :class:`~bb.cloud.models.gpg_account_key.GPGAccountKey`, or ``None`` if not found.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import users

    client = BBClient.from_env()
    key = users.get_gpg_key(client, "{account-uuid}", "ABCD1234...")
    ```

References:
    `GET /2.0/users/{selected_user}/gpg-keys/{fingerprint}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-gpg/#api-users-selected-user-gpg-keys-fingerprint-get>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.users.get_gpg_key`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.get_gpg_key(client, selected_user, fingerprint))

def add_gpg_key(client: BBClient, selected_user: str, *, body: GpgAccountKey | Unset=UNSET) -> GpgAccountKey | Error | None:
    """Add a GPG key to a user account.

Synchronous wrapper around :func:`~bb.cloud.sdk.users.add_gpg_key`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    selected_user: The account UUID or username of the target user.
    body: GPG key payload.

Returns:
    Created :class:`~bb.cloud.models.gpg_account_key.GPGAccountKey`, or ``None`` on error.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import users
    from bb.cloud.models.gpg_account_key import GPGAccountKey

    client = BBClient.from_env()
    key = users.add_gpg_key(client, "{account-uuid}", body=GPGAccountKey(...))
    ```

References:
    `POST /2.0/users/{selected_user}/gpg-keys
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-gpg/#api-users-selected-user-gpg-keys-post>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.users.add_gpg_key`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.add_gpg_key(client, selected_user, body=body))

def delete_gpg_key(client: BBClient, selected_user: str, fingerprint: str) -> None:
    """Delete a GPG key from a user account.

Synchronous wrapper around :func:`~bb.cloud.sdk.users.delete_gpg_key`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    selected_user: The account UUID or username of the target user.
    fingerprint: GPG key fingerprint.

Returns:
    None.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import users

    client = BBClient.from_env()
    users.delete_gpg_key(client, "{account-uuid}", "ABCD1234...")
    ```

References:
    `DELETE /2.0/users/{selected_user}/gpg-keys/{fingerprint}
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-gpg/#api-users-selected-user-gpg-keys-fingerprint-delete>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.users.delete_gpg_key`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.delete_gpg_key(client, selected_user, fingerprint))
