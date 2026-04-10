from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_ssh_keys_for_project_response_200 import GetSshKeysForProjectResponse200
from ...models.get_ssh_keys_for_project_response_401 import GetSshKeysForProjectResponse401
from ...models.get_ssh_keys_for_project_response_404 import GetSshKeysForProjectResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    *,
    filter_: str | Unset = UNSET,
    permission: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["filter"] = filter_

    params["permission"] = permission

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/keys/latest/projects/{project_key}/ssh".format(
            project_key=quote(str(project_key), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetSshKeysForProjectResponse200 | GetSshKeysForProjectResponse401 | GetSshKeysForProjectResponse404 | None:
    if response.status_code == 200:
        response_200 = GetSshKeysForProjectResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetSshKeysForProjectResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetSshKeysForProjectResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetSshKeysForProjectResponse200 | GetSshKeysForProjectResponse401 | GetSshKeysForProjectResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    permission: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetSshKeysForProjectResponse200 | GetSshKeysForProjectResponse401 | GetSshKeysForProjectResponse404]:
    """Get SSH key

     Retrieves the access keys for the project identified in the URL.

    Args:
        project_key (str):
        filter_ (str | Unset):
        permission (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSshKeysForProjectResponse200 | GetSshKeysForProjectResponse401 | GetSshKeysForProjectResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        filter_=filter_,
        permission=permission,
        start=start,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    permission: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetSshKeysForProjectResponse200 | GetSshKeysForProjectResponse401 | GetSshKeysForProjectResponse404 | None:
    """Get SSH key

     Retrieves the access keys for the project identified in the URL.

    Args:
        project_key (str):
        filter_ (str | Unset):
        permission (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSshKeysForProjectResponse200 | GetSshKeysForProjectResponse401 | GetSshKeysForProjectResponse404
    """

    return sync_detailed(
        project_key=project_key,
        client=client,
        filter_=filter_,
        permission=permission,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    permission: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetSshKeysForProjectResponse200 | GetSshKeysForProjectResponse401 | GetSshKeysForProjectResponse404]:
    """Get SSH key

     Retrieves the access keys for the project identified in the URL.

    Args:
        project_key (str):
        filter_ (str | Unset):
        permission (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSshKeysForProjectResponse200 | GetSshKeysForProjectResponse401 | GetSshKeysForProjectResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        filter_=filter_,
        permission=permission,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    permission: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetSshKeysForProjectResponse200 | GetSshKeysForProjectResponse401 | GetSshKeysForProjectResponse404 | None:
    """Get SSH key

     Retrieves the access keys for the project identified in the URL.

    Args:
        project_key (str):
        filter_ (str | Unset):
        permission (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSshKeysForProjectResponse200 | GetSshKeysForProjectResponse401 | GetSshKeysForProjectResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            client=client,
            filter_=filter_,
            permission=permission,
            start=start,
            limit=limit,
        )
    ).parsed
