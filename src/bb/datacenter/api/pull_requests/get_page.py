from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_page_response_200 import GetPageResponse200
from ...models.get_page_response_400 import GetPageResponse400
from ...models.get_page_response_401 import GetPageResponse401
from ...models.get_page_response_404 import GetPageResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    with_attributes: str | Unset = UNSET,
    at: str | Unset = UNSET,
    with_properties: str | Unset = UNSET,
    draft: str | Unset = UNSET,
    filter_text: str | Unset = UNSET,
    state: str | Unset = UNSET,
    order: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["withAttributes"] = with_attributes

    params["at"] = at

    params["withProperties"] = with_properties

    params["draft"] = draft

    params["filterText"] = filter_text

    params["state"] = state

    params["order"] = order

    params["direction"] = direction

    params["start"] = start

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/pull-requests".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetPageResponse200 | GetPageResponse400 | GetPageResponse401 | GetPageResponse404 | None:
    if response.status_code == 200:
        response_200 = GetPageResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetPageResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetPageResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetPageResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetPageResponse200 | GetPageResponse400 | GetPageResponse401 | GetPageResponse404]:
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
    with_attributes: str | Unset = UNSET,
    at: str | Unset = UNSET,
    with_properties: str | Unset = UNSET,
    draft: str | Unset = UNSET,
    filter_text: str | Unset = UNSET,
    state: str | Unset = UNSET,
    order: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetPageResponse200 | GetPageResponse400 | GetPageResponse401 | GetPageResponse404]:
    r"""Get pull requests for repository

     Retrieve a page of pull requests to or from the specified repository.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.  Optionally clients can specify PR participant filters. Each filter has a
    mandatory username.N parameter, and the optional role.N and approved.N parameters.

    - username.N - the \"root\" of a single participant filter, where \"N\" is a natural number
    starting from 1. This allows clients to specify multiple participant filters, by providing
    consecutive   filters as username.1, username.2 etc. Note that the filters numbering has to start
    with 1 and be continuous for all filters to be processed. The total allowed number of participant
    filters is 10 and all filters exceeding that limit will be dropped.
    - role.N(optional) the role associated with username.N.   This must be one of AUTHOR, REVIEWER, or
    PARTICIPANT
    - approved.N (optional) the approved status associated with username.N.   That is whether username.N
    has approved the PR. Either true, or false

    Args:
        project_key (str):
        repository_slug (str):
        with_attributes (str | Unset):
        at (str | Unset):
        with_properties (str | Unset):
        draft (str | Unset):
        filter_text (str | Unset):
        state (str | Unset):
        order (str | Unset):
        direction (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPageResponse200 | GetPageResponse400 | GetPageResponse401 | GetPageResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        with_attributes=with_attributes,
        at=at,
        with_properties=with_properties,
        draft=draft,
        filter_text=filter_text,
        state=state,
        order=order,
        direction=direction,
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
    with_attributes: str | Unset = UNSET,
    at: str | Unset = UNSET,
    with_properties: str | Unset = UNSET,
    draft: str | Unset = UNSET,
    filter_text: str | Unset = UNSET,
    state: str | Unset = UNSET,
    order: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetPageResponse200 | GetPageResponse400 | GetPageResponse401 | GetPageResponse404 | None:
    r"""Get pull requests for repository

     Retrieve a page of pull requests to or from the specified repository.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.  Optionally clients can specify PR participant filters. Each filter has a
    mandatory username.N parameter, and the optional role.N and approved.N parameters.

    - username.N - the \"root\" of a single participant filter, where \"N\" is a natural number
    starting from 1. This allows clients to specify multiple participant filters, by providing
    consecutive   filters as username.1, username.2 etc. Note that the filters numbering has to start
    with 1 and be continuous for all filters to be processed. The total allowed number of participant
    filters is 10 and all filters exceeding that limit will be dropped.
    - role.N(optional) the role associated with username.N.   This must be one of AUTHOR, REVIEWER, or
    PARTICIPANT
    - approved.N (optional) the approved status associated with username.N.   That is whether username.N
    has approved the PR. Either true, or false

    Args:
        project_key (str):
        repository_slug (str):
        with_attributes (str | Unset):
        at (str | Unset):
        with_properties (str | Unset):
        draft (str | Unset):
        filter_text (str | Unset):
        state (str | Unset):
        order (str | Unset):
        direction (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPageResponse200 | GetPageResponse400 | GetPageResponse401 | GetPageResponse404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        client=client,
        with_attributes=with_attributes,
        at=at,
        with_properties=with_properties,
        draft=draft,
        filter_text=filter_text,
        state=state,
        order=order,
        direction=direction,
        start=start,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    with_attributes: str | Unset = UNSET,
    at: str | Unset = UNSET,
    with_properties: str | Unset = UNSET,
    draft: str | Unset = UNSET,
    filter_text: str | Unset = UNSET,
    state: str | Unset = UNSET,
    order: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> Response[GetPageResponse200 | GetPageResponse400 | GetPageResponse401 | GetPageResponse404]:
    r"""Get pull requests for repository

     Retrieve a page of pull requests to or from the specified repository.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.  Optionally clients can specify PR participant filters. Each filter has a
    mandatory username.N parameter, and the optional role.N and approved.N parameters.

    - username.N - the \"root\" of a single participant filter, where \"N\" is a natural number
    starting from 1. This allows clients to specify multiple participant filters, by providing
    consecutive   filters as username.1, username.2 etc. Note that the filters numbering has to start
    with 1 and be continuous for all filters to be processed. The total allowed number of participant
    filters is 10 and all filters exceeding that limit will be dropped.
    - role.N(optional) the role associated with username.N.   This must be one of AUTHOR, REVIEWER, or
    PARTICIPANT
    - approved.N (optional) the approved status associated with username.N.   That is whether username.N
    has approved the PR. Either true, or false

    Args:
        project_key (str):
        repository_slug (str):
        with_attributes (str | Unset):
        at (str | Unset):
        with_properties (str | Unset):
        draft (str | Unset):
        filter_text (str | Unset):
        state (str | Unset):
        order (str | Unset):
        direction (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPageResponse200 | GetPageResponse400 | GetPageResponse401 | GetPageResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        with_attributes=with_attributes,
        at=at,
        with_properties=with_properties,
        draft=draft,
        filter_text=filter_text,
        state=state,
        order=order,
        direction=direction,
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
    with_attributes: str | Unset = UNSET,
    at: str | Unset = UNSET,
    with_properties: str | Unset = UNSET,
    draft: str | Unset = UNSET,
    filter_text: str | Unset = UNSET,
    state: str | Unset = UNSET,
    order: str | Unset = UNSET,
    direction: str | Unset = UNSET,
    start: float | Unset = UNSET,
    limit: float | Unset = UNSET,
) -> GetPageResponse200 | GetPageResponse400 | GetPageResponse401 | GetPageResponse404 | None:
    r"""Get pull requests for repository

     Retrieve a page of pull requests to or from the specified repository.

    The authenticated user must have <strong>REPO_READ</strong> permission for the specified repository
    to call this resource.  Optionally clients can specify PR participant filters. Each filter has a
    mandatory username.N parameter, and the optional role.N and approved.N parameters.

    - username.N - the \"root\" of a single participant filter, where \"N\" is a natural number
    starting from 1. This allows clients to specify multiple participant filters, by providing
    consecutive   filters as username.1, username.2 etc. Note that the filters numbering has to start
    with 1 and be continuous for all filters to be processed. The total allowed number of participant
    filters is 10 and all filters exceeding that limit will be dropped.
    - role.N(optional) the role associated with username.N.   This must be one of AUTHOR, REVIEWER, or
    PARTICIPANT
    - approved.N (optional) the approved status associated with username.N.   That is whether username.N
    has approved the PR. Either true, or false

    Args:
        project_key (str):
        repository_slug (str):
        with_attributes (str | Unset):
        at (str | Unset):
        with_properties (str | Unset):
        draft (str | Unset):
        filter_text (str | Unset):
        state (str | Unset):
        order (str | Unset):
        direction (str | Unset):
        start (float | Unset):
        limit (float | Unset):  Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPageResponse200 | GetPageResponse400 | GetPageResponse401 | GetPageResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            with_attributes=with_attributes,
            at=at,
            with_properties=with_properties,
            draft=draft,
            filter_text=filter_text,
            state=state,
            order=order,
            direction=direction,
            start=start,
            limit=limit,
        )
    ).parsed
