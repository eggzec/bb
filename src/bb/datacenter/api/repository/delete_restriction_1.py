from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_restriction_1_response_400 import DeleteRestriction1Response400
from ...models.delete_restriction_1_response_401 import DeleteRestriction1Response401
from ...types import Response


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/branch-permissions/latest/projects/{project_key}/repos/{repository_slug}/restrictions/{id}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteRestriction1Response400 | DeleteRestriction1Response401 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = DeleteRestriction1Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DeleteRestriction1Response401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteRestriction1Response400 | DeleteRestriction1Response401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteRestriction1Response400 | DeleteRestriction1Response401]:
    """Delete a ref restriction

     Deletes a restriction as specified by a restriction id.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission or higher to call this
    resource. Only authenticated users may call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteRestriction1Response400 | DeleteRestriction1Response401]
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
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteRestriction1Response400 | DeleteRestriction1Response401 | None:
    """Delete a ref restriction

     Deletes a restriction as specified by a restriction id.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission or higher to call this
    resource. Only authenticated users may call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteRestriction1Response400 | DeleteRestriction1Response401
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
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteRestriction1Response400 | DeleteRestriction1Response401]:
    """Delete a ref restriction

     Deletes a restriction as specified by a restriction id.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission or higher to call this
    resource. Only authenticated users may call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteRestriction1Response400 | DeleteRestriction1Response401]
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
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteRestriction1Response400 | DeleteRestriction1Response401 | None:
    """Delete a ref restriction

     Deletes a restriction as specified by a restriction id.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission or higher to call this
    resource. Only authenticated users may call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteRestriction1Response400 | DeleteRestriction1Response401
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            id=id,
            client=client,
        )
    ).parsed
