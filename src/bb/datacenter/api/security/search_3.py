from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_3_order import Search3Order
from ...models.search_3_response_200 import Search3Response200
from ...models.search_3_response_400 import Search3Response400
from ...models.search_3_response_401 import Search3Response401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    filter_: str | Unset = UNSET,
    order: Search3Order | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["filter"] = filter_

    json_order: str | Unset = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/secret-scanning/rules".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Search3Response200 | Search3Response400 | Search3Response401 | None:
    if response.status_code == 200:
        response_200 = Search3Response200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Search3Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Search3Response401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Search3Response200 | Search3Response400 | Search3Response401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    order: Search3Order | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[Search3Response200 | Search3Response400 | Search3Response401]:
    """Find repository secret scanning rules

     Find repository secret scanning rules by filtering.

    Repository **Admin** is required

    Args:
        project_key (str):
        repository_slug (str):
        filter_ (str | Unset):
        order (Search3Order | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Search3Response200 | Search3Response400 | Search3Response401]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        filter_=filter_,
        order=order,
        start=start,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    order: Search3Order | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Search3Response200 | Search3Response400 | Search3Response401 | None:
    """Find repository secret scanning rules

     Find repository secret scanning rules by filtering.

    Repository **Admin** is required

    Args:
        project_key (str):
        repository_slug (str):
        filter_ (str | Unset):
        order (Search3Order | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Search3Response200 | Search3Response400 | Search3Response401
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        client=client,
        filter_=filter_,
        order=order,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    order: Search3Order | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[Search3Response200 | Search3Response400 | Search3Response401]:
    """Find repository secret scanning rules

     Find repository secret scanning rules by filtering.

    Repository **Admin** is required

    Args:
        project_key (str):
        repository_slug (str):
        filter_ (str | Unset):
        order (Search3Order | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Search3Response200 | Search3Response400 | Search3Response401]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        filter_=filter_,
        order=order,
        start=start,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    filter_: str | Unset = UNSET,
    order: Search3Order | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Search3Response200 | Search3Response400 | Search3Response401 | None:
    """Find repository secret scanning rules

     Find repository secret scanning rules by filtering.

    Repository **Admin** is required

    Args:
        project_key (str):
        repository_slug (str):
        filter_ (str | Unset):
        order (Search3Order | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Search3Response200 | Search3Response400 | Search3Response401
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            filter_=filter_,
            order=order,
            start=start,
            limit=limit,
        )
    ).parsed
