from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_tag_response_400 import CreateTagResponse400
from ...models.create_tag_response_401 import CreateTagResponse401
from ...models.rest_git_tag_create_request import RestGitTagCreateRequest
from ...models.rest_tag import RestTag
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    body: RestGitTagCreateRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/git/latest/projects/{project_key}/repos/{repository_slug}/tags".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateTagResponse400 | CreateTagResponse401 | RestTag | None:
    if response.status_code == 201:
        response_201 = RestTag.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = CreateTagResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateTagResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateTagResponse400 | CreateTagResponse401 | RestTag]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestGitTagCreateRequest | Unset = UNSET,
) -> Response[CreateTagResponse400 | CreateTagResponse401 | RestTag]:
    """Create tag

     Creates a tag in the specified repository.

    The authenticated user must have an effective <strong>REPO_WRITE</strong> permission to call this
    resource.

    'LIGHTWEIGHT' and 'ANNOTATED' are the two type of tags that can be created. The 'startPoint' can
    either be a ref or a 'commit'.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestGitTagCreateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateTagResponse400 | CreateTagResponse401 | RestTag]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestGitTagCreateRequest | Unset = UNSET,
) -> CreateTagResponse400 | CreateTagResponse401 | RestTag | None:
    """Create tag

     Creates a tag in the specified repository.

    The authenticated user must have an effective <strong>REPO_WRITE</strong> permission to call this
    resource.

    'LIGHTWEIGHT' and 'ANNOTATED' are the two type of tags that can be created. The 'startPoint' can
    either be a ref or a 'commit'.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestGitTagCreateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateTagResponse400 | CreateTagResponse401 | RestTag
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestGitTagCreateRequest | Unset = UNSET,
) -> Response[CreateTagResponse400 | CreateTagResponse401 | RestTag]:
    """Create tag

     Creates a tag in the specified repository.

    The authenticated user must have an effective <strong>REPO_WRITE</strong> permission to call this
    resource.

    'LIGHTWEIGHT' and 'ANNOTATED' are the two type of tags that can be created. The 'startPoint' can
    either be a ref or a 'commit'.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestGitTagCreateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateTagResponse400 | CreateTagResponse401 | RestTag]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestGitTagCreateRequest | Unset = UNSET,
) -> CreateTagResponse400 | CreateTagResponse401 | RestTag | None:
    """Create tag

     Creates a tag in the specified repository.

    The authenticated user must have an effective <strong>REPO_WRITE</strong> permission to call this
    resource.

    'LIGHTWEIGHT' and 'ANNOTATED' are the two type of tags that can be created. The 'startPoint' can
    either be a ref or a 'commit'.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestGitTagCreateRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateTagResponse400 | CreateTagResponse401 | RestTag
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            body=body,
        )
    ).parsed
