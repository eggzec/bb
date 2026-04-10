from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_required_builds_merge_check_response_401 import DeleteRequiredBuildsMergeCheckResponse401
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/required-builds/latest/projects/{project_key}/repos/{repository_slug}/condition/{id}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteRequiredBuildsMergeCheckResponse401 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = DeleteRequiredBuildsMergeCheckResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteRequiredBuildsMergeCheckResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteRequiredBuildsMergeCheckResponse401]:
    """Delete a required builds merge check

     Deletes a required build existing merge check, given it's ID.

    The authenticated user must have **REPO_ADMIN** permission for the target repository to delete a
    required build merge check.

    Args:
        project_key (str):
        repository_slug (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteRequiredBuildsMergeCheckResponse401]
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
    id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteRequiredBuildsMergeCheckResponse401 | None:
    """Delete a required builds merge check

     Deletes a required build existing merge check, given it's ID.

    The authenticated user must have **REPO_ADMIN** permission for the target repository to delete a
    required build merge check.

    Args:
        project_key (str):
        repository_slug (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteRequiredBuildsMergeCheckResponse401
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
    id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteRequiredBuildsMergeCheckResponse401]:
    """Delete a required builds merge check

     Deletes a required build existing merge check, given it's ID.

    The authenticated user must have **REPO_ADMIN** permission for the target repository to delete a
    required build merge check.

    Args:
        project_key (str):
        repository_slug (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteRequiredBuildsMergeCheckResponse401]
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
    id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteRequiredBuildsMergeCheckResponse401 | None:
    """Delete a required builds merge check

     Deletes a required build existing merge check, given it's ID.

    The authenticated user must have **REPO_ADMIN** permission for the target repository to delete a
    required build merge check.

    Args:
        project_key (str):
        repository_slug (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteRequiredBuildsMergeCheckResponse401
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            id=id,
            client=client,
        )
    ).parsed
