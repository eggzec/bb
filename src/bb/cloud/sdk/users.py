from __future__ import annotations

from typing import Any

from bb.cloud.api.gpg import (
    delete_users_selected_user_gpg_keys_fingerprint,
    get_users_selected_user_gpg_keys,
    get_users_selected_user_gpg_keys_fingerprint,
    post_users_selected_user_gpg_keys,
)
from bb.cloud.api.ssh import (
    delete_users_selected_user_ssh_keys_key_id,
    get_users_selected_user_ssh_keys,
    get_users_selected_user_ssh_keys_key_id,
    post_users_selected_user_ssh_keys,
    put_users_selected_user_ssh_keys_key_id,
)
from bb.cloud.api.users import (
    get_user,
    get_user_emails,
    get_user_emails_email,
    get_users_selected_user,
)
from bb.cloud.models.account import Account
from bb.cloud.models.gpg_account_key import GPGAccountKey as GpgAccountKey
from bb.cloud.models.ssh_account_key import SshAccountKey
from bb.cloud.models.user import User
from bb.cloud.sdk._auth_validation import AuthMethod, require_auth
from bb.cloud.sdk._client import BBClient
from bb.cloud.sdk._pagination import async_paginate
from bb.cloud.types import UNSET, Unset

__all__ = [
    "me",
    "get",
    "emails",
    "get_email",
    "ssh_keys",
    "get_ssh_key",
    "add_ssh_key",
    "update_ssh_key",
    "delete_ssh_key",
    "gpg_keys",
    "get_gpg_key",
    "add_gpg_key",
    "delete_gpg_key",
]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def me(client: BBClient) -> User | None:
    """Return the currently authenticated user.

    Args:
        client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.

    Returns:
        :class:`~bb.cloud.models.user.User` for the authenticated account, or ``None`` on error.

    Raises:
        :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
        :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
        :exc:`httpx.HTTPError`: On network-level failures.

    Example:
        ```python
        from bb.cloud import BBClient
        from bb.cloud.sdk import users

        client = BBClient.from_env()
        user = await users.me(client)
        ```

    References:
        `GET /2.0/user
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-users/#api-user-get>`_
    """
    result = await get_user.asyncio(client=client.auth)
    return result if isinstance(result, User) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get(client: BBClient, selected_user: str) -> Account | None:
    """Return a user by account ID or username, or ``None`` if not found.

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
        account = await users.get(client, "{account-uuid}")
        ```

    References:
        `GET /2.0/users/{selected_user}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-users/#api-users-selected-user-get>`_
    """
    result = await get_users_selected_user.asyncio(selected_user, client=client.auth)
    return result if isinstance(result, Account) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def emails(client: BBClient) -> list[Any]:
    """Return all email addresses of the authenticated user.

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
        addrs = await users.emails(client)
        ```

    References:
        `GET /2.0/user/emails
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-users/#api-user-emails-get>`_
    """
    return [
        e
        async for e in async_paginate(
            get_user_emails.asyncio,
            client=client.auth,
        )
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_email(client: BBClient, email: str) -> object | None:
    """Return a specific email address of the authenticated user.

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
        addr = await users.get_email(client, "me@example.com")
        ```

    References:
        `GET /2.0/user/emails/{email}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-users/#api-user-emails-email-get>`_
    """
    return await get_user_emails_email.asyncio(email, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def ssh_keys(client: BBClient, selected_user: str, *, pagelen: int = 25) -> list[SshAccountKey]:
    """Return all SSH keys for a user.

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
        keys = await users.ssh_keys(client, "{account-uuid}")
        ```

    References:
        `GET /2.0/users/{selected_user}/ssh-keys
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-ssh/#api-users-selected-user-ssh-keys-get>`_
    """
    return [
        k
        async for k in async_paginate(
            get_users_selected_user_ssh_keys.asyncio,
            selected_user,
            client=client.auth,
            pagelen=pagelen,
        )
        if isinstance(k, SshAccountKey)
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_ssh_key(client: BBClient, selected_user: str, key_id: int) -> SshAccountKey | None:
    """Return a single SSH key by ID, or ``None`` if not found.

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
        key = await users.get_ssh_key(client, "{account-uuid}", 123)
        ```

    References:
        `GET /2.0/users/{selected_user}/ssh-keys/{key_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-ssh/#api-users-selected-user-ssh-keys-key-id-get>`_
    """
    result = await get_users_selected_user_ssh_keys_key_id.asyncio(selected_user, key_id, client=client.auth)
    return result if isinstance(result, SshAccountKey) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def add_ssh_key(
    client: BBClient,
    selected_user: str,
    *,
    body: SshAccountKey | Unset = UNSET,
) -> SshAccountKey | None:
    """Add an SSH key to a user account.

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
        key = await users.add_ssh_key(client, "{account-uuid}", body=SshAccountKey(...))
        ```

    References:
        `POST /2.0/users/{selected_user}/ssh-keys
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-ssh/#api-users-selected-user-ssh-keys-post>`_
    """
    result = await post_users_selected_user_ssh_keys.asyncio(selected_user, client=client.auth, body=body)
    return result if isinstance(result, SshAccountKey) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def update_ssh_key(
    client: BBClient,
    selected_user: str,
    key_id: int,
    *,
    body: SshAccountKey | Unset = UNSET,
) -> SshAccountKey | None:
    """Update an SSH key on a user account.

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
        key = await users.update_ssh_key(client, "{account-uuid}", 123, body=SshAccountKey(...))
        ```

    References:
        `PUT /2.0/users/{selected_user}/ssh-keys/{key_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-ssh/#api-users-selected-user-ssh-keys-key-id-put>`_
    """
    result = await put_users_selected_user_ssh_keys_key_id.asyncio(selected_user, key_id, client=client.auth, body=body)
    return result if isinstance(result, SshAccountKey) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete_ssh_key(client: BBClient, selected_user: str, key_id: int) -> None:
    """Delete an SSH key from a user account.

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
        await users.delete_ssh_key(client, "{account-uuid}", 123)
        ```

    References:
        `DELETE /2.0/users/{selected_user}/ssh-keys/{key_id}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-ssh/#api-users-selected-user-ssh-keys-key-id-delete>`_
    """
    await delete_users_selected_user_ssh_keys_key_id.asyncio(selected_user, key_id, client=client.auth)


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def gpg_keys(client: BBClient, selected_user: str, *, pagelen: int = 25) -> list[GpgAccountKey]:
    """Return all GPG keys for a user.

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
        keys = await users.gpg_keys(client, "{account-uuid}")
        ```

    References:
        `GET /2.0/users/{selected_user}/gpg-keys
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-gpg/#api-users-selected-user-gpg-keys-get>`_
    """
    return [
        k
        async for k in async_paginate(
            get_users_selected_user_gpg_keys.asyncio,
            selected_user,
            client=client.auth,
            pagelen=pagelen,
        )
        if isinstance(k, GpgAccountKey)
    ]


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def get_gpg_key(client: BBClient, selected_user: str, fingerprint: str) -> GpgAccountKey | None:
    """Return a single GPG key by fingerprint, or ``None`` if not found.

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
        key = await users.get_gpg_key(client, "{account-uuid}", "ABCD1234...")
        ```

    References:
        `GET /2.0/users/{selected_user}/gpg-keys/{fingerprint}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-gpg/#api-users-selected-user-gpg-keys-fingerprint-get>`_
    """
    result = await get_users_selected_user_gpg_keys_fingerprint.asyncio(selected_user, fingerprint, client=client.auth)
    return result if isinstance(result, GpgAccountKey) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def add_gpg_key(
    client: BBClient,
    selected_user: str,
    *,
    body: GpgAccountKey | Unset = UNSET,
) -> GpgAccountKey | None:
    """Add a GPG key to a user account.

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
        key = await users.add_gpg_key(client, "{account-uuid}", body=GPGAccountKey(...))
        ```

    References:
        `POST /2.0/users/{selected_user}/gpg-keys
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-gpg/#api-users-selected-user-gpg-keys-post>`_
    """
    result = await post_users_selected_user_gpg_keys.asyncio(selected_user, client=client.auth, body=body)
    return result if isinstance(result, GpgAccountKey) else None


@require_auth(AuthMethod.OAUTH2, AuthMethod.BASIC, AuthMethod.API_KEY)
async def delete_gpg_key(client: BBClient, selected_user: str, fingerprint: str) -> None:
    """Delete a GPG key from a user account.

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
        await users.delete_gpg_key(client, "{account-uuid}", "ABCD1234...")
        ```

    References:
        `DELETE /2.0/users/{selected_user}/gpg-keys/{fingerprint}
        <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-gpg/#api-users-selected-user-gpg-keys-fingerprint-delete>`_
    """
    await delete_users_selected_user_gpg_keys_fingerprint.asyncio(selected_user, fingerprint, client=client.auth)
