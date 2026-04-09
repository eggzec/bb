from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.paginated_repository_permissions import PaginatedRepositoryPermissions
from ...types import UNSET, Response, Unset

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    workspace: str,
    *,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/user/workspaces/{workspace}/permissions/repositories".format(
            workspace=quote(str(workspace), safe=""),
        ),
        "params": params,
    }

    return _kwargs


type ParsedPayload = Error | PaginatedRepositoryPermissions
type ParseResult = Error | PaginatedRepositoryPermissions | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = PaginatedRepositoryPermissions.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ParsedPayload]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: str,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[ParsedPayload]:
    r"""List repository permissions in a workspace for a user

     Returns an object for each repository the caller has explicit access to in the
    specified workspace and their effective permission — the highest level of
    permission the caller has. This does not return public repositories that the
    user was not granted any specific permission in, and does not distinguish between
    explicit and implicit privileges.

    Permissions can be:

    * `admin`
    * `write`
    * `read`

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by
    repository or permission by adding the following query string
    parameters:

    * `q=repository.name=\"bits\"` or `q=permission>\"read\"`
    * `sort=repository.name`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    Args:
        workspace (str):
        q (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedRepositoryPermissions]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        q=q,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> ParsedPayload | None:
    r"""List repository permissions in a workspace for a user

     Returns an object for each repository the caller has explicit access to in the
    specified workspace and their effective permission — the highest level of
    permission the caller has. This does not return public repositories that the
    user was not granted any specific permission in, and does not distinguish between
    explicit and implicit privileges.

    Permissions can be:

    * `admin`
    * `write`
    * `read`

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by
    repository or permission by adding the following query string
    parameters:

    * `q=repository.name=\"bits\"` or `q=permission>\"read\"`
    * `sort=repository.name`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    Args:
        workspace (str):
        q (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedRepositoryPermissions
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
        q=q,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[ParsedPayload]:
    r"""List repository permissions in a workspace for a user

     Returns an object for each repository the caller has explicit access to in the
    specified workspace and their effective permission — the highest level of
    permission the caller has. This does not return public repositories that the
    user was not granted any specific permission in, and does not distinguish between
    explicit and implicit privileges.

    Permissions can be:

    * `admin`
    * `write`
    * `read`

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by
    repository or permission by adding the following query string
    parameters:

    * `q=repository.name=\"bits\"` or `q=permission>\"read\"`
    * `sort=repository.name`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    Args:
        workspace (str):
        q (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedRepositoryPermissions]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        q=q,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> ParsedPayload | None:
    r"""List repository permissions in a workspace for a user

     Returns an object for each repository the caller has explicit access to in the
    specified workspace and their effective permission — the highest level of
    permission the caller has. This does not return public repositories that the
    user was not granted any specific permission in, and does not distinguish between
    explicit and implicit privileges.

    Permissions can be:

    * `admin`
    * `write`
    * `read`

    Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by
    repository or permission by adding the following query string
    parameters:

    * `q=repository.name=\"bits\"` or `q=permission>\"read\"`
    * `sort=repository.name`

    Note that the query parameter values need to be URL escaped so that `=`
    would become `%3D`.

    Args:
        workspace (str):
        q (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedRepositoryPermissions
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            q=q,
            sort=sort,
        )
    ).parsed
