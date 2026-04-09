from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.repository import Repository
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
    body: Repository | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/repositories/{workspace}/{repo_slug}/forks".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Repository
type ParseResult = Repository | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 201:
        response_201 = Repository.from_dict(response.json())

        return response_201

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
    body: Repository | Unset = UNSET,
) -> Response[ParsedPayload]:
    r""" Fork a repository

     Creates a new fork of the specified repository.

    #### Forking a repository

    To create a fork, specify the workspace explicitly as part of the
    request body:

    ```
    $ curl -X POST -u jdoe https://api.bitbucket.org/2.0/repositories/atlassian/bbql/forks \
      -H 'Content-Type: application/json' -d '{
        \"name\": \"bbql_fork\",
        \"workspace\": {
          \"slug\": \"atlassian\"
        }
    }'
    ```

    To fork a repository into the same workspace, also specify a new `name`.

    When you specify a value for `name`, it will also affect the `slug`.
    The `slug` is reflected in the repository URL of the new fork. It is
    derived from `name` by substituting non-ASCII characters, removes
    whitespace, and changes characters to lower case. For example,
    `My repo` would turn into `my_repo`.

    You need contributor access to create new forks within a workspace.


    #### Change the properties of a new fork

    By default the fork inherits most of its properties from the parent.
    However, since the optional POST body document follows the normal
    `repository` JSON schema and you can override the new fork's
    properties.

    Properties that can be overridden include:

    * description
    * fork_policy
    * language
    * mainbranch
    * is_private (note that a private repo's fork_policy might prohibit
      the creation of public forks, in which `is_private=False` would fail)
    * has_issues (to initialize or disable the new repo's issue tracker --
      note that the actual contents of the parent repository's issue
      tracker are not copied during forking)
    * has_wiki (to initialize or disable the new repo's wiki --
      note that the actual contents of the parent repository's wiki are not
      copied during forking)
    * project (when forking into a private project, the fork's `is_private`
      must be `true`)

    Properties that cannot be modified include:

    * scm
    * parent
    * full_name

    Args:
        workspace (str):
        repo_slug (str):
        body (Repository | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Repository]
     """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        body=body,
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
    body: Repository | Unset = UNSET,
) -> ParsedPayload | None:
    r""" Fork a repository

     Creates a new fork of the specified repository.

    #### Forking a repository

    To create a fork, specify the workspace explicitly as part of the
    request body:

    ```
    $ curl -X POST -u jdoe https://api.bitbucket.org/2.0/repositories/atlassian/bbql/forks \
      -H 'Content-Type: application/json' -d '{
        \"name\": \"bbql_fork\",
        \"workspace\": {
          \"slug\": \"atlassian\"
        }
    }'
    ```

    To fork a repository into the same workspace, also specify a new `name`.

    When you specify a value for `name`, it will also affect the `slug`.
    The `slug` is reflected in the repository URL of the new fork. It is
    derived from `name` by substituting non-ASCII characters, removes
    whitespace, and changes characters to lower case. For example,
    `My repo` would turn into `my_repo`.

    You need contributor access to create new forks within a workspace.


    #### Change the properties of a new fork

    By default the fork inherits most of its properties from the parent.
    However, since the optional POST body document follows the normal
    `repository` JSON schema and you can override the new fork's
    properties.

    Properties that can be overridden include:

    * description
    * fork_policy
    * language
    * mainbranch
    * is_private (note that a private repo's fork_policy might prohibit
      the creation of public forks, in which `is_private=False` would fail)
    * has_issues (to initialize or disable the new repo's issue tracker --
      note that the actual contents of the parent repository's issue
      tracker are not copied during forking)
    * has_wiki (to initialize or disable the new repo's wiki --
      note that the actual contents of the parent repository's wiki are not
      copied during forking)
    * project (when forking into a private project, the fork's `is_private`
      must be `true`)

    Properties that cannot be modified include:

    * scm
    * parent
    * full_name

    Args:
        workspace (str):
        repo_slug (str):
        body (Repository | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Repository
     """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    body: Repository | Unset = UNSET,
) -> Response[ParsedPayload]:
    r""" Fork a repository

     Creates a new fork of the specified repository.

    #### Forking a repository

    To create a fork, specify the workspace explicitly as part of the
    request body:

    ```
    $ curl -X POST -u jdoe https://api.bitbucket.org/2.0/repositories/atlassian/bbql/forks \
      -H 'Content-Type: application/json' -d '{
        \"name\": \"bbql_fork\",
        \"workspace\": {
          \"slug\": \"atlassian\"
        }
    }'
    ```

    To fork a repository into the same workspace, also specify a new `name`.

    When you specify a value for `name`, it will also affect the `slug`.
    The `slug` is reflected in the repository URL of the new fork. It is
    derived from `name` by substituting non-ASCII characters, removes
    whitespace, and changes characters to lower case. For example,
    `My repo` would turn into `my_repo`.

    You need contributor access to create new forks within a workspace.


    #### Change the properties of a new fork

    By default the fork inherits most of its properties from the parent.
    However, since the optional POST body document follows the normal
    `repository` JSON schema and you can override the new fork's
    properties.

    Properties that can be overridden include:

    * description
    * fork_policy
    * language
    * mainbranch
    * is_private (note that a private repo's fork_policy might prohibit
      the creation of public forks, in which `is_private=False` would fail)
    * has_issues (to initialize or disable the new repo's issue tracker --
      note that the actual contents of the parent repository's issue
      tracker are not copied during forking)
    * has_wiki (to initialize or disable the new repo's wiki --
      note that the actual contents of the parent repository's wiki are not
      copied during forking)
    * project (when forking into a private project, the fork's `is_private`
      must be `true`)

    Properties that cannot be modified include:

    * scm
    * parent
    * full_name

    Args:
        workspace (str):
        repo_slug (str):
        body (Repository | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Repository]
     """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    *,
    client: AuthenticatedClient,
    body: Repository | Unset = UNSET,
) -> ParsedPayload | None:
    r""" Fork a repository

     Creates a new fork of the specified repository.

    #### Forking a repository

    To create a fork, specify the workspace explicitly as part of the
    request body:

    ```
    $ curl -X POST -u jdoe https://api.bitbucket.org/2.0/repositories/atlassian/bbql/forks \
      -H 'Content-Type: application/json' -d '{
        \"name\": \"bbql_fork\",
        \"workspace\": {
          \"slug\": \"atlassian\"
        }
    }'
    ```

    To fork a repository into the same workspace, also specify a new `name`.

    When you specify a value for `name`, it will also affect the `slug`.
    The `slug` is reflected in the repository URL of the new fork. It is
    derived from `name` by substituting non-ASCII characters, removes
    whitespace, and changes characters to lower case. For example,
    `My repo` would turn into `my_repo`.

    You need contributor access to create new forks within a workspace.


    #### Change the properties of a new fork

    By default the fork inherits most of its properties from the parent.
    However, since the optional POST body document follows the normal
    `repository` JSON schema and you can override the new fork's
    properties.

    Properties that can be overridden include:

    * description
    * fork_policy
    * language
    * mainbranch
    * is_private (note that a private repo's fork_policy might prohibit
      the creation of public forks, in which `is_private=False` would fail)
    * has_issues (to initialize or disable the new repo's issue tracker --
      note that the actual contents of the parent repository's issue
      tracker are not copied during forking)
    * has_wiki (to initialize or disable the new repo's wiki --
      note that the actual contents of the parent repository's wiki are not
      copied during forking)
    * project (when forking into a private project, the fork's `is_private`
      must be `true`)

    Properties that cannot be modified include:

    * scm
    * parent
    * full_name

    Args:
        workspace (str):
        repo_slug (str):
        body (Repository | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Repository
     """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
            body=body,
        )
    ).parsed
