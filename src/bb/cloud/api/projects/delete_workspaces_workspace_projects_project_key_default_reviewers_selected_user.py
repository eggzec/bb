from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
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
    project_key: str,
    selected_user: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user}".format(
            workspace=quote(str(workspace), safe=""),
            project_key=quote(str(project_key), safe=""),
            selected_user=quote(str(selected_user), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Any | Error
type ParseResult = Any | Error | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_400 = Error.from_dict(response.json())

        return response_400

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
    selected_user: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Remove the specific user from the project's default reviewers

     Removes a default reviewer from the project.

    Example:
    ```
    $ curl https://api.bitbucket.org/2.0/.../default-
    reviewers/%7Bf0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6%7D

    HTTP/1.1 204
    ```

    Args:
        workspace (str):
        project_key (str):
        selected_user (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        project_key=project_key,
        selected_user=selected_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    project_key: str,
    selected_user: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Remove the specific user from the project's default reviewers

     Removes a default reviewer from the project.

    Example:
    ```
    $ curl https://api.bitbucket.org/2.0/.../default-
    reviewers/%7Bf0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6%7D

    HTTP/1.1 204
    ```

    Args:
        workspace (str):
        project_key (str):
        selected_user (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return sync_detailed(
        workspace=workspace,
        project_key=project_key,
        selected_user=selected_user,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    project_key: str,
    selected_user: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Remove the specific user from the project's default reviewers

     Removes a default reviewer from the project.

    Example:
    ```
    $ curl https://api.bitbucket.org/2.0/.../default-
    reviewers/%7Bf0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6%7D

    HTTP/1.1 204
    ```

    Args:
        workspace (str):
        project_key (str):
        selected_user (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        project_key=project_key,
        selected_user=selected_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    project_key: str,
    selected_user: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Remove the specific user from the project's default reviewers

     Removes a default reviewer from the project.

    Example:
    ```
    $ curl https://api.bitbucket.org/2.0/.../default-
    reviewers/%7Bf0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6%7D

    HTTP/1.1 204
    ```

    Args:
        workspace (str):
        project_key (str):
        selected_user (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            project_key=project_key,
            selected_user=selected_user,
            client=client,
        )
    ).parsed
