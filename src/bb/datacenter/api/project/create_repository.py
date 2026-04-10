from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_repository_response_400 import CreateRepositoryResponse400
from ...models.create_repository_response_401 import CreateRepositoryResponse401
from ...models.create_repository_response_409 import CreateRepositoryResponse409
from ...models.rest_repository import RestRepository
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    *,
    body: RestRepository | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/projects/{project_key}/repos".format(
            project_key=quote(str(project_key), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateRepositoryResponse400 | CreateRepositoryResponse401 | CreateRepositoryResponse409 | RestRepository | None:
    if response.status_code == 201:
        response_201 = RestRepository.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = CreateRepositoryResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateRepositoryResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 409:
        response_409 = CreateRepositoryResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateRepositoryResponse400 | CreateRepositoryResponse401 | CreateRepositoryResponse409 | RestRepository]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestRepository | Unset = UNSET,
) -> Response[CreateRepositoryResponse400 | CreateRepositoryResponse401 | CreateRepositoryResponse409 | RestRepository]:
    """Create repository

     Create a new repository. Requires an existing project in which this repository will be created. The
    only parameters which will be used are name and scmId.

    The authenticated user must have <strong>REPO_CREATE</strong> permission or higher, for the context
    project to call this resource.

    Args:
        project_key (str):
        body (RestRepository | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateRepositoryResponse400 | CreateRepositoryResponse401 | CreateRepositoryResponse409 | RestRepository]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestRepository | Unset = UNSET,
) -> CreateRepositoryResponse400 | CreateRepositoryResponse401 | CreateRepositoryResponse409 | RestRepository | None:
    """Create repository

     Create a new repository. Requires an existing project in which this repository will be created. The
    only parameters which will be used are name and scmId.

    The authenticated user must have <strong>REPO_CREATE</strong> permission or higher, for the context
    project to call this resource.

    Args:
        project_key (str):
        body (RestRepository | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateRepositoryResponse400 | CreateRepositoryResponse401 | CreateRepositoryResponse409 | RestRepository
    """

    return sync_detailed(
        project_key=project_key,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestRepository | Unset = UNSET,
) -> Response[CreateRepositoryResponse400 | CreateRepositoryResponse401 | CreateRepositoryResponse409 | RestRepository]:
    """Create repository

     Create a new repository. Requires an existing project in which this repository will be created. The
    only parameters which will be used are name and scmId.

    The authenticated user must have <strong>REPO_CREATE</strong> permission or higher, for the context
    project to call this resource.

    Args:
        project_key (str):
        body (RestRepository | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateRepositoryResponse400 | CreateRepositoryResponse401 | CreateRepositoryResponse409 | RestRepository]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestRepository | Unset = UNSET,
) -> CreateRepositoryResponse400 | CreateRepositoryResponse401 | CreateRepositoryResponse409 | RestRepository | None:
    """Create repository

     Create a new repository. Requires an existing project in which this repository will be created. The
    only parameters which will be used are name and scmId.

    The authenticated user must have <strong>REPO_CREATE</strong> permission or higher, for the context
    project to call this resource.

    Args:
        project_key (str):
        body (RestRepository | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateRepositoryResponse400 | CreateRepositoryResponse401 | CreateRepositoryResponse409 | RestRepository
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            client=client,
            body=body,
        )
    ).parsed
