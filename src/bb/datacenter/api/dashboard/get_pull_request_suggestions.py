from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_pull_request_suggestions_response_200 import GetPullRequestSuggestionsResponse200
from ...models.get_pull_request_suggestions_response_400 import GetPullRequestSuggestionsResponse400
from ...models.get_pull_request_suggestions_response_401 import GetPullRequestSuggestionsResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    changes_since: str | Unset = UNSET,
    limit: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["changesSince"] = changes_since

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/dashboard/pull-request-suggestions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetPullRequestSuggestionsResponse200
    | GetPullRequestSuggestionsResponse400
    | GetPullRequestSuggestionsResponse401
    | None
):
    if response.status_code == 200:
        response_200 = GetPullRequestSuggestionsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetPullRequestSuggestionsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetPullRequestSuggestionsResponse401.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetPullRequestSuggestionsResponse200 | GetPullRequestSuggestionsResponse400 | GetPullRequestSuggestionsResponse401
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    changes_since: str | Unset = UNSET,
    limit: str | Unset = UNSET,
) -> Response[
    GetPullRequestSuggestionsResponse200 | GetPullRequestSuggestionsResponse400 | GetPullRequestSuggestionsResponse401
]:
    """Get pull request suggestions

     Retrieves a page of suggestions for pull requests that the currently authenticated user may wish to
    raise. Such suggestions are based on ref changes occurring and so contain the ref change that
    prompted the suggestion plus the time the change event occurred. Changes will be returned in
    descending order based on the time the change that prompted the suggestion occurred.

    Note that although the response is a page object, the interface does not support paging, however a
    limit can be applied to the size of the returned page.

    Args:
        changes_since (str | Unset):
        limit (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPullRequestSuggestionsResponse200 | GetPullRequestSuggestionsResponse400 | GetPullRequestSuggestionsResponse401]
    """

    kwargs = _get_kwargs(
        changes_since=changes_since,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    changes_since: str | Unset = UNSET,
    limit: str | Unset = UNSET,
) -> (
    GetPullRequestSuggestionsResponse200
    | GetPullRequestSuggestionsResponse400
    | GetPullRequestSuggestionsResponse401
    | None
):
    """Get pull request suggestions

     Retrieves a page of suggestions for pull requests that the currently authenticated user may wish to
    raise. Such suggestions are based on ref changes occurring and so contain the ref change that
    prompted the suggestion plus the time the change event occurred. Changes will be returned in
    descending order based on the time the change that prompted the suggestion occurred.

    Note that although the response is a page object, the interface does not support paging, however a
    limit can be applied to the size of the returned page.

    Args:
        changes_since (str | Unset):
        limit (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPullRequestSuggestionsResponse200 | GetPullRequestSuggestionsResponse400 | GetPullRequestSuggestionsResponse401
    """

    return sync_detailed(
        client=client,
        changes_since=changes_since,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    changes_since: str | Unset = UNSET,
    limit: str | Unset = UNSET,
) -> Response[
    GetPullRequestSuggestionsResponse200 | GetPullRequestSuggestionsResponse400 | GetPullRequestSuggestionsResponse401
]:
    """Get pull request suggestions

     Retrieves a page of suggestions for pull requests that the currently authenticated user may wish to
    raise. Such suggestions are based on ref changes occurring and so contain the ref change that
    prompted the suggestion plus the time the change event occurred. Changes will be returned in
    descending order based on the time the change that prompted the suggestion occurred.

    Note that although the response is a page object, the interface does not support paging, however a
    limit can be applied to the size of the returned page.

    Args:
        changes_since (str | Unset):
        limit (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetPullRequestSuggestionsResponse200 | GetPullRequestSuggestionsResponse400 | GetPullRequestSuggestionsResponse401]
    """

    kwargs = _get_kwargs(
        changes_since=changes_since,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    changes_since: str | Unset = UNSET,
    limit: str | Unset = UNSET,
) -> (
    GetPullRequestSuggestionsResponse200
    | GetPullRequestSuggestionsResponse400
    | GetPullRequestSuggestionsResponse401
    | None
):
    """Get pull request suggestions

     Retrieves a page of suggestions for pull requests that the currently authenticated user may wish to
    raise. Such suggestions are based on ref changes occurring and so contain the ref change that
    prompted the suggestion plus the time the change event occurred. Changes will be returned in
    descending order based on the time the change that prompted the suggestion occurred.

    Note that although the response is a page object, the interface does not support paging, however a
    limit can be applied to the size of the returned page.

    Args:
        changes_since (str | Unset):
        limit (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetPullRequestSuggestionsResponse200 | GetPullRequestSuggestionsResponse400 | GetPullRequestSuggestionsResponse401
    """

    return (
        await asyncio_detailed(
            client=client,
            changes_since=changes_since,
            limit=limit,
        )
    ).parsed
