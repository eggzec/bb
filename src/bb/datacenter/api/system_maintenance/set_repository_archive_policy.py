from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_repository_policy import RestRepositoryPolicy
from ...models.set_repository_archive_policy_response_400 import SetRepositoryArchivePolicyResponse400
from ...models.set_repository_archive_policy_response_401 import SetRepositoryArchivePolicyResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RestRepositoryPolicy | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/policies/latest/admin/repos/archive",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RestRepositoryPolicy | SetRepositoryArchivePolicyResponse400 | SetRepositoryArchivePolicyResponse401 | None:
    if response.status_code == 200:
        response_200 = RestRepositoryPolicy.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = SetRepositoryArchivePolicyResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SetRepositoryArchivePolicyResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestRepositoryPolicy | SetRepositoryArchivePolicyResponse400 | SetRepositoryArchivePolicyResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestRepositoryPolicy | Unset = UNSET,
) -> Response[RestRepositoryPolicy | SetRepositoryArchivePolicyResponse400 | SetRepositoryArchivePolicyResponse401]:
    """Update repository archive policy

     Sets the repository archive policy for the instance.

    The authenticated user must have <b>SYS_ADMIN</b> permission.

    Args:
        body (RestRepositoryPolicy | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestRepositoryPolicy | SetRepositoryArchivePolicyResponse400 | SetRepositoryArchivePolicyResponse401]
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
    body: RestRepositoryPolicy | Unset = UNSET,
) -> RestRepositoryPolicy | SetRepositoryArchivePolicyResponse400 | SetRepositoryArchivePolicyResponse401 | None:
    """Update repository archive policy

     Sets the repository archive policy for the instance.

    The authenticated user must have <b>SYS_ADMIN</b> permission.

    Args:
        body (RestRepositoryPolicy | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestRepositoryPolicy | SetRepositoryArchivePolicyResponse400 | SetRepositoryArchivePolicyResponse401
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestRepositoryPolicy | Unset = UNSET,
) -> Response[RestRepositoryPolicy | SetRepositoryArchivePolicyResponse400 | SetRepositoryArchivePolicyResponse401]:
    """Update repository archive policy

     Sets the repository archive policy for the instance.

    The authenticated user must have <b>SYS_ADMIN</b> permission.

    Args:
        body (RestRepositoryPolicy | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestRepositoryPolicy | SetRepositoryArchivePolicyResponse400 | SetRepositoryArchivePolicyResponse401]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RestRepositoryPolicy | Unset = UNSET,
) -> RestRepositoryPolicy | SetRepositoryArchivePolicyResponse400 | SetRepositoryArchivePolicyResponse401 | None:
    """Update repository archive policy

     Sets the repository archive policy for the instance.

    The authenticated user must have <b>SYS_ADMIN</b> permission.

    Args:
        body (RestRepositoryPolicy | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestRepositoryPolicy | SetRepositoryArchivePolicyResponse400 | SetRepositoryArchivePolicyResponse401
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
