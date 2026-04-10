from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rest_project import RestProject
from ...models.update_project_response_400 import UpdateProjectResponse400
from ...models.update_project_response_401 import UpdateProjectResponse401
from ...models.update_project_response_404 import UpdateProjectResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    *,
    body: RestProject | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/projects/{project_key}".format(
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
) -> RestProject | UpdateProjectResponse400 | UpdateProjectResponse401 | UpdateProjectResponse404 | None:
    if response.status_code == 200:
        response_200 = RestProject.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = RestProject.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = UpdateProjectResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UpdateProjectResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = UpdateProjectResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RestProject | UpdateProjectResponse400 | UpdateProjectResponse401 | UpdateProjectResponse404]:
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
    body: RestProject | Unset = UNSET,
) -> Response[RestProject | UpdateProjectResponse400 | UpdateProjectResponse401 | UpdateProjectResponse404]:
    """Update project

     Update the project matching the <strong>projectKey</strong> supplied in the resource path.

    To include a custom avatar for the updated project, the project definition should contain an
    additional attribute with the key <code>avatar</code> and the value a data URI containing
    Base64-encoded image data. The URI should be in the following format:
    ```    data:(content type, e.g. image/png);base64,(data)```

    If the data is not Base64-encoded, or if a character set is defined in the URI, or the URI is
    otherwise invalid, <em>project creation will fail</em>.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        body (RestProject | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestProject | UpdateProjectResponse400 | UpdateProjectResponse401 | UpdateProjectResponse404]
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
    body: RestProject | Unset = UNSET,
) -> RestProject | UpdateProjectResponse400 | UpdateProjectResponse401 | UpdateProjectResponse404 | None:
    """Update project

     Update the project matching the <strong>projectKey</strong> supplied in the resource path.

    To include a custom avatar for the updated project, the project definition should contain an
    additional attribute with the key <code>avatar</code> and the value a data URI containing
    Base64-encoded image data. The URI should be in the following format:
    ```    data:(content type, e.g. image/png);base64,(data)```

    If the data is not Base64-encoded, or if a character set is defined in the URI, or the URI is
    otherwise invalid, <em>project creation will fail</em>.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        body (RestProject | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestProject | UpdateProjectResponse400 | UpdateProjectResponse401 | UpdateProjectResponse404
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
    body: RestProject | Unset = UNSET,
) -> Response[RestProject | UpdateProjectResponse400 | UpdateProjectResponse401 | UpdateProjectResponse404]:
    """Update project

     Update the project matching the <strong>projectKey</strong> supplied in the resource path.

    To include a custom avatar for the updated project, the project definition should contain an
    additional attribute with the key <code>avatar</code> and the value a data URI containing
    Base64-encoded image data. The URI should be in the following format:
    ```    data:(content type, e.g. image/png);base64,(data)```

    If the data is not Base64-encoded, or if a character set is defined in the URI, or the URI is
    otherwise invalid, <em>project creation will fail</em>.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        body (RestProject | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestProject | UpdateProjectResponse400 | UpdateProjectResponse401 | UpdateProjectResponse404]
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
    body: RestProject | Unset = UNSET,
) -> RestProject | UpdateProjectResponse400 | UpdateProjectResponse401 | UpdateProjectResponse404 | None:
    """Update project

     Update the project matching the <strong>projectKey</strong> supplied in the resource path.

    To include a custom avatar for the updated project, the project definition should contain an
    additional attribute with the key <code>avatar</code> and the value a data URI containing
    Base64-encoded image data. The URI should be in the following format:
    ```    data:(content type, e.g. image/png);base64,(data)```

    If the data is not Base64-encoded, or if a character set is defined in the URI, or the URI is
    otherwise invalid, <em>project creation will fail</em>.

    The authenticated user must have <strong>PROJECT_ADMIN</strong> permission for the specified project
    to call this resource.

    Args:
        project_key (str):
        body (RestProject | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestProject | UpdateProjectResponse400 | UpdateProjectResponse401 | UpdateProjectResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            client=client,
            body=body,
        )
    ).parsed
