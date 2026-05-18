from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_repositories_workspace_repo_slug_src_commit_path_format import (
    GetRepositoriesWorkspaceRepoSlugSrcCommitPathFormat,
)
from ...models.paginated_tree_entry import PaginatedTreeEntry
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
    format_: GetRepositoriesWorkspaceRepoSlugSrcCommitPathFormat | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    max_depth: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_format_: str | Unset = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params["q"] = q

    params["sort"] = sort

    params["max_depth"] = max_depth

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repositories/{workspace}/{repo_slug}/src/{commit}/{path}".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
            commit=quote(str(commit), safe=""),
            path=quote(str(path), safe=""),
        ),
        "params": params,
    }

    return _kwargs


type ParsedPayload = Error | PaginatedTreeEntry
type ParseResult = Error | PaginatedTreeEntry | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = PaginatedTreeEntry.from_dict(response.json())

        return response_200

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

    if response.status_code == 555:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_555 = Error.from_dict(response.json())

        return response_555

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
    format_: GetRepositoriesWorkspaceRepoSlugSrcCommitPathFormat | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    max_depth: int | Unset = UNSET,
) -> Response[ParsedPayload]:
    r"""Get file or directory contents

     This endpoints is used to retrieve the contents of a single file,
    or the contents of a directory at a specified revision.

    #### Raw file contents

    When `path` points to a file, this endpoint returns the raw contents.
    The response's Content-Type is derived from the filename
    extension (not from the contents). The file contents are not processed
    and no character encoding/recoding is performed and as a result no
    character encoding is included as part of the Content-Type.

    The `Content-Disposition` header will be \"attachment\" to prevent
    browsers from running executable files.

    If the file is managed by LFS, then a 301 redirect pointing to
    Atlassian's media services platform is returned.

    The response includes an ETag that is based on the contents of the file
    and its attributes. This means that an empty `__init__.py` always
    returns the same ETag, regardless on the directory it lives in, or the
    commit it is on.

    #### File meta data

    When the request for a file path includes the query parameter
    `?format=meta`, instead of returning the file's raw contents, Bitbucket
    instead returns the JSON object describing the file's properties:

    ```javascript
    $ curl
    https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef/tests/__init__.py?format=meta
    {
      \"links\": {
        \"self\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629
    f650959d6706d54cd335/tests/__init__.py\"
        },
        \"meta\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629
    f650959d6706d54cd335/tests/__init__.py?format=meta\"
        }
      },
      \"path\": \"tests/__init__.py\",
      \"commit\": {
        \"type\": \"commit\",
        \"hash\": \"eefd5ef5d3df01aed629f650959d6706d54cd335\",
        \"links\": {
          \"self\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/commit/eefd5ef5d3df01a
    ed629f650959d6706d54cd335\"
          },
          \"html\": {
            \"href\":
    \"https://bitbucket.org/atlassian/bbql/commits/eefd5ef5d3df01aed629f650959d6706d54cd335\"
          }
        }
      },
      \"attributes\": [],
      \"type\": \"commit_file\",
      \"size\": 0
    }
    ```

    File objects contain an `attributes` element that contains a list of
    possible modifiers. Currently defined values are:

    * `link` -- indicates that the entry is a symbolic link. The contents
        of the file represent the path the link points to.
    * `executable` -- indicates that the file has the executable bit set.
    * `subrepository` -- indicates that the entry points to a submodule or
        subrepo. The contents of the file is the SHA1 of the repository
        pointed to.
    * `binary` -- indicates whether Bitbucket thinks the file is binary.

    This endpoint can provide an alternative to how a HEAD request can be
    used to check for the existence of a file, or a file's size without
    incurring the overhead of receiving its full contents.


    #### Directory listings

    When `path` points to a directory instead of a file, the response is a
    paginated list of directory and file objects in the same order as the
    underlying SCM system would return them.

    For example:

    ```javascript
    $ curl https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef/tests
    {
      \"pagelen\": 10,
      \"values\": [
        {
          \"path\": \"tests/test_project\",
          \"type\": \"commit_directory\",
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01ae
    d629f650959d6706d54cd335/tests/test_project/\"
            },
            \"meta\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01ae
    d629f650959d6706d54cd335/tests/test_project/?format=meta\"
            }
          },
          \"commit\": {
            \"type\": \"commit\",
            \"hash\": \"eefd5ef5d3df01aed629f650959d6706d54cd335\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/commit/eefd5ef5d3d
    f01aed629f650959d6706d54cd335\"
              },
              \"html\": {
                \"href\":
    \"https://bitbucket.org/atlassian/bbql/commits/eefd5ef5d3df01aed629f650959d6706d54cd335\"
              }
            }
          }
        },
        {
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01ae
    d629f650959d6706d54cd335/tests/__init__.py\"
            },
            \"meta\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01ae
    d629f650959d6706d54cd335/tests/__init__.py?format=meta\"
            }
          },
          \"path\": \"tests/__init__.py\",
          \"commit\": {
            \"type\": \"commit\",
            \"hash\": \"eefd5ef5d3df01aed629f650959d6706d54cd335\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/commit/eefd5ef5d3d
    f01aed629f650959d6706d54cd335\"
              },
              \"html\": {
                \"href\":
    \"https://bitbucket.org/atlassian/bbql/commits/eefd5ef5d3df01aed629f650959d6706d54cd335\"
              }
            }
          },
          \"attributes\": [],
          \"type\": \"commit_file\",
          \"size\": 0
        }
      ],
      \"page\": 1,
      \"size\": 2
    }
    ```

    When listing the contents of the repo's root directory, the use of a
    trailing slash at the end of the URL is required.

    The response by default is not recursive, meaning that only the direct contents of
    a path are returned. The response does not recurse down into
    subdirectories. In order to \"walk\" the entire directory tree, the
    client can either parse each response and follow the `self` links of each
    `commit_directory` object, or can specify a `max_depth` to recurse to.

    The max_depth parameter will do a breadth-first search to return the contents of the subdirectories
    up to the depth specified. Breadth-first search was chosen as it leads to the least amount of
    file system operations for git. If the `max_depth` parameter is specified to be too
    large, the call will time out and return a 555.

    Each returned object is either a `commit_file`, or a `commit_directory`,
    both of which contain a `path` element. This path is the absolute path
    from the root of the repository. Each object also contains a `commit`
    object which embeds the commit the file is on. Note that this is merely
    the commit that was used in the URL. It is *not* the commit that last
    modified the file.

    Directory objects have 2 representations. Their `self` link returns the
    paginated contents of the directory. The `meta` link on the other hand
    returns the actual `directory` object itself, e.g.:

    ```javascript
    {
      \"path\": \"tests/test_project\",
      \"type\": \"commit_directory\",
      \"links\": {
        \"self\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629
    f650959d6706d54cd335/tests/test_project/\"
        },
        \"meta\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629
    f650959d6706d54cd335/tests/test_project/?format=meta\"
        }
      },
      \"commit\": { ... }
    }
    ```

    #### Querying, filtering and sorting

    Like most API endpoints, this API supports the Bitbucket
    querying/filtering syntax and so you could filter a directory listing
    to only include entries that match certain criteria. For instance, to
    list all binary files over 1kb use the expression:

    `size > 1024 and attributes = \"binary\"`

    which after urlencoding yields the query string:

    `?q=size%3E1024+and+attributes%3D%22binary%22`

    To change the ordering of the response, use the `?sort` parameter:

    `.../src/eefd5ef/?sort=-size`

    See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more
    details.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        path (str):
        format_ (GetRepositoriesWorkspaceRepoSlugSrcCommitPathFormat | Unset):
        q (str | Unset):
        sort (str | Unset):
        max_depth (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedTreeEntry]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        path=path,
        format_=format_,
        q=q,
        sort=sort,
        max_depth=max_depth,
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
    format_: GetRepositoriesWorkspaceRepoSlugSrcCommitPathFormat | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    max_depth: int | Unset = UNSET,
) -> ParsedPayload | None:
    r"""Get file or directory contents

     This endpoints is used to retrieve the contents of a single file,
    or the contents of a directory at a specified revision.

    #### Raw file contents

    When `path` points to a file, this endpoint returns the raw contents.
    The response's Content-Type is derived from the filename
    extension (not from the contents). The file contents are not processed
    and no character encoding/recoding is performed and as a result no
    character encoding is included as part of the Content-Type.

    The `Content-Disposition` header will be \"attachment\" to prevent
    browsers from running executable files.

    If the file is managed by LFS, then a 301 redirect pointing to
    Atlassian's media services platform is returned.

    The response includes an ETag that is based on the contents of the file
    and its attributes. This means that an empty `__init__.py` always
    returns the same ETag, regardless on the directory it lives in, or the
    commit it is on.

    #### File meta data

    When the request for a file path includes the query parameter
    `?format=meta`, instead of returning the file's raw contents, Bitbucket
    instead returns the JSON object describing the file's properties:

    ```javascript
    $ curl
    https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef/tests/__init__.py?format=meta
    {
      \"links\": {
        \"self\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629
    f650959d6706d54cd335/tests/__init__.py\"
        },
        \"meta\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629
    f650959d6706d54cd335/tests/__init__.py?format=meta\"
        }
      },
      \"path\": \"tests/__init__.py\",
      \"commit\": {
        \"type\": \"commit\",
        \"hash\": \"eefd5ef5d3df01aed629f650959d6706d54cd335\",
        \"links\": {
          \"self\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/commit/eefd5ef5d3df01a
    ed629f650959d6706d54cd335\"
          },
          \"html\": {
            \"href\":
    \"https://bitbucket.org/atlassian/bbql/commits/eefd5ef5d3df01aed629f650959d6706d54cd335\"
          }
        }
      },
      \"attributes\": [],
      \"type\": \"commit_file\",
      \"size\": 0
    }
    ```

    File objects contain an `attributes` element that contains a list of
    possible modifiers. Currently defined values are:

    * `link` -- indicates that the entry is a symbolic link. The contents
        of the file represent the path the link points to.
    * `executable` -- indicates that the file has the executable bit set.
    * `subrepository` -- indicates that the entry points to a submodule or
        subrepo. The contents of the file is the SHA1 of the repository
        pointed to.
    * `binary` -- indicates whether Bitbucket thinks the file is binary.

    This endpoint can provide an alternative to how a HEAD request can be
    used to check for the existence of a file, or a file's size without
    incurring the overhead of receiving its full contents.


    #### Directory listings

    When `path` points to a directory instead of a file, the response is a
    paginated list of directory and file objects in the same order as the
    underlying SCM system would return them.

    For example:

    ```javascript
    $ curl https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef/tests
    {
      \"pagelen\": 10,
      \"values\": [
        {
          \"path\": \"tests/test_project\",
          \"type\": \"commit_directory\",
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01ae
    d629f650959d6706d54cd335/tests/test_project/\"
            },
            \"meta\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01ae
    d629f650959d6706d54cd335/tests/test_project/?format=meta\"
            }
          },
          \"commit\": {
            \"type\": \"commit\",
            \"hash\": \"eefd5ef5d3df01aed629f650959d6706d54cd335\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/commit/eefd5ef5d3d
    f01aed629f650959d6706d54cd335\"
              },
              \"html\": {
                \"href\":
    \"https://bitbucket.org/atlassian/bbql/commits/eefd5ef5d3df01aed629f650959d6706d54cd335\"
              }
            }
          }
        },
        {
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01ae
    d629f650959d6706d54cd335/tests/__init__.py\"
            },
            \"meta\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01ae
    d629f650959d6706d54cd335/tests/__init__.py?format=meta\"
            }
          },
          \"path\": \"tests/__init__.py\",
          \"commit\": {
            \"type\": \"commit\",
            \"hash\": \"eefd5ef5d3df01aed629f650959d6706d54cd335\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/commit/eefd5ef5d3d
    f01aed629f650959d6706d54cd335\"
              },
              \"html\": {
                \"href\":
    \"https://bitbucket.org/atlassian/bbql/commits/eefd5ef5d3df01aed629f650959d6706d54cd335\"
              }
            }
          },
          \"attributes\": [],
          \"type\": \"commit_file\",
          \"size\": 0
        }
      ],
      \"page\": 1,
      \"size\": 2
    }
    ```

    When listing the contents of the repo's root directory, the use of a
    trailing slash at the end of the URL is required.

    The response by default is not recursive, meaning that only the direct contents of
    a path are returned. The response does not recurse down into
    subdirectories. In order to \"walk\" the entire directory tree, the
    client can either parse each response and follow the `self` links of each
    `commit_directory` object, or can specify a `max_depth` to recurse to.

    The max_depth parameter will do a breadth-first search to return the contents of the subdirectories
    up to the depth specified. Breadth-first search was chosen as it leads to the least amount of
    file system operations for git. If the `max_depth` parameter is specified to be too
    large, the call will time out and return a 555.

    Each returned object is either a `commit_file`, or a `commit_directory`,
    both of which contain a `path` element. This path is the absolute path
    from the root of the repository. Each object also contains a `commit`
    object which embeds the commit the file is on. Note that this is merely
    the commit that was used in the URL. It is *not* the commit that last
    modified the file.

    Directory objects have 2 representations. Their `self` link returns the
    paginated contents of the directory. The `meta` link on the other hand
    returns the actual `directory` object itself, e.g.:

    ```javascript
    {
      \"path\": \"tests/test_project\",
      \"type\": \"commit_directory\",
      \"links\": {
        \"self\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629
    f650959d6706d54cd335/tests/test_project/\"
        },
        \"meta\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629
    f650959d6706d54cd335/tests/test_project/?format=meta\"
        }
      },
      \"commit\": { ... }
    }
    ```

    #### Querying, filtering and sorting

    Like most API endpoints, this API supports the Bitbucket
    querying/filtering syntax and so you could filter a directory listing
    to only include entries that match certain criteria. For instance, to
    list all binary files over 1kb use the expression:

    `size > 1024 and attributes = \"binary\"`

    which after urlencoding yields the query string:

    `?q=size%3E1024+and+attributes%3D%22binary%22`

    To change the ordering of the response, use the `?sort` parameter:

    `.../src/eefd5ef/?sort=-size`

    See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more
    details.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        path (str):
        format_ (GetRepositoriesWorkspaceRepoSlugSrcCommitPathFormat | Unset):
        q (str | Unset):
        sort (str | Unset):
        max_depth (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedTreeEntry
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        path=path,
        client=client,
        format_=format_,
        q=q,
        sort=sort,
        max_depth=max_depth,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    commit: str,
    path: str,
    *,
    client: AuthenticatedClient,
    format_: GetRepositoriesWorkspaceRepoSlugSrcCommitPathFormat | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    max_depth: int | Unset = UNSET,
) -> Response[ParsedPayload]:
    r"""Get file or directory contents

     This endpoints is used to retrieve the contents of a single file,
    or the contents of a directory at a specified revision.

    #### Raw file contents

    When `path` points to a file, this endpoint returns the raw contents.
    The response's Content-Type is derived from the filename
    extension (not from the contents). The file contents are not processed
    and no character encoding/recoding is performed and as a result no
    character encoding is included as part of the Content-Type.

    The `Content-Disposition` header will be \"attachment\" to prevent
    browsers from running executable files.

    If the file is managed by LFS, then a 301 redirect pointing to
    Atlassian's media services platform is returned.

    The response includes an ETag that is based on the contents of the file
    and its attributes. This means that an empty `__init__.py` always
    returns the same ETag, regardless on the directory it lives in, or the
    commit it is on.

    #### File meta data

    When the request for a file path includes the query parameter
    `?format=meta`, instead of returning the file's raw contents, Bitbucket
    instead returns the JSON object describing the file's properties:

    ```javascript
    $ curl
    https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef/tests/__init__.py?format=meta
    {
      \"links\": {
        \"self\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629
    f650959d6706d54cd335/tests/__init__.py\"
        },
        \"meta\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629
    f650959d6706d54cd335/tests/__init__.py?format=meta\"
        }
      },
      \"path\": \"tests/__init__.py\",
      \"commit\": {
        \"type\": \"commit\",
        \"hash\": \"eefd5ef5d3df01aed629f650959d6706d54cd335\",
        \"links\": {
          \"self\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/commit/eefd5ef5d3df01a
    ed629f650959d6706d54cd335\"
          },
          \"html\": {
            \"href\":
    \"https://bitbucket.org/atlassian/bbql/commits/eefd5ef5d3df01aed629f650959d6706d54cd335\"
          }
        }
      },
      \"attributes\": [],
      \"type\": \"commit_file\",
      \"size\": 0
    }
    ```

    File objects contain an `attributes` element that contains a list of
    possible modifiers. Currently defined values are:

    * `link` -- indicates that the entry is a symbolic link. The contents
        of the file represent the path the link points to.
    * `executable` -- indicates that the file has the executable bit set.
    * `subrepository` -- indicates that the entry points to a submodule or
        subrepo. The contents of the file is the SHA1 of the repository
        pointed to.
    * `binary` -- indicates whether Bitbucket thinks the file is binary.

    This endpoint can provide an alternative to how a HEAD request can be
    used to check for the existence of a file, or a file's size without
    incurring the overhead of receiving its full contents.


    #### Directory listings

    When `path` points to a directory instead of a file, the response is a
    paginated list of directory and file objects in the same order as the
    underlying SCM system would return them.

    For example:

    ```javascript
    $ curl https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef/tests
    {
      \"pagelen\": 10,
      \"values\": [
        {
          \"path\": \"tests/test_project\",
          \"type\": \"commit_directory\",
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01ae
    d629f650959d6706d54cd335/tests/test_project/\"
            },
            \"meta\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01ae
    d629f650959d6706d54cd335/tests/test_project/?format=meta\"
            }
          },
          \"commit\": {
            \"type\": \"commit\",
            \"hash\": \"eefd5ef5d3df01aed629f650959d6706d54cd335\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/commit/eefd5ef5d3d
    f01aed629f650959d6706d54cd335\"
              },
              \"html\": {
                \"href\":
    \"https://bitbucket.org/atlassian/bbql/commits/eefd5ef5d3df01aed629f650959d6706d54cd335\"
              }
            }
          }
        },
        {
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01ae
    d629f650959d6706d54cd335/tests/__init__.py\"
            },
            \"meta\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01ae
    d629f650959d6706d54cd335/tests/__init__.py?format=meta\"
            }
          },
          \"path\": \"tests/__init__.py\",
          \"commit\": {
            \"type\": \"commit\",
            \"hash\": \"eefd5ef5d3df01aed629f650959d6706d54cd335\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/commit/eefd5ef5d3d
    f01aed629f650959d6706d54cd335\"
              },
              \"html\": {
                \"href\":
    \"https://bitbucket.org/atlassian/bbql/commits/eefd5ef5d3df01aed629f650959d6706d54cd335\"
              }
            }
          },
          \"attributes\": [],
          \"type\": \"commit_file\",
          \"size\": 0
        }
      ],
      \"page\": 1,
      \"size\": 2
    }
    ```

    When listing the contents of the repo's root directory, the use of a
    trailing slash at the end of the URL is required.

    The response by default is not recursive, meaning that only the direct contents of
    a path are returned. The response does not recurse down into
    subdirectories. In order to \"walk\" the entire directory tree, the
    client can either parse each response and follow the `self` links of each
    `commit_directory` object, or can specify a `max_depth` to recurse to.

    The max_depth parameter will do a breadth-first search to return the contents of the subdirectories
    up to the depth specified. Breadth-first search was chosen as it leads to the least amount of
    file system operations for git. If the `max_depth` parameter is specified to be too
    large, the call will time out and return a 555.

    Each returned object is either a `commit_file`, or a `commit_directory`,
    both of which contain a `path` element. This path is the absolute path
    from the root of the repository. Each object also contains a `commit`
    object which embeds the commit the file is on. Note that this is merely
    the commit that was used in the URL. It is *not* the commit that last
    modified the file.

    Directory objects have 2 representations. Their `self` link returns the
    paginated contents of the directory. The `meta` link on the other hand
    returns the actual `directory` object itself, e.g.:

    ```javascript
    {
      \"path\": \"tests/test_project\",
      \"type\": \"commit_directory\",
      \"links\": {
        \"self\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629
    f650959d6706d54cd335/tests/test_project/\"
        },
        \"meta\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629
    f650959d6706d54cd335/tests/test_project/?format=meta\"
        }
      },
      \"commit\": { ... }
    }
    ```

    #### Querying, filtering and sorting

    Like most API endpoints, this API supports the Bitbucket
    querying/filtering syntax and so you could filter a directory listing
    to only include entries that match certain criteria. For instance, to
    list all binary files over 1kb use the expression:

    `size > 1024 and attributes = \"binary\"`

    which after urlencoding yields the query string:

    `?q=size%3E1024+and+attributes%3D%22binary%22`

    To change the ordering of the response, use the `?sort` parameter:

    `.../src/eefd5ef/?sort=-size`

    See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more
    details.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        path (str):
        format_ (GetRepositoriesWorkspaceRepoSlugSrcCommitPathFormat | Unset):
        q (str | Unset):
        sort (str | Unset):
        max_depth (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PaginatedTreeEntry]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        path=path,
        format_=format_,
        q=q,
        sort=sort,
        max_depth=max_depth,
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
    format_: GetRepositoriesWorkspaceRepoSlugSrcCommitPathFormat | Unset = UNSET,
    q: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    max_depth: int | Unset = UNSET,
) -> ParsedPayload | None:
    r"""Get file or directory contents

     This endpoints is used to retrieve the contents of a single file,
    or the contents of a directory at a specified revision.

    #### Raw file contents

    When `path` points to a file, this endpoint returns the raw contents.
    The response's Content-Type is derived from the filename
    extension (not from the contents). The file contents are not processed
    and no character encoding/recoding is performed and as a result no
    character encoding is included as part of the Content-Type.

    The `Content-Disposition` header will be \"attachment\" to prevent
    browsers from running executable files.

    If the file is managed by LFS, then a 301 redirect pointing to
    Atlassian's media services platform is returned.

    The response includes an ETag that is based on the contents of the file
    and its attributes. This means that an empty `__init__.py` always
    returns the same ETag, regardless on the directory it lives in, or the
    commit it is on.

    #### File meta data

    When the request for a file path includes the query parameter
    `?format=meta`, instead of returning the file's raw contents, Bitbucket
    instead returns the JSON object describing the file's properties:

    ```javascript
    $ curl
    https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef/tests/__init__.py?format=meta
    {
      \"links\": {
        \"self\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629
    f650959d6706d54cd335/tests/__init__.py\"
        },
        \"meta\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629
    f650959d6706d54cd335/tests/__init__.py?format=meta\"
        }
      },
      \"path\": \"tests/__init__.py\",
      \"commit\": {
        \"type\": \"commit\",
        \"hash\": \"eefd5ef5d3df01aed629f650959d6706d54cd335\",
        \"links\": {
          \"self\": {
            \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/commit/eefd5ef5d3df01a
    ed629f650959d6706d54cd335\"
          },
          \"html\": {
            \"href\":
    \"https://bitbucket.org/atlassian/bbql/commits/eefd5ef5d3df01aed629f650959d6706d54cd335\"
          }
        }
      },
      \"attributes\": [],
      \"type\": \"commit_file\",
      \"size\": 0
    }
    ```

    File objects contain an `attributes` element that contains a list of
    possible modifiers. Currently defined values are:

    * `link` -- indicates that the entry is a symbolic link. The contents
        of the file represent the path the link points to.
    * `executable` -- indicates that the file has the executable bit set.
    * `subrepository` -- indicates that the entry points to a submodule or
        subrepo. The contents of the file is the SHA1 of the repository
        pointed to.
    * `binary` -- indicates whether Bitbucket thinks the file is binary.

    This endpoint can provide an alternative to how a HEAD request can be
    used to check for the existence of a file, or a file's size without
    incurring the overhead of receiving its full contents.


    #### Directory listings

    When `path` points to a directory instead of a file, the response is a
    paginated list of directory and file objects in the same order as the
    underlying SCM system would return them.

    For example:

    ```javascript
    $ curl https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef/tests
    {
      \"pagelen\": 10,
      \"values\": [
        {
          \"path\": \"tests/test_project\",
          \"type\": \"commit_directory\",
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01ae
    d629f650959d6706d54cd335/tests/test_project/\"
            },
            \"meta\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01ae
    d629f650959d6706d54cd335/tests/test_project/?format=meta\"
            }
          },
          \"commit\": {
            \"type\": \"commit\",
            \"hash\": \"eefd5ef5d3df01aed629f650959d6706d54cd335\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/commit/eefd5ef5d3d
    f01aed629f650959d6706d54cd335\"
              },
              \"html\": {
                \"href\":
    \"https://bitbucket.org/atlassian/bbql/commits/eefd5ef5d3df01aed629f650959d6706d54cd335\"
              }
            }
          }
        },
        {
          \"links\": {
            \"self\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01ae
    d629f650959d6706d54cd335/tests/__init__.py\"
            },
            \"meta\": {
              \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01ae
    d629f650959d6706d54cd335/tests/__init__.py?format=meta\"
            }
          },
          \"path\": \"tests/__init__.py\",
          \"commit\": {
            \"type\": \"commit\",
            \"hash\": \"eefd5ef5d3df01aed629f650959d6706d54cd335\",
            \"links\": {
              \"self\": {
                \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/commit/eefd5ef5d3d
    f01aed629f650959d6706d54cd335\"
              },
              \"html\": {
                \"href\":
    \"https://bitbucket.org/atlassian/bbql/commits/eefd5ef5d3df01aed629f650959d6706d54cd335\"
              }
            }
          },
          \"attributes\": [],
          \"type\": \"commit_file\",
          \"size\": 0
        }
      ],
      \"page\": 1,
      \"size\": 2
    }
    ```

    When listing the contents of the repo's root directory, the use of a
    trailing slash at the end of the URL is required.

    The response by default is not recursive, meaning that only the direct contents of
    a path are returned. The response does not recurse down into
    subdirectories. In order to \"walk\" the entire directory tree, the
    client can either parse each response and follow the `self` links of each
    `commit_directory` object, or can specify a `max_depth` to recurse to.

    The max_depth parameter will do a breadth-first search to return the contents of the subdirectories
    up to the depth specified. Breadth-first search was chosen as it leads to the least amount of
    file system operations for git. If the `max_depth` parameter is specified to be too
    large, the call will time out and return a 555.

    Each returned object is either a `commit_file`, or a `commit_directory`,
    both of which contain a `path` element. This path is the absolute path
    from the root of the repository. Each object also contains a `commit`
    object which embeds the commit the file is on. Note that this is merely
    the commit that was used in the URL. It is *not* the commit that last
    modified the file.

    Directory objects have 2 representations. Their `self` link returns the
    paginated contents of the directory. The `meta` link on the other hand
    returns the actual `directory` object itself, e.g.:

    ```javascript
    {
      \"path\": \"tests/test_project\",
      \"type\": \"commit_directory\",
      \"links\": {
        \"self\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629
    f650959d6706d54cd335/tests/test_project/\"
        },
        \"meta\": {
          \"href\": \"https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629
    f650959d6706d54cd335/tests/test_project/?format=meta\"
        }
      },
      \"commit\": { ... }
    }
    ```

    #### Querying, filtering and sorting

    Like most API endpoints, this API supports the Bitbucket
    querying/filtering syntax and so you could filter a directory listing
    to only include entries that match certain criteria. For instance, to
    list all binary files over 1kb use the expression:

    `size > 1024 and attributes = \"binary\"`

    which after urlencoding yields the query string:

    `?q=size%3E1024+and+attributes%3D%22binary%22`

    To change the ordering of the response, use the `?sort` parameter:

    `.../src/eefd5ef/?sort=-size`

    See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more
    details.

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        path (str):
        format_ (GetRepositoriesWorkspaceRepoSlugSrcCommitPathFormat | Unset):
        q (str | Unset):
        sort (str | Unset):
        max_depth (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PaginatedTreeEntry
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            commit=commit,
            path=path,
            client=client,
            format_=format_,
            q=q,
            sort=sort,
            max_depth=max_depth,
        )
    ).parsed
