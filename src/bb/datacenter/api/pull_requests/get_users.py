from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_application_user import RestApplicationUser
from ...models.rest_errors import RestErrors
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/settings/reviewer-groups/{id}/users".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RestErrors | list[RestApplicationUser] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RestApplicationUser.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = RestErrors.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = RestErrors.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestErrors | list[RestApplicationUser]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RestErrors | list[RestApplicationUser]]:
    """Get reviewer group users

     Retrieve a list of the users of a reviewer group.

    This does not return all the users of the group, only the users who are licensed and have
    <b>REPO_READ</b> permission for the specified repository.

    The authenticated user must have <b>REPO_READ</b> permission for the specified repository to call
    this resource.

    Args:
        project_key (str):
        repository_slug (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestErrors | list[RestApplicationUser]]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RestErrors | list[RestApplicationUser] | None:
    """Get reviewer group users

     Retrieve a list of the users of a reviewer group.

    This does not return all the users of the group, only the users who are licensed and have
    <b>REPO_READ</b> permission for the specified repository.

    The authenticated user must have <b>REPO_READ</b> permission for the specified repository to call
    this resource.

    Args:
        project_key (str):
        repository_slug (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestErrors | list[RestApplicationUser]
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[RestErrors | list[RestApplicationUser]]:
    """Get reviewer group users

     Retrieve a list of the users of a reviewer group.

    This does not return all the users of the group, only the users who are licensed and have
    <b>REPO_READ</b> permission for the specified repository.

    The authenticated user must have <b>REPO_READ</b> permission for the specified repository to call
    this resource.

    Args:
        project_key (str):
        repository_slug (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestErrors | list[RestApplicationUser]]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> RestErrors | list[RestApplicationUser] | None:
    """Get reviewer group users

     Retrieve a list of the users of a reviewer group.

    This does not return all the users of the group, only the users who are licensed and have
    <b>REPO_READ</b> permission for the specified repository.

    The authenticated user must have <b>REPO_READ</b> permission for the specified repository to call
    this resource.

    Args:
        project_key (str):
        repository_slug (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestErrors | list[RestApplicationUser]
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            id=id,
            client=client,
        )
    ).parsed
