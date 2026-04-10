from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...deprecation import deprecated_endpoint
from ...models.add_exempt_repo_response_401 import AddExemptRepoResponse401
from ...models.add_exempt_repo_response_409 import AddExemptRepoResponse409
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/secret-scanning/exempt".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AddExemptRepoResponse401 | AddExemptRepoResponse409 | Any | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = AddExemptRepoResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 409:
        response_409 = AddExemptRepoResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AddExemptRepoResponse401 | AddExemptRepoResponse409 | Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


@deprecated_endpoint(None)
def sync_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AddExemptRepoResponse401 | AddExemptRepoResponse409 | Any]:
    """Exempt a repo from secret scanning

     Exempt a repository from being scanned for secrets

    <strong>Deprecated since 8.6</strong>. Exemptions are now managed by scope.
    Use POST /rest/api/1.0/secret-scanning/exempt for global scope
    Use POST /rest/api/1.0/projects/{projectKey}/secret-scanning/exempt for the project scope

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddExemptRepoResponse401 | AddExemptRepoResponse409 | Any]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


@deprecated_endpoint(None)
def sync(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> AddExemptRepoResponse401 | AddExemptRepoResponse409 | Any | None:
    """Exempt a repo from secret scanning

     Exempt a repository from being scanned for secrets

    <strong>Deprecated since 8.6</strong>. Exemptions are now managed by scope.
    Use POST /rest/api/1.0/secret-scanning/exempt for global scope
    Use POST /rest/api/1.0/projects/{projectKey}/secret-scanning/exempt for the project scope

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddExemptRepoResponse401 | AddExemptRepoResponse409 | Any
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        client=client,
    ).parsed


@deprecated_endpoint(None)
async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AddExemptRepoResponse401 | AddExemptRepoResponse409 | Any]:
    """Exempt a repo from secret scanning

     Exempt a repository from being scanned for secrets

    <strong>Deprecated since 8.6</strong>. Exemptions are now managed by scope.
    Use POST /rest/api/1.0/secret-scanning/exempt for global scope
    Use POST /rest/api/1.0/projects/{projectKey}/secret-scanning/exempt for the project scope

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddExemptRepoResponse401 | AddExemptRepoResponse409 | Any]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


@deprecated_endpoint(None)
async def asyncio(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
) -> AddExemptRepoResponse401 | AddExemptRepoResponse409 | Any | None:
    """Exempt a repo from secret scanning

     Exempt a repository from being scanned for secrets

    <strong>Deprecated since 8.6</strong>. Exemptions are now managed by scope.
    Use POST /rest/api/1.0/secret-scanning/exempt for global scope
    Use POST /rest/api/1.0/projects/{projectKey}/secret-scanning/exempt for the project scope

    Args:
        project_key (str):
        repository_slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddExemptRepoResponse401 | AddExemptRepoResponse409 | Any
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
        )
    ).parsed
