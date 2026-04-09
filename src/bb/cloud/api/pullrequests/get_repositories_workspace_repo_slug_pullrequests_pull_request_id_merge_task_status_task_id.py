from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response

__all__ = [
    "sync_detailed",
    "asyncio_detailed",
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


type ParsedPayload = Any
type ParseResult = Any | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 409:
        return None

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
        Response[Any]
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
        Response[Any]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        pull_request_id=pull_request_id,
        task_id=task_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
