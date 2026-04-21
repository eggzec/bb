from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.paginated_files import PaginatedFiles
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
    commit: str,
    path: str,
    *,
    renames: str | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["renames"] = renames

    params["q"] = q

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repositories/{workspace}/{repo_slug}/filehistory/{commit}/{path}".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
            commit=quote(str(commit), safe=""),
            path=quote(str(path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


type ParsedPayload = Error | PaginatedFiles
type ParseResult = Error | PaginatedFiles | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = PaginatedFiles.from_dict(response.json())

        return response_200

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
    commit: str,
    path: str,
    *,
    client: AuthenticatedClient,
    renames: str | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[ParsedPayload]:
    r""" List commits that modified a file

     Returns a paginated list of commits that modified the specified file.

    Commits are returned in reverse chronological order. This is roughly
    equivalent to the following commands:

        $ git log --follow --date-order <sha> <path>

    By default, Bitbucket will follow renames and the path name in the
    returned entries reflects that. This can be turned off using the
    `?renames=false` query parameter.

    Results are returned in descending chronological order by default, and
    like most endpoints you can
    [filter and sort](/cloud/bitbucket/rest/intro/#filtering) the response to
    only provide exactly the data you want.

    The example response returns commits made before 2011-05-18 against a file
    named `README.rst`. The results are filtered to only return the path and
    date. This request can be made using:

    ```
    $ curl 'https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/filehistory/master/README.rst'\
      '?fields=values.next,values.path,values.commit.date&q=commit.date<=2011-05-18'
    ```

    In the response you can see that the file was renamed to `README.rst`
    by the commit made on 2011-05-16, and was previously named `README.txt`.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        path (str):
        renames (str | Unset):
        q (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedFiles]
     """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        path=path,
        renames=renames,
        q=q,
        sort=sort,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    repo_slug: str,
    commit: str,
    path: str,
    *,
    client: AuthenticatedClient,
    renames: str | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> ParsedPayload | None:
    r""" List commits that modified a file

     Returns a paginated list of commits that modified the specified file.

    Commits are returned in reverse chronological order. This is roughly
    equivalent to the following commands:

        $ git log --follow --date-order <sha> <path>

    By default, Bitbucket will follow renames and the path name in the
    returned entries reflects that. This can be turned off using the
    `?renames=false` query parameter.

    Results are returned in descending chronological order by default, and
    like most endpoints you can
    [filter and sort](/cloud/bitbucket/rest/intro/#filtering) the response to
    only provide exactly the data you want.

    The example response returns commits made before 2011-05-18 against a file
    named `README.rst`. The results are filtered to only return the path and
    date. This request can be made using:

    ```
    $ curl 'https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/filehistory/master/README.rst'\
      '?fields=values.next,values.path,values.commit.date&q=commit.date<=2011-05-18'
    ```

    In the response you can see that the file was renamed to `README.rst`
    by the commit made on 2011-05-16, and was previously named `README.txt`.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        path (str):
        renames (str | Unset):
        q (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedFiles
     """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        path=path,
        client=client,
        renames=renames,
        q=q,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    commit: str,
    path: str,
    *,
    client: AuthenticatedClient,
    renames: str | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[ParsedPayload]:
    r""" List commits that modified a file

     Returns a paginated list of commits that modified the specified file.

    Commits are returned in reverse chronological order. This is roughly
    equivalent to the following commands:

        $ git log --follow --date-order <sha> <path>

    By default, Bitbucket will follow renames and the path name in the
    returned entries reflects that. This can be turned off using the
    `?renames=false` query parameter.

    Results are returned in descending chronological order by default, and
    like most endpoints you can
    [filter and sort](/cloud/bitbucket/rest/intro/#filtering) the response to
    only provide exactly the data you want.

    The example response returns commits made before 2011-05-18 against a file
    named `README.rst`. The results are filtered to only return the path and
    date. This request can be made using:

    ```
    $ curl 'https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/filehistory/master/README.rst'\
      '?fields=values.next,values.path,values.commit.date&q=commit.date<=2011-05-18'
    ```

    In the response you can see that the file was renamed to `README.rst`
    by the commit made on 2011-05-16, and was previously named `README.txt`.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        path (str):
        renames (str | Unset):
        q (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedFiles]
     """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        path=path,
        renames=renames,
        q=q,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    commit: str,
    path: str,
    *,
    client: AuthenticatedClient,
    renames: str | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> ParsedPayload | None:
    r""" List commits that modified a file

     Returns a paginated list of commits that modified the specified file.

    Commits are returned in reverse chronological order. This is roughly
    equivalent to the following commands:

        $ git log --follow --date-order <sha> <path>

    By default, Bitbucket will follow renames and the path name in the
    returned entries reflects that. This can be turned off using the
    `?renames=false` query parameter.

    Results are returned in descending chronological order by default, and
    like most endpoints you can
    [filter and sort](/cloud/bitbucket/rest/intro/#filtering) the response to
    only provide exactly the data you want.

    The example response returns commits made before 2011-05-18 against a file
    named `README.rst`. The results are filtered to only return the path and
    date. This request can be made using:

    ```
    $ curl 'https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/filehistory/master/README.rst'\
      '?fields=values.next,values.path,values.commit.date&q=commit.date<=2011-05-18'
    ```

    In the response you can see that the file was renamed to `README.rst`
    by the commit made on 2011-05-16, and was previously named `README.txt`.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        path (str):
        renames (str | Unset):
        q (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedFiles
     """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            commit=commit,
            path=path,
            client=client,
            renames=renames,
            q=q,
            sort=sort,
        )
    ).parsed
