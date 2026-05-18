from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.search_result_page import SearchResultPage
from ...types import UNSET, Response, Unset

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    username: str,
    *,
    search_query: str,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["search_query"] = search_query

    params["page"] = page

    params["pagelen"] = pagelen

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/teams/{username}/search/code".format(
            username=quote(str(username), safe=""),
        ),
        "params": params,
    }

    return _kwargs


type ParsedPayload = Error | SearchResultPage
type ParseResult = Error | SearchResultPage | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = SearchResultPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_429 = Error.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ParsedPayload]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
    search_query: str,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> Response[ParsedPayload]:
    r"""Search for code in a team's repositories

     Search for code in the repositories of the specified team.

    Note that searches can match in the file's text (`content_matches`),
    the path (`path_matches`), or both.

    You can use the same syntax for the search query as in the UI.
    E.g. to search for \"foo\" only within the repository \"demo\",
    use the query parameter `search_query=foo+repo:demo`.

    Similar to other APIs, you can request more fields using a
    `fields` query parameter. E.g. to get some more information about
    the repository of matched files, use the query parameter
    `search_query=foo&fields=%2Bvalues.file.commit.repository`
    (the `%2B` is a URL-encoded `+`).

    Try `fields=%2Bvalues.*.*.*.*` to get an idea what's possible.

    Args:
        username (str):
        search_query (str):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SearchResultPage]
    """

    kwargs = _get_kwargs(
        username=username,
        search_query=search_query,
        page=page,
        pagelen=pagelen,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: str,
    *,
    client: AuthenticatedClient,
    search_query: str,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> ParsedPayload | None:
    r"""Search for code in a team's repositories

     Search for code in the repositories of the specified team.

    Note that searches can match in the file's text (`content_matches`),
    the path (`path_matches`), or both.

    You can use the same syntax for the search query as in the UI.
    E.g. to search for \"foo\" only within the repository \"demo\",
    use the query parameter `search_query=foo+repo:demo`.

    Similar to other APIs, you can request more fields using a
    `fields` query parameter. E.g. to get some more information about
    the repository of matched files, use the query parameter
    `search_query=foo&fields=%2Bvalues.file.commit.repository`
    (the `%2B` is a URL-encoded `+`).

    Try `fields=%2Bvalues.*.*.*.*` to get an idea what's possible.

    Args:
        username (str):
        search_query (str):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SearchResultPage
    """

    return sync_detailed(
        username=username,
        client=client,
        search_query=search_query,
        page=page,
        pagelen=pagelen,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
    search_query: str,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> Response[ParsedPayload]:
    r"""Search for code in a team's repositories

     Search for code in the repositories of the specified team.

    Note that searches can match in the file's text (`content_matches`),
    the path (`path_matches`), or both.

    You can use the same syntax for the search query as in the UI.
    E.g. to search for \"foo\" only within the repository \"demo\",
    use the query parameter `search_query=foo+repo:demo`.

    Similar to other APIs, you can request more fields using a
    `fields` query parameter. E.g. to get some more information about
    the repository of matched files, use the query parameter
    `search_query=foo&fields=%2Bvalues.file.commit.repository`
    (the `%2B` is a URL-encoded `+`).

    Try `fields=%2Bvalues.*.*.*.*` to get an idea what's possible.

    Args:
        username (str):
        search_query (str):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SearchResultPage]
    """

    kwargs = _get_kwargs(
        username=username,
        search_query=search_query,
        page=page,
        pagelen=pagelen,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    *,
    client: AuthenticatedClient,
    search_query: str,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> ParsedPayload | None:
    r"""Search for code in a team's repositories

     Search for code in the repositories of the specified team.

    Note that searches can match in the file's text (`content_matches`),
    the path (`path_matches`), or both.

    You can use the same syntax for the search query as in the UI.
    E.g. to search for \"foo\" only within the repository \"demo\",
    use the query parameter `search_query=foo+repo:demo`.

    Similar to other APIs, you can request more fields using a
    `fields` query parameter. E.g. to get some more information about
    the repository of matched files, use the query parameter
    `search_query=foo&fields=%2Bvalues.file.commit.repository`
    (the `%2B` is a URL-encoded `+`).

    Try `fields=%2Bvalues.*.*.*.*` to get an idea what's possible.

    Args:
        username (str):
        search_query (str):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SearchResultPage
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
            search_query=search_query,
            page=page,
            pagelen=pagelen,
        )
    ).parsed
