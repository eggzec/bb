from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_restrictions_1_matcher_type import GetRestrictions1MatcherType
from ...models.get_restrictions_1_response_200 import GetRestrictions1Response200
from ...models.get_restrictions_1_response_400 import GetRestrictions1Response400
from ...models.get_restrictions_1_response_401 import GetRestrictions1Response401
from ...models.get_restrictions_1_response_404 import GetRestrictions1Response404
from ...models.get_restrictions_1_type import GetRestrictions1Type
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    matcher_type: GetRestrictions1MatcherType | Unset = UNSET,
    matcher_id: str | Unset = UNSET,
    type_: GetRestrictions1Type | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_matcher_type: str | Unset = UNSET
    if not isinstance(matcher_type, Unset):
        json_matcher_type = matcher_type.value

    params["matcherType"] = json_matcher_type

    params["matcherId"] = matcher_id

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/branch-permissions/latest/projects/{project_key}/repos/{repository_slug}/restrictions".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetRestrictions1Response200
    | GetRestrictions1Response400
    | GetRestrictions1Response401
    | GetRestrictions1Response404
    | None
):
    if response.status_code == 200:
        response_200 = GetRestrictions1Response200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetRestrictions1Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetRestrictions1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetRestrictions1Response404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetRestrictions1Response200
    | GetRestrictions1Response400
    | GetRestrictions1Response401
    | GetRestrictions1Response404
]:
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
    matcher_type: GetRestrictions1MatcherType | Unset = UNSET,
    matcher_id: str | Unset = UNSET,
    type_: GetRestrictions1Type | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[
    GetRestrictions1Response200
    | GetRestrictions1Response400
    | GetRestrictions1Response401
    | GetRestrictions1Response404
]:
    """Search for ref restrictions

     Search for restrictions using the supplied parameters.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission or higher to call this
    resource. Only authenticated users may call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        matcher_type (GetRestrictions1MatcherType | Unset):
        matcher_id (str | Unset):
        type_ (GetRestrictions1Type | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRestrictions1Response200 | GetRestrictions1Response400 | GetRestrictions1Response401 | GetRestrictions1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        matcher_type=matcher_type,
        matcher_id=matcher_id,
        type_=type_,
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
    matcher_type: GetRestrictions1MatcherType | Unset = UNSET,
    matcher_id: str | Unset = UNSET,
    type_: GetRestrictions1Type | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> (
    GetRestrictions1Response200
    | GetRestrictions1Response400
    | GetRestrictions1Response401
    | GetRestrictions1Response404
    | None
):
    """Search for ref restrictions

     Search for restrictions using the supplied parameters.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission or higher to call this
    resource. Only authenticated users may call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        matcher_type (GetRestrictions1MatcherType | Unset):
        matcher_id (str | Unset):
        type_ (GetRestrictions1Type | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRestrictions1Response200 | GetRestrictions1Response400 | GetRestrictions1Response401 | GetRestrictions1Response404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        client=client,
        matcher_type=matcher_type,
        matcher_id=matcher_id,
        type_=type_,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    matcher_type: GetRestrictions1MatcherType | Unset = UNSET,
    matcher_id: str | Unset = UNSET,
    type_: GetRestrictions1Type | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[
    GetRestrictions1Response200
    | GetRestrictions1Response400
    | GetRestrictions1Response401
    | GetRestrictions1Response404
]:
    """Search for ref restrictions

     Search for restrictions using the supplied parameters.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission or higher to call this
    resource. Only authenticated users may call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        matcher_type (GetRestrictions1MatcherType | Unset):
        matcher_id (str | Unset):
        type_ (GetRestrictions1Type | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRestrictions1Response200 | GetRestrictions1Response400 | GetRestrictions1Response401 | GetRestrictions1Response404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        matcher_type=matcher_type,
        matcher_id=matcher_id,
        type_=type_,
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
    matcher_type: GetRestrictions1MatcherType | Unset = UNSET,
    matcher_id: str | Unset = UNSET,
    type_: GetRestrictions1Type | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> (
    GetRestrictions1Response200
    | GetRestrictions1Response400
    | GetRestrictions1Response401
    | GetRestrictions1Response404
    | None
):
    """Search for ref restrictions

     Search for restrictions using the supplied parameters.

    The authenticated user must have <strong>REPO_ADMIN</strong> permission or higher to call this
    resource. Only authenticated users may call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        matcher_type (GetRestrictions1MatcherType | Unset):
        matcher_id (str | Unset):
        type_ (GetRestrictions1Type | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRestrictions1Response200 | GetRestrictions1Response400 | GetRestrictions1Response401 | GetRestrictions1Response404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            matcher_type=matcher_type,
            matcher_id=matcher_id,
            type_=type_,
            start=start,
            limit=limit,
        )
    ).parsed
