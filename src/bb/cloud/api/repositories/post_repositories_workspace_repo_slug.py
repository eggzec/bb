from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
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
        "url": "/repositories/{workspace}/{repo_slug}".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Error | Repository
type ParseResult = Error | Repository | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_200 = Repository.from_dict(response.json())

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
    r"""Create a repository

     Creates a new repository.

    Note: In order to set the project for the newly created repository,
    pass in either the project key or the project UUID as part of the
    request body as shown in the examples below:

    ```
    $ curl -X POST -H \"Content-Type: application/json\" -d '{
        \"scm\": \"git\",
        \"project\": {
            \"key\": \"MARS\"
        }
    }' https://api.bitbucket.org/2.0/repositories/teamsinspace/hablanding
    ```

    or

    ```
    $ curl -X POST -H \"Content-Type: application/json\" -d '{
        \"scm\": \"git\",
        \"project\": {
            \"key\": \"{ba516952-992a-4c2d-acbd-17d502922f96}\"
        }
    }' https://api.bitbucket.org/2.0/repositories/teamsinspace/hablanding
    ```

    The project must be assigned for all repositories. If the project is not provided,
    the repository is automatically assigned to the oldest project in the workspace.

    Note: In the examples above, the workspace ID `teamsinspace`,
    and/or the repository name `hablanding` can be replaced by UUIDs.

    Args:
        workspace (str):
        repo_slug (str):
        body (Repository | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Repository]
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
    r"""Create a repository

     Creates a new repository.

    Note: In order to set the project for the newly created repository,
    pass in either the project key or the project UUID as part of the
    request body as shown in the examples below:

    ```
    $ curl -X POST -H \"Content-Type: application/json\" -d '{
        \"scm\": \"git\",
        \"project\": {
            \"key\": \"MARS\"
        }
    }' https://api.bitbucket.org/2.0/repositories/teamsinspace/hablanding
    ```

    or

    ```
    $ curl -X POST -H \"Content-Type: application/json\" -d '{
        \"scm\": \"git\",
        \"project\": {
            \"key\": \"{ba516952-992a-4c2d-acbd-17d502922f96}\"
        }
    }' https://api.bitbucket.org/2.0/repositories/teamsinspace/hablanding
    ```

    The project must be assigned for all repositories. If the project is not provided,
    the repository is automatically assigned to the oldest project in the workspace.

    Note: In the examples above, the workspace ID `teamsinspace`,
    and/or the repository name `hablanding` can be replaced by UUIDs.

    Args:
        workspace (str):
        repo_slug (str):
        body (Repository | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Repository
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
    r"""Create a repository

     Creates a new repository.

    Note: In order to set the project for the newly created repository,
    pass in either the project key or the project UUID as part of the
    request body as shown in the examples below:

    ```
    $ curl -X POST -H \"Content-Type: application/json\" -d '{
        \"scm\": \"git\",
        \"project\": {
            \"key\": \"MARS\"
        }
    }' https://api.bitbucket.org/2.0/repositories/teamsinspace/hablanding
    ```

    or

    ```
    $ curl -X POST -H \"Content-Type: application/json\" -d '{
        \"scm\": \"git\",
        \"project\": {
            \"key\": \"{ba516952-992a-4c2d-acbd-17d502922f96}\"
        }
    }' https://api.bitbucket.org/2.0/repositories/teamsinspace/hablanding
    ```

    The project must be assigned for all repositories. If the project is not provided,
    the repository is automatically assigned to the oldest project in the workspace.

    Note: In the examples above, the workspace ID `teamsinspace`,
    and/or the repository name `hablanding` can be replaced by UUIDs.

    Args:
        workspace (str):
        repo_slug (str):
        body (Repository | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Repository]
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
    r"""Create a repository

     Creates a new repository.

    Note: In order to set the project for the newly created repository,
    pass in either the project key or the project UUID as part of the
    request body as shown in the examples below:

    ```
    $ curl -X POST -H \"Content-Type: application/json\" -d '{
        \"scm\": \"git\",
        \"project\": {
            \"key\": \"MARS\"
        }
    }' https://api.bitbucket.org/2.0/repositories/teamsinspace/hablanding
    ```

    or

    ```
    $ curl -X POST -H \"Content-Type: application/json\" -d '{
        \"scm\": \"git\",
        \"project\": {
            \"key\": \"{ba516952-992a-4c2d-acbd-17d502922f96}\"
        }
    }' https://api.bitbucket.org/2.0/repositories/teamsinspace/hablanding
    ```

    The project must be assigned for all repositories. If the project is not provided,
    the repository is automatically assigned to the oldest project in the workspace.

    Note: In the examples above, the workspace ID `teamsinspace`,
    and/or the repository name `hablanding` can be replaced by UUIDs.

    Args:
        workspace (str):
        repo_slug (str):
        body (Repository | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Repository
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
            body=body,
        )
    ).parsed
