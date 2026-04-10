from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_entity import ErrorEntity
from ...models.totp_elevation_rest_dto import TotpElevationRestDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_name: str,
    *,
    body: TotpElevationRestDTO | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/tsv/latest/totp/unenroll/user/{user_name}".format(
            user_name=quote(str(user_name), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorEntity | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = ErrorEntity.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorEntity.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorEntity.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorEntity.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorEntity]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: TotpElevationRestDTO | Unset = UNSET,
) -> Response[Any | ErrorEntity]:
    """Unenroll specific user from two-step verification

     Unenroll a user from two-step verification specified by the given username.

    Args:
        user_name (str):
        body (TotpElevationRestDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorEntity]
    """

    kwargs = _get_kwargs(
        user_name=user_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: TotpElevationRestDTO | Unset = UNSET,
) -> Any | ErrorEntity | None:
    """Unenroll specific user from two-step verification

     Unenroll a user from two-step verification specified by the given username.

    Args:
        user_name (str):
        body (TotpElevationRestDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorEntity
    """

    return sync_detailed(
        user_name=user_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    user_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: TotpElevationRestDTO | Unset = UNSET,
) -> Response[Any | ErrorEntity]:
    """Unenroll specific user from two-step verification

     Unenroll a user from two-step verification specified by the given username.

    Args:
        user_name (str):
        body (TotpElevationRestDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorEntity]
    """

    kwargs = _get_kwargs(
        user_name=user_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: TotpElevationRestDTO | Unset = UNSET,
) -> Any | ErrorEntity | None:
    """Unenroll specific user from two-step verification

     Unenroll a user from two-step verification specified by the given username.

    Args:
        user_name (str):
        body (TotpElevationRestDTO | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorEntity
    """

    return (
        await asyncio_detailed(
            user_name=user_name,
            client=client,
            body=body,
        )
    ).parsed
