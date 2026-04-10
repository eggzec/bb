from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.revoke_for_repository_response_401 import RevokeForRepositoryResponse401
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    key_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/keys/latest/projects/{project_key}/repos/{repository_slug}/ssh/{key_id}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            key_id=quote(str(key_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | RevokeForRepositoryResponse401 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = RevokeForRepositoryResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | RevokeForRepositoryResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    key_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | RevokeForRepositoryResponse401]:
    """Revoke repository SSH key

     Remove an existing access key for the repository identified in the URL. If the same SSH key is used
    as an access key for multiple projects or repositories, only the access to the repository identified
    in the URL will be revoked.

    Args:
        project_key (str):
        repository_slug (str):
        key_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RevokeForRepositoryResponse401]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        key_id=key_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    key_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | RevokeForRepositoryResponse401 | None:
    """Revoke repository SSH key

     Remove an existing access key for the repository identified in the URL. If the same SSH key is used
    as an access key for multiple projects or repositories, only the access to the repository identified
    in the URL will be revoked.

    Args:
        project_key (str):
        repository_slug (str):
        key_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RevokeForRepositoryResponse401
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        key_id=key_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    key_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | RevokeForRepositoryResponse401]:
    """Revoke repository SSH key

     Remove an existing access key for the repository identified in the URL. If the same SSH key is used
    as an access key for multiple projects or repositories, only the access to the repository identified
    in the URL will be revoked.

    Args:
        project_key (str):
        repository_slug (str):
        key_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | RevokeForRepositoryResponse401]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        key_id=key_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    key_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | RevokeForRepositoryResponse401 | None:
    """Revoke repository SSH key

     Remove an existing access key for the repository identified in the URL. If the same SSH key is used
    as an access key for multiple projects or repositories, only the access to the repository identified
    in the URL will be revoked.

    Args:
        project_key (str):
        repository_slug (str):
        key_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | RevokeForRepositoryResponse401
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            key_id=key_id,
            client=client,
        )
    ).parsed
