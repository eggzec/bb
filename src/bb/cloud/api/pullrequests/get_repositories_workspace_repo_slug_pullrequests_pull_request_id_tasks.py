from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.paginated_tasks import PaginatedTasks
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
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagelen: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["sort"] = sort

    params["pagelen"] = pagelen

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/tasks".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
            pull_request_id=quote(str(pull_request_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


type ParsedPayload = Error | PaginatedTasks
type ParseResult = Error | PaginatedTasks | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = PaginatedTasks.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_404 = Error.from_dict(response.json())

        return response_404

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
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagelen: int | Unset = UNSET,
) -> Response[ParsedPayload]:
    """List tasks on a pull request

     Returns a paginated list of the pull request's tasks.

    This endpoint supports filtering and sorting of the results by the 'task' field.
    See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

    Args:
        workspace (str):
        repo_slug (str):
        pull_request_id (int):
        q (str | Unset):
        sort (str | Unset):
        pagelen (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedTasks]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        pull_request_id=pull_request_id,
        q=q,
        sort=sort,
        pagelen=pagelen,
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
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagelen: int | Unset = UNSET,
) -> ParsedPayload | None:
    """List tasks on a pull request

     Returns a paginated list of the pull request's tasks.

    This endpoint supports filtering and sorting of the results by the 'task' field.
    See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

    Args:
        workspace (str):
        repo_slug (str):
        pull_request_id (int):
        q (str | Unset):
        sort (str | Unset):
        pagelen (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedTasks
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        pull_request_id=pull_request_id,
        client=client,
        q=q,
        sort=sort,
        pagelen=pagelen,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagelen: int | Unset = UNSET,
) -> Response[ParsedPayload]:
    """List tasks on a pull request

     Returns a paginated list of the pull request's tasks.

    This endpoint supports filtering and sorting of the results by the 'task' field.
    See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

    Args:
        workspace (str):
        repo_slug (str):
        pull_request_id (int):
        q (str | Unset):
        sort (str | Unset):
        pagelen (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedTasks]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        pull_request_id=pull_request_id,
        q=q,
        sort=sort,
        pagelen=pagelen,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    pagelen: int | Unset = UNSET,
) -> ParsedPayload | None:
    """List tasks on a pull request

     Returns a paginated list of the pull request's tasks.

    This endpoint supports filtering and sorting of the results by the 'task' field.
    See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

    Args:
        workspace (str):
        repo_slug (str):
        pull_request_id (int):
        q (str | Unset):
        sort (str | Unset):
        pagelen (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedTasks
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            pull_request_id=pull_request_id,
            client=client,
            q=q,
            sort=sort,
            pagelen=pagelen,
        )
    ).parsed
