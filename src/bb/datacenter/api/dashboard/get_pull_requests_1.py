from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_pull_requests_1_response_200 import GetPullRequests1Response200
from ...models.get_pull_requests_1_response_400 import GetPullRequests1Response400
from ...models.get_pull_requests_1_response_401 import GetPullRequests1Response401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    closed_since: str | Unset = UNSET,
    role: str | Unset = UNSET,
    participant_status: str | Unset = UNSET,
    state: str | Unset = UNSET,
    user: str | Unset = UNSET,
    order: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["closedSince"] = closed_since

    params["role"] = role

    params["participantStatus"] = participant_status

    params["state"] = state

    params["user"] = user

    params["order"] = order

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/dashboard/pull-requests",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetPullRequests1Response200 | GetPullRequests1Response400 | GetPullRequests1Response401 | None:
    if response.status_code == 200:
        response_200 = GetPullRequests1Response200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetPullRequests1Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetPullRequests1Response401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetPullRequests1Response200 | GetPullRequests1Response400 | GetPullRequests1Response401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    closed_since: str | Unset = UNSET,
    role: str | Unset = UNSET,
    participant_status: str | Unset = UNSET,
    state: str | Unset = UNSET,
    user: str | Unset = UNSET,
    order: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetPullRequests1Response200 | GetPullRequests1Response400 | GetPullRequests1Response401]:
    """Get pull requests for a user

     Retrieve a page of pull requests where a user is involved as either a reviewer, author or a
    participant. The request may be filtered by pull request state, role or participant status.

    Args:
        closed_since (str | Unset):
        role (str | Unset):
        participant_status (str | Unset):
        state (str | Unset):
        user (str | Unset):
        order (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPullRequests1Response200 | GetPullRequests1Response400 | GetPullRequests1Response401]
    """

    kwargs = _get_kwargs(
        closed_since=closed_since,
        role=role,
        participant_status=participant_status,
        state=state,
        user=user,
        order=order,
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
    closed_since: str | Unset = UNSET,
    role: str | Unset = UNSET,
    participant_status: str | Unset = UNSET,
    state: str | Unset = UNSET,
    user: str | Unset = UNSET,
    order: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetPullRequests1Response200 | GetPullRequests1Response400 | GetPullRequests1Response401 | None:
    """Get pull requests for a user

     Retrieve a page of pull requests where a user is involved as either a reviewer, author or a
    participant. The request may be filtered by pull request state, role or participant status.

    Args:
        closed_since (str | Unset):
        role (str | Unset):
        participant_status (str | Unset):
        state (str | Unset):
        user (str | Unset):
        order (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPullRequests1Response200 | GetPullRequests1Response400 | GetPullRequests1Response401
    """

    return sync_detailed(
        client=client,
        closed_since=closed_since,
        role=role,
        participant_status=participant_status,
        state=state,
        user=user,
        order=order,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    closed_since: str | Unset = UNSET,
    role: str | Unset = UNSET,
    participant_status: str | Unset = UNSET,
    state: str | Unset = UNSET,
    user: str | Unset = UNSET,
    order: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetPullRequests1Response200 | GetPullRequests1Response400 | GetPullRequests1Response401]:
    """Get pull requests for a user

     Retrieve a page of pull requests where a user is involved as either a reviewer, author or a
    participant. The request may be filtered by pull request state, role or participant status.

    Args:
        closed_since (str | Unset):
        role (str | Unset):
        participant_status (str | Unset):
        state (str | Unset):
        user (str | Unset):
        order (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPullRequests1Response200 | GetPullRequests1Response400 | GetPullRequests1Response401]
    """

    kwargs = _get_kwargs(
        closed_since=closed_since,
        role=role,
        participant_status=participant_status,
        state=state,
        user=user,
        order=order,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    closed_since: str | Unset = UNSET,
    role: str | Unset = UNSET,
    participant_status: str | Unset = UNSET,
    state: str | Unset = UNSET,
    user: str | Unset = UNSET,
    order: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetPullRequests1Response200 | GetPullRequests1Response400 | GetPullRequests1Response401 | None:
    """Get pull requests for a user

     Retrieve a page of pull requests where a user is involved as either a reviewer, author or a
    participant. The request may be filtered by pull request state, role or participant status.

    Args:
        closed_since (str | Unset):
        role (str | Unset):
        participant_status (str | Unset):
        state (str | Unset):
        user (str | Unset):
        order (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPullRequests1Response200 | GetPullRequests1Response400 | GetPullRequests1Response401
    """

    return (
        await asyncio_detailed(
            client=client,
            closed_since=closed_since,
            role=role,
            participant_status=participant_status,
            state=state,
            user=user,
            order=order,
            start=start,
            limit=limit,
        )
    ).parsed
