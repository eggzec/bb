from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_add_exempt_repositories_1_response_401 import BulkAddExemptRepositories1Response401
from ...models.rest_repository_selector import RestRepositorySelector
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    *,
    body: list[RestRepositorySelector] | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/projects/{project_key}/secret-scanning/exempt".format(
            project_key=quote(str(project_key), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = []
        for body_item_data in body:
            body_item = body_item_data.to_dict()
            _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BulkAddExemptRepositories1Response401 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = BulkAddExemptRepositories1Response401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | BulkAddExemptRepositories1Response401]:
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
    body: list[RestRepositorySelector] | Unset = UNSET,
) -> Response[Any | BulkAddExemptRepositories1Response401]:
    """Bulk exempt repos from secret scanning

     Bulk exempt a  list of repositories from being scanned for secrets. User must be have **PROJECT
    ADMIN** permissions.

    Args:
        project_key (str):
        body (list[RestRepositorySelector] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BulkAddExemptRepositories1Response401]
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
    body: list[RestRepositorySelector] | Unset = UNSET,
) -> Any | BulkAddExemptRepositories1Response401 | None:
    """Bulk exempt repos from secret scanning

     Bulk exempt a  list of repositories from being scanned for secrets. User must be have **PROJECT
    ADMIN** permissions.

    Args:
        project_key (str):
        body (list[RestRepositorySelector] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BulkAddExemptRepositories1Response401
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
    body: list[RestRepositorySelector] | Unset = UNSET,
) -> Response[Any | BulkAddExemptRepositories1Response401]:
    """Bulk exempt repos from secret scanning

     Bulk exempt a  list of repositories from being scanned for secrets. User must be have **PROJECT
    ADMIN** permissions.

    Args:
        project_key (str):
        body (list[RestRepositorySelector] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BulkAddExemptRepositories1Response401]
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
    body: list[RestRepositorySelector] | Unset = UNSET,
) -> Any | BulkAddExemptRepositories1Response401 | None:
    """Bulk exempt repos from secret scanning

     Bulk exempt a  list of repositories from being scanned for secrets. User must be have **PROJECT
    ADMIN** permissions.

    Args:
        project_key (str):
        body (list[RestRepositorySelector] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BulkAddExemptRepositories1Response401
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            client=client,
            body=body,
        )
    ).parsed
