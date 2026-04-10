from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.remove_configuration_response_401 import RemoveConfigurationResponse401
from ...models.remove_configuration_response_404 import RemoveConfigurationResponse404
from ...types import Response


def _get_kwargs(
    project_key: str,
    script_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/latest/projects/{project_key}/hook-scripts/{script_id}".format(
            project_key=quote(str(project_key), safe=""),
            script_id=quote(str(script_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RemoveConfigurationResponse401 | RemoveConfigurationResponse404 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = RemoveConfigurationResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = RemoveConfigurationResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RemoveConfigurationResponse401 | RemoveConfigurationResponse404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    script_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | RemoveConfigurationResponse401 | RemoveConfigurationResponse404]:
    """Remove a hook script

     Removes the hook script from the set of hook scripts configured to run in all repositories under the
    project.

    This endpoint requires **PROJECT_ADMIN** permission.

    Args:
        project_key (str):
        script_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RemoveConfigurationResponse401 | RemoveConfigurationResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        script_id=script_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    script_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | RemoveConfigurationResponse401 | RemoveConfigurationResponse404 | None:
    """Remove a hook script

     Removes the hook script from the set of hook scripts configured to run in all repositories under the
    project.

    This endpoint requires **PROJECT_ADMIN** permission.

    Args:
        project_key (str):
        script_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RemoveConfigurationResponse401 | RemoveConfigurationResponse404
    """

    return sync_detailed(
        project_key=project_key,
        script_id=script_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    script_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | RemoveConfigurationResponse401 | RemoveConfigurationResponse404]:
    """Remove a hook script

     Removes the hook script from the set of hook scripts configured to run in all repositories under the
    project.

    This endpoint requires **PROJECT_ADMIN** permission.

    Args:
        project_key (str):
        script_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RemoveConfigurationResponse401 | RemoveConfigurationResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        script_id=script_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    script_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | RemoveConfigurationResponse401 | RemoveConfigurationResponse404 | None:
    """Remove a hook script

     Removes the hook script from the set of hook scripts configured to run in all repositories under the
    project.

    This endpoint requires **PROJECT_ADMIN** permission.

    Args:
        project_key (str):
        script_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RemoveConfigurationResponse401 | RemoveConfigurationResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            script_id=script_id,
            client=client,
        )
    ).parsed
