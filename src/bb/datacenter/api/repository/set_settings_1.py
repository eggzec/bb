from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.example_settings import ExampleSettings
from ...models.set_settings_1_response_400 import SetSettings1Response400
from ...models.set_settings_1_response_401 import SetSettings1Response401
from ...models.set_settings_1_response_404 import SetSettings1Response404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    hook_key: str,
    *,
    body: ExampleSettings | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/settings/hooks/{hook_key}/settings".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            hook_key=quote(str(hook_key), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExampleSettings | SetSettings1Response400 | SetSettings1Response401 | SetSettings1Response404 | None:
    if response.status_code == 200:
        response_200 = ExampleSettings.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = SetSettings1Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SetSettings1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = SetSettings1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ExampleSettings | SetSettings1Response400 | SetSettings1Response401 | SetSettings1Response404]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    hook_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExampleSettings | Unset = UNSET,
) -> Response[ExampleSettings | SetSettings1Response400 | SetSettings1Response401 | SetSettings1Response404]:
    """Update repository hook settings

     Modify the settings for a repository hook for this repository.

    The service will reject any settings which are too large, the current limit is 32KB once serialized.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    A JSON document can be provided to use as the settings for the hook. These structure and validity of
    the document is decided by the plugin providing the hook.

    Args:
        project_key (str):
        repository_slug (str):
        hook_key (str):
        body (ExampleSettings | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExampleSettings | SetSettings1Response400 | SetSettings1Response401 | SetSettings1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        hook_key=hook_key,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    hook_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExampleSettings | Unset = UNSET,
) -> ExampleSettings | SetSettings1Response400 | SetSettings1Response401 | SetSettings1Response404 | None:
    """Update repository hook settings

     Modify the settings for a repository hook for this repository.

    The service will reject any settings which are too large, the current limit is 32KB once serialized.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    A JSON document can be provided to use as the settings for the hook. These structure and validity of
    the document is decided by the plugin providing the hook.

    Args:
        project_key (str):
        repository_slug (str):
        hook_key (str):
        body (ExampleSettings | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExampleSettings | SetSettings1Response400 | SetSettings1Response401 | SetSettings1Response404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        hook_key=hook_key,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    hook_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExampleSettings | Unset = UNSET,
) -> Response[ExampleSettings | SetSettings1Response400 | SetSettings1Response401 | SetSettings1Response404]:
    """Update repository hook settings

     Modify the settings for a repository hook for this repository.

    The service will reject any settings which are too large, the current limit is 32KB once serialized.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    A JSON document can be provided to use as the settings for the hook. These structure and validity of
    the document is decided by the plugin providing the hook.

    Args:
        project_key (str):
        repository_slug (str):
        hook_key (str):
        body (ExampleSettings | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExampleSettings | SetSettings1Response400 | SetSettings1Response401 | SetSettings1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        hook_key=hook_key,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    hook_key: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExampleSettings | Unset = UNSET,
) -> ExampleSettings | SetSettings1Response400 | SetSettings1Response401 | SetSettings1Response404 | None:
    """Update repository hook settings

     Modify the settings for a repository hook for this repository.

    The service will reject any settings which are too large, the current limit is 32KB once serialized.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission for the specified repository
    to call this resource.

    A JSON document can be provided to use as the settings for the hook. These structure and validity of
    the document is decided by the plugin providing the hook.

    Args:
        project_key (str):
        repository_slug (str):
        hook_key (str):
        body (ExampleSettings | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExampleSettings | SetSettings1Response400 | SetSettings1Response401 | SetSettings1Response404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            hook_key=hook_key,
            client=client,
            body=body,
        )
    ).parsed
