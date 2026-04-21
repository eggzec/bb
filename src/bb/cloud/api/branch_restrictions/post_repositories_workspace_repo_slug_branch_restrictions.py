from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.branchrestriction import Branchrestriction
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
    *,
    body: Branchrestriction,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/repositories/{workspace}/{repo_slug}/branch-restrictions".format(
            workspace=quote(str(workspace), safe=""),
            repo_slug=quote(str(repo_slug), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


type ParsedPayload = Branchrestriction | Error
type ParseResult = Branchrestriction | Error | None


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ParseResult:
    if response.status_code == 201:
        if "application/json" not in response.headers.get("content-type", ""):
            return None
        response_201 = Branchrestriction.from_dict(response.json())

        return response_201

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
    body: Branchrestriction,
) -> Response[ParsedPayload]:
    """Create a branch restriction rule

     Creates a new branch restriction rule for a repository.

    `kind` describes what will be restricted. Allowed values include:
    `push`, `force`, `delete`, `restrict_merges`, `require_tasks_to_be_completed`,
    `require_approvals_to_merge`, `require_default_reviewer_approvals_to_merge`,
    `require_no_changes_requested`, `require_passing_builds_to_merge`, `require_commits_behind`,
    `reset_pullrequest_approvals_on_change`, `smart_reset_pullrequest_approvals`,
    `reset_pullrequest_changes_requested_on_change`, `require_all_dependencies_merged`,
    `enforce_merge_checks`, and `allow_auto_merge_when_builds_pass`.

    Different kinds of branch restrictions have different requirements:

    * `push` and `restrict_merges` require `users` and `groups` to be
      specified. Empty lists are allowed, in which case permission is
      denied for everybody.

    The restriction applies to all branches that match. There are
    two ways to match a branch. It is configured in `branch_match_kind`:

    1. `glob`: Matches a branch against the `pattern`. A `'*'` in
       `pattern` will expand to match zero or more characters, and every
       other character matches itself. For example, `'foo*'` will match
       `'foo'` and `'foobar'`, but not `'barfoo'`. `'*'` will match all
       branches.
    2. `branching_model`: Matches a branch against the repository's
       branching model. The `branch_type` controls the type of branch
       to match. Allowed values include: `production`, `development`,
       `bugfix`, `release`, `feature` and `hotfix`.

    The combination of `kind` and match must be unique. This means that
    two `glob` restrictions in a repository cannot have the same `kind` and
    `pattern`. Additionally, two `branching_model` restrictions in a
    repository cannot have the same `kind` and `branch_type`.

    `users` and `groups` are lists of users and groups that are except from
    the restriction. They can only be configured in `push` and
    `restrict_merges` restrictions. The `push` restriction stops a user
    pushing to matching branches unless that user is in `users` or is a
    member of a group in `groups`. The `restrict_merges` stops a user
    merging pull requests to matching branches unless that user is in
    `users` or is a member of a group in `groups`. Adding new users or
    groups to an existing restriction should be done via `PUT`.

    Note that branch restrictions with overlapping matchers is allowed,
    but the resulting behavior may be surprising.

    Args:
        workspace (str):
        repo_slug (str):
        body (Branchrestriction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Branchrestriction | Error]
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
    body: Branchrestriction,
) -> ParsedPayload | None:
    """Create a branch restriction rule

     Creates a new branch restriction rule for a repository.

    `kind` describes what will be restricted. Allowed values include:
    `push`, `force`, `delete`, `restrict_merges`, `require_tasks_to_be_completed`,
    `require_approvals_to_merge`, `require_default_reviewer_approvals_to_merge`,
    `require_no_changes_requested`, `require_passing_builds_to_merge`, `require_commits_behind`,
    `reset_pullrequest_approvals_on_change`, `smart_reset_pullrequest_approvals`,
    `reset_pullrequest_changes_requested_on_change`, `require_all_dependencies_merged`,
    `enforce_merge_checks`, and `allow_auto_merge_when_builds_pass`.

    Different kinds of branch restrictions have different requirements:

    * `push` and `restrict_merges` require `users` and `groups` to be
      specified. Empty lists are allowed, in which case permission is
      denied for everybody.

    The restriction applies to all branches that match. There are
    two ways to match a branch. It is configured in `branch_match_kind`:

    1. `glob`: Matches a branch against the `pattern`. A `'*'` in
       `pattern` will expand to match zero or more characters, and every
       other character matches itself. For example, `'foo*'` will match
       `'foo'` and `'foobar'`, but not `'barfoo'`. `'*'` will match all
       branches.
    2. `branching_model`: Matches a branch against the repository's
       branching model. The `branch_type` controls the type of branch
       to match. Allowed values include: `production`, `development`,
       `bugfix`, `release`, `feature` and `hotfix`.

    The combination of `kind` and match must be unique. This means that
    two `glob` restrictions in a repository cannot have the same `kind` and
    `pattern`. Additionally, two `branching_model` restrictions in a
    repository cannot have the same `kind` and `branch_type`.

    `users` and `groups` are lists of users and groups that are except from
    the restriction. They can only be configured in `push` and
    `restrict_merges` restrictions. The `push` restriction stops a user
    pushing to matching branches unless that user is in `users` or is a
    member of a group in `groups`. The `restrict_merges` stops a user
    merging pull requests to matching branches unless that user is in
    `users` or is a member of a group in `groups`. Adding new users or
    groups to an existing restriction should be done via `PUT`.

    Note that branch restrictions with overlapping matchers is allowed,
    but the resulting behavior may be surprising.

    Args:
        workspace (str):
        repo_slug (str):
        body (Branchrestriction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Branchrestriction | Error
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
    body: Branchrestriction,
) -> Response[ParsedPayload]:
    """Create a branch restriction rule

     Creates a new branch restriction rule for a repository.

    `kind` describes what will be restricted. Allowed values include:
    `push`, `force`, `delete`, `restrict_merges`, `require_tasks_to_be_completed`,
    `require_approvals_to_merge`, `require_default_reviewer_approvals_to_merge`,
    `require_no_changes_requested`, `require_passing_builds_to_merge`, `require_commits_behind`,
    `reset_pullrequest_approvals_on_change`, `smart_reset_pullrequest_approvals`,
    `reset_pullrequest_changes_requested_on_change`, `require_all_dependencies_merged`,
    `enforce_merge_checks`, and `allow_auto_merge_when_builds_pass`.

    Different kinds of branch restrictions have different requirements:

    * `push` and `restrict_merges` require `users` and `groups` to be
      specified. Empty lists are allowed, in which case permission is
      denied for everybody.

    The restriction applies to all branches that match. There are
    two ways to match a branch. It is configured in `branch_match_kind`:

    1. `glob`: Matches a branch against the `pattern`. A `'*'` in
       `pattern` will expand to match zero or more characters, and every
       other character matches itself. For example, `'foo*'` will match
       `'foo'` and `'foobar'`, but not `'barfoo'`. `'*'` will match all
       branches.
    2. `branching_model`: Matches a branch against the repository's
       branching model. The `branch_type` controls the type of branch
       to match. Allowed values include: `production`, `development`,
       `bugfix`, `release`, `feature` and `hotfix`.

    The combination of `kind` and match must be unique. This means that
    two `glob` restrictions in a repository cannot have the same `kind` and
    `pattern`. Additionally, two `branching_model` restrictions in a
    repository cannot have the same `kind` and `branch_type`.

    `users` and `groups` are lists of users and groups that are except from
    the restriction. They can only be configured in `push` and
    `restrict_merges` restrictions. The `push` restriction stops a user
    pushing to matching branches unless that user is in `users` or is a
    member of a group in `groups`. The `restrict_merges` stops a user
    merging pull requests to matching branches unless that user is in
    `users` or is a member of a group in `groups`. Adding new users or
    groups to an existing restriction should be done via `PUT`.

    Note that branch restrictions with overlapping matchers is allowed,
    but the resulting behavior may be surprising.

    Args:
        workspace (str):
        repo_slug (str):
        body (Branchrestriction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Branchrestriction | Error]
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
    body: Branchrestriction,
) -> ParsedPayload | None:
    """Create a branch restriction rule

     Creates a new branch restriction rule for a repository.

    `kind` describes what will be restricted. Allowed values include:
    `push`, `force`, `delete`, `restrict_merges`, `require_tasks_to_be_completed`,
    `require_approvals_to_merge`, `require_default_reviewer_approvals_to_merge`,
    `require_no_changes_requested`, `require_passing_builds_to_merge`, `require_commits_behind`,
    `reset_pullrequest_approvals_on_change`, `smart_reset_pullrequest_approvals`,
    `reset_pullrequest_changes_requested_on_change`, `require_all_dependencies_merged`,
    `enforce_merge_checks`, and `allow_auto_merge_when_builds_pass`.

    Different kinds of branch restrictions have different requirements:

    * `push` and `restrict_merges` require `users` and `groups` to be
      specified. Empty lists are allowed, in which case permission is
      denied for everybody.

    The restriction applies to all branches that match. There are
    two ways to match a branch. It is configured in `branch_match_kind`:

    1. `glob`: Matches a branch against the `pattern`. A `'*'` in
       `pattern` will expand to match zero or more characters, and every
       other character matches itself. For example, `'foo*'` will match
       `'foo'` and `'foobar'`, but not `'barfoo'`. `'*'` will match all
       branches.
    2. `branching_model`: Matches a branch against the repository's
       branching model. The `branch_type` controls the type of branch
       to match. Allowed values include: `production`, `development`,
       `bugfix`, `release`, `feature` and `hotfix`.

    The combination of `kind` and match must be unique. This means that
    two `glob` restrictions in a repository cannot have the same `kind` and
    `pattern`. Additionally, two `branching_model` restrictions in a
    repository cannot have the same `kind` and `branch_type`.

    `users` and `groups` are lists of users and groups that are except from
    the restriction. They can only be configured in `push` and
    `restrict_merges` restrictions. The `push` restriction stops a user
    pushing to matching branches unless that user is in `users` or is a
    member of a group in `groups`. The `restrict_merges` stops a user
    merging pull requests to matching branches unless that user is in
    `users` or is a member of a group in `groups`. Adding new users or
    groups to an existing restriction should be done via `PUT`.

    Note that branch restrictions with overlapping matchers is allowed,
    but the resulting behavior may be surprising.

    Args:
        workspace (str):
        repo_slug (str):
        body (Branchrestriction):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Branchrestriction | Error
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            repo_slug=repo_slug,
            client=client,
            body=body,
        )
    ).parsed
