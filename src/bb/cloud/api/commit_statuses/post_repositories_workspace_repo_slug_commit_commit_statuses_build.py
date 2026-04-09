from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.commitstatus import Commitstatus
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
    commit: str,
    *,
    body: Commitstatus | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
            commit=quote(str(commit), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Any | Commitstatus | Error
type ParseResult = Any | Commitstatus | Error | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 201:
        response_201 = Commitstatus.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
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
    commit: str,
    *,
    client: AuthenticatedClient,
    body: Commitstatus | Unset = UNSET,
) -> Response[ParsedPayload]:
    r"""Create a build status for a commit

     Creates a new build status against the specified commit.

    If the specified key already exists, the existing status object will
    be overwritten.

    Example:

    ```
    curl https://api.bitbucket.org/2.0/repositories/my-workspace/my-
    repo/commit/e10dae226959c2194f2b07b077c07762d93821cf/statuses/build/           -X POST -u jdoe -H
    'Content-Type: application/json'           -d '{
        \"key\": \"MY-BUILD\",
        \"state\": \"SUCCESSFUL\",
        \"description\": \"42 tests passed\",
        \"url\": \"https://www.example.org/my-build-result\"
      }'
    ```

    When creating a new commit status, you can use a URI template for the URL.
    Templates are URLs that contain variable names that Bitbucket will
    evaluate at runtime whenever the URL is displayed anywhere similar to
    parameter substitution in
    [Bitbucket Connect](https://developer.atlassian.com/bitbucket/concepts/context-parameters.html).
    For example, one could use `https://foo.com/builds/{repository.full_name}`
    which Bitbucket will turn into `https://foo.com/builds/foo/bar` at render time.
    The context variables available are `repository` and `commit`.

    To associate a commit status to a pull request, the refname field must be set to the source branch
    of the pull request.

    Example:
    ```
    curl https://api.bitbucket.org/2.0/repositories/my-workspace/my-
    repo/commit/e10dae226959c2194f2b07b077c07762d93821cf/statuses/build/           -X POST -u jdoe -H
    'Content-Type: application/json'           -d '{
        \"key\": \"MY-BUILD\",
        \"state\": \"SUCCESSFUL\",
        \"description\": \"42 tests passed\",
        \"url\": \"https://www.example.org/my-build-result\",
        \"refname\": \"my-pr-branch\"
      }'
    ```

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        body (Commitstatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Commitstatus | Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    client: AuthenticatedClient,
    body: Commitstatus | Unset = UNSET,
) -> ParsedPayload | None:
    r"""Create a build status for a commit

     Creates a new build status against the specified commit.

    If the specified key already exists, the existing status object will
    be overwritten.

    Example:

    ```
    curl https://api.bitbucket.org/2.0/repositories/my-workspace/my-
    repo/commit/e10dae226959c2194f2b07b077c07762d93821cf/statuses/build/           -X POST -u jdoe -H
    'Content-Type: application/json'           -d '{
        \"key\": \"MY-BUILD\",
        \"state\": \"SUCCESSFUL\",
        \"description\": \"42 tests passed\",
        \"url\": \"https://www.example.org/my-build-result\"
      }'
    ```

    When creating a new commit status, you can use a URI template for the URL.
    Templates are URLs that contain variable names that Bitbucket will
    evaluate at runtime whenever the URL is displayed anywhere similar to
    parameter substitution in
    [Bitbucket Connect](https://developer.atlassian.com/bitbucket/concepts/context-parameters.html).
    For example, one could use `https://foo.com/builds/{repository.full_name}`
    which Bitbucket will turn into `https://foo.com/builds/foo/bar` at render time.
    The context variables available are `repository` and `commit`.

    To associate a commit status to a pull request, the refname field must be set to the source branch
    of the pull request.

    Example:
    ```
    curl https://api.bitbucket.org/2.0/repositories/my-workspace/my-
    repo/commit/e10dae226959c2194f2b07b077c07762d93821cf/statuses/build/           -X POST -u jdoe -H
    'Content-Type: application/json'           -d '{
        \"key\": \"MY-BUILD\",
        \"state\": \"SUCCESSFUL\",
        \"description\": \"42 tests passed\",
        \"url\": \"https://www.example.org/my-build-result\",
        \"refname\": \"my-pr-branch\"
      }'
    ```

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        body (Commitstatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Commitstatus | Error
    """

    return sync_detailed(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    client: AuthenticatedClient,
    body: Commitstatus | Unset = UNSET,
) -> Response[ParsedPayload]:
    r"""Create a build status for a commit

     Creates a new build status against the specified commit.

    If the specified key already exists, the existing status object will
    be overwritten.

    Example:

    ```
    curl https://api.bitbucket.org/2.0/repositories/my-workspace/my-
    repo/commit/e10dae226959c2194f2b07b077c07762d93821cf/statuses/build/           -X POST -u jdoe -H
    'Content-Type: application/json'           -d '{
        \"key\": \"MY-BUILD\",
        \"state\": \"SUCCESSFUL\",
        \"description\": \"42 tests passed\",
        \"url\": \"https://www.example.org/my-build-result\"
      }'
    ```

    When creating a new commit status, you can use a URI template for the URL.
    Templates are URLs that contain variable names that Bitbucket will
    evaluate at runtime whenever the URL is displayed anywhere similar to
    parameter substitution in
    [Bitbucket Connect](https://developer.atlassian.com/bitbucket/concepts/context-parameters.html).
    For example, one could use `https://foo.com/builds/{repository.full_name}`
    which Bitbucket will turn into `https://foo.com/builds/foo/bar` at render time.
    The context variables available are `repository` and `commit`.

    To associate a commit status to a pull request, the refname field must be set to the source branch
    of the pull request.

    Example:
    ```
    curl https://api.bitbucket.org/2.0/repositories/my-workspace/my-
    repo/commit/e10dae226959c2194f2b07b077c07762d93821cf/statuses/build/           -X POST -u jdoe -H
    'Content-Type: application/json'           -d '{
        \"key\": \"MY-BUILD\",
        \"state\": \"SUCCESSFUL\",
        \"description\": \"42 tests passed\",
        \"url\": \"https://www.example.org/my-build-result\",
        \"refname\": \"my-pr-branch\"
      }'
    ```

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        body (Commitstatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Commitstatus | Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        repo_slug=repo_slug,
        commit=commit,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    repo_slug: str,
    commit: str,
    *,
    client: AuthenticatedClient,
    body: Commitstatus | Unset = UNSET,
) -> ParsedPayload | None:
    r"""Create a build status for a commit

     Creates a new build status against the specified commit.

    If the specified key already exists, the existing status object will
    be overwritten.

    Example:

    ```
    curl https://api.bitbucket.org/2.0/repositories/my-workspace/my-
    repo/commit/e10dae226959c2194f2b07b077c07762d93821cf/statuses/build/           -X POST -u jdoe -H
    'Content-Type: application/json'           -d '{
        \"key\": \"MY-BUILD\",
        \"state\": \"SUCCESSFUL\",
        \"description\": \"42 tests passed\",
        \"url\": \"https://www.example.org/my-build-result\"
      }'
    ```

    When creating a new commit status, you can use a URI template for the URL.
    Templates are URLs that contain variable names that Bitbucket will
    evaluate at runtime whenever the URL is displayed anywhere similar to
    parameter substitution in
    [Bitbucket Connect](https://developer.atlassian.com/bitbucket/concepts/context-parameters.html).
    For example, one could use `https://foo.com/builds/{repository.full_name}`
    which Bitbucket will turn into `https://foo.com/builds/foo/bar` at render time.
    The context variables available are `repository` and `commit`.

    To associate a commit status to a pull request, the refname field must be set to the source branch
    of the pull request.

    Example:
    ```
    curl https://api.bitbucket.org/2.0/repositories/my-workspace/my-
    repo/commit/e10dae226959c2194f2b07b077c07762d93821cf/statuses/build/           -X POST -u jdoe -H
    'Content-Type: application/json'           -d '{
        \"key\": \"MY-BUILD\",
        \"state\": \"SUCCESSFUL\",
        \"description\": \"42 tests passed\",
        \"url\": \"https://www.example.org/my-build-result\",
        \"refname\": \"my-pr-branch\"
      }'
    ```

    Args:
        workspace (str):
        repo_slug (str):
        commit (str):
        body (Commitstatus | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Commitstatus | Error
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            commit=commit,
            client=client,
            body=body,
        )
    ).parsed
