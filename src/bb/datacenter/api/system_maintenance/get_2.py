from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_2_response_401 import Get2Response401
from ...models.get_2_response_404 import Get2Response404
from ...models.rest_bitbucket_license import RestBitbucketLicense
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/admin/license",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Get2Response401 | Get2Response404 | RestBitbucketLicense | None:
    if response.status_code == 200:
        response_200 = RestBitbucketLicense.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Get2Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Get2Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Get2Response401 | Get2Response404 | RestBitbucketLicense]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Get2Response401 | Get2Response404 | RestBitbucketLicense]:
    """Get license details

     Retrieves details about the current license, as well as the current status of the system with
    regards to the installed license. The status includes the current number of users applied toward the
    license limit, as well as any status messages about the license (warnings about expiry or user
    counts exceeding license limits).

    The authenticated user must have <b>ADMIN</b> permission. Unauthenticated users, and non-
    administrators, are not permitted to access license details.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Get2Response401 | Get2Response404 | RestBitbucketLicense]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Get2Response401 | Get2Response404 | RestBitbucketLicense | None:
    """Get license details

     Retrieves details about the current license, as well as the current status of the system with
    regards to the installed license. The status includes the current number of users applied toward the
    license limit, as well as any status messages about the license (warnings about expiry or user
    counts exceeding license limits).

    The authenticated user must have <b>ADMIN</b> permission. Unauthenticated users, and non-
    administrators, are not permitted to access license details.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Get2Response401 | Get2Response404 | RestBitbucketLicense
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Get2Response401 | Get2Response404 | RestBitbucketLicense]:
    """Get license details

     Retrieves details about the current license, as well as the current status of the system with
    regards to the installed license. The status includes the current number of users applied toward the
    license limit, as well as any status messages about the license (warnings about expiry or user
    counts exceeding license limits).

    The authenticated user must have <b>ADMIN</b> permission. Unauthenticated users, and non-
    administrators, are not permitted to access license details.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Get2Response401 | Get2Response404 | RestBitbucketLicense]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Get2Response401 | Get2Response404 | RestBitbucketLicense | None:
    """Get license details

     Retrieves details about the current license, as well as the current status of the system with
    regards to the installed license. The status includes the current number of users applied toward the
    license limit, as well as any status messages about the license (warnings about expiry or user
    counts exceeding license limits).

    The authenticated user must have <b>ADMIN</b> permission. Unauthenticated users, and non-
    administrators, are not permitted to access license details.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Get2Response401 | Get2Response404 | RestBitbucketLicense
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
