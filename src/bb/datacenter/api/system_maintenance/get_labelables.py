from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_labelables_response_200 import GetLabelablesResponse200
from ...models.get_labelables_response_400 import GetLabelablesResponse400
from ...models.get_labelables_response_401 import GetLabelablesResponse401
from ...models.get_labelables_response_404 import GetLabelablesResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    label_name: str,
    *,
    type_: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["type"] = type_

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/labels/{label_name}/labeled".format(
            label_name=quote(str(label_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetLabelablesResponse200 | GetLabelablesResponse400 | GetLabelablesResponse401 | GetLabelablesResponse404 | None:
    if response.status_code == 200:
        response_200 = GetLabelablesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetLabelablesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetLabelablesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetLabelablesResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetLabelablesResponse200 | GetLabelablesResponse400 | GetLabelablesResponse401 | GetLabelablesResponse404
]:
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
    type_: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[
    GetLabelablesResponse200 | GetLabelablesResponse400 | GetLabelablesResponse401 | GetLabelablesResponse404
]:
    """Get labelables for label

     Returns a page of labelables for a given label.

    Only labelables that the authenticated user has view access to will be returned.

    Args:
        label_name (str):
        type_ (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLabelablesResponse200 | GetLabelablesResponse400 | GetLabelablesResponse401 | GetLabelablesResponse404]
    """

    kwargs = _get_kwargs(
        label_name=label_name,
        type_=type_,
        start=start,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    label_name: str,
    *,
    client: AuthenticatedClient | Client,
    type_: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetLabelablesResponse200 | GetLabelablesResponse400 | GetLabelablesResponse401 | GetLabelablesResponse404 | None:
    """Get labelables for label

     Returns a page of labelables for a given label.

    Only labelables that the authenticated user has view access to will be returned.

    Args:
        label_name (str):
        type_ (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetLabelablesResponse200 | GetLabelablesResponse400 | GetLabelablesResponse401 | GetLabelablesResponse404
    """

    return sync_detailed(
        label_name=label_name,
        client=client,
        type_=type_,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    label_name: str,
    *,
    client: AuthenticatedClient | Client,
    type_: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[
    GetLabelablesResponse200 | GetLabelablesResponse400 | GetLabelablesResponse401 | GetLabelablesResponse404
]:
    """Get labelables for label

     Returns a page of labelables for a given label.

    Only labelables that the authenticated user has view access to will be returned.

    Args:
        label_name (str):
        type_ (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLabelablesResponse200 | GetLabelablesResponse400 | GetLabelablesResponse401 | GetLabelablesResponse404]
    """

    kwargs = _get_kwargs(
        label_name=label_name,
        type_=type_,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    label_name: str,
    *,
    client: AuthenticatedClient | Client,
    type_: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetLabelablesResponse200 | GetLabelablesResponse400 | GetLabelablesResponse401 | GetLabelablesResponse404 | None:
    """Get labelables for label

     Returns a page of labelables for a given label.

    Only labelables that the authenticated user has view access to will be returned.

    Args:
        label_name (str):
        type_ (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetLabelablesResponse200 | GetLabelablesResponse400 | GetLabelablesResponse401 | GetLabelablesResponse404
    """

    return (
        await asyncio_detailed(
            label_name=label_name,
            client=client,
            type_=type_,
            start=start,
            limit=limit,
        )
    ).parsed
