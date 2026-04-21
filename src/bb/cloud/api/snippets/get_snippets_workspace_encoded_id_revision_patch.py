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
    encoded_id: str,
    revision: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/snippets/{workspace}/{encoded_id}/{revision}/patch".format(
            workspace=quote(str(workspace), safe=""),
            encoded_id=quote(str(encoded_id), safe=""),
            revision=quote(str(revision), safe=""),
        ),
    }

    return _kwargs


type ParsedPayload = Any | Error
type ParseResult = Any | Error | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

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
    encoded_id: str,
    revision: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Get snippet patch between versions

     Returns the patch of the specified commit against its first
    parent.

    Note that this resource is different in functionality from the `diff`
    resource.

    The differences between a diff and a patch are:

    * patches have a commit header with the username, message, etc
    * diffs support the optional `path=foo/bar.py` query param to filter the
      diff to just that one file diff (not supported for patches)
    * for a merge, the diff will show the diff between the merge commit and
      its first parent (identical to how PRs work), while patch returns a
      response containing separate patches for each commit on the second
      parent's ancestry, up to the oldest common ancestor (identical to
      its reachability).

    Note that the character encoding of the contents of the patch is
    unspecified as Git does not track this, making it hard for
    Bitbucket to reliably determine this.

    Args:
        workspace (str):
        encoded_id (str):
        revision (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        encoded_id=encoded_id,
        revision=revision,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    encoded_id: str,
    revision: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Get snippet patch between versions

     Returns the patch of the specified commit against its first
    parent.

    Note that this resource is different in functionality from the `diff`
    resource.

    The differences between a diff and a patch are:

    * patches have a commit header with the username, message, etc
    * diffs support the optional `path=foo/bar.py` query param to filter the
      diff to just that one file diff (not supported for patches)
    * for a merge, the diff will show the diff between the merge commit and
      its first parent (identical to how PRs work), while patch returns a
      response containing separate patches for each commit on the second
      parent's ancestry, up to the oldest common ancestor (identical to
      its reachability).

    Note that the character encoding of the contents of the patch is
    unspecified as Git does not track this, making it hard for
    Bitbucket to reliably determine this.

    Args:
        workspace (str):
        encoded_id (str):
        revision (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return sync_detailed(
        workspace=workspace,
        encoded_id=encoded_id,
        revision=revision,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    encoded_id: str,
    revision: str,
    *,
    client: AuthenticatedClient,
) -> Response[ParsedPayload]:
    """Get snippet patch between versions

     Returns the patch of the specified commit against its first
    parent.

    Note that this resource is different in functionality from the `diff`
    resource.

    The differences between a diff and a patch are:

    * patches have a commit header with the username, message, etc
    * diffs support the optional `path=foo/bar.py` query param to filter the
      diff to just that one file diff (not supported for patches)
    * for a merge, the diff will show the diff between the merge commit and
      its first parent (identical to how PRs work), while patch returns a
      response containing separate patches for each commit on the second
      parent's ancestry, up to the oldest common ancestor (identical to
      its reachability).

    Note that the character encoding of the contents of the patch is
    unspecified as Git does not track this, making it hard for
    Bitbucket to reliably determine this.

    Args:
        workspace (str):
        encoded_id (str):
        revision (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        encoded_id=encoded_id,
        revision=revision,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    encoded_id: str,
    revision: str,
    *,
    client: AuthenticatedClient,
) -> ParsedPayload | None:
    """Get snippet patch between versions

     Returns the patch of the specified commit against its first
    parent.

    Note that this resource is different in functionality from the `diff`
    resource.

    The differences between a diff and a patch are:

    * patches have a commit header with the username, message, etc
    * diffs support the optional `path=foo/bar.py` query param to filter the
      diff to just that one file diff (not supported for patches)
    * for a merge, the diff will show the diff between the merge commit and
      its first parent (identical to how PRs work), while patch returns a
      response containing separate patches for each commit on the second
      parent's ancestry, up to the oldest common ancestor (identical to
      its reachability).

    Note that the character encoding of the contents of the patch is
    unspecified as Git does not track this, making it hard for
    Bitbucket to reliably determine this.

    Args:
        workspace (str):
        encoded_id (str):
        revision (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            encoded_id=encoded_id,
            revision=revision,
            client=client,
        )
    ).parsed
