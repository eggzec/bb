from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.tag import Tag
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
    *,
    body: Tag,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/repositories/{workspace}/{repo_slug}/refs/tags".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Error | Tag
type ParseResult = Error | Tag | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 201:
        response_201 = Tag.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

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
    body: Tag,
) -> Response[ParsedPayload]:
    r""" Create a tag

     Creates a new annotated tag in the specified repository.

    The payload of the POST should consist of a JSON document that
    contains the name of the tag and the target hash.

    ```
    curl https://api.bitbucket.org/2.0/repositories/jdoe/myrepo/refs/tags \
    -s -u jdoe -X POST -H \"Content-Type: application/json\" \
    -d '{
        \"name\" : \"new-tag-name\",
        \"target\" : {
            \"hash\" : \"a1b2c3d4e5f6\",
        }
    }'
    ```

    This endpoint does support using short hash prefixes for the commit
    hash, but it may return a 400 response if the provided prefix is
    ambiguous. Using a full commit hash is the preferred approach.

    A message for the tag object may optionally be provided. If it is
    omitted or the provided message is empty, a default message of
    \"Added tag <tagname> for changeset <shorthash>\" will be used.

    Args:
        workspace (str):
        repo_slug (str):
        body (Tag):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Tag]
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
    body: Tag,
) -> ParsedPayload | None:
    r""" Create a tag

     Creates a new annotated tag in the specified repository.

    The payload of the POST should consist of a JSON document that
    contains the name of the tag and the target hash.

    ```
    curl https://api.bitbucket.org/2.0/repositories/jdoe/myrepo/refs/tags \
    -s -u jdoe -X POST -H \"Content-Type: application/json\" \
    -d '{
        \"name\" : \"new-tag-name\",
        \"target\" : {
            \"hash\" : \"a1b2c3d4e5f6\",
        }
    }'
    ```

    This endpoint does support using short hash prefixes for the commit
    hash, but it may return a 400 response if the provided prefix is
    ambiguous. Using a full commit hash is the preferred approach.

    A message for the tag object may optionally be provided. If it is
    omitted or the provided message is empty, a default message of
    \"Added tag <tagname> for changeset <shorthash>\" will be used.

    Args:
        workspace (str):
        repo_slug (str):
        body (Tag):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Tag
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
    body: Tag,
) -> Response[ParsedPayload]:
    r""" Create a tag

     Creates a new annotated tag in the specified repository.

    The payload of the POST should consist of a JSON document that
    contains the name of the tag and the target hash.

    ```
    curl https://api.bitbucket.org/2.0/repositories/jdoe/myrepo/refs/tags \
    -s -u jdoe -X POST -H \"Content-Type: application/json\" \
    -d '{
        \"name\" : \"new-tag-name\",
        \"target\" : {
            \"hash\" : \"a1b2c3d4e5f6\",
        }
    }'
    ```

    This endpoint does support using short hash prefixes for the commit
    hash, but it may return a 400 response if the provided prefix is
    ambiguous. Using a full commit hash is the preferred approach.

    A message for the tag object may optionally be provided. If it is
    omitted or the provided message is empty, a default message of
    \"Added tag <tagname> for changeset <shorthash>\" will be used.

    Args:
        workspace (str):
        repo_slug (str):
        body (Tag):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Tag]
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
    body: Tag,
) -> ParsedPayload | None:
    r""" Create a tag

     Creates a new annotated tag in the specified repository.

    The payload of the POST should consist of a JSON document that
    contains the name of the tag and the target hash.

    ```
    curl https://api.bitbucket.org/2.0/repositories/jdoe/myrepo/refs/tags \
    -s -u jdoe -X POST -H \"Content-Type: application/json\" \
    -d '{
        \"name\" : \"new-tag-name\",
        \"target\" : {
            \"hash\" : \"a1b2c3d4e5f6\",
        }
    }'
    ```

    This endpoint does support using short hash prefixes for the commit
    hash, but it may return a 400 response if the provided prefix is
    ambiguous. Using a full commit hash is the preferred approach.

    A message for the tag object may optionally be provided. If it is
    omitted or the provided message is empty, a default message of
    \"Added tag <tagname> for changeset <shorthash>\" will be used.

    Args:
        workspace (str):
        repo_slug (str):
        body (Tag):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Tag
     """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
            body=body,
        )
    ).parsed
