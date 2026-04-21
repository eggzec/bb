from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.paginated_tags import PaginatedTags
from ...types import UNSET, Response, Unset

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    *,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["sort"] = sort

    params["page"] = page

    params["pagelen"] = pagelen

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repositories/{workspace}/{repo_slug}/refs/tags".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


type ParsedPayload = Error | PaginatedTags
type ParseResult = Error | PaginatedTags | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = PaginatedTags.from_dict(response.json())

        return response_200

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
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> Response[ParsedPayload]:
    r"""List tags

     Returns the tags in the repository.

    By default, results will be in the order the underlying source control system returns them and
    identical to
    the ordering one sees when running \"$ git tag --list\". Note that this follows simple
    lexical ordering of the ref names.

    This can be undesirable as it does apply any natural sorting semantics, meaning for instance that
    tags are
    sorted [\"v10\", \"v11\", \"v9\"] instead of [\"v9\", \"v10\", \"v11\"].

    Sorting can be changed using the ?sort= query parameter. When using ?sort=name to explicitly sort on
    ref name,
    Bitbucket will apply natural sorting and interpret numerical values as numbers instead of strings.

    Args:
        workspace (str):
        repo_slug (str):
        q (str | Unset):
        sort (str | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedTags]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        q=q,
        sort=sort,
        page=page,
        pagelen=pagelen,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> ParsedPayload | None:
    r"""List tags

     Returns the tags in the repository.

    By default, results will be in the order the underlying source control system returns them and
    identical to
    the ordering one sees when running \"$ git tag --list\". Note that this follows simple
    lexical ordering of the ref names.

    This can be undesirable as it does apply any natural sorting semantics, meaning for instance that
    tags are
    sorted [\"v10\", \"v11\", \"v9\"] instead of [\"v9\", \"v10\", \"v11\"].

    Sorting can be changed using the ?sort= query parameter. When using ?sort=name to explicitly sort on
    ref name,
    Bitbucket will apply natural sorting and interpret numerical values as numbers instead of strings.

    Args:
        workspace (str):
        repo_slug (str):
        q (str | Unset):
        sort (str | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedTags
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        q=q,
        sort=sort,
        page=page,
        pagelen=pagelen,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> Response[ParsedPayload]:
    r"""List tags

     Returns the tags in the repository.

    By default, results will be in the order the underlying source control system returns them and
    identical to
    the ordering one sees when running \"$ git tag --list\". Note that this follows simple
    lexical ordering of the ref names.

    This can be undesirable as it does apply any natural sorting semantics, meaning for instance that
    tags are
    sorted [\"v10\", \"v11\", \"v9\"] instead of [\"v9\", \"v10\", \"v11\"].

    Sorting can be changed using the ?sort= query parameter. When using ?sort=name to explicitly sort on
    ref name,
    Bitbucket will apply natural sorting and interpret numerical values as numbers instead of strings.

    Args:
        workspace (str):
        repo_slug (str):
        q (str | Unset):
        sort (str | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedTags]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        q=q,
        sort=sort,
        page=page,
        pagelen=pagelen,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    page: int | Unset = 1,
    pagelen: int | Unset = 10,
) -> ParsedPayload | None:
    r"""List tags

     Returns the tags in the repository.

    By default, results will be in the order the underlying source control system returns them and
    identical to
    the ordering one sees when running \"$ git tag --list\". Note that this follows simple
    lexical ordering of the ref names.

    This can be undesirable as it does apply any natural sorting semantics, meaning for instance that
    tags are
    sorted [\"v10\", \"v11\", \"v9\"] instead of [\"v9\", \"v10\", \"v11\"].

    Sorting can be changed using the ?sort= query parameter. When using ?sort=name to explicitly sort on
    ref name,
    Bitbucket will apply natural sorting and interpret numerical values as numbers instead of strings.

    Args:
        workspace (str):
        repo_slug (str):
        q (str | Unset):
        sort (str | Unset):
        page (int | Unset):  Default: 1.
        pagelen (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedTags
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
            q=q,
            sort=sort,
            page=page,
            pagelen=pagelen,
        )
    ).parsed
