from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.pullrequest import Pullrequest
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
    body: Pullrequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/repositories/{workspace}/{repo_slug}/pullrequests".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Error | Pullrequest
type ParseResult = Error | Pullrequest | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 201:
        response_201 = Pullrequest.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

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
    body: Pullrequest | Unset = UNSET,
) -> Response[ParsedPayload]:
    r""" Create a pull request

     Creates a new pull request where the destination repository is
    this repository and the author is the authenticated user.

    The minimum required fields to create a pull request are `title` and
    `source`, specified by a branch name.

    ```
    curl https://api.bitbucket.org/2.0/repositories/my-workspace/my-repository/pullrequests \
        -u my-username:my-password \
        --request POST \
        --header 'Content-Type: application/json' \
        --data '{
            \"title\": \"My Title\",
            \"source\": {
                \"branch\": {
                    \"name\": \"staging\"
                }
            }
        }'
    ```

    If the pull request's `destination` is not specified, it will default
    to the `repository.mainbranch`. To open a pull request to a
    different branch, say from a feature branch to a staging branch,
    specify a `destination` (same format as the `source`):

    ```
    {
        \"title\": \"My Title\",
        \"source\": {
            \"branch\": {
                \"name\": \"my-feature-branch\"
            }
        },
        \"destination\": {
            \"branch\": {
                \"name\": \"staging\"
            }
        }
    }
    ```

    Reviewers can be specified by adding an array of user objects as the
    `reviewers` property.

    ```
    {
        \"title\": \"My Title\",
        \"source\": {
            \"branch\": {
                \"name\": \"my-feature-branch\"
            }
        },
        \"reviewers\": [
            {
                \"uuid\": \"{504c3b62-8120-4f0c-a7bc-87800b9d6f70}\"
            }
        ]
    }
    ```

    Other fields:

    * `description` - a string
    * `close_source_branch` - boolean that specifies if the source branch should be closed upon merging
    * `draft` - boolean that specifies whether the pull request is a draft

    Args:
        workspace (str):
        repo_slug (str):
        body (Pullrequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Pullrequest]
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
    body: Pullrequest | Unset = UNSET,
) -> ParsedPayload | None:
    r""" Create a pull request

     Creates a new pull request where the destination repository is
    this repository and the author is the authenticated user.

    The minimum required fields to create a pull request are `title` and
    `source`, specified by a branch name.

    ```
    curl https://api.bitbucket.org/2.0/repositories/my-workspace/my-repository/pullrequests \
        -u my-username:my-password \
        --request POST \
        --header 'Content-Type: application/json' \
        --data '{
            \"title\": \"My Title\",
            \"source\": {
                \"branch\": {
                    \"name\": \"staging\"
                }
            }
        }'
    ```

    If the pull request's `destination` is not specified, it will default
    to the `repository.mainbranch`. To open a pull request to a
    different branch, say from a feature branch to a staging branch,
    specify a `destination` (same format as the `source`):

    ```
    {
        \"title\": \"My Title\",
        \"source\": {
            \"branch\": {
                \"name\": \"my-feature-branch\"
            }
        },
        \"destination\": {
            \"branch\": {
                \"name\": \"staging\"
            }
        }
    }
    ```

    Reviewers can be specified by adding an array of user objects as the
    `reviewers` property.

    ```
    {
        \"title\": \"My Title\",
        \"source\": {
            \"branch\": {
                \"name\": \"my-feature-branch\"
            }
        },
        \"reviewers\": [
            {
                \"uuid\": \"{504c3b62-8120-4f0c-a7bc-87800b9d6f70}\"
            }
        ]
    }
    ```

    Other fields:

    * `description` - a string
    * `close_source_branch` - boolean that specifies if the source branch should be closed upon merging
    * `draft` - boolean that specifies whether the pull request is a draft

    Args:
        workspace (str):
        repo_slug (str):
        body (Pullrequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Pullrequest
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
    body: Pullrequest | Unset = UNSET,
) -> Response[ParsedPayload]:
    r""" Create a pull request

     Creates a new pull request where the destination repository is
    this repository and the author is the authenticated user.

    The minimum required fields to create a pull request are `title` and
    `source`, specified by a branch name.

    ```
    curl https://api.bitbucket.org/2.0/repositories/my-workspace/my-repository/pullrequests \
        -u my-username:my-password \
        --request POST \
        --header 'Content-Type: application/json' \
        --data '{
            \"title\": \"My Title\",
            \"source\": {
                \"branch\": {
                    \"name\": \"staging\"
                }
            }
        }'
    ```

    If the pull request's `destination` is not specified, it will default
    to the `repository.mainbranch`. To open a pull request to a
    different branch, say from a feature branch to a staging branch,
    specify a `destination` (same format as the `source`):

    ```
    {
        \"title\": \"My Title\",
        \"source\": {
            \"branch\": {
                \"name\": \"my-feature-branch\"
            }
        },
        \"destination\": {
            \"branch\": {
                \"name\": \"staging\"
            }
        }
    }
    ```

    Reviewers can be specified by adding an array of user objects as the
    `reviewers` property.

    ```
    {
        \"title\": \"My Title\",
        \"source\": {
            \"branch\": {
                \"name\": \"my-feature-branch\"
            }
        },
        \"reviewers\": [
            {
                \"uuid\": \"{504c3b62-8120-4f0c-a7bc-87800b9d6f70}\"
            }
        ]
    }
    ```

    Other fields:

    * `description` - a string
    * `close_source_branch` - boolean that specifies if the source branch should be closed upon merging
    * `draft` - boolean that specifies whether the pull request is a draft

    Args:
        workspace (str):
        repo_slug (str):
        body (Pullrequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Pullrequest]
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
    body: Pullrequest | Unset = UNSET,
) -> ParsedPayload | None:
    r""" Create a pull request

     Creates a new pull request where the destination repository is
    this repository and the author is the authenticated user.

    The minimum required fields to create a pull request are `title` and
    `source`, specified by a branch name.

    ```
    curl https://api.bitbucket.org/2.0/repositories/my-workspace/my-repository/pullrequests \
        -u my-username:my-password \
        --request POST \
        --header 'Content-Type: application/json' \
        --data '{
            \"title\": \"My Title\",
            \"source\": {
                \"branch\": {
                    \"name\": \"staging\"
                }
            }
        }'
    ```

    If the pull request's `destination` is not specified, it will default
    to the `repository.mainbranch`. To open a pull request to a
    different branch, say from a feature branch to a staging branch,
    specify a `destination` (same format as the `source`):

    ```
    {
        \"title\": \"My Title\",
        \"source\": {
            \"branch\": {
                \"name\": \"my-feature-branch\"
            }
        },
        \"destination\": {
            \"branch\": {
                \"name\": \"staging\"
            }
        }
    }
    ```

    Reviewers can be specified by adding an array of user objects as the
    `reviewers` property.

    ```
    {
        \"title\": \"My Title\",
        \"source\": {
            \"branch\": {
                \"name\": \"my-feature-branch\"
            }
        },
        \"reviewers\": [
            {
                \"uuid\": \"{504c3b62-8120-4f0c-a7bc-87800b9d6f70}\"
            }
        ]
    }
    ```

    Other fields:

    * `description` - a string
    * `close_source_branch` - boolean that specifies if the source branch should be closed upon merging
    * `draft` - boolean that specifies whether the pull request is a draft

    Args:
        workspace (str):
        repo_slug (str):
        body (Pullrequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Pullrequest
     """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
            body=body,
        )
    ).parsed
