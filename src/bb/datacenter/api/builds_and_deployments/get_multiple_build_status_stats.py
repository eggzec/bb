from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_multiple_build_status_stats_response_401 import GetMultipleBuildStatusStatsResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[str] | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/build-status/latest/commits/stats",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetMultipleBuildStatusStatsResponse401 | None:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200

    if response.status_code == 401:
        response_401 = GetMultipleBuildStatusStatsResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetMultipleBuildStatusStatsResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[str] | Unset = UNSET,
) -> Response[Any | GetMultipleBuildStatusStatsResponse401]:
    """Get build status statistics for multiple commits

     Produces a list of the build statistics for multiple commits. Commits <em>without any builds
    associated with them</em> will not be returned.<br> For example if the commit
    <code>e00cf62997a027bbf785614a93e2e55bb331d268</code> does not have any build statuses associated
    with it, it will not be present in the response.

    Args:
        body (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetMultipleBuildStatusStatsResponse401]
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
    body: list[str] | Unset = UNSET,
) -> Any | GetMultipleBuildStatusStatsResponse401 | None:
    """Get build status statistics for multiple commits

     Produces a list of the build statistics for multiple commits. Commits <em>without any builds
    associated with them</em> will not be returned.<br> For example if the commit
    <code>e00cf62997a027bbf785614a93e2e55bb331d268</code> does not have any build statuses associated
    with it, it will not be present in the response.

    Args:
        body (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetMultipleBuildStatusStatsResponse401
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[str] | Unset = UNSET,
) -> Response[Any | GetMultipleBuildStatusStatsResponse401]:
    """Get build status statistics for multiple commits

     Produces a list of the build statistics for multiple commits. Commits <em>without any builds
    associated with them</em> will not be returned.<br> For example if the commit
    <code>e00cf62997a027bbf785614a93e2e55bb331d268</code> does not have any build statuses associated
    with it, it will not be present in the response.

    Args:
        body (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetMultipleBuildStatusStatsResponse401]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[str] | Unset = UNSET,
) -> Any | GetMultipleBuildStatusStatsResponse401 | None:
    """Get build status statistics for multiple commits

     Produces a list of the build statistics for multiple commits. Commits <em>without any builds
    associated with them</em> will not be returned.<br> For example if the commit
    <code>e00cf62997a027bbf785614a93e2e55bb331d268</code> does not have any build statuses associated
    with it, it will not be present in the response.

    Args:
        body (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetMultipleBuildStatusStatsResponse401
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
