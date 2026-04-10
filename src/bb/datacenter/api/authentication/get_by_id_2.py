from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_by_id_2_response_401 import GetById2Response401
from ...models.get_by_id_2_response_404 import GetById2Response404
from ...models.rest_access_token import RestAccessToken
from ...types import Response


def _get_kwargs(
    user_slug: str,
    token_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/access-tokens/latest/users/{user_slug}/{token_id}".format(
            user_slug=quote(str(user_slug), safe=""),
            token_id=quote(str(token_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetById2Response401 | GetById2Response404 | RestAccessToken | None:
    if response.status_code == 200:
        response_200 = RestAccessToken.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetById2Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetById2Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetById2Response401 | GetById2Response404 | RestAccessToken]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_slug: str,
    token_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetById2Response401 | GetById2Response404 | RestAccessToken]:
    """Get HTTP token by ID

     Get the access token identified by the given ID.

    Args:
        user_slug (str):
        token_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetById2Response401 | GetById2Response404 | RestAccessToken]
    """

    kwargs = _get_kwargs(
        user_slug=user_slug,
        token_id=token_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_slug: str,
    token_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetById2Response401 | GetById2Response404 | RestAccessToken | None:
    """Get HTTP token by ID

     Get the access token identified by the given ID.

    Args:
        user_slug (str):
        token_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetById2Response401 | GetById2Response404 | RestAccessToken
    """

    return sync_detailed(
        user_slug=user_slug,
        token_id=token_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_slug: str,
    token_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetById2Response401 | GetById2Response404 | RestAccessToken]:
    """Get HTTP token by ID

     Get the access token identified by the given ID.

    Args:
        user_slug (str):
        token_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetById2Response401 | GetById2Response404 | RestAccessToken]
    """

    kwargs = _get_kwargs(
        user_slug=user_slug,
        token_id=token_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_slug: str,
    token_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetById2Response401 | GetById2Response404 | RestAccessToken | None:
    """Get HTTP token by ID

     Get the access token identified by the given ID.

    Args:
        user_slug (str):
        token_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetById2Response401 | GetById2Response404 | RestAccessToken
    """

    return (
        await asyncio_detailed(
            user_slug=user_slug,
            token_id=token_id,
            client=client,
        )
    ).parsed
