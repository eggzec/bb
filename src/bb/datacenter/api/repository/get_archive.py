from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_archive_response_400 import GetArchiveResponse400
from ...models.get_archive_response_401 import GetArchiveResponse401
from ...models.get_archive_response_404 import GetArchiveResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    *,
    path: str | Unset = UNSET,
    filename: str | Unset = UNSET,
    at: str | Unset = UNSET,
    prefix: str | Unset = UNSET,
    format_: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["path"] = path

    params["filename"] = filename

    params["at"] = at

    params["prefix"] = prefix

    params["format"] = format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/archive".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetArchiveResponse400 | GetArchiveResponse401 | GetArchiveResponse404 | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = GetArchiveResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetArchiveResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetArchiveResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetArchiveResponse400 | GetArchiveResponse401 | GetArchiveResponse404]:
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
    path: str | Unset = UNSET,
    filename: str | Unset = UNSET,
    at: str | Unset = UNSET,
    prefix: str | Unset = UNSET,
    format_: str | Unset = UNSET,
) -> Response[Any | GetArchiveResponse400 | GetArchiveResponse401 | GetArchiveResponse404]:
    r"""Stream archive of repository

     Streams an archive of the repository's contents at the requested commit. If no `at=` commit is
    requested, an archive of the default branch is streamed.

    The <code>filename=</code> query parameter may be used to specify the exact filename to include in
    the \"Content-Disposition\" header. If an explicit filename is not provided, one will be
    automatically generated based on what is being archived. Its format depends on the at= value:

    - No <code>at=</code> commit:     &lt;slug&gt;-&lt;default-branch-
    name&gt;@&lt;commit&gt;.&lt;format&gt;;     e.g. example-master@43c2f8a0fe8.zip
    - <code>at=</code>sha: &lt;slug&gt;-&lt;at&gt;.&lt;format&gt;; e.g.
    example-09bcbb00100cfbb5310fb6834a1d5ce6cac253e9.tar.gz
    - <code>at=</code>branchOrTag: &lt;slug&gt;-&lt;branchOrTag&gt;@&lt;commit&gt;.&lt;format&gt;;
    e.g. example-feature@bbb225f16e1.tar

        - If the branch or tag is qualified (e.g. refs/heads/master, the short name         (master)
    will be included in the filename
        - If the branch or tag's <i>short name</i> includes slashes (e.g. release/4.6),         they
    will be converted to hyphens in the filename (release-4.5)




    Archives may be requested in the following formats by adding the <code>format=</code> query
    parameter:

    - zip: A zip file using standard compression (Default)
    - tar: An uncompressed tarball
    - tar.gz or tgz: A GZip-compressed tarball


    The contents of the archive may be filtered by using the <code>path=</code> query parameter to
    specify paths to include. <code>path=</code> may be specified multiple times to include multiple
    paths.

    The <code>prefix=</code> query parameter may be used to define a directory (or multiple directories)
    where the archive's contents should be placed. If the prefix does not end with /, one will be added
    automatically. The prefix is <i>always</i> treated as a directory; it is not possible to use it to
    prepend characters to the entries in the archive.

    Archives of public repositories may be streamed by any authenticated or anonymous user. Streaming
    archives for non-public repositories requires an <i>authenticated user</i> with at least
    <b>REPO_READ</b> permission.

    Args:
        project_key (str):
        repository_slug (str):
        path (str | Unset):
        filename (str | Unset):
        at (str | Unset):
        prefix (str | Unset):
        format_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetArchiveResponse400 | GetArchiveResponse401 | GetArchiveResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        path=path,
        filename=filename,
        at=at,
        prefix=prefix,
        format_=format_,
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
    path: str | Unset = UNSET,
    filename: str | Unset = UNSET,
    at: str | Unset = UNSET,
    prefix: str | Unset = UNSET,
    format_: str | Unset = UNSET,
) -> Any | GetArchiveResponse400 | GetArchiveResponse401 | GetArchiveResponse404 | None:
    r"""Stream archive of repository

     Streams an archive of the repository's contents at the requested commit. If no `at=` commit is
    requested, an archive of the default branch is streamed.

    The <code>filename=</code> query parameter may be used to specify the exact filename to include in
    the \"Content-Disposition\" header. If an explicit filename is not provided, one will be
    automatically generated based on what is being archived. Its format depends on the at= value:

    - No <code>at=</code> commit:     &lt;slug&gt;-&lt;default-branch-
    name&gt;@&lt;commit&gt;.&lt;format&gt;;     e.g. example-master@43c2f8a0fe8.zip
    - <code>at=</code>sha: &lt;slug&gt;-&lt;at&gt;.&lt;format&gt;; e.g.
    example-09bcbb00100cfbb5310fb6834a1d5ce6cac253e9.tar.gz
    - <code>at=</code>branchOrTag: &lt;slug&gt;-&lt;branchOrTag&gt;@&lt;commit&gt;.&lt;format&gt;;
    e.g. example-feature@bbb225f16e1.tar

        - If the branch or tag is qualified (e.g. refs/heads/master, the short name         (master)
    will be included in the filename
        - If the branch or tag's <i>short name</i> includes slashes (e.g. release/4.6),         they
    will be converted to hyphens in the filename (release-4.5)




    Archives may be requested in the following formats by adding the <code>format=</code> query
    parameter:

    - zip: A zip file using standard compression (Default)
    - tar: An uncompressed tarball
    - tar.gz or tgz: A GZip-compressed tarball


    The contents of the archive may be filtered by using the <code>path=</code> query parameter to
    specify paths to include. <code>path=</code> may be specified multiple times to include multiple
    paths.

    The <code>prefix=</code> query parameter may be used to define a directory (or multiple directories)
    where the archive's contents should be placed. If the prefix does not end with /, one will be added
    automatically. The prefix is <i>always</i> treated as a directory; it is not possible to use it to
    prepend characters to the entries in the archive.

    Archives of public repositories may be streamed by any authenticated or anonymous user. Streaming
    archives for non-public repositories requires an <i>authenticated user</i> with at least
    <b>REPO_READ</b> permission.

    Args:
        project_key (str):
        repository_slug (str):
        path (str | Unset):
        filename (str | Unset):
        at (str | Unset):
        prefix (str | Unset):
        format_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetArchiveResponse400 | GetArchiveResponse401 | GetArchiveResponse404
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        client=client,
        path=path,
        filename=filename,
        at=at,
        prefix=prefix,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    path: str | Unset = UNSET,
    filename: str | Unset = UNSET,
    at: str | Unset = UNSET,
    prefix: str | Unset = UNSET,
    format_: str | Unset = UNSET,
) -> Response[Any | GetArchiveResponse400 | GetArchiveResponse401 | GetArchiveResponse404]:
    r"""Stream archive of repository

     Streams an archive of the repository's contents at the requested commit. If no `at=` commit is
    requested, an archive of the default branch is streamed.

    The <code>filename=</code> query parameter may be used to specify the exact filename to include in
    the \"Content-Disposition\" header. If an explicit filename is not provided, one will be
    automatically generated based on what is being archived. Its format depends on the at= value:

    - No <code>at=</code> commit:     &lt;slug&gt;-&lt;default-branch-
    name&gt;@&lt;commit&gt;.&lt;format&gt;;     e.g. example-master@43c2f8a0fe8.zip
    - <code>at=</code>sha: &lt;slug&gt;-&lt;at&gt;.&lt;format&gt;; e.g.
    example-09bcbb00100cfbb5310fb6834a1d5ce6cac253e9.tar.gz
    - <code>at=</code>branchOrTag: &lt;slug&gt;-&lt;branchOrTag&gt;@&lt;commit&gt;.&lt;format&gt;;
    e.g. example-feature@bbb225f16e1.tar

        - If the branch or tag is qualified (e.g. refs/heads/master, the short name         (master)
    will be included in the filename
        - If the branch or tag's <i>short name</i> includes slashes (e.g. release/4.6),         they
    will be converted to hyphens in the filename (release-4.5)




    Archives may be requested in the following formats by adding the <code>format=</code> query
    parameter:

    - zip: A zip file using standard compression (Default)
    - tar: An uncompressed tarball
    - tar.gz or tgz: A GZip-compressed tarball


    The contents of the archive may be filtered by using the <code>path=</code> query parameter to
    specify paths to include. <code>path=</code> may be specified multiple times to include multiple
    paths.

    The <code>prefix=</code> query parameter may be used to define a directory (or multiple directories)
    where the archive's contents should be placed. If the prefix does not end with /, one will be added
    automatically. The prefix is <i>always</i> treated as a directory; it is not possible to use it to
    prepend characters to the entries in the archive.

    Archives of public repositories may be streamed by any authenticated or anonymous user. Streaming
    archives for non-public repositories requires an <i>authenticated user</i> with at least
    <b>REPO_READ</b> permission.

    Args:
        project_key (str):
        repository_slug (str):
        path (str | Unset):
        filename (str | Unset):
        at (str | Unset):
        prefix (str | Unset):
        format_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetArchiveResponse400 | GetArchiveResponse401 | GetArchiveResponse404]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        path=path,
        filename=filename,
        at=at,
        prefix=prefix,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    *,
    client: AuthenticatedClient | Client,
    path: str | Unset = UNSET,
    filename: str | Unset = UNSET,
    at: str | Unset = UNSET,
    prefix: str | Unset = UNSET,
    format_: str | Unset = UNSET,
) -> Any | GetArchiveResponse400 | GetArchiveResponse401 | GetArchiveResponse404 | None:
    r"""Stream archive of repository

     Streams an archive of the repository's contents at the requested commit. If no `at=` commit is
    requested, an archive of the default branch is streamed.

    The <code>filename=</code> query parameter may be used to specify the exact filename to include in
    the \"Content-Disposition\" header. If an explicit filename is not provided, one will be
    automatically generated based on what is being archived. Its format depends on the at= value:

    - No <code>at=</code> commit:     &lt;slug&gt;-&lt;default-branch-
    name&gt;@&lt;commit&gt;.&lt;format&gt;;     e.g. example-master@43c2f8a0fe8.zip
    - <code>at=</code>sha: &lt;slug&gt;-&lt;at&gt;.&lt;format&gt;; e.g.
    example-09bcbb00100cfbb5310fb6834a1d5ce6cac253e9.tar.gz
    - <code>at=</code>branchOrTag: &lt;slug&gt;-&lt;branchOrTag&gt;@&lt;commit&gt;.&lt;format&gt;;
    e.g. example-feature@bbb225f16e1.tar

        - If the branch or tag is qualified (e.g. refs/heads/master, the short name         (master)
    will be included in the filename
        - If the branch or tag's <i>short name</i> includes slashes (e.g. release/4.6),         they
    will be converted to hyphens in the filename (release-4.5)




    Archives may be requested in the following formats by adding the <code>format=</code> query
    parameter:

    - zip: A zip file using standard compression (Default)
    - tar: An uncompressed tarball
    - tar.gz or tgz: A GZip-compressed tarball


    The contents of the archive may be filtered by using the <code>path=</code> query parameter to
    specify paths to include. <code>path=</code> may be specified multiple times to include multiple
    paths.

    The <code>prefix=</code> query parameter may be used to define a directory (or multiple directories)
    where the archive's contents should be placed. If the prefix does not end with /, one will be added
    automatically. The prefix is <i>always</i> treated as a directory; it is not possible to use it to
    prepend characters to the entries in the archive.

    Archives of public repositories may be streamed by any authenticated or anonymous user. Streaming
    archives for non-public repositories requires an <i>authenticated user</i> with at least
    <b>REPO_READ</b> permission.

    Args:
        project_key (str):
        repository_slug (str):
        path (str | Unset):
        filename (str | Unset):
        at (str | Unset):
        prefix (str | Unset):
        format_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetArchiveResponse400 | GetArchiveResponse401 | GetArchiveResponse404
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            client=client,
            path=path,
            filename=filename,
            at=at,
            prefix=prefix,
            format_=format_,
        )
    ).parsed
