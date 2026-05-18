from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.project import Project
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    workspace: str,
    project_key: str,
    *,
    body: Project,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/workspaces/{workspace}/projects/{project_key}".format(
            workspace=quote(str(workspace), safe=""),
            project_key=quote(str(project_key), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Error | Project
type ParseResult = Error | Project | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = Project.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_201 = Project.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_401 = Error.from_dict(response.json())

        return response_401

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
    project_key: str,
    *,
    client: AuthenticatedClient,
    body: Project,
) -> Response[ParsedPayload]:
    """Update a project for a workspace

     Since this endpoint can be used to both update and to create a
    project, the request body depends on the intent.

    #### Creation

    See the POST documentation for the project collection for an
    example of the request body.

    Note: The `key` should not be specified in the body of request
    (since it is already present in the URL). The `name` is required,
    everything else is optional.

    #### Update

    See the POST documentation for the project collection for an
    example of the request body.

    Note: The key is not required in the body (since it is already in
    the URL). The key may be specified in the body, if the intent is
    to change the key itself. In such a scenario, the location of the
    project is changed and is returned in the `Location` header of the
    response.

    Args:
        workspace (str):
        project_key (str):
        body (Project):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Project]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        project_key=project_key,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    project_key: str,
    *,
    client: AuthenticatedClient,
    body: Project,
) -> ParsedPayload | None:
    """Update a project for a workspace

     Since this endpoint can be used to both update and to create a
    project, the request body depends on the intent.

    #### Creation

    See the POST documentation for the project collection for an
    example of the request body.

    Note: The `key` should not be specified in the body of request
    (since it is already present in the URL). The `name` is required,
    everything else is optional.

    #### Update

    See the POST documentation for the project collection for an
    example of the request body.

    Note: The key is not required in the body (since it is already in
    the URL). The key may be specified in the body, if the intent is
    to change the key itself. In such a scenario, the location of the
    project is changed and is returned in the `Location` header of the
    response.

    Args:
        workspace (str):
        project_key (str):
        body (Project):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Project
    """

    return sync_detailed(
        workspace=workspace,
        project_key=project_key,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    project_key: str,
    *,
    client: AuthenticatedClient,
    body: Project,
) -> Response[ParsedPayload]:
    """Update a project for a workspace

     Since this endpoint can be used to both update and to create a
    project, the request body depends on the intent.

    #### Creation

    See the POST documentation for the project collection for an
    example of the request body.

    Note: The `key` should not be specified in the body of request
    (since it is already present in the URL). The `name` is required,
    everything else is optional.

    #### Update

    See the POST documentation for the project collection for an
    example of the request body.

    Note: The key is not required in the body (since it is already in
    the URL). The key may be specified in the body, if the intent is
    to change the key itself. In such a scenario, the location of the
    project is changed and is returned in the `Location` header of the
    response.

    Args:
        workspace (str):
        project_key (str):
        body (Project):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Project]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        project_key=project_key,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    project_key: str,
    *,
    client: AuthenticatedClient,
    body: Project,
) -> ParsedPayload | None:
    """Update a project for a workspace

     Since this endpoint can be used to both update and to create a
    project, the request body depends on the intent.

    #### Creation

    See the POST documentation for the project collection for an
    example of the request body.

    Note: The `key` should not be specified in the body of request
    (since it is already present in the URL). The `name` is required,
    everything else is optional.

    #### Update

    See the POST documentation for the project collection for an
    example of the request body.

    Note: The key is not required in the body (since it is already in
    the URL). The key may be specified in the body, if the intent is
    to change the key itself. In such a scenario, the location of the
    project is changed and is returned in the `Location` header of the
    response.

    Args:
        workspace (str):
        project_key (str):
        body (Project):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Project
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            project_key=project_key,
            client=client,
            body=body,
        )
    ).parsed
