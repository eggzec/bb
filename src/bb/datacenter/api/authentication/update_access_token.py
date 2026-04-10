from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_access_token import RestAccessToken
from ...models.rest_access_token_request import RestAccessTokenRequest
from ...models.update_access_token_response_400 import UpdateAccessTokenResponse400
from ...models.update_access_token_response_401 import UpdateAccessTokenResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    token_id: str,
    *,
    body: RestAccessTokenRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/access-tokens/latest/projects/{project_key}/{token_id}".format(
            project_key=quote(str(project_key), safe=""),
            token_id=quote(str(token_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RestAccessToken | UpdateAccessTokenResponse400 | UpdateAccessTokenResponse401 | None:
    if response.status_code == 200:
        response_200 = RestAccessToken.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateAccessTokenResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateAccessTokenResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestAccessToken | UpdateAccessTokenResponse400 | UpdateAccessTokenResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    token_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestAccessTokenRequest | Unset = UNSET,
) -> Response[RestAccessToken | UpdateAccessTokenResponse400 | UpdateAccessTokenResponse401]:
    """Update HTTP token

     Modify an access token according to the given request. Any fields not specified will not be altered.

    Args:
        project_key (str):
        token_id (str):
        body (RestAccessTokenRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestAccessToken | UpdateAccessTokenResponse400 | UpdateAccessTokenResponse401]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        token_id=token_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    token_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestAccessTokenRequest | Unset = UNSET,
) -> RestAccessToken | UpdateAccessTokenResponse400 | UpdateAccessTokenResponse401 | None:
    """Update HTTP token

     Modify an access token according to the given request. Any fields not specified will not be altered.

    Args:
        project_key (str):
        token_id (str):
        body (RestAccessTokenRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestAccessToken | UpdateAccessTokenResponse400 | UpdateAccessTokenResponse401
    """

    return sync_detailed(
        project_key=project_key,
        token_id=token_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    token_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestAccessTokenRequest | Unset = UNSET,
) -> Response[RestAccessToken | UpdateAccessTokenResponse400 | UpdateAccessTokenResponse401]:
    """Update HTTP token

     Modify an access token according to the given request. Any fields not specified will not be altered.

    Args:
        project_key (str):
        token_id (str):
        body (RestAccessTokenRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestAccessToken | UpdateAccessTokenResponse400 | UpdateAccessTokenResponse401]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        token_id=token_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    token_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestAccessTokenRequest | Unset = UNSET,
) -> RestAccessToken | UpdateAccessTokenResponse400 | UpdateAccessTokenResponse401 | None:
    """Update HTTP token

     Modify an access token according to the given request. Any fields not specified will not be altered.

    Args:
        project_key (str):
        token_id (str):
        body (RestAccessTokenRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestAccessToken | UpdateAccessTokenResponse400 | UpdateAccessTokenResponse401
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            token_id=token_id,
            client=client,
            body=body,
        )
    ).parsed
