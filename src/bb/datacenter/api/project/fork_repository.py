from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fork_repository_response_400 import ForkRepositoryResponse400
from ...models.fork_repository_response_401 import ForkRepositoryResponse401
from ...models.fork_repository_response_404 import ForkRepositoryResponse404
from ...models.rest_repository import RestRepository
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    body: RestRepository | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}".format(
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
) -> ForkRepositoryResponse400 | ForkRepositoryResponse401 | ForkRepositoryResponse404 | RestRepository | None:
    if response.status_code == 201:
        response_201 = RestRepository.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ForkRepositoryResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ForkRepositoryResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ForkRepositoryResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ForkRepositoryResponse400 | ForkRepositoryResponse401 | ForkRepositoryResponse404 | RestRepository]:
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
    body: RestRepository | Unset = UNSET,
) -> Response[ForkRepositoryResponse400 | ForkRepositoryResponse401 | ForkRepositoryResponse404 | RestRepository]:
    r"""Fork repository

     Create a new repository forked from an existing repository.

    The JSON body for this <code>POST</code> is not required to contain <i>any</i> properties. Even the
    name may be omitted. The following properties will be used, if provided:

    - <code>\"name\":\"Fork name\"</code> - Specifies the forked repository's name
      - Defaults to the name of the origin repository if not specified
    - <code>\"defaultBranch\":\"main\"</code> - Specifies the forked repository's default branch
      - Defaults to the origin repository's default branch if not specified
    - <code>\"project\":{\"key\":\"TARGET_KEY\"}</code> - Specifies the forked repository's target
    project by key
      - Defaults to the current user's personal project if not specified


    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    and <strong>PROJECT_ADMIN</strong> on the target project to call this resource. Note that users
    <i>always</i> have <b>PROJECT_ADMIN</b> permission on their personal projects.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestRepository | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ForkRepositoryResponse400 | ForkRepositoryResponse401 | ForkRepositoryResponse404 | RestRepository]
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
    body: RestRepository | Unset = UNSET,
) -> ForkRepositoryResponse400 | ForkRepositoryResponse401 | ForkRepositoryResponse404 | RestRepository | None:
    r"""Fork repository

     Create a new repository forked from an existing repository.

    The JSON body for this <code>POST</code> is not required to contain <i>any</i> properties. Even the
    name may be omitted. The following properties will be used, if provided:

    - <code>\"name\":\"Fork name\"</code> - Specifies the forked repository's name
      - Defaults to the name of the origin repository if not specified
    - <code>\"defaultBranch\":\"main\"</code> - Specifies the forked repository's default branch
      - Defaults to the origin repository's default branch if not specified
    - <code>\"project\":{\"key\":\"TARGET_KEY\"}</code> - Specifies the forked repository's target
    project by key
      - Defaults to the current user's personal project if not specified


    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    and <strong>PROJECT_ADMIN</strong> on the target project to call this resource. Note that users
    <i>always</i> have <b>PROJECT_ADMIN</b> permission on their personal projects.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestRepository | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ForkRepositoryResponse400 | ForkRepositoryResponse401 | ForkRepositoryResponse404 | RestRepository
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
    body: RestRepository | Unset = UNSET,
) -> Response[ForkRepositoryResponse400 | ForkRepositoryResponse401 | ForkRepositoryResponse404 | RestRepository]:
    r"""Fork repository

     Create a new repository forked from an existing repository.

    The JSON body for this <code>POST</code> is not required to contain <i>any</i> properties. Even the
    name may be omitted. The following properties will be used, if provided:

    - <code>\"name\":\"Fork name\"</code> - Specifies the forked repository's name
      - Defaults to the name of the origin repository if not specified
    - <code>\"defaultBranch\":\"main\"</code> - Specifies the forked repository's default branch
      - Defaults to the origin repository's default branch if not specified
    - <code>\"project\":{\"key\":\"TARGET_KEY\"}</code> - Specifies the forked repository's target
    project by key
      - Defaults to the current user's personal project if not specified


    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    and <strong>PROJECT_ADMIN</strong> on the target project to call this resource. Note that users
    <i>always</i> have <b>PROJECT_ADMIN</b> permission on their personal projects.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestRepository | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ForkRepositoryResponse400 | ForkRepositoryResponse401 | ForkRepositoryResponse404 | RestRepository]
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
    body: RestRepository | Unset = UNSET,
) -> ForkRepositoryResponse400 | ForkRepositoryResponse401 | ForkRepositoryResponse404 | RestRepository | None:
    r"""Fork repository

     Create a new repository forked from an existing repository.

    The JSON body for this <code>POST</code> is not required to contain <i>any</i> properties. Even the
    name may be omitted. The following properties will be used, if provided:

    - <code>\"name\":\"Fork name\"</code> - Specifies the forked repository's name
      - Defaults to the name of the origin repository if not specified
    - <code>\"defaultBranch\":\"main\"</code> - Specifies the forked repository's default branch
      - Defaults to the origin repository's default branch if not specified
    - <code>\"project\":{\"key\":\"TARGET_KEY\"}</code> - Specifies the forked repository's target
    project by key
      - Defaults to the current user's personal project if not specified


    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    and <strong>PROJECT_ADMIN</strong> on the target project to call this resource. Note that users
    <i>always</i> have <b>PROJECT_ADMIN</b> permission on their personal projects.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestRepository | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ForkRepositoryResponse400 | ForkRepositoryResponse401 | ForkRepositoryResponse404 | RestRepository
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            body=body,
        )
    ).parsed
