from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_access_token_2_response_400 import CreateAccessToken2Response400
from ...models.create_access_token_2_response_401 import CreateAccessToken2Response401
from ...models.create_access_token_2_response_404 import CreateAccessToken2Response404
from ...models.rest_access_token_request import RestAccessTokenRequest
from ...models.rest_raw_access_token import RestRawAccessToken
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_slug: str,
    *,
    body: RestAccessTokenRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/access-tokens/latest/users/{user_slug}".format(
            user_slug=quote(str(user_slug), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateAccessToken2Response400
    | CreateAccessToken2Response401
    | CreateAccessToken2Response404
    | RestRawAccessToken
    | None
):
    if response.status_code == 200:
        response_200 = RestRawAccessToken.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateAccessToken2Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateAccessToken2Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = CreateAccessToken2Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateAccessToken2Response400 | CreateAccessToken2Response401 | CreateAccessToken2Response404 | RestRawAccessToken
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestAccessTokenRequest | Unset = UNSET,
) -> Response[
    CreateAccessToken2Response400 | CreateAccessToken2Response401 | CreateAccessToken2Response404 | RestRawAccessToken
]:
    """Create personal HTTP token

     Create an access token for the user according to the given request.

    Args:
        user_slug (str):
        body (RestAccessTokenRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAccessToken2Response400 | CreateAccessToken2Response401 | CreateAccessToken2Response404 | RestRawAccessToken]
    """

    kwargs = _get_kwargs(
        user_slug=user_slug,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestAccessTokenRequest | Unset = UNSET,
) -> (
    CreateAccessToken2Response400
    | CreateAccessToken2Response401
    | CreateAccessToken2Response404
    | RestRawAccessToken
    | None
):
    """Create personal HTTP token

     Create an access token for the user according to the given request.

    Args:
        user_slug (str):
        body (RestAccessTokenRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAccessToken2Response400 | CreateAccessToken2Response401 | CreateAccessToken2Response404 | RestRawAccessToken
    """

    return sync_detailed(
        user_slug=user_slug,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    user_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestAccessTokenRequest | Unset = UNSET,
) -> Response[
    CreateAccessToken2Response400 | CreateAccessToken2Response401 | CreateAccessToken2Response404 | RestRawAccessToken
]:
    """Create personal HTTP token

     Create an access token for the user according to the given request.

    Args:
        user_slug (str):
        body (RestAccessTokenRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAccessToken2Response400 | CreateAccessToken2Response401 | CreateAccessToken2Response404 | RestRawAccessToken]
    """

    kwargs = _get_kwargs(
        user_slug=user_slug,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestAccessTokenRequest | Unset = UNSET,
) -> (
    CreateAccessToken2Response400
    | CreateAccessToken2Response401
    | CreateAccessToken2Response404
    | RestRawAccessToken
    | None
):
    """Create personal HTTP token

     Create an access token for the user according to the given request.

    Args:
        user_slug (str):
        body (RestAccessTokenRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAccessToken2Response400 | CreateAccessToken2Response401 | CreateAccessToken2Response404 | RestRawAccessToken
    """

    return (
        await asyncio_detailed(
            user_slug=user_slug,
            client=client,
            body=body,
        )
    ).parsed
