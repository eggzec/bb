from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_for_project_response_400 import AddForProjectResponse400
from ...models.add_for_project_response_401 import AddForProjectResponse401
from ...models.add_for_project_response_404 import AddForProjectResponse404
from ...models.rest_ssh_access_key import RestSshAccessKey
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    *,
    body: RestSshAccessKey | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/keys/latest/projects/{project_key}/ssh".format(
            project_key=quote(str(project_key), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AddForProjectResponse400 | AddForProjectResponse401 | AddForProjectResponse404 | RestSshAccessKey | None:
    if response.status_code == 201:
        response_201 = RestSshAccessKey.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = AddForProjectResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AddForProjectResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = AddForProjectResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AddForProjectResponse400 | AddForProjectResponse401 | AddForProjectResponse404 | RestSshAccessKey]:
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
    body: RestSshAccessKey | Unset = UNSET,
) -> Response[AddForProjectResponse400 | AddForProjectResponse401 | AddForProjectResponse404 | RestSshAccessKey]:
    """Add project SSH key

     Register a new SSH key and grants access to the project identified in the URL.

    Args:
        project_key (str):
        body (RestSshAccessKey | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddForProjectResponse400 | AddForProjectResponse401 | AddForProjectResponse404 | RestSshAccessKey]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestSshAccessKey | Unset = UNSET,
) -> AddForProjectResponse400 | AddForProjectResponse401 | AddForProjectResponse404 | RestSshAccessKey | None:
    """Add project SSH key

     Register a new SSH key and grants access to the project identified in the URL.

    Args:
        project_key (str):
        body (RestSshAccessKey | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddForProjectResponse400 | AddForProjectResponse401 | AddForProjectResponse404 | RestSshAccessKey
    """

    return sync_detailed(
        project_key=project_key,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestSshAccessKey | Unset = UNSET,
) -> Response[AddForProjectResponse400 | AddForProjectResponse401 | AddForProjectResponse404 | RestSshAccessKey]:
    """Add project SSH key

     Register a new SSH key and grants access to the project identified in the URL.

    Args:
        project_key (str):
        body (RestSshAccessKey | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddForProjectResponse400 | AddForProjectResponse401 | AddForProjectResponse404 | RestSshAccessKey]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestSshAccessKey | Unset = UNSET,
) -> AddForProjectResponse400 | AddForProjectResponse401 | AddForProjectResponse404 | RestSshAccessKey | None:
    """Add project SSH key

     Register a new SSH key and grants access to the project identified in the URL.

    Args:
        project_key (str):
        body (RestSshAccessKey | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddForProjectResponse400 | AddForProjectResponse401 | AddForProjectResponse404 | RestSshAccessKey
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            client=client,
            body=body,
        )
    ).parsed
