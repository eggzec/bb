from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.revoke_many_body import RevokeManyBody
from ...models.revoke_many_response_401 import RevokeManyResponse401
from ...models.revoke_many_response_404 import RevokeManyResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    key_id: str,
    *,
    body: RevokeManyBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/keys/latest/ssh/{key_id}".format(
            key_id=quote(str(key_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RevokeManyResponse401 | RevokeManyResponse404 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = RevokeManyResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = RevokeManyResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RevokeManyResponse401 | RevokeManyResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    key_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RevokeManyBody | Unset = UNSET,
) -> Response[Any | RevokeManyResponse401 | RevokeManyResponse404]:
    """Revoke project SSH key

     Remove an existing access key for the projects and repositories in the submitted entity. If the same
    SSH key is used as an access key for multiple projects or repositories not supplied, only the access
    to the projects or repositories identified will be revoked.

    Args:
        key_id (str):
        body (RevokeManyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RevokeManyResponse401 | RevokeManyResponse404]
    """

    kwargs = _get_kwargs(
        key_id=key_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    key_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RevokeManyBody | Unset = UNSET,
) -> Any | RevokeManyResponse401 | RevokeManyResponse404 | None:
    """Revoke project SSH key

     Remove an existing access key for the projects and repositories in the submitted entity. If the same
    SSH key is used as an access key for multiple projects or repositories not supplied, only the access
    to the projects or repositories identified will be revoked.

    Args:
        key_id (str):
        body (RevokeManyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RevokeManyResponse401 | RevokeManyResponse404
    """

    return sync_detailed(
        key_id=key_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    key_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RevokeManyBody | Unset = UNSET,
) -> Response[Any | RevokeManyResponse401 | RevokeManyResponse404]:
    """Revoke project SSH key

     Remove an existing access key for the projects and repositories in the submitted entity. If the same
    SSH key is used as an access key for multiple projects or repositories not supplied, only the access
    to the projects or repositories identified will be revoked.

    Args:
        key_id (str):
        body (RevokeManyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RevokeManyResponse401 | RevokeManyResponse404]
    """

    kwargs = _get_kwargs(
        key_id=key_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    key_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RevokeManyBody | Unset = UNSET,
) -> Any | RevokeManyResponse401 | RevokeManyResponse404 | None:
    """Revoke project SSH key

     Remove an existing access key for the projects and repositories in the submitted entity. If the same
    SSH key is used as an access key for multiple projects or repositories not supplied, only the access
    to the projects or repositories identified will be revoked.

    Args:
        key_id (str):
        body (RevokeManyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RevokeManyResponse401 | RevokeManyResponse404
    """

    return (
        await asyncio_detailed(
            key_id=key_id,
            client=client,
            body=body,
        )
    ).parsed
