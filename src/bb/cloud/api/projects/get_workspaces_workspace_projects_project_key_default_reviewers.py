from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.paginated_default_reviewer_and_type import PaginatedDefaultReviewerAndType
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
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/workspaces/{workspace}/projects/{project_key}/default-reviewers".format(
            workspace=quote(str(workspace), safe=""),
            project_key=quote(str(project_key), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Error | PaginatedDefaultReviewerAndType
type ParseResult = Error | PaginatedDefaultReviewerAndType | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = PaginatedDefaultReviewerAndType.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
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
) -> Response[ParsedPayload]:
    """List the default reviewers in a project

     Return a list of all default reviewers for a project. This is a list of users that will be added as
    default
    reviewers to pull requests for any repository within the project.

    Args:
        workspace (str):
        project_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedDefaultReviewerAndType]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        project_key=project_key,
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
) -> ParsedPayload | None:
    """List the default reviewers in a project

     Return a list of all default reviewers for a project. This is a list of users that will be added as
    default
    reviewers to pull requests for any repository within the project.

    Args:
        workspace (str):
        project_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedDefaultReviewerAndType
    """

    return sync_detailed(
        workspace=workspace,
        project_key=project_key,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    project_key: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """List the default reviewers in a project

     Return a list of all default reviewers for a project. This is a list of users that will be added as
    default
    reviewers to pull requests for any repository within the project.

    Args:
        workspace (str):
        project_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedDefaultReviewerAndType]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        project_key=project_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    project_key: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """List the default reviewers in a project

     Return a list of all default reviewers for a project. This is a list of users that will be added as
    default
    reviewers to pull requests for any repository within the project.

    Args:
        workspace (str):
        project_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedDefaultReviewerAndType
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            project_key=project_key,
            client=client,
        )
    ).parsed
