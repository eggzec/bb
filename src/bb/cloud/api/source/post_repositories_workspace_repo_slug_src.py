from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
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
    message: str | Unset = UNSET,
    author: str | Unset = UNSET,
    parents: str | Unset = UNSET,
    files: str | Unset = UNSET,
    branch: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["message"] = message

    params["author"] = author

    params["parents"] = parents

    params["files"] = files

    params["branch"] = branch

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/repositories/{workspace}/{repo_slug}/src".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
        ),
        "params": params,
    }

    return _kwargs


type ParsedPayload = Any | Error
type ParseResult = Any | Error | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

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
    message: str | Unset = UNSET,
    author: str | Unset = UNSET,
    parents: str | Unset = UNSET,
    files: str | Unset = UNSET,
    branch: str | Unset = UNSET,
) -> Response[ParsedPayload]:
    r""" Create a commit by uploading a file

     This endpoint is used to create new commits in the repository by
    uploading files.

    To add a new file to a repository:

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/username/slug/src \
      -F /repo/path/to/image.png=@image.png
    ```

    This will create a new commit on top of the main branch, inheriting the
    contents of the main branch, but adding (or overwriting) the
    `image.png` file to the repository in the `/repo/path/to` directory.

    To create a commit that deletes files, use the `files` parameter:

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/username/slug/src \
      -F files=/file/to/delete/1.txt \
      -F files=/file/to/delete/2.txt
    ```

    You can add/modify/delete multiple files in a request. Rename/move a
    file by deleting the old path and adding the content at the new path.

    This endpoint accepts `multipart/form-data` (as in the examples above),
    as well as `application/x-www-form-urlencoded`.

    Note: `multipart/form-data` is currently not supported by Forge apps
    for this API.

    #### multipart/form-data

    A `multipart/form-data` post contains a series of \"form fields\" that
    identify both the individual files that are being uploaded, as well as
    additional, optional meta data.

    Files are uploaded in file form fields (those that have a
    `Content-Disposition` parameter) whose field names point to the remote
    path in the repository where the file should be stored. Path field
    names are always interpreted to be absolute from the root of the
    repository, regardless whether the client uses a leading slash (as the
    above `curl` example did).

    File contents are treated as bytes and are not decoded as text.

    The commit message, as well as other non-file meta data for the
    request, is sent along as normal form field elements. Meta data fields
    share the same namespace as the file objects. For `multipart/form-data`
    bodies that should not lead to any ambiguity, as the
    `Content-Disposition` header will contain the `filename` parameter to
    distinguish between a file named \"message\" and the commit message field.

    #### application/x-www-form-urlencoded

    It is also possible to upload new files using a simple
    `application/x-www-form-urlencoded` POST. This can be convenient when
    uploading pure text files:

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src \
      --data-urlencode \"/path/to/me.txt=Lorem ipsum.\" \
      --data-urlencode \"message=Initial commit\" \
      --data-urlencode \"author=Erik van Zijst <erik.van.zijst@gmail.com>\"
    ```

    There could be a field name clash if a client were to upload a file
    named \"message\", as this filename clashes with the meta data property
    for the commit message. To avoid this and to upload files whose names
    clash with the meta data properties, use a leading slash for the files,
    e.g. `curl --data-urlencode \"/message=file contents\"`.

    When an explicit slash is omitted for a file whose path matches that of
    a meta data parameter, then it is interpreted as meta data, not as a
    file.

    #### Executables and links

    While this API aims to facilitate the most common use cases, it is
    possible to perform some more advanced operations like creating a new
    symlink in the repository, or creating an executable file.

    Files can be supplied with a `x-attributes` value in the
    `Content-Disposition` header. For example, to upload an executable
    file, as well as create a symlink from `README.txt` to `README`:

    ```
    --===============1438169132528273974==
    Content-Type: text/plain; charset=\"us-ascii\"
    MIME-Version: 1.0
    Content-Transfer-Encoding: 7bit
    Content-ID: \"bin/shutdown.sh\"
    Content-Disposition: attachment; filename=\"shutdown.sh\"; x-attributes:\"executable\"

    #!/bin/sh
    halt

    --===============1438169132528273974==
    Content-Type: text/plain; charset=\"us-ascii\"
    MIME-Version: 1.0
    Content-Transfer-Encoding: 7bit
    Content-ID: \"/README.txt\"
    Content-Disposition: attachment; filename=\"README.txt\"; x-attributes:\"link\"

    README
    --===============1438169132528273974==--
    ```

    Links are files that contain the target path and have
    `x-attributes:\"link\"` set.

    When overwriting links with files, or vice versa, the newly uploaded
    file determines both the new contents, as well as the attributes. That
    means uploading a file without specifying `x-attributes=\"link\"` will
    create a regular file, even if the parent commit hosted a symlink at
    the same path.

    The same applies to executables. When modifying an existing executable
    file, the form-data file element must include
    `x-attributes=\"executable\"` in order to preserve the executable status
    of the file.

    Note that this API does not support the creation or manipulation of
    subrepos / submodules.

    Args:
        workspace (str):
        repo_slug (str):
        message (str | Unset):
        author (str | Unset):
        parents (str | Unset):
        files (str | Unset):
        branch (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        message=message,
        author=author,
        parents=parents,
        files=files,
        branch=branch,
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
    message: str | Unset = UNSET,
    author: str | Unset = UNSET,
    parents: str | Unset = UNSET,
    files: str | Unset = UNSET,
    branch: str | Unset = UNSET,
) -> ParsedPayload | None:
    r""" Create a commit by uploading a file

     This endpoint is used to create new commits in the repository by
    uploading files.

    To add a new file to a repository:

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/username/slug/src \
      -F /repo/path/to/image.png=@image.png
    ```

    This will create a new commit on top of the main branch, inheriting the
    contents of the main branch, but adding (or overwriting) the
    `image.png` file to the repository in the `/repo/path/to` directory.

    To create a commit that deletes files, use the `files` parameter:

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/username/slug/src \
      -F files=/file/to/delete/1.txt \
      -F files=/file/to/delete/2.txt
    ```

    You can add/modify/delete multiple files in a request. Rename/move a
    file by deleting the old path and adding the content at the new path.

    This endpoint accepts `multipart/form-data` (as in the examples above),
    as well as `application/x-www-form-urlencoded`.

    Note: `multipart/form-data` is currently not supported by Forge apps
    for this API.

    #### multipart/form-data

    A `multipart/form-data` post contains a series of \"form fields\" that
    identify both the individual files that are being uploaded, as well as
    additional, optional meta data.

    Files are uploaded in file form fields (those that have a
    `Content-Disposition` parameter) whose field names point to the remote
    path in the repository where the file should be stored. Path field
    names are always interpreted to be absolute from the root of the
    repository, regardless whether the client uses a leading slash (as the
    above `curl` example did).

    File contents are treated as bytes and are not decoded as text.

    The commit message, as well as other non-file meta data for the
    request, is sent along as normal form field elements. Meta data fields
    share the same namespace as the file objects. For `multipart/form-data`
    bodies that should not lead to any ambiguity, as the
    `Content-Disposition` header will contain the `filename` parameter to
    distinguish between a file named \"message\" and the commit message field.

    #### application/x-www-form-urlencoded

    It is also possible to upload new files using a simple
    `application/x-www-form-urlencoded` POST. This can be convenient when
    uploading pure text files:

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src \
      --data-urlencode \"/path/to/me.txt=Lorem ipsum.\" \
      --data-urlencode \"message=Initial commit\" \
      --data-urlencode \"author=Erik van Zijst <erik.van.zijst@gmail.com>\"
    ```

    There could be a field name clash if a client were to upload a file
    named \"message\", as this filename clashes with the meta data property
    for the commit message. To avoid this and to upload files whose names
    clash with the meta data properties, use a leading slash for the files,
    e.g. `curl --data-urlencode \"/message=file contents\"`.

    When an explicit slash is omitted for a file whose path matches that of
    a meta data parameter, then it is interpreted as meta data, not as a
    file.

    #### Executables and links

    While this API aims to facilitate the most common use cases, it is
    possible to perform some more advanced operations like creating a new
    symlink in the repository, or creating an executable file.

    Files can be supplied with a `x-attributes` value in the
    `Content-Disposition` header. For example, to upload an executable
    file, as well as create a symlink from `README.txt` to `README`:

    ```
    --===============1438169132528273974==
    Content-Type: text/plain; charset=\"us-ascii\"
    MIME-Version: 1.0
    Content-Transfer-Encoding: 7bit
    Content-ID: \"bin/shutdown.sh\"
    Content-Disposition: attachment; filename=\"shutdown.sh\"; x-attributes:\"executable\"

    #!/bin/sh
    halt

    --===============1438169132528273974==
    Content-Type: text/plain; charset=\"us-ascii\"
    MIME-Version: 1.0
    Content-Transfer-Encoding: 7bit
    Content-ID: \"/README.txt\"
    Content-Disposition: attachment; filename=\"README.txt\"; x-attributes:\"link\"

    README
    --===============1438169132528273974==--
    ```

    Links are files that contain the target path and have
    `x-attributes:\"link\"` set.

    When overwriting links with files, or vice versa, the newly uploaded
    file determines both the new contents, as well as the attributes. That
    means uploading a file without specifying `x-attributes=\"link\"` will
    create a regular file, even if the parent commit hosted a symlink at
    the same path.

    The same applies to executables. When modifying an existing executable
    file, the form-data file element must include
    `x-attributes=\"executable\"` in order to preserve the executable status
    of the file.

    Note that this API does not support the creation or manipulation of
    subrepos / submodules.

    Args:
        workspace (str):
        repo_slug (str):
        message (str | Unset):
        author (str | Unset):
        parents (str | Unset):
        files (str | Unset):
        branch (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        message=message,
        author=author,
        parents=parents,
        files=files,
        branch=branch,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    message: str | Unset = UNSET,
    author: str | Unset = UNSET,
    parents: str | Unset = UNSET,
    files: str | Unset = UNSET,
    branch: str | Unset = UNSET,
) -> Response[ParsedPayload]:
    r""" Create a commit by uploading a file

     This endpoint is used to create new commits in the repository by
    uploading files.

    To add a new file to a repository:

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/username/slug/src \
      -F /repo/path/to/image.png=@image.png
    ```

    This will create a new commit on top of the main branch, inheriting the
    contents of the main branch, but adding (or overwriting) the
    `image.png` file to the repository in the `/repo/path/to` directory.

    To create a commit that deletes files, use the `files` parameter:

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/username/slug/src \
      -F files=/file/to/delete/1.txt \
      -F files=/file/to/delete/2.txt
    ```

    You can add/modify/delete multiple files in a request. Rename/move a
    file by deleting the old path and adding the content at the new path.

    This endpoint accepts `multipart/form-data` (as in the examples above),
    as well as `application/x-www-form-urlencoded`.

    Note: `multipart/form-data` is currently not supported by Forge apps
    for this API.

    #### multipart/form-data

    A `multipart/form-data` post contains a series of \"form fields\" that
    identify both the individual files that are being uploaded, as well as
    additional, optional meta data.

    Files are uploaded in file form fields (those that have a
    `Content-Disposition` parameter) whose field names point to the remote
    path in the repository where the file should be stored. Path field
    names are always interpreted to be absolute from the root of the
    repository, regardless whether the client uses a leading slash (as the
    above `curl` example did).

    File contents are treated as bytes and are not decoded as text.

    The commit message, as well as other non-file meta data for the
    request, is sent along as normal form field elements. Meta data fields
    share the same namespace as the file objects. For `multipart/form-data`
    bodies that should not lead to any ambiguity, as the
    `Content-Disposition` header will contain the `filename` parameter to
    distinguish between a file named \"message\" and the commit message field.

    #### application/x-www-form-urlencoded

    It is also possible to upload new files using a simple
    `application/x-www-form-urlencoded` POST. This can be convenient when
    uploading pure text files:

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src \
      --data-urlencode \"/path/to/me.txt=Lorem ipsum.\" \
      --data-urlencode \"message=Initial commit\" \
      --data-urlencode \"author=Erik van Zijst <erik.van.zijst@gmail.com>\"
    ```

    There could be a field name clash if a client were to upload a file
    named \"message\", as this filename clashes with the meta data property
    for the commit message. To avoid this and to upload files whose names
    clash with the meta data properties, use a leading slash for the files,
    e.g. `curl --data-urlencode \"/message=file contents\"`.

    When an explicit slash is omitted for a file whose path matches that of
    a meta data parameter, then it is interpreted as meta data, not as a
    file.

    #### Executables and links

    While this API aims to facilitate the most common use cases, it is
    possible to perform some more advanced operations like creating a new
    symlink in the repository, or creating an executable file.

    Files can be supplied with a `x-attributes` value in the
    `Content-Disposition` header. For example, to upload an executable
    file, as well as create a symlink from `README.txt` to `README`:

    ```
    --===============1438169132528273974==
    Content-Type: text/plain; charset=\"us-ascii\"
    MIME-Version: 1.0
    Content-Transfer-Encoding: 7bit
    Content-ID: \"bin/shutdown.sh\"
    Content-Disposition: attachment; filename=\"shutdown.sh\"; x-attributes:\"executable\"

    #!/bin/sh
    halt

    --===============1438169132528273974==
    Content-Type: text/plain; charset=\"us-ascii\"
    MIME-Version: 1.0
    Content-Transfer-Encoding: 7bit
    Content-ID: \"/README.txt\"
    Content-Disposition: attachment; filename=\"README.txt\"; x-attributes:\"link\"

    README
    --===============1438169132528273974==--
    ```

    Links are files that contain the target path and have
    `x-attributes:\"link\"` set.

    When overwriting links with files, or vice versa, the newly uploaded
    file determines both the new contents, as well as the attributes. That
    means uploading a file without specifying `x-attributes=\"link\"` will
    create a regular file, even if the parent commit hosted a symlink at
    the same path.

    The same applies to executables. When modifying an existing executable
    file, the form-data file element must include
    `x-attributes=\"executable\"` in order to preserve the executable status
    of the file.

    Note that this API does not support the creation or manipulation of
    subrepos / submodules.

    Args:
        workspace (str):
        repo_slug (str):
        message (str | Unset):
        author (str | Unset):
        parents (str | Unset):
        files (str | Unset):
        branch (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        message=message,
        author=author,
        parents=parents,
        files=files,
        branch=branch,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    message: str | Unset = UNSET,
    author: str | Unset = UNSET,
    parents: str | Unset = UNSET,
    files: str | Unset = UNSET,
    branch: str | Unset = UNSET,
) -> ParsedPayload | None:
    r""" Create a commit by uploading a file

     This endpoint is used to create new commits in the repository by
    uploading files.

    To add a new file to a repository:

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/username/slug/src \
      -F /repo/path/to/image.png=@image.png
    ```

    This will create a new commit on top of the main branch, inheriting the
    contents of the main branch, but adding (or overwriting) the
    `image.png` file to the repository in the `/repo/path/to` directory.

    To create a commit that deletes files, use the `files` parameter:

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/username/slug/src \
      -F files=/file/to/delete/1.txt \
      -F files=/file/to/delete/2.txt
    ```

    You can add/modify/delete multiple files in a request. Rename/move a
    file by deleting the old path and adding the content at the new path.

    This endpoint accepts `multipart/form-data` (as in the examples above),
    as well as `application/x-www-form-urlencoded`.

    Note: `multipart/form-data` is currently not supported by Forge apps
    for this API.

    #### multipart/form-data

    A `multipart/form-data` post contains a series of \"form fields\" that
    identify both the individual files that are being uploaded, as well as
    additional, optional meta data.

    Files are uploaded in file form fields (those that have a
    `Content-Disposition` parameter) whose field names point to the remote
    path in the repository where the file should be stored. Path field
    names are always interpreted to be absolute from the root of the
    repository, regardless whether the client uses a leading slash (as the
    above `curl` example did).

    File contents are treated as bytes and are not decoded as text.

    The commit message, as well as other non-file meta data for the
    request, is sent along as normal form field elements. Meta data fields
    share the same namespace as the file objects. For `multipart/form-data`
    bodies that should not lead to any ambiguity, as the
    `Content-Disposition` header will contain the `filename` parameter to
    distinguish between a file named \"message\" and the commit message field.

    #### application/x-www-form-urlencoded

    It is also possible to upload new files using a simple
    `application/x-www-form-urlencoded` POST. This can be convenient when
    uploading pure text files:

    ```
    $ curl https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src \
      --data-urlencode \"/path/to/me.txt=Lorem ipsum.\" \
      --data-urlencode \"message=Initial commit\" \
      --data-urlencode \"author=Erik van Zijst <erik.van.zijst@gmail.com>\"
    ```

    There could be a field name clash if a client were to upload a file
    named \"message\", as this filename clashes with the meta data property
    for the commit message. To avoid this and to upload files whose names
    clash with the meta data properties, use a leading slash for the files,
    e.g. `curl --data-urlencode \"/message=file contents\"`.

    When an explicit slash is omitted for a file whose path matches that of
    a meta data parameter, then it is interpreted as meta data, not as a
    file.

    #### Executables and links

    While this API aims to facilitate the most common use cases, it is
    possible to perform some more advanced operations like creating a new
    symlink in the repository, or creating an executable file.

    Files can be supplied with a `x-attributes` value in the
    `Content-Disposition` header. For example, to upload an executable
    file, as well as create a symlink from `README.txt` to `README`:

    ```
    --===============1438169132528273974==
    Content-Type: text/plain; charset=\"us-ascii\"
    MIME-Version: 1.0
    Content-Transfer-Encoding: 7bit
    Content-ID: \"bin/shutdown.sh\"
    Content-Disposition: attachment; filename=\"shutdown.sh\"; x-attributes:\"executable\"

    #!/bin/sh
    halt

    --===============1438169132528273974==
    Content-Type: text/plain; charset=\"us-ascii\"
    MIME-Version: 1.0
    Content-Transfer-Encoding: 7bit
    Content-ID: \"/README.txt\"
    Content-Disposition: attachment; filename=\"README.txt\"; x-attributes:\"link\"

    README
    --===============1438169132528273974==--
    ```

    Links are files that contain the target path and have
    `x-attributes:\"link\"` set.

    When overwriting links with files, or vice versa, the newly uploaded
    file determines both the new contents, as well as the attributes. That
    means uploading a file without specifying `x-attributes=\"link\"` will
    create a regular file, even if the parent commit hosted a symlink at
    the same path.

    The same applies to executables. When modifying an existing executable
    file, the form-data file element must include
    `x-attributes=\"executable\"` in order to preserve the executable status
    of the file.

    Note that this API does not support the creation or manipulation of
    subrepos / submodules.

    Args:
        workspace (str):
        repo_slug (str):
        message (str | Unset):
        author (str | Unset):
        parents (str | Unset):
        files (str | Unset):
        branch (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
            message=message,
            author=author,
            parents=parents,
            files=files,
            branch=branch,
        )
    ).parsed
