from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_merge_config_response_401 import GetMergeConfigResponse401
from ...models.get_merge_config_response_404 import GetMergeConfigResponse404
from ...models.rest_pull_request_merge_config import RestPullRequestMergeConfig
from ...types import Response


def _get_kwargs(
    scm_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/admin/pull-requests/{scm_id}".format(
            scm_id=quote(str(scm_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetMergeConfigResponse401 | GetMergeConfigResponse404 | RestPullRequestMergeConfig | None:
    if response.status_code == 200:
        response_200 = RestPullRequestMergeConfig.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetMergeConfigResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetMergeConfigResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetMergeConfigResponse401 | GetMergeConfigResponse404 | RestPullRequestMergeConfig]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    scm_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetMergeConfigResponse401 | GetMergeConfigResponse404 | RestPullRequestMergeConfig]:
    """Get merge strategies

     Retrieve the merge strategies available for this instance.

    The user must be authenticated to call this resource.

    Args:
        scm_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMergeConfigResponse401 | GetMergeConfigResponse404 | RestPullRequestMergeConfig]
    """

    kwargs = _get_kwargs(
        scm_id=scm_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    scm_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetMergeConfigResponse401 | GetMergeConfigResponse404 | RestPullRequestMergeConfig | None:
    """Get merge strategies

     Retrieve the merge strategies available for this instance.

    The user must be authenticated to call this resource.

    Args:
        scm_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMergeConfigResponse401 | GetMergeConfigResponse404 | RestPullRequestMergeConfig
    """

    return sync_detailed(
        scm_id=scm_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    scm_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetMergeConfigResponse401 | GetMergeConfigResponse404 | RestPullRequestMergeConfig]:
    """Get merge strategies

     Retrieve the merge strategies available for this instance.

    The user must be authenticated to call this resource.

    Args:
        scm_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMergeConfigResponse401 | GetMergeConfigResponse404 | RestPullRequestMergeConfig]
    """

    kwargs = _get_kwargs(
        scm_id=scm_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    scm_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetMergeConfigResponse401 | GetMergeConfigResponse404 | RestPullRequestMergeConfig | None:
    """Get merge strategies

     Retrieve the merge strategies available for this instance.

    The user must be authenticated to call this resource.

    Args:
        scm_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMergeConfigResponse401 | GetMergeConfigResponse404 | RestPullRequestMergeConfig
    """

    return (
        await asyncio_detailed(
            scm_id=scm_id,
            client=client,
        )
    ).parsed
