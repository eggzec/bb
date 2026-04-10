from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_project_response_400 import CreateProjectResponse400
from ...models.create_project_response_401 import CreateProjectResponse401
from ...models.create_project_response_409 import CreateProjectResponse409
from ...models.rest_project import RestProject
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RestProject | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/projects",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateProjectResponse400 | CreateProjectResponse401 | CreateProjectResponse409 | RestProject | None:
    if response.status_code == 201:
        response_201 = RestProject.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = CreateProjectResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateProjectResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 409:
        response_409 = CreateProjectResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateProjectResponse400 | CreateProjectResponse401 | CreateProjectResponse409 | RestProject]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestProject | Unset = UNSET,
) -> Response[CreateProjectResponse400 | CreateProjectResponse401 | CreateProjectResponse409 | RestProject]:
    """Create a new project

     Create a new project.

    To include a custom avatar for the project, the project definition should contain an additional
    attribute with the key <code>avatar</code> and the value a data URI containing Base64-encoded image
    data. The URI should be in the following format: <pre>    data:(content type, e.g.
    image/png);base64,(data) </pre>If the data is not Base64-encoded, or if a character set is defined
    in the URI, or the URI is otherwise invalid, <em>project creation will fail</em>.

    The authenticated user must have <strong>PROJECT_CREATE</strong> permission to call this resource.

    Args:
        body (RestProject | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateProjectResponse400 | CreateProjectResponse401 | CreateProjectResponse409 | RestProject]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: RestProject | Unset = UNSET,
) -> CreateProjectResponse400 | CreateProjectResponse401 | CreateProjectResponse409 | RestProject | None:
    """Create a new project

     Create a new project.

    To include a custom avatar for the project, the project definition should contain an additional
    attribute with the key <code>avatar</code> and the value a data URI containing Base64-encoded image
    data. The URI should be in the following format: <pre>    data:(content type, e.g.
    image/png);base64,(data) </pre>If the data is not Base64-encoded, or if a character set is defined
    in the URI, or the URI is otherwise invalid, <em>project creation will fail</em>.

    The authenticated user must have <strong>PROJECT_CREATE</strong> permission to call this resource.

    Args:
        body (RestProject | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateProjectResponse400 | CreateProjectResponse401 | CreateProjectResponse409 | RestProject
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RestProject | Unset = UNSET,
) -> Response[CreateProjectResponse400 | CreateProjectResponse401 | CreateProjectResponse409 | RestProject]:
    """Create a new project

     Create a new project.

    To include a custom avatar for the project, the project definition should contain an additional
    attribute with the key <code>avatar</code> and the value a data URI containing Base64-encoded image
    data. The URI should be in the following format: <pre>    data:(content type, e.g.
    image/png);base64,(data) </pre>If the data is not Base64-encoded, or if a character set is defined
    in the URI, or the URI is otherwise invalid, <em>project creation will fail</em>.

    The authenticated user must have <strong>PROJECT_CREATE</strong> permission to call this resource.

    Args:
        body (RestProject | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateProjectResponse400 | CreateProjectResponse401 | CreateProjectResponse409 | RestProject]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RestProject | Unset = UNSET,
) -> CreateProjectResponse400 | CreateProjectResponse401 | CreateProjectResponse409 | RestProject | None:
    """Create a new project

     Create a new project.

    To include a custom avatar for the project, the project definition should contain an additional
    attribute with the key <code>avatar</code> and the value a data URI containing Base64-encoded image
    data. The URI should be in the following format: <pre>    data:(content type, e.g.
    image/png);base64,(data) </pre>If the data is not Base64-encoded, or if a character set is defined
    in the URI, or the URI is otherwise invalid, <em>project creation will fail</em>.

    The authenticated user must have <strong>PROJECT_CREATE</strong> permission to call this resource.

    Args:
        body (RestProject | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateProjectResponse400 | CreateProjectResponse401 | CreateProjectResponse409 | RestProject
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
