from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_label_response_401 import GetLabelResponse401
from ...models.get_label_response_404 import GetLabelResponse404
from ...models.rest_label import RestLabel
from ...types import Response


def _get_kwargs(
    label_name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/labels/{label_name}".format(
            label_name=quote(str(label_name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetLabelResponse401 | GetLabelResponse404 | RestLabel | None:
    if response.status_code == 200:
        response_200 = RestLabel.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetLabelResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetLabelResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetLabelResponse401 | GetLabelResponse404 | RestLabel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    label_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetLabelResponse401 | GetLabelResponse404 | RestLabel]:
    """Get label

     Returns a label.

    The user needs to be authenticated to use this resource.

    Args:
        label_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLabelResponse401 | GetLabelResponse404 | RestLabel]
    """

    kwargs = _get_kwargs(
        label_name=label_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    label_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetLabelResponse401 | GetLabelResponse404 | RestLabel | None:
    """Get label

     Returns a label.

    The user needs to be authenticated to use this resource.

    Args:
        label_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetLabelResponse401 | GetLabelResponse404 | RestLabel
    """

    return sync_detailed(
        label_name=label_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    label_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetLabelResponse401 | GetLabelResponse404 | RestLabel]:
    """Get label

     Returns a label.

    The user needs to be authenticated to use this resource.

    Args:
        label_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLabelResponse401 | GetLabelResponse404 | RestLabel]
    """

    kwargs = _get_kwargs(
        label_name=label_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    label_name: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetLabelResponse401 | GetLabelResponse404 | RestLabel | None:
    """Get label

     Returns a label.

    The user needs to be authenticated to use this resource.

    Args:
        label_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetLabelResponse401 | GetLabelResponse404 | RestLabel
    """

    return (
        await asyncio_detailed(
            label_name=label_name,
            client=client,
        )
    ).parsed
