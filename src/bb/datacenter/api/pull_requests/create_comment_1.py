from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_comment_1_response_400 import CreateComment1Response400
from ...models.create_comment_1_response_401 import CreateComment1Response401
from ...models.create_comment_1_response_404 import CreateComment1Response404
from ...models.create_comment_1_response_409 import CreateComment1Response409
from ...models.rest_comment import RestComment
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    body: RestComment | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/pull-requests/{pull_request_id}/blocker-comments".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            pull_request_id=quote(str(pull_request_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateComment1Response400
    | CreateComment1Response401
    | CreateComment1Response404
    | CreateComment1Response409
    | RestComment
    | None
):
    if response.status_code == 201:
        response_201 = RestComment.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = CreateComment1Response400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreateComment1Response401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = CreateComment1Response404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = CreateComment1Response409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateComment1Response400
    | CreateComment1Response401
    | CreateComment1Response404
    | CreateComment1Response409
    | RestComment
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestComment | Unset = UNSET,
) -> Response[
    CreateComment1Response400
    | CreateComment1Response401
    | CreateComment1Response404
    | CreateComment1Response409
    | RestComment
]:
    r"""Add new blocker comment

     Add a new blocker comment.

    Comments can be added in a few places by setting different attributes:

    General pull request blocker comment:
    ```

    {
         \"text\": \"A task on a pull request.\"
    }
    ```

    Blocker reply to a comment:

    ```

    {
         \"text\": \"This reply is a task.\",
         \"parent\": {
             \"id\": 1
         }
    }
    ```

    General blocker file comment:

    ```

    {
         \"text\": \"A blocker comment on a file.\",
         \"anchor\": {
             \"diffType\": \"RANGE\",
             \"fromHash\": \"6df3858eeb9a53a911cd17e66a9174d44ffb02cd\",
             \"path\": \"path/to/file\",
             \"srcPath\": \"path/to/file\",
             \"toHash\": \"04c7c5c931b9418ca7b66f51fe934d0bd9b2ba4b\"
         }
     }
    ```

    Blocker file line comment:

    ```

    {
         \"text\": \"A task on a particular line within a file.\",
         \"anchor\": {
             \"diffType\": \"COMMIT\",
             \"line\": 1,
             \"lineType\": \"CONTEXT\",
             \"fileType\": \"FROM\",
             \"fromHash\": \"6df3858eeb9a53a911cd17e66a9174d44ffb02cd\",
             \"path\": \"path/to/file\",
             \"srcPath\": \"path/to/file\",
             \"toHash\": \"04c7c5c931b9418ca7b66f51fe934d0bd9b2ba4b\"
         }
     }
    ```

    For file and line comments, 'path' refers to the path of the file to which the comment should be
    applied and 'srcPath' refers to the path the that file used to have (only required for copies and
    moves). Also, fromHash and toHash refer to the sinceId / untilId (respectively) used to produce the
    diff on which the comment was added. Finally diffType refers to the type of diff the comment was
    added on. For backwards compatibility purposes if no diffType is provided and no fromHash/toHash
    pair is provided the diffType will be resolved to 'EFFECTIVE'. In any other cases the diffType is
    REQUIRED.

    For line comments, 'line' refers to the line in the diff that the comment should apply to.
    'lineType' refers to the type of diff hunk, which can be:

    - 'ADDED' - for an added line;
    - 'REMOVED' - for a removed line; or
    - 'CONTEXT' - for a line that was unmodified but is in the vicinity of the diff.


    'fileType' refers to the file of the diff to which the anchor should be attached - which is of
    relevance when displaying the diff in a side-by-side way. Currently the supported values are:

    - 'FROM' - the source file of the diff
     - 'TO' - the destination file of the diff


    If the current user is not a participant the user is added as a watcher of the pull request.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        body (RestComment | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateComment1Response400 | CreateComment1Response401 | CreateComment1Response404 | CreateComment1Response409 | RestComment]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestComment | Unset = UNSET,
) -> (
    CreateComment1Response400
    | CreateComment1Response401
    | CreateComment1Response404
    | CreateComment1Response409
    | RestComment
    | None
):
    r"""Add new blocker comment

     Add a new blocker comment.

    Comments can be added in a few places by setting different attributes:

    General pull request blocker comment:
    ```

    {
         \"text\": \"A task on a pull request.\"
    }
    ```

    Blocker reply to a comment:

    ```

    {
         \"text\": \"This reply is a task.\",
         \"parent\": {
             \"id\": 1
         }
    }
    ```

    General blocker file comment:

    ```

    {
         \"text\": \"A blocker comment on a file.\",
         \"anchor\": {
             \"diffType\": \"RANGE\",
             \"fromHash\": \"6df3858eeb9a53a911cd17e66a9174d44ffb02cd\",
             \"path\": \"path/to/file\",
             \"srcPath\": \"path/to/file\",
             \"toHash\": \"04c7c5c931b9418ca7b66f51fe934d0bd9b2ba4b\"
         }
     }
    ```

    Blocker file line comment:

    ```

    {
         \"text\": \"A task on a particular line within a file.\",
         \"anchor\": {
             \"diffType\": \"COMMIT\",
             \"line\": 1,
             \"lineType\": \"CONTEXT\",
             \"fileType\": \"FROM\",
             \"fromHash\": \"6df3858eeb9a53a911cd17e66a9174d44ffb02cd\",
             \"path\": \"path/to/file\",
             \"srcPath\": \"path/to/file\",
             \"toHash\": \"04c7c5c931b9418ca7b66f51fe934d0bd9b2ba4b\"
         }
     }
    ```

    For file and line comments, 'path' refers to the path of the file to which the comment should be
    applied and 'srcPath' refers to the path the that file used to have (only required for copies and
    moves). Also, fromHash and toHash refer to the sinceId / untilId (respectively) used to produce the
    diff on which the comment was added. Finally diffType refers to the type of diff the comment was
    added on. For backwards compatibility purposes if no diffType is provided and no fromHash/toHash
    pair is provided the diffType will be resolved to 'EFFECTIVE'. In any other cases the diffType is
    REQUIRED.

    For line comments, 'line' refers to the line in the diff that the comment should apply to.
    'lineType' refers to the type of diff hunk, which can be:

    - 'ADDED' - for an added line;
    - 'REMOVED' - for a removed line; or
    - 'CONTEXT' - for a line that was unmodified but is in the vicinity of the diff.


    'fileType' refers to the file of the diff to which the anchor should be attached - which is of
    relevance when displaying the diff in a side-by-side way. Currently the supported values are:

    - 'FROM' - the source file of the diff
     - 'TO' - the destination file of the diff


    If the current user is not a participant the user is added as a watcher of the pull request.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        body (RestComment | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateComment1Response400 | CreateComment1Response401 | CreateComment1Response404 | CreateComment1Response409 | RestComment
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestComment | Unset = UNSET,
) -> Response[
    CreateComment1Response400
    | CreateComment1Response401
    | CreateComment1Response404
    | CreateComment1Response409
    | RestComment
]:
    r"""Add new blocker comment

     Add a new blocker comment.

    Comments can be added in a few places by setting different attributes:

    General pull request blocker comment:
    ```

    {
         \"text\": \"A task on a pull request.\"
    }
    ```

    Blocker reply to a comment:

    ```

    {
         \"text\": \"This reply is a task.\",
         \"parent\": {
             \"id\": 1
         }
    }
    ```

    General blocker file comment:

    ```

    {
         \"text\": \"A blocker comment on a file.\",
         \"anchor\": {
             \"diffType\": \"RANGE\",
             \"fromHash\": \"6df3858eeb9a53a911cd17e66a9174d44ffb02cd\",
             \"path\": \"path/to/file\",
             \"srcPath\": \"path/to/file\",
             \"toHash\": \"04c7c5c931b9418ca7b66f51fe934d0bd9b2ba4b\"
         }
     }
    ```

    Blocker file line comment:

    ```

    {
         \"text\": \"A task on a particular line within a file.\",
         \"anchor\": {
             \"diffType\": \"COMMIT\",
             \"line\": 1,
             \"lineType\": \"CONTEXT\",
             \"fileType\": \"FROM\",
             \"fromHash\": \"6df3858eeb9a53a911cd17e66a9174d44ffb02cd\",
             \"path\": \"path/to/file\",
             \"srcPath\": \"path/to/file\",
             \"toHash\": \"04c7c5c931b9418ca7b66f51fe934d0bd9b2ba4b\"
         }
     }
    ```

    For file and line comments, 'path' refers to the path of the file to which the comment should be
    applied and 'srcPath' refers to the path the that file used to have (only required for copies and
    moves). Also, fromHash and toHash refer to the sinceId / untilId (respectively) used to produce the
    diff on which the comment was added. Finally diffType refers to the type of diff the comment was
    added on. For backwards compatibility purposes if no diffType is provided and no fromHash/toHash
    pair is provided the diffType will be resolved to 'EFFECTIVE'. In any other cases the diffType is
    REQUIRED.

    For line comments, 'line' refers to the line in the diff that the comment should apply to.
    'lineType' refers to the type of diff hunk, which can be:

    - 'ADDED' - for an added line;
    - 'REMOVED' - for a removed line; or
    - 'CONTEXT' - for a line that was unmodified but is in the vicinity of the diff.


    'fileType' refers to the file of the diff to which the anchor should be attached - which is of
    relevance when displaying the diff in a side-by-side way. Currently the supported values are:

    - 'FROM' - the source file of the diff
     - 'TO' - the destination file of the diff


    If the current user is not a participant the user is added as a watcher of the pull request.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        body (RestComment | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateComment1Response400 | CreateComment1Response401 | CreateComment1Response404 | CreateComment1Response409 | RestComment]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        pull_request_id=pull_request_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    pull_request_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RestComment | Unset = UNSET,
) -> (
    CreateComment1Response400
    | CreateComment1Response401
    | CreateComment1Response404
    | CreateComment1Response409
    | RestComment
    | None
):
    r"""Add new blocker comment

     Add a new blocker comment.

    Comments can be added in a few places by setting different attributes:

    General pull request blocker comment:
    ```

    {
         \"text\": \"A task on a pull request.\"
    }
    ```

    Blocker reply to a comment:

    ```

    {
         \"text\": \"This reply is a task.\",
         \"parent\": {
             \"id\": 1
         }
    }
    ```

    General blocker file comment:

    ```

    {
         \"text\": \"A blocker comment on a file.\",
         \"anchor\": {
             \"diffType\": \"RANGE\",
             \"fromHash\": \"6df3858eeb9a53a911cd17e66a9174d44ffb02cd\",
             \"path\": \"path/to/file\",
             \"srcPath\": \"path/to/file\",
             \"toHash\": \"04c7c5c931b9418ca7b66f51fe934d0bd9b2ba4b\"
         }
     }
    ```

    Blocker file line comment:

    ```

    {
         \"text\": \"A task on a particular line within a file.\",
         \"anchor\": {
             \"diffType\": \"COMMIT\",
             \"line\": 1,
             \"lineType\": \"CONTEXT\",
             \"fileType\": \"FROM\",
             \"fromHash\": \"6df3858eeb9a53a911cd17e66a9174d44ffb02cd\",
             \"path\": \"path/to/file\",
             \"srcPath\": \"path/to/file\",
             \"toHash\": \"04c7c5c931b9418ca7b66f51fe934d0bd9b2ba4b\"
         }
     }
    ```

    For file and line comments, 'path' refers to the path of the file to which the comment should be
    applied and 'srcPath' refers to the path the that file used to have (only required for copies and
    moves). Also, fromHash and toHash refer to the sinceId / untilId (respectively) used to produce the
    diff on which the comment was added. Finally diffType refers to the type of diff the comment was
    added on. For backwards compatibility purposes if no diffType is provided and no fromHash/toHash
    pair is provided the diffType will be resolved to 'EFFECTIVE'. In any other cases the diffType is
    REQUIRED.

    For line comments, 'line' refers to the line in the diff that the comment should apply to.
    'lineType' refers to the type of diff hunk, which can be:

    - 'ADDED' - for an added line;
    - 'REMOVED' - for a removed line; or
    - 'CONTEXT' - for a line that was unmodified but is in the vicinity of the diff.


    'fileType' refers to the file of the diff to which the anchor should be attached - which is of
    relevance when displaying the diff in a side-by-side way. Currently the supported values are:

    - 'FROM' - the source file of the diff
     - 'TO' - the destination file of the diff


    If the current user is not a participant the user is added as a watcher of the pull request.

    The authenticated user must have <strong>REPO_READ</strong> permission for the repository that this
    pull request targets to call this resource.

    Args:
        project_key (str):
        repository_slug (str):
        pull_request_id (str):
        body (RestComment | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateComment1Response400 | CreateComment1Response401 | CreateComment1Response404 | CreateComment1Response409 | RestComment
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            pull_request_id=pull_request_id,
            client=client,
            body=body,
        )
    ).parsed
