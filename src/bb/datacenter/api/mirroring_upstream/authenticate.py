from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.authenticate_response_400 import AuthenticateResponse400
from ...models.authenticate_response_401 import AuthenticateResponse401
from ...models.rest_application_user_with_permissions import RestApplicationUserWithPermissions
from ...models.rest_authentication_request import RestAuthenticationRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RestAuthenticationRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/mirroring/latest/authenticate",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AuthenticateResponse400 | AuthenticateResponse401 | RestApplicationUserWithPermissions | None:
    if response.status_code == 200:
        response_200 = RestApplicationUserWithPermissions.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AuthenticateResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AuthenticateResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AuthenticateResponse400 | AuthenticateResponse401 | RestApplicationUserWithPermissions]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestAuthenticationRequest | Unset = UNSET,
) -> Response[AuthenticateResponse400 | AuthenticateResponse401 | RestApplicationUserWithPermissions]:
    """Authenticate on behalf of a user

     Authenticates on behalf of a user. Used by mirrors to check the credentials supplied to them by
    users. If successful a user and their effective permissions are returned as follows -

    * For SSH credentials - all the effective user permissions are returned.
    * For all other credentials - the highest global permission is returned along with highest
    repository permission if repository ID is also provided in the request.

    Currently only username/password, bearer token and SSH credentials are supported.

    Args:
        body (RestAuthenticationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthenticateResponse400 | AuthenticateResponse401 | RestApplicationUserWithPermissions]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: RestAuthenticationRequest | Unset = UNSET,
) -> AuthenticateResponse400 | AuthenticateResponse401 | RestApplicationUserWithPermissions | None:
    """Authenticate on behalf of a user

     Authenticates on behalf of a user. Used by mirrors to check the credentials supplied to them by
    users. If successful a user and their effective permissions are returned as follows -

    * For SSH credentials - all the effective user permissions are returned.
    * For all other credentials - the highest global permission is returned along with highest
    repository permission if repository ID is also provided in the request.

    Currently only username/password, bearer token and SSH credentials are supported.

    Args:
        body (RestAuthenticationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthenticateResponse400 | AuthenticateResponse401 | RestApplicationUserWithPermissions
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestAuthenticationRequest | Unset = UNSET,
) -> Response[AuthenticateResponse400 | AuthenticateResponse401 | RestApplicationUserWithPermissions]:
    """Authenticate on behalf of a user

     Authenticates on behalf of a user. Used by mirrors to check the credentials supplied to them by
    users. If successful a user and their effective permissions are returned as follows -

    * For SSH credentials - all the effective user permissions are returned.
    * For all other credentials - the highest global permission is returned along with highest
    repository permission if repository ID is also provided in the request.

    Currently only username/password, bearer token and SSH credentials are supported.

    Args:
        body (RestAuthenticationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuthenticateResponse400 | AuthenticateResponse401 | RestApplicationUserWithPermissions]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RestAuthenticationRequest | Unset = UNSET,
) -> AuthenticateResponse400 | AuthenticateResponse401 | RestApplicationUserWithPermissions | None:
    """Authenticate on behalf of a user

     Authenticates on behalf of a user. Used by mirrors to check the credentials supplied to them by
    users. If successful a user and their effective permissions are returned as follows -

    * For SSH credentials - all the effective user permissions are returned.
    * For all other credentials - the highest global permission is returned along with highest
    repository permission if repository ID is also provided in the request.

    Currently only username/password, bearer token and SSH credentials are supported.

    Args:
        body (RestAuthenticationRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuthenticateResponse400 | AuthenticateResponse401 | RestApplicationUserWithPermissions
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
