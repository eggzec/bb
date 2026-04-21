from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.branch import Branch
from ...models.error import Error
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    workspace: str,
    repo_slug: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/repositories/{workspace}/{repo_slug}/refs/branches".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Branch | Error
type ParseResult = Branch | Error | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 201:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_201 = Branch.from_dict(response.json())

        return response_201

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
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    r""" Create a branch

     Creates a new branch in the specified repository.

    The payload of the POST should consist of a JSON document that
    contains the name of the tag and the target hash.

    ```
    curl https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/branches \
    -s -u seanfarley -X POST -H \"Content-Type: application/json\" \
    -d '{
        \"name\" : \"smf/create-feature\",
        \"target\" : {
            \"hash\" : \"default\",
        }
    }'
    ```

    This call requires authentication. Private repositories require the
    caller to authenticate with an account that has appropriate
    authorization.

    The branch name should not include any prefixes (e.g.
    refs/heads). This endpoint does support using short hash prefixes for
    the commit hash, but it may return a 400 response if the provided
    prefix is ambiguous. Using a full commit hash is the preferred
    approach.

    Args:
        workspace (str):
        repo_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Branch | Error]
     """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
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
) -> ParsedPayload | None:
    r""" Create a branch

     Creates a new branch in the specified repository.

    The payload of the POST should consist of a JSON document that
    contains the name of the tag and the target hash.

    ```
    curl https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/branches \
    -s -u seanfarley -X POST -H \"Content-Type: application/json\" \
    -d '{
        \"name\" : \"smf/create-feature\",
        \"target\" : {
            \"hash\" : \"default\",
        }
    }'
    ```

    This call requires authentication. Private repositories require the
    caller to authenticate with an account that has appropriate
    authorization.

    The branch name should not include any prefixes (e.g.
    refs/heads). This endpoint does support using short hash prefixes for
    the commit hash, but it may return a 400 response if the provided
    prefix is ambiguous. Using a full commit hash is the preferred
    approach.

    Args:
        workspace (str):
        repo_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Branch | Error
     """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    r""" Create a branch

     Creates a new branch in the specified repository.

    The payload of the POST should consist of a JSON document that
    contains the name of the tag and the target hash.

    ```
    curl https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/branches \
    -s -u seanfarley -X POST -H \"Content-Type: application/json\" \
    -d '{
        \"name\" : \"smf/create-feature\",
        \"target\" : {
            \"hash\" : \"default\",
        }
    }'
    ```

    This call requires authentication. Private repositories require the
    caller to authenticate with an account that has appropriate
    authorization.

    The branch name should not include any prefixes (e.g.
    refs/heads). This endpoint does support using short hash prefixes for
    the commit hash, but it may return a 400 response if the provided
    prefix is ambiguous. Using a full commit hash is the preferred
    approach.

    Args:
        workspace (str):
        repo_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Branch | Error]
     """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    r""" Create a branch

     Creates a new branch in the specified repository.

    The payload of the POST should consist of a JSON document that
    contains the name of the tag and the target hash.

    ```
    curl https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/branches \
    -s -u seanfarley -X POST -H \"Content-Type: application/json\" \
    -d '{
        \"name\" : \"smf/create-feature\",
        \"target\" : {
            \"hash\" : \"default\",
        }
    }'
    ```

    This call requires authentication. Private repositories require the
    caller to authenticate with an account that has appropriate
    authorization.

    The branch name should not include any prefixes (e.g.
    refs/heads). This endpoint does support using short hash prefixes for
    the commit hash, but it may return a 400 response if the provided
    prefix is ambiguous. Using a full commit hash is the preferred
    approach.

    Args:
        workspace (str):
        repo_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Branch | Error
     """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
        )
    ).parsed
