from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
    "sync",
    "asyncio",
]


def _get_kwargs(
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    task_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/merge/task-status/{task_id}".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
            pull_request_id=quote(str(pull_request_id), safe=""),
            task_id=quote(str(task_id), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Any | Error
type ParseResult = Any | Error | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

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
    pull_request_id: int,
    task_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    r"""Get the merge task status for a pull request

     When merging a pull request takes too long, the client receives a
    task ID along with a 202 status code. The task ID can be used in a call
    to this endpoint to check the status of a merge task.

    ```
    curl -X GET
    https://api.bitbucket.org/2.0/repositories/atlassian/bitbucket/pullrequests/2286/merge/task-
    status/<task_id>
    ```

    If the merge task is not yet finished, a PENDING status will be returned.

    ```
    HTTP/2 200
    {
        \"task_status\": \"PENDING\",
        \"links\": {
            \"self\": {
                \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/bitbucket/pullrequests/2286/merge/task-
    status/<task_id>\"
            }
        }
    }
    ```

    If the merge was successful, a SUCCESS status will be returned.

    ```
    HTTP/2 200
    {
        \"task_status\": \"SUCCESS\",
        \"links\": {
            \"self\": {
                \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/bitbucket/pullrequests/2286/merge/task-
    status/<task_id>\"
            }
        },
        \"merge_result\": <the merged pull request object>
    }
    ```

    If the merge task failed, an error will be returned.

    ```
    {
        \"type\": \"error\",
        \"error\": {
            \"message\": \"<error message>\"
        }
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):
        pull_request_id (int):
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        pull_request_id=pull_request_id,
        task_id=task_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    task_id: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    r"""Get the merge task status for a pull request

     When merging a pull request takes too long, the client receives a
    task ID along with a 202 status code. The task ID can be used in a call
    to this endpoint to check the status of a merge task.

    ```
    curl -X GET
    https://api.bitbucket.org/2.0/repositories/atlassian/bitbucket/pullrequests/2286/merge/task-
    status/<task_id>
    ```

    If the merge task is not yet finished, a PENDING status will be returned.

    ```
    HTTP/2 200
    {
        \"task_status\": \"PENDING\",
        \"links\": {
            \"self\": {
                \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/bitbucket/pullrequests/2286/merge/task-
    status/<task_id>\"
            }
        }
    }
    ```

    If the merge was successful, a SUCCESS status will be returned.

    ```
    HTTP/2 200
    {
        \"task_status\": \"SUCCESS\",
        \"links\": {
            \"self\": {
                \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/bitbucket/pullrequests/2286/merge/task-
    status/<task_id>\"
            }
        },
        \"merge_result\": <the merged pull request object>
    }
    ```

    If the merge task failed, an error will be returned.

    ```
    {
        \"type\": \"error\",
        \"error\": {
            \"message\": \"<error message>\"
        }
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):
        pull_request_id (int):
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        pull_request_id=pull_request_id,
        task_id=task_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    task_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    r"""Get the merge task status for a pull request

     When merging a pull request takes too long, the client receives a
    task ID along with a 202 status code. The task ID can be used in a call
    to this endpoint to check the status of a merge task.

    ```
    curl -X GET
    https://api.bitbucket.org/2.0/repositories/atlassian/bitbucket/pullrequests/2286/merge/task-
    status/<task_id>
    ```

    If the merge task is not yet finished, a PENDING status will be returned.

    ```
    HTTP/2 200
    {
        \"task_status\": \"PENDING\",
        \"links\": {
            \"self\": {
                \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/bitbucket/pullrequests/2286/merge/task-
    status/<task_id>\"
            }
        }
    }
    ```

    If the merge was successful, a SUCCESS status will be returned.

    ```
    HTTP/2 200
    {
        \"task_status\": \"SUCCESS\",
        \"links\": {
            \"self\": {
                \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/bitbucket/pullrequests/2286/merge/task-
    status/<task_id>\"
            }
        },
        \"merge_result\": <the merged pull request object>
    }
    ```

    If the merge task failed, an error will be returned.

    ```
    {
        \"type\": \"error\",
        \"error\": {
            \"message\": \"<error message>\"
        }
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):
        pull_request_id (int):
        task_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        pull_request_id=pull_request_id,
        task_id=task_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    pull_request_id: int,
    task_id: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    r"""Get the merge task status for a pull request

     When merging a pull request takes too long, the client receives a
    task ID along with a 202 status code. The task ID can be used in a call
    to this endpoint to check the status of a merge task.

    ```
    curl -X GET
    https://api.bitbucket.org/2.0/repositories/atlassian/bitbucket/pullrequests/2286/merge/task-
    status/<task_id>
    ```

    If the merge task is not yet finished, a PENDING status will be returned.

    ```
    HTTP/2 200
    {
        \"task_status\": \"PENDING\",
        \"links\": {
            \"self\": {
                \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/bitbucket/pullrequests/2286/merge/task-
    status/<task_id>\"
            }
        }
    }
    ```

    If the merge was successful, a SUCCESS status will be returned.

    ```
    HTTP/2 200
    {
        \"task_status\": \"SUCCESS\",
        \"links\": {
            \"self\": {
                \"href\":
    \"https://api.bitbucket.org/2.0/repositories/atlassian/bitbucket/pullrequests/2286/merge/task-
    status/<task_id>\"
            }
        },
        \"merge_result\": <the merged pull request object>
    }
    ```

    If the merge task failed, an error will be returned.

    ```
    {
        \"type\": \"error\",
        \"error\": {
            \"message\": \"<error message>\"
        }
    }
    ```

    Args:
        workspace (str):
        repo_slug (str):
        pull_request_id (int):
        task_id (str):

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
            pull_request_id=pull_request_id,
            task_id=task_id,
            client=client,
        )
    ).parsed
