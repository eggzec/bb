from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_branches_order_by import GetBranchesOrderBy
from ...models.get_branches_response_200 import GetBranchesResponse200
from ...models.get_branches_response_401 import GetBranchesResponse401
from ...models.get_branches_response_404 import GetBranchesResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    boost_matches: bool | Unset = UNSET,
    context: str | Unset = UNSET,
    order_by: GetBranchesOrderBy | Unset = UNSET,
    details: bool | Unset = UNSET,
    filter_text: str | Unset = UNSET,
    base: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["boostMatches"] = boost_matches

    params["context"] = context

    json_order_by: str | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["orderBy"] = json_order_by

    params["details"] = details

    params["filterText"] = filter_text

    params["base"] = base

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/branches".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetBranchesResponse200 | GetBranchesResponse401 | GetBranchesResponse404 | None:
    if response.status_code == 200:
        response_200 = GetBranchesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = GetBranchesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetBranchesResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetBranchesResponse200 | GetBranchesResponse401 | GetBranchesResponse404]:
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
    boost_matches: bool | Unset = UNSET,
    context: str | Unset = UNSET,
    order_by: GetBranchesOrderBy | Unset = UNSET,
    details: bool | Unset = UNSET,
    filter_text: str | Unset = UNSET,
    base: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetBranchesResponse200 | GetBranchesResponse401 | GetBranchesResponse404]:
    """Find branches

     Retrieve the branches matching the supplied <strong>filterText</strong> param.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        boost_matches (bool | Unset):
        context (str | Unset):
        order_by (GetBranchesOrderBy | Unset):
        details (bool | Unset):
        filter_text (str | Unset):
        base (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBranchesResponse200 | GetBranchesResponse401 | GetBranchesResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        boost_matches=boost_matches,
        context=context,
        order_by=order_by,
        details=details,
        filter_text=filter_text,
        base=base,
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
    boost_matches: bool | Unset = UNSET,
    context: str | Unset = UNSET,
    order_by: GetBranchesOrderBy | Unset = UNSET,
    details: bool | Unset = UNSET,
    filter_text: str | Unset = UNSET,
    base: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetBranchesResponse200 | GetBranchesResponse401 | GetBranchesResponse404 | None:
    """Find branches

     Retrieve the branches matching the supplied <strong>filterText</strong> param.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        boost_matches (bool | Unset):
        context (str | Unset):
        order_by (GetBranchesOrderBy | Unset):
        details (bool | Unset):
        filter_text (str | Unset):
        base (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBranchesResponse200 | GetBranchesResponse401 | GetBranchesResponse404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        client=client,
        boost_matches=boost_matches,
        context=context,
        order_by=order_by,
        details=details,
        filter_text=filter_text,
        base=base,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    boost_matches: bool | Unset = UNSET,
    context: str | Unset = UNSET,
    order_by: GetBranchesOrderBy | Unset = UNSET,
    details: bool | Unset = UNSET,
    filter_text: str | Unset = UNSET,
    base: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetBranchesResponse200 | GetBranchesResponse401 | GetBranchesResponse404]:
    """Find branches

     Retrieve the branches matching the supplied <strong>filterText</strong> param.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        boost_matches (bool | Unset):
        context (str | Unset):
        order_by (GetBranchesOrderBy | Unset):
        details (bool | Unset):
        filter_text (str | Unset):
        base (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBranchesResponse200 | GetBranchesResponse401 | GetBranchesResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        boost_matches=boost_matches,
        context=context,
        order_by=order_by,
        details=details,
        filter_text=filter_text,
        base=base,
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
    boost_matches: bool | Unset = UNSET,
    context: str | Unset = UNSET,
    order_by: GetBranchesOrderBy | Unset = UNSET,
    details: bool | Unset = UNSET,
    filter_text: str | Unset = UNSET,
    base: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetBranchesResponse200 | GetBranchesResponse401 | GetBranchesResponse404 | None:
    """Find branches

     Retrieve the branches matching the supplied <strong>filterText</strong> param.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        boost_matches (bool | Unset):
        context (str | Unset):
        order_by (GetBranchesOrderBy | Unset):
        details (bool | Unset):
        filter_text (str | Unset):
        base (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBranchesResponse200 | GetBranchesResponse401 | GetBranchesResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            boost_matches=boost_matches,
            context=context,
            order_by=order_by,
            details=details,
            filter_text=filter_text,
            base=base,
            start=start,
            limit=limit,
        )
    ).parsed
