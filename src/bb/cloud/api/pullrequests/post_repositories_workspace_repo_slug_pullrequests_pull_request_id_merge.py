from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.pull_request_merge_parameters import PullRequestMergeParameters
from ...models.pullrequest import Pullrequest
from ...types import UNSET, Response, Unset

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    body: PullRequestMergeParameters | Unset = UNSET,
    async_: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["async"] = async_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/merge".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
            pull_request_id=quote(str(pull_request_id), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Any | Error | Pullrequest
type ParseResult = Any | Error | Pullrequest | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = Pullrequest.from_dict(response.json())

        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 403:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if response.status_code == 555:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_555 = Error.from_dict(response.json())

        return response_555

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ParsedPayload]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    client: AuthenticatedClient,
    body: PullRequestMergeParameters | Unset = UNSET,
    async_: bool | Unset = UNSET,
) -> Response[ParsedPayload]:
    """Merge a pull request

     Merges the pull request.

    Args:
        workspace (str):
        repo_slug (str):
        pull_request_id (int):
        async_ (bool | Unset):
        body (PullRequestMergeParameters | Unset): The metadata that describes a pull request
            merge.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | Pullrequest]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        pull_request_id=pull_request_id,
        body=body,
        async_=async_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    client: AuthenticatedClient,
    body: PullRequestMergeParameters | Unset = UNSET,
    async_: bool | Unset = UNSET,
) -> ParsedPayload | None:
    """Merge a pull request

     Merges the pull request.

    Args:
        workspace (str):
        repo_slug (str):
        pull_request_id (int):
        async_ (bool | Unset):
        body (PullRequestMergeParameters | Unset): The metadata that describes a pull request
            merge.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | Pullrequest
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        pull_request_id=pull_request_id,
        client=client,
        body=body,
        async_=async_,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    client: AuthenticatedClient,
    body: PullRequestMergeParameters | Unset = UNSET,
    async_: bool | Unset = UNSET,
) -> Response[ParsedPayload]:
    """Merge a pull request

     Merges the pull request.

    Args:
        workspace (str):
        repo_slug (str):
        pull_request_id (int):
        async_ (bool | Unset):
        body (PullRequestMergeParameters | Unset): The metadata that describes a pull request
            merge.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | Pullrequest]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        pull_request_id=pull_request_id,
        body=body,
        async_=async_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    client: AuthenticatedClient,
    body: PullRequestMergeParameters | Unset = UNSET,
    async_: bool | Unset = UNSET,
) -> ParsedPayload | None:
    """Merge a pull request

     Merges the pull request.

    Args:
        workspace (str):
        repo_slug (str):
        pull_request_id (int):
        async_ (bool | Unset):
        body (PullRequestMergeParameters | Unset): The metadata that describes a pull request
            merge.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | Pullrequest
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            pull_request_id=pull_request_id,
            client=client,
            body=body,
            async_=async_,
        )
    ).parsed
