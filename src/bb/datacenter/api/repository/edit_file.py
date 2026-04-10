from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.edit_file_response_400 import EditFileResponse400
from ...models.edit_file_response_401 import EditFileResponse401
from ...models.edit_file_response_403 import EditFileResponse403
from ...models.edit_file_response_404 import EditFileResponse404
from ...models.edit_file_response_409 import EditFileResponse409
from ...models.example_multipart_form_data import ExampleMultipartFormData
from ...models.rest_commit import RestCommit
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_key: str,
    repository_slug: str,
    path: str,
    *,
    body: ExampleMultipartFormData | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/latest/projects/{project_key}/repos/{repository_slug}/browse/{path}".format(
            project_key=quote(str(project_key), safe=""),
            repository_slug=quote(str(repository_slug), safe=""),
            path=quote(str(path), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    EditFileResponse400
    | EditFileResponse401
    | EditFileResponse403
    | EditFileResponse404
    | EditFileResponse409
    | RestCommit
    | None
):
    if response.status_code == 200:
        response_200 = RestCommit.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = EditFileResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = EditFileResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = EditFileResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = EditFileResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = EditFileResponse409.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    EditFileResponse400
    | EditFileResponse401
    | EditFileResponse403
    | EditFileResponse404
    | EditFileResponse409
    | RestCommit
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
    path: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExampleMultipartFormData | Unset = UNSET,
) -> Response[
    EditFileResponse400
    | EditFileResponse401
    | EditFileResponse403
    | EditFileResponse404
    | EditFileResponse409
    | RestCommit
]:
    r"""Edit file

     Update the content of path, on the given repository and branch.

    This resource accepts PUT multipart form data, containing the file in a form-field named content.

    An example <a href=\"http://curl.haxx.se/\">curl</a> request to update 'README.md' would be:

    ```curl -X PUT -u username:password -F content=@README.md  -F 'message=Updated using file-edit REST
    API' -F branch=master -F  sourceCommitId=5636641a50b
    http://example.com/rest/api/latest/projects/PROJECT_1/repos/repo_1/browse/README.md ```

    - branch:  the branch on which the path should be modified or created
    - content: the full content of the file at path
    - message: the message associated with this change, to be used as the commit message. Or null if the
    default message should be used.
    - sourceCommitId: the commit ID of the file before it was edited, used to identify if content has
    changed. Or null if this is a new file


    The file can be updated or created on a new branch. In this case, the sourceBranch parameter should
    be provided to identify the starting point for the new branch and the branch parameter identifies
    the branch to create the new commit on.

    Args:
        project_key (str):
        repository_slug (str):
        path (str):
        body (ExampleMultipartFormData | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EditFileResponse400 | EditFileResponse401 | EditFileResponse403 | EditFileResponse404 | EditFileResponse409 | RestCommit]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        path=path,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_key: str,
    repository_slug: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExampleMultipartFormData | Unset = UNSET,
) -> (
    EditFileResponse400
    | EditFileResponse401
    | EditFileResponse403
    | EditFileResponse404
    | EditFileResponse409
    | RestCommit
    | None
):
    r"""Edit file

     Update the content of path, on the given repository and branch.

    This resource accepts PUT multipart form data, containing the file in a form-field named content.

    An example <a href=\"http://curl.haxx.se/\">curl</a> request to update 'README.md' would be:

    ```curl -X PUT -u username:password -F content=@README.md  -F 'message=Updated using file-edit REST
    API' -F branch=master -F  sourceCommitId=5636641a50b
    http://example.com/rest/api/latest/projects/PROJECT_1/repos/repo_1/browse/README.md ```

    - branch:  the branch on which the path should be modified or created
    - content: the full content of the file at path
    - message: the message associated with this change, to be used as the commit message. Or null if the
    default message should be used.
    - sourceCommitId: the commit ID of the file before it was edited, used to identify if content has
    changed. Or null if this is a new file


    The file can be updated or created on a new branch. In this case, the sourceBranch parameter should
    be provided to identify the starting point for the new branch and the branch parameter identifies
    the branch to create the new commit on.

    Args:
        project_key (str):
        repository_slug (str):
        path (str):
        body (ExampleMultipartFormData | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EditFileResponse400 | EditFileResponse401 | EditFileResponse403 | EditFileResponse404 | EditFileResponse409 | RestCommit
    """

    return sync_detailed(
        project_key=project_key,
        repository_slug=repository_slug,
        path=path,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_key: str,
    repository_slug: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExampleMultipartFormData | Unset = UNSET,
) -> Response[
    EditFileResponse400
    | EditFileResponse401
    | EditFileResponse403
    | EditFileResponse404
    | EditFileResponse409
    | RestCommit
]:
    r"""Edit file

     Update the content of path, on the given repository and branch.

    This resource accepts PUT multipart form data, containing the file in a form-field named content.

    An example <a href=\"http://curl.haxx.se/\">curl</a> request to update 'README.md' would be:

    ```curl -X PUT -u username:password -F content=@README.md  -F 'message=Updated using file-edit REST
    API' -F branch=master -F  sourceCommitId=5636641a50b
    http://example.com/rest/api/latest/projects/PROJECT_1/repos/repo_1/browse/README.md ```

    - branch:  the branch on which the path should be modified or created
    - content: the full content of the file at path
    - message: the message associated with this change, to be used as the commit message. Or null if the
    default message should be used.
    - sourceCommitId: the commit ID of the file before it was edited, used to identify if content has
    changed. Or null if this is a new file


    The file can be updated or created on a new branch. In this case, the sourceBranch parameter should
    be provided to identify the starting point for the new branch and the branch parameter identifies
    the branch to create the new commit on.

    Args:
        project_key (str):
        repository_slug (str):
        path (str):
        body (ExampleMultipartFormData | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EditFileResponse400 | EditFileResponse401 | EditFileResponse403 | EditFileResponse404 | EditFileResponse409 | RestCommit]
    """

    kwargs = _get_kwargs(
        project_key=project_key,
        repository_slug=repository_slug,
        path=path,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_key: str,
    repository_slug: str,
    path: str,
    *,
    client: AuthenticatedClient | Client,
    body: ExampleMultipartFormData | Unset = UNSET,
) -> (
    EditFileResponse400
    | EditFileResponse401
    | EditFileResponse403
    | EditFileResponse404
    | EditFileResponse409
    | RestCommit
    | None
):
    r"""Edit file

     Update the content of path, on the given repository and branch.

    This resource accepts PUT multipart form data, containing the file in a form-field named content.

    An example <a href=\"http://curl.haxx.se/\">curl</a> request to update 'README.md' would be:

    ```curl -X PUT -u username:password -F content=@README.md  -F 'message=Updated using file-edit REST
    API' -F branch=master -F  sourceCommitId=5636641a50b
    http://example.com/rest/api/latest/projects/PROJECT_1/repos/repo_1/browse/README.md ```

    - branch:  the branch on which the path should be modified or created
    - content: the full content of the file at path
    - message: the message associated with this change, to be used as the commit message. Or null if the
    default message should be used.
    - sourceCommitId: the commit ID of the file before it was edited, used to identify if content has
    changed. Or null if this is a new file


    The file can be updated or created on a new branch. In this case, the sourceBranch parameter should
    be provided to identify the starting point for the new branch and the branch parameter identifies
    the branch to create the new commit on.

    Args:
        project_key (str):
        repository_slug (str):
        path (str):
        body (ExampleMultipartFormData | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EditFileResponse400 | EditFileResponse401 | EditFileResponse403 | EditFileResponse404 | EditFileResponse409 | RestCommit
    """

    return (
        await asyncio_detailed(
            project_key=project_key,
            repository_slug=repository_slug,
            path=path,
            client=client,
            body=body,
        )
    ).parsed
