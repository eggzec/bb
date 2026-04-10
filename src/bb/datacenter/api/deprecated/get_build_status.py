from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...deprecation import deprecated_endpoint
from ...models.get_build_status_response_200 import GetBuildStatusResponse200
from ...models.get_build_status_response_401 import GetBuildStatusResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    commit_id: str,
    *,
    order_by: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["orderBy"] = order_by

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/build-status/latest/commits/{commit_id}".format(
            commit_id=quote(str(commit_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetBuildStatusResponse200 | GetBuildStatusResponse401 | None:
    if response.status_code == 200:
        response_200 = GetBuildStatusResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetBuildStatusResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetBuildStatusResponse200 | GetBuildStatusResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated_endpoint(None)
def sync_detailed(
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    order_by: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetBuildStatusResponse200 | GetBuildStatusResponse401]:
    """Get build statuses for commit

     Gets build statuses associated with a commit.

    <strong>Deprecated in 7.14, please use the repository based builds resource instead.</strong>

    Args:
        commit_id (str):
        order_by (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBuildStatusResponse200 | GetBuildStatusResponse401]
    """

    kwargs = _get_kwargs(
        commit_id=commit_id,
        order_by=order_by,
        start=start,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated_endpoint(None)
def sync(
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    order_by: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetBuildStatusResponse200 | GetBuildStatusResponse401 | None:
    """Get build statuses for commit

     Gets build statuses associated with a commit.

    <strong>Deprecated in 7.14, please use the repository based builds resource instead.</strong>

    Args:
        commit_id (str):
        order_by (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBuildStatusResponse200 | GetBuildStatusResponse401
    """

    return sync_detailed(
        commit_id=commit_id,
        client=client,
        order_by=order_by,
        start=start,
        limit=limit,
    ).parsed


@deprecated_endpoint(None)
async def asyncio_detailed(
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    order_by: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetBuildStatusResponse200 | GetBuildStatusResponse401]:
    """Get build statuses for commit

     Gets build statuses associated with a commit.

    <strong>Deprecated in 7.14, please use the repository based builds resource instead.</strong>

    Args:
        commit_id (str):
        order_by (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBuildStatusResponse200 | GetBuildStatusResponse401]
    """

    kwargs = _get_kwargs(
        commit_id=commit_id,
        order_by=order_by,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated_endpoint(None)
async def asyncio(
    commit_id: str,
    *,
    client: AuthenticatedClient | Client,
    order_by: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetBuildStatusResponse200 | GetBuildStatusResponse401 | None:
    """Get build statuses for commit

     Gets build statuses associated with a commit.

    <strong>Deprecated in 7.14, please use the repository based builds resource instead.</strong>

    Args:
        commit_id (str):
        order_by (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBuildStatusResponse200 | GetBuildStatusResponse401
    """

    return (
        await asyncio_detailed(
            commit_id=commit_id,
            client=client,
            order_by=order_by,
            start=start,
            limit=limit,
        )
    ).parsed
