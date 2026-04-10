from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_bitbucket_license import RestBitbucketLicense
from ...models.update_license_response_400 import UpdateLicenseResponse400
from ...models.update_license_response_401 import UpdateLicenseResponse401
from ...models.update_license_response_409 import UpdateLicenseResponse409
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RestBitbucketLicense | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/admin/license",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RestBitbucketLicense | UpdateLicenseResponse400 | UpdateLicenseResponse401 | UpdateLicenseResponse409 | None:
    if response.status_code == 200:
        response_200 = RestBitbucketLicense.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UpdateLicenseResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateLicenseResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 409:
        response_409 = UpdateLicenseResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestBitbucketLicense | UpdateLicenseResponse400 | UpdateLicenseResponse401 | UpdateLicenseResponse409]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestBitbucketLicense | Unset = UNSET,
) -> Response[RestBitbucketLicense | UpdateLicenseResponse400 | UpdateLicenseResponse401 | UpdateLicenseResponse409]:
    """Update license

     Decodes the provided encoded license and sets it as the active license. If no license was provided,
    a 400 is returned. If the license cannot be decoded, or cannot be applied, a 409 is returned. Some
    possible reasons a license may not be applied include:

    - It is for a different product
    - It is already expired


    Otherwise, if the license is updated successfully, details for the new license are returned with a
    200 response.

    <b>Warning</b>: It is possible to downgrade the license during update, applying a license with a
    lower number of permitted users. If the number of currently-licensed users exceeds the limits of the
    new license, pushing will be disabled until the licensed user count is brought into compliance with
    the new license.

    The authenticated user must have <b>SYS_ADMIN</b> permission. <b>ADMIN</b> users may <i>view</i> the
    current license details, but they may not <i>update</i> the license.

    Args:
        body (RestBitbucketLicense | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestBitbucketLicense | UpdateLicenseResponse400 | UpdateLicenseResponse401 | UpdateLicenseResponse409]
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
    body: RestBitbucketLicense | Unset = UNSET,
) -> RestBitbucketLicense | UpdateLicenseResponse400 | UpdateLicenseResponse401 | UpdateLicenseResponse409 | None:
    """Update license

     Decodes the provided encoded license and sets it as the active license. If no license was provided,
    a 400 is returned. If the license cannot be decoded, or cannot be applied, a 409 is returned. Some
    possible reasons a license may not be applied include:

    - It is for a different product
    - It is already expired


    Otherwise, if the license is updated successfully, details for the new license are returned with a
    200 response.

    <b>Warning</b>: It is possible to downgrade the license during update, applying a license with a
    lower number of permitted users. If the number of currently-licensed users exceeds the limits of the
    new license, pushing will be disabled until the licensed user count is brought into compliance with
    the new license.

    The authenticated user must have <b>SYS_ADMIN</b> permission. <b>ADMIN</b> users may <i>view</i> the
    current license details, but they may not <i>update</i> the license.

    Args:
        body (RestBitbucketLicense | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestBitbucketLicense | UpdateLicenseResponse400 | UpdateLicenseResponse401 | UpdateLicenseResponse409
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestBitbucketLicense | Unset = UNSET,
) -> Response[RestBitbucketLicense | UpdateLicenseResponse400 | UpdateLicenseResponse401 | UpdateLicenseResponse409]:
    """Update license

     Decodes the provided encoded license and sets it as the active license. If no license was provided,
    a 400 is returned. If the license cannot be decoded, or cannot be applied, a 409 is returned. Some
    possible reasons a license may not be applied include:

    - It is for a different product
    - It is already expired


    Otherwise, if the license is updated successfully, details for the new license are returned with a
    200 response.

    <b>Warning</b>: It is possible to downgrade the license during update, applying a license with a
    lower number of permitted users. If the number of currently-licensed users exceeds the limits of the
    new license, pushing will be disabled until the licensed user count is brought into compliance with
    the new license.

    The authenticated user must have <b>SYS_ADMIN</b> permission. <b>ADMIN</b> users may <i>view</i> the
    current license details, but they may not <i>update</i> the license.

    Args:
        body (RestBitbucketLicense | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestBitbucketLicense | UpdateLicenseResponse400 | UpdateLicenseResponse401 | UpdateLicenseResponse409]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RestBitbucketLicense | Unset = UNSET,
) -> RestBitbucketLicense | UpdateLicenseResponse400 | UpdateLicenseResponse401 | UpdateLicenseResponse409 | None:
    """Update license

     Decodes the provided encoded license and sets it as the active license. If no license was provided,
    a 400 is returned. If the license cannot be decoded, or cannot be applied, a 409 is returned. Some
    possible reasons a license may not be applied include:

    - It is for a different product
    - It is already expired


    Otherwise, if the license is updated successfully, details for the new license are returned with a
    200 response.

    <b>Warning</b>: It is possible to downgrade the license during update, applying a license with a
    lower number of permitted users. If the number of currently-licensed users exceeds the limits of the
    new license, pushing will be disabled until the licensed user count is brought into compliance with
    the new license.

    The authenticated user must have <b>SYS_ADMIN</b> permission. <b>ADMIN</b> users may <i>view</i> the
    current license details, but they may not <i>update</i> the license.

    Args:
        body (RestBitbucketLicense | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestBitbucketLicense | UpdateLicenseResponse400 | UpdateLicenseResponse401 | UpdateLicenseResponse409
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
