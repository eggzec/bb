from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.find_groups_for_user_response_200 import FindGroupsForUserResponse200
from ...models.find_groups_for_user_response_401 import FindGroupsForUserResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    filter_: str | Unset = UNSET,
    context: str,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["filter"] = filter_

    params["context"] = context

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/admin/users/more-members",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FindGroupsForUserResponse200 | FindGroupsForUserResponse401 | None:
    if response.status_code == 200:
        response_200 = FindGroupsForUserResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = FindGroupsForUserResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FindGroupsForUserResponse200 | FindGroupsForUserResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    context: str,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[FindGroupsForUserResponse200 | FindGroupsForUserResponse401]:
    """Get groups for user

     Retrieves a list of users that are <em>not</em> members of a specified group. <p>The authenticated
    user must have the <strong>LICENSED_USER</strong> permission to call this resource.

    Args:
        filter_ (str | Unset):
        context (str):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FindGroupsForUserResponse200 | FindGroupsForUserResponse401]
    """

    kwargs = _get_kwargs(
        filter_=filter_,
        context=context,
        start=start,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    context: str,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> FindGroupsForUserResponse200 | FindGroupsForUserResponse401 | None:
    """Get groups for user

     Retrieves a list of users that are <em>not</em> members of a specified group. <p>The authenticated
    user must have the <strong>LICENSED_USER</strong> permission to call this resource.

    Args:
        filter_ (str | Unset):
        context (str):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FindGroupsForUserResponse200 | FindGroupsForUserResponse401
    """

    return sync_detailed(
        client=client,
        filter_=filter_,
        context=context,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    context: str,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[FindGroupsForUserResponse200 | FindGroupsForUserResponse401]:
    """Get groups for user

     Retrieves a list of users that are <em>not</em> members of a specified group. <p>The authenticated
    user must have the <strong>LICENSED_USER</strong> permission to call this resource.

    Args:
        filter_ (str | Unset):
        context (str):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FindGroupsForUserResponse200 | FindGroupsForUserResponse401]
    """

    kwargs = _get_kwargs(
        filter_=filter_,
        context=context,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    context: str,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> FindGroupsForUserResponse200 | FindGroupsForUserResponse401 | None:
    """Get groups for user

     Retrieves a list of users that are <em>not</em> members of a specified group. <p>The authenticated
    user must have the <strong>LICENSED_USER</strong> permission to call this resource.

    Args:
        filter_ (str | Unset):
        context (str):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FindGroupsForUserResponse200 | FindGroupsForUserResponse401
    """

    return (
        await asyncio_detailed(
            client=client,
            filter_=filter_,
            context=context,
            start=start,
            limit=limit,
        )
    ).parsed
