from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.find_exempt_repos_by_project_order import FindExemptReposByProjectOrder
from ...models.find_exempt_repos_by_project_response_200 import FindExemptReposByProjectResponse200
from ...models.find_exempt_repos_by_project_response_401 import FindExemptReposByProjectResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    *,
    order: FindExemptReposByProjectOrder | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_order: str | Unset = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/secret-scanning/exempt".format(
            project_key=quote(str(project_key), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FindExemptReposByProjectResponse200 | FindExemptReposByProjectResponse401 | None:
    if response.status_code == 200:
        response_200 = FindExemptReposByProjectResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = FindExemptReposByProjectResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[FindExemptReposByProjectResponse200 | FindExemptReposByProjectResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    order: FindExemptReposByProjectOrder | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[FindExemptReposByProjectResponse200 | FindExemptReposByProjectResponse401]:
    """Find repos exempt from secret scanning for a project

     Find repositories exempt from secret scanning in a project

    Args:
        project_key (str):
        order (FindExemptReposByProjectOrder | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FindExemptReposByProjectResponse200 | FindExemptReposByProjectResponse401]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        order=order,
        start=start,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    order: FindExemptReposByProjectOrder | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> FindExemptReposByProjectResponse200 | FindExemptReposByProjectResponse401 | None:
    """Find repos exempt from secret scanning for a project

     Find repositories exempt from secret scanning in a project

    Args:
        project_key (str):
        order (FindExemptReposByProjectOrder | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FindExemptReposByProjectResponse200 | FindExemptReposByProjectResponse401
    """

    return sync_detailed(
        project_key=project_key,
        client=client,
        order=order,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    order: FindExemptReposByProjectOrder | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[FindExemptReposByProjectResponse200 | FindExemptReposByProjectResponse401]:
    """Find repos exempt from secret scanning for a project

     Find repositories exempt from secret scanning in a project

    Args:
        project_key (str):
        order (FindExemptReposByProjectOrder | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FindExemptReposByProjectResponse200 | FindExemptReposByProjectResponse401]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        order=order,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    order: FindExemptReposByProjectOrder | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> FindExemptReposByProjectResponse200 | FindExemptReposByProjectResponse401 | None:
    """Find repos exempt from secret scanning for a project

     Find repositories exempt from secret scanning in a project

    Args:
        project_key (str):
        order (FindExemptReposByProjectOrder | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FindExemptReposByProjectResponse200 | FindExemptReposByProjectResponse401
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            client=client,
            order=order,
            start=start,
            limit=limit,
        )
    ).parsed
