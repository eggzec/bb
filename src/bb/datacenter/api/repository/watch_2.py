from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_repository import RestRepository
from ...models.watch_2_response_401 import Watch2Response401
from ...models.watch_2_response_404 import Watch2Response404
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
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/watch".format(
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
) -> Any | Watch2Response401 | Watch2Response404 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = Watch2Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Watch2Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Watch2Response401 | Watch2Response404]:
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
) -> Response[Any | Watch2Response401 | Watch2Response404]:
    """Watch repository

     Add the authenticated user as a watcher for the specified repository.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository to call
    this resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestRepository | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Watch2Response401 | Watch2Response404]
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
) -> Any | Watch2Response401 | Watch2Response404 | None:
    """Watch repository

     Add the authenticated user as a watcher for the specified repository.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository to call
    this resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestRepository | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Watch2Response401 | Watch2Response404
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
) -> Response[Any | Watch2Response401 | Watch2Response404]:
    """Watch repository

     Add the authenticated user as a watcher for the specified repository.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository to call
    this resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestRepository | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Watch2Response401 | Watch2Response404]
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
) -> Any | Watch2Response401 | Watch2Response404 | None:
    """Watch repository

     Add the authenticated user as a watcher for the specified repository.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository to call
    this resource.

    Args:
        project_key (str):
        repository_slug (str):
        body (RestRepository | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Watch2Response401 | Watch2Response404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            body=body,
        )
    ).parsed
