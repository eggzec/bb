from __future__ import annotations
from bb.cloud.models.error import Error
from bb.cloud.models.search_code_search_result import SearchCodeSearchResult
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET, Unset
from bb.cloud.sdk import search as _async
__all__ = ['code', 'account', 'team']

def code(client: BBClient, workspace: str, *, query: str, search_query: str | Unset=UNSET, pagelen: int=10) -> list[SearchCodeSearchResult] | Error:
    """Search for code in a workspace.

Synchronous wrapper around :func:`~bb.cloud.sdk.search.code`.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    workspace: Workspace slug or UUID.
    query: The search query string.
    search_query: Alternative parameter name used by the API (maps to ``search_query``).
        If both are given, ``search_query`` takes precedence.
    pagelen: Number of results per page (max 100). Defaults to ``10``.

Returns:
    List of :class:`~bb.cloud.models.search_code_search_result.SearchCodeSearchResult`
    objects matching the query.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import search

    client = BBClient.from_env()
    results = search.code(client, workspace="myws", query="def my_function")
    ```

References:
    `GET /2.0/workspaces/{workspace}/search/code
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-search/>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.search.code`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.code(client, workspace, query=query, search_query=search_query, pagelen=pagelen))

def account(client: BBClient, selected_user: str, *, search_query: str, pagelen: int=10) -> list[SearchCodeSearchResult] | Error:
    """Search for code in a user account.

Synchronous wrapper around :func:`~bb.cloud.sdk.search.account`.

Warning:
    Deprecated. This endpoint is no longer recommended by Atlassian.
    Use :func:`code` with a workspace slug instead.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    selected_user: The user's UUID, account ID, or username (slug).
    search_query: The search query string.
    pagelen: Number of results per page (max 100). Defaults to ``10``.

Returns:
    List of :class:`~bb.cloud.models.search_code_search_result.SearchCodeSearchResult`
    objects matching the query.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import search

    client = BBClient.from_env()
    results = search.account(
        client, selected_user="jsmith", search_query="def my_function"
    )
    ```

References:
    `GET /2.0/users/{selected_user}/search/code
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-search/>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.search.account`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.account(client, selected_user, search_query=search_query, pagelen=pagelen))

def team(client: BBClient, username: str, *, search_query: str, pagelen: int=10) -> list[SearchCodeSearchResult] | Error:
    """Search for code in a team.

Synchronous wrapper around :func:`~bb.cloud.sdk.search.team`.

Warning:
    Deprecated. This endpoint is no longer recommended by Atlassian.
    Use :func:`code` with a workspace slug instead.

Args:
    client: Authenticated :class:`~bb.cloud.sdk._client.BBClient` instance.
    username: The team's username (slug).
    search_query: The search query string.
    pagelen: Number of results per page (max 100). Defaults to ``10``.

Returns:
    List of :class:`~bb.cloud.models.search_code_search_result.SearchCodeSearchResult`
    objects matching the query.

Raises:
    :exc:`~bb.cloud.sdk._errors.AuthenticationError`: If ``client`` uses an unrecognised or unsupported auth method.
    :exc:`~bb.cloud.errors.UnexpectedStatus`: If the API returns an unexpected HTTP status.
    :exc:`httpx.HTTPError`: On network-level failures.

Example:
    ```python
    from bb.cloud import BBClient
    from bb.cloud.sdk import search

    client = BBClient.from_env()
    results = search.team(
        client, username="myteam", search_query="def my_function"
    )
    ```

References:
    `GET /2.0/teams/{username}/search/code
    <https://developer.atlassian.com/cloud/bitbucket/rest/api-group-search/>`_

Note:
    This synchronous wrapper executes :func:`~bb.cloud.sdk.search.team`
    with :func:`asyncio.run`. Use the async SDK directly from an existing event loop."""
    return client.run_sync(_async.team(client, username, search_query=search_query, pagelen=pagelen))
