from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.repository import Repository
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
    *,
    body: Repository | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/repositories/{workspace}/{repo_slug}".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Error | Repository
type ParseResult = Error | Repository | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = Repository.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = Repository.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

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
    *,
    client: AuthenticatedClient,
    body: Repository | Unset = UNSET,
) -> Response[ParsedPayload]:
    """Update a repository

     Since this endpoint can be used to both update and to create a
    repository, the request body depends on the intent.

    #### Creation

    See the POST documentation for the repository endpoint for an example
    of the request body.

    #### Update

    Note: Changing the `name` of the repository will cause the location to
    be changed. This is because the URL of the repo is derived from the
    name (a process called slugification). In such a scenario, it is
    possible for the request to fail if the newly created slug conflicts
    with an existing repository's slug. But if there is no conflict,
    the new location will be returned in the `Location` header of the
    response.

    Args:
        workspace (str):
        repo_slug (str):
        body (Repository | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Repository]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    body: Repository | Unset = UNSET,
) -> ParsedPayload | None:
    """Update a repository

     Since this endpoint can be used to both update and to create a
    repository, the request body depends on the intent.

    #### Creation

    See the POST documentation for the repository endpoint for an example
    of the request body.

    #### Update

    Note: Changing the `name` of the repository will cause the location to
    be changed. This is because the URL of the repo is derived from the
    name (a process called slugification). In such a scenario, it is
    possible for the request to fail if the newly created slug conflicts
    with an existing repository's slug. But if there is no conflict,
    the new location will be returned in the `Location` header of the
    response.

    Args:
        workspace (str):
        repo_slug (str):
        body (Repository | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Repository
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    body: Repository | Unset = UNSET,
) -> Response[ParsedPayload]:
    """Update a repository

     Since this endpoint can be used to both update and to create a
    repository, the request body depends on the intent.

    #### Creation

    See the POST documentation for the repository endpoint for an example
    of the request body.

    #### Update

    Note: Changing the `name` of the repository will cause the location to
    be changed. This is because the URL of the repo is derived from the
    name (a process called slugification). In such a scenario, it is
    possible for the request to fail if the newly created slug conflicts
    with an existing repository's slug. But if there is no conflict,
    the new location will be returned in the `Location` header of the
    response.

    Args:
        workspace (str):
        repo_slug (str):
        body (Repository | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Repository]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    body: Repository | Unset = UNSET,
) -> ParsedPayload | None:
    """Update a repository

     Since this endpoint can be used to both update and to create a
    repository, the request body depends on the intent.

    #### Creation

    See the POST documentation for the repository endpoint for an example
    of the request body.

    #### Update

    Note: Changing the `name` of the repository will cause the location to
    be changed. This is because the URL of the repo is derived from the
    name (a process called slugification). In such a scenario, it is
    possible for the request to fail if the newly created slug conflicts
    with an existing repository's slug. But if there is no conflict,
    the new location will be returned in the `Location` header of the
    response.

    Args:
        workspace (str):
        repo_slug (str):
        body (Repository | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Repository
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
            body=body,
        )
    ).parsed
