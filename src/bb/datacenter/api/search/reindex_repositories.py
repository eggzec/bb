from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.reindex_repositories_response_400 import ReindexRepositoriesResponse400
from ...models.reindex_repositories_response_401 import ReindexRepositoriesResponse401
from ...models.reindex_repositories_response_409 import ReindexRepositoriesResponse409
from ...models.rest_repository_selector import RestRepositorySelector
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: list[RestRepositorySelector] | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/indexing/latest/reindex",
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
) -> Any | ReindexRepositoriesResponse400 | ReindexRepositoriesResponse401 | ReindexRepositoriesResponse409 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = ReindexRepositoriesResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ReindexRepositoriesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 409:
        response_409 = ReindexRepositoriesResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ReindexRepositoriesResponse400 | ReindexRepositoriesResponse401 | ReindexRepositoriesResponse409]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[RestRepositorySelector] | Unset = UNSET,
) -> Response[Any | ReindexRepositoriesResponse400 | ReindexRepositoriesResponse401 | ReindexRepositoriesResponse409]:
    """Re-indexes the search index of the provided list of repositories

     Forces the provided repositories to reindex with the search server. For each repository the current
    index on the search server will be deleted and it will be queued for re-indexing. Note that this can
    result in diminished instance performance as deleting and reindexing a large repository can take
    some time

    Args:
        body (list[RestRepositorySelector] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ReindexRepositoriesResponse400 | ReindexRepositoriesResponse401 | ReindexRepositoriesResponse409]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: list[RestRepositorySelector] | Unset = UNSET,
) -> Any | ReindexRepositoriesResponse400 | ReindexRepositoriesResponse401 | ReindexRepositoriesResponse409 | None:
    """Re-indexes the search index of the provided list of repositories

     Forces the provided repositories to reindex with the search server. For each repository the current
    index on the search server will be deleted and it will be queued for re-indexing. Note that this can
    result in diminished instance performance as deleting and reindexing a large repository can take
    some time

    Args:
        body (list[RestRepositorySelector] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ReindexRepositoriesResponse400 | ReindexRepositoriesResponse401 | ReindexRepositoriesResponse409
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: list[RestRepositorySelector] | Unset = UNSET,
) -> Response[Any | ReindexRepositoriesResponse400 | ReindexRepositoriesResponse401 | ReindexRepositoriesResponse409]:
    """Re-indexes the search index of the provided list of repositories

     Forces the provided repositories to reindex with the search server. For each repository the current
    index on the search server will be deleted and it will be queued for re-indexing. Note that this can
    result in diminished instance performance as deleting and reindexing a large repository can take
    some time

    Args:
        body (list[RestRepositorySelector] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ReindexRepositoriesResponse400 | ReindexRepositoriesResponse401 | ReindexRepositoriesResponse409]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: list[RestRepositorySelector] | Unset = UNSET,
) -> Any | ReindexRepositoriesResponse400 | ReindexRepositoriesResponse401 | ReindexRepositoriesResponse409 | None:
    """Re-indexes the search index of the provided list of repositories

     Forces the provided repositories to reindex with the search server. For each repository the current
    index on the search server will be deleted and it will be queued for re-indexing. Note that this can
    result in diminished instance performance as deleting and reindexing a large repository can take
    some time

    Args:
        body (list[RestRepositorySelector] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ReindexRepositoriesResponse400 | ReindexRepositoriesResponse401 | ReindexRepositoriesResponse409
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
