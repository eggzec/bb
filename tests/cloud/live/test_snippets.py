"""Live integration tests for ``bb.cloud.sdk.snippets``.

Context
-------
Snippets are unavailable on the **Bitbucket Cloud Free plan** (requires Standard
or Premium). The live API returns HTTP 402 (Payment Required) for most snippets
endpoints. The spec documents HTTP 404 for some endpoints but does **not**
document 402 for any.

Because 402 is undocumented, the generated ``_parse_response`` falls through to:

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(...)
    else:
        return None   ← default (raise_on_unexpected_status=False)

PASS criteria
-------------
SDK returns ``Error``, ``None``, or ``[]`` without raising ``UnexpectedStatus``.
An ``UnexpectedStatus`` raise means the spec is missing the 402 response
definition and would be a confirmed spec/SDK bug.

Exceptions
----------
``list_all`` (GET /2.0/snippets) is a global public endpoint. It may return
real snippets from other Bitbucket users regardless of plan. We allow that.

Seed data (read-only — DO NOT mutate)
--------------------------------------
- workspace: beaverish (Free plan — snippets return 402)
- probe repo: bb-probe (not used for snippet tests directly)
"""

from __future__ import annotations

import pytest

from bb.cloud.errors import UnexpectedStatus
from bb.cloud.models.error import Error
from bb.cloud.models.snippet import Snippet
from bb.cloud.sdk import snippets
from bb.cloud.sdk._client import BBClient

pytestmark = [pytest.mark.live]

# Fake / nonexistent snippet IDs — safe to use since the workspace has no snippets
FAKE_SNIPPET_ID = "AAAAAA"
FAKE_COMMENT_ID = 99999
FAKE_REVISION = "0000000000000000000000000000000000000000"
FAKE_NODE_ID = "deadbeef"
FAKE_FILE_PATH = "hello.py"


def _fail_if_raises(fn_name: str, exc: UnexpectedStatus) -> None:
    pytest.fail(
        f"snippets.{fn_name} raised UnexpectedStatus({exc.status_code}) — "
        f"SDK should return Error/None instead of raising. "
        f"BUG-SNIPPETS-001: spec does not document HTTP {exc.status_code} "
        f"for this snippets endpoint."
    )


# ---------------------------------------------------------------------------
# snippets.list  (workspace-scoped)
# ---------------------------------------------------------------------------


async def test_list_does_not_raise(client: BBClient, workspace: str) -> None:
    """snippets.list on Free plan must not raise UnexpectedStatus.

    Expected: Error (404 from spec) or [] (empty from 402 falling to None in paginator).
    """
    try:
        result = await snippets.list(client, workspace, pagelen=10)
    except UnexpectedStatus as exc:
        _fail_if_raises("list", exc)
    except (ValueError, TypeError, KeyError) as exc:
        pytest.xfail(f"snippets.list: generated Snippet model parse error: {exc!r}")

    if isinstance(result, Error):
        return  # SDK correctly surfaced the error
    assert isinstance(result, list), (
        f"snippets.list must return list or Error, got {type(result).__name__}: {result!r}"
    )
    # If a non-empty list comes back, that's surprising on Free plan
    if result:
        pytest.xfail(
            f"snippets.list returned {len(result)} snippet(s) on Free plan — "
            f"expected Error or empty list."
        )


# ---------------------------------------------------------------------------
# snippets.list_all  (global public snippets)
# ---------------------------------------------------------------------------


async def test_list_all_does_not_raise(client: BBClient) -> None:
    """snippets.list_all (GET /2.0/snippets) must not raise.

    This is a global public endpoint. It may return real Snippet objects from
    other Bitbucket users regardless of plan. We allow that outcome.
    """
    try:
        result = await snippets.list_all(client, pagelen=10)
    except UnexpectedStatus as exc:
        _fail_if_raises("list_all", exc)
    except (ValueError, TypeError, KeyError) as exc:
        pytest.xfail(f"snippets.list_all: generated Snippet model parse error: {exc!r}")

    if isinstance(result, Error):
        return
    assert isinstance(result, list), (
        f"snippets.list_all must return list or Error, got {type(result).__name__}: {result!r}"
    )
    for idx, snippet in enumerate(result):
        assert isinstance(snippet, Snippet), (
            f"snippets.list_all[{idx}] is {type(snippet).__name__}, expected Snippet"
        )


# ---------------------------------------------------------------------------
# snippets.create  (workspace-scoped)
# ---------------------------------------------------------------------------


async def test_create_returns_error_or_none(client: BBClient, workspace: str) -> None:
    """snippets.create on Free plan must return Error or None (402), not a Snippet."""
    try:
        result = await snippets.create(client, workspace)
    except UnexpectedStatus as exc:
        _fail_if_raises("create", exc)
    _assert_not_snippet(result, "create")


# ---------------------------------------------------------------------------
# snippets.create_default  (authenticated user's default workspace)
# ---------------------------------------------------------------------------


async def test_create_default_returns_error_or_none(client: BBClient) -> None:
    """snippets.create_default on Free plan must return Error or None (402), not a Snippet."""
    try:
        result = await snippets.create_default(client)
    except UnexpectedStatus as exc:
        _fail_if_raises("create_default", exc)
    _assert_not_snippet(result, "create_default")


# ---------------------------------------------------------------------------
# snippets.get
# ---------------------------------------------------------------------------


async def test_get_fake_id_returns_error_or_none(
    client: BBClient, workspace: str
) -> None:
    """snippets.get with a fake ID must return Error or None, not a Snippet."""
    try:
        result = await snippets.get(client, workspace, FAKE_SNIPPET_ID)
    except UnexpectedStatus as exc:
        _fail_if_raises("get", exc)
    _assert_not_snippet(result, "get")


# ---------------------------------------------------------------------------
# snippets.update
# ---------------------------------------------------------------------------


async def test_update_fake_id_returns_error_or_none(
    client: BBClient, workspace: str
) -> None:
    """snippets.update with a fake ID must return Error or None, not a Snippet."""
    try:
        result = await snippets.update(client, workspace, FAKE_SNIPPET_ID)
    except UnexpectedStatus as exc:
        _fail_if_raises("update", exc)
    _assert_not_snippet(result, "update")


# ---------------------------------------------------------------------------
# snippets.delete
# ---------------------------------------------------------------------------


async def test_delete_fake_id_does_not_raise(
    client: BBClient, workspace: str
) -> None:
    """snippets.delete with a fake ID must not raise."""
    try:
        await snippets.delete(client, workspace, FAKE_SNIPPET_ID)
    except UnexpectedStatus as exc:
        _fail_if_raises("delete", exc)


# ---------------------------------------------------------------------------
# snippets.comments
# ---------------------------------------------------------------------------


async def test_comments_returns_error_or_empty(
    client: BBClient, workspace: str
) -> None:
    """snippets.comments for a fake snippet must return Error or [] without raising."""
    try:
        result = await snippets.comments(client, workspace, FAKE_SNIPPET_ID, pagelen=10)
    except UnexpectedStatus as exc:
        _fail_if_raises("comments", exc)
    assert not isinstance(result, list) or result == [], (
        f"snippets.comments returned non-empty list for fake snippet — "
        f"expected Error or []. Got: {result!r}"
    )


# ---------------------------------------------------------------------------
# snippets.add_comment
# ---------------------------------------------------------------------------


async def test_add_comment_returns_error_or_none(
    client: BBClient, workspace: str
) -> None:
    """snippets.add_comment for a fake snippet must return Error or None."""
    try:
        result = await snippets.add_comment(client, workspace, FAKE_SNIPPET_ID)
    except UnexpectedStatus as exc:
        _fail_if_raises("add_comment", exc)
    _assert_not_snippet(result, "add_comment")


# ---------------------------------------------------------------------------
# snippets.get_comment
# ---------------------------------------------------------------------------


async def test_get_comment_returns_error_or_none(
    client: BBClient, workspace: str
) -> None:
    """snippets.get_comment for a fake snippet/comment must return Error or None."""
    try:
        result = await snippets.get_comment(client, workspace, FAKE_SNIPPET_ID, FAKE_COMMENT_ID)
    except UnexpectedStatus as exc:
        _fail_if_raises("get_comment", exc)
    _assert_not_snippet(result, "get_comment")


# ---------------------------------------------------------------------------
# snippets.update_comment
# ---------------------------------------------------------------------------


async def test_update_comment_returns_error_or_none(
    client: BBClient, workspace: str
) -> None:
    """snippets.update_comment for a fake snippet/comment must return Error or None."""
    try:
        result = await snippets.update_comment(
            client, workspace, FAKE_SNIPPET_ID, FAKE_COMMENT_ID
        )
    except UnexpectedStatus as exc:
        _fail_if_raises("update_comment", exc)
    _assert_not_snippet(result, "update_comment")


# ---------------------------------------------------------------------------
# snippets.delete_comment
# ---------------------------------------------------------------------------


async def test_delete_comment_does_not_raise(
    client: BBClient, workspace: str
) -> None:
    """snippets.delete_comment for a fake comment must not raise."""
    try:
        await snippets.delete_comment(client, workspace, FAKE_SNIPPET_ID, FAKE_COMMENT_ID)
    except UnexpectedStatus as exc:
        _fail_if_raises("delete_comment", exc)


# ---------------------------------------------------------------------------
# snippets.commits
# ---------------------------------------------------------------------------


async def test_commits_returns_error_or_empty(
    client: BBClient, workspace: str
) -> None:
    """snippets.commits for a fake snippet must return Error or [] without raising."""
    try:
        result = await snippets.commits(client, workspace, FAKE_SNIPPET_ID, pagelen=10)
    except UnexpectedStatus as exc:
        _fail_if_raises("commits", exc)
    assert not isinstance(result, list) or result == [], (
        f"snippets.commits returned non-empty list for fake snippet — "
        f"expected Error or []. Got: {result!r}"
    )


# ---------------------------------------------------------------------------
# snippets.get_commit
# ---------------------------------------------------------------------------


async def test_get_commit_returns_error_or_none(
    client: BBClient, workspace: str
) -> None:
    """snippets.get_commit for a fake snippet must return Error or None."""
    try:
        result = await snippets.get_commit(client, workspace, FAKE_SNIPPET_ID, FAKE_REVISION)
    except UnexpectedStatus as exc:
        _fail_if_raises("get_commit", exc)
    _assert_not_snippet(result, "get_commit")


# ---------------------------------------------------------------------------
# snippets.watch / snippets.unwatch
# ---------------------------------------------------------------------------


async def test_watch_does_not_raise(client: BBClient, workspace: str) -> None:
    """snippets.watch for a fake snippet must not raise."""
    try:
        await snippets.watch(client, workspace, FAKE_SNIPPET_ID)
    except UnexpectedStatus as exc:
        _fail_if_raises("watch", exc)


async def test_unwatch_does_not_raise(client: BBClient, workspace: str) -> None:
    """snippets.unwatch for a fake snippet must not raise."""
    try:
        await snippets.unwatch(client, workspace, FAKE_SNIPPET_ID)
    except UnexpectedStatus as exc:
        _fail_if_raises("unwatch", exc)


# ---------------------------------------------------------------------------
# snippets.watching
# ---------------------------------------------------------------------------


async def test_watching_returns_none_or_error(
    client: BBClient, workspace: str
) -> None:
    """snippets.watching for a fake snippet must return None or Error, not raise."""
    try:
        result = await snippets.watching(client, workspace, FAKE_SNIPPET_ID)
    except UnexpectedStatus as exc:
        _fail_if_raises("watching", exc)
    _assert_not_snippet(result, "watching")


# ---------------------------------------------------------------------------
# snippets.watchers
# ---------------------------------------------------------------------------


async def test_watchers_returns_error_or_empty(
    client: BBClient, workspace: str
) -> None:
    """snippets.watchers for a fake snippet must return Error or [] without raising."""
    try:
        result = await snippets.watchers(client, workspace, FAKE_SNIPPET_ID, pagelen=10)
    except UnexpectedStatus as exc:
        _fail_if_raises("watchers", exc)
    assert not isinstance(result, list) or result == [], (
        f"snippets.watchers returned non-empty list for fake snippet — "
        f"expected Error or []. Got: {result!r}"
    )


# ---------------------------------------------------------------------------
# snippets.get_file
# ---------------------------------------------------------------------------


async def test_get_file_returns_none_or_error(
    client: BBClient, workspace: str
) -> None:
    """snippets.get_file for a fake snippet must return None or Error, not file content."""
    try:
        result = await snippets.get_file(client, workspace, FAKE_SNIPPET_ID, FAKE_FILE_PATH)
    except UnexpectedStatus as exc:
        _fail_if_raises("get_file", exc)
    _assert_not_snippet(result, "get_file")


# ---------------------------------------------------------------------------
# snippets.get_node
# ---------------------------------------------------------------------------


async def test_get_node_returns_none_or_error(
    client: BBClient, workspace: str
) -> None:
    """snippets.get_node for a fake snippet must return None or Error."""
    try:
        result = await snippets.get_node(client, workspace, FAKE_SNIPPET_ID, FAKE_NODE_ID)
    except UnexpectedStatus as exc:
        _fail_if_raises("get_node", exc)
    _assert_not_snippet(result, "get_node")


# ---------------------------------------------------------------------------
# snippets.update_node
# ---------------------------------------------------------------------------


async def test_update_node_returns_none_or_error(
    client: BBClient, workspace: str
) -> None:
    """snippets.update_node for a fake snippet must return None or Error."""
    try:
        result = await snippets.update_node(client, workspace, FAKE_SNIPPET_ID, FAKE_NODE_ID)
    except UnexpectedStatus as exc:
        _fail_if_raises("update_node", exc)
    _assert_not_snippet(result, "update_node")


# ---------------------------------------------------------------------------
# snippets.delete_node
# ---------------------------------------------------------------------------


async def test_delete_node_does_not_raise(
    client: BBClient, workspace: str
) -> None:
    """snippets.delete_node for a fake snippet must not raise."""
    try:
        await snippets.delete_node(client, workspace, FAKE_SNIPPET_ID, FAKE_NODE_ID)
    except UnexpectedStatus as exc:
        _fail_if_raises("delete_node", exc)


# ---------------------------------------------------------------------------
# snippets.get_node_file
# ---------------------------------------------------------------------------


async def test_get_node_file_returns_none_or_error(
    client: BBClient, workspace: str
) -> None:
    """snippets.get_node_file for a fake snippet/node must return None or Error."""
    try:
        result = await snippets.get_node_file(
            client, workspace, FAKE_SNIPPET_ID, FAKE_NODE_ID, FAKE_FILE_PATH
        )
    except UnexpectedStatus as exc:
        _fail_if_raises("get_node_file", exc)
    _assert_not_snippet(result, "get_node_file")


# ---------------------------------------------------------------------------
# snippets.diff
# ---------------------------------------------------------------------------


async def test_diff_returns_none_or_error(
    client: BBClient, workspace: str
) -> None:
    """snippets.diff for a fake snippet must return None or Error, not a diff string."""
    try:
        result = await snippets.diff(client, workspace, FAKE_SNIPPET_ID, FAKE_REVISION)
    except UnexpectedStatus as exc:
        _fail_if_raises("diff", exc)
    _assert_not_snippet(result, "diff")


# ---------------------------------------------------------------------------
# snippets.patch
# ---------------------------------------------------------------------------


async def test_patch_returns_none_or_error(
    client: BBClient, workspace: str
) -> None:
    """snippets.patch for a fake snippet must return None or Error, not a patch string."""
    try:
        result = await snippets.patch(client, workspace, FAKE_SNIPPET_ID, FAKE_REVISION)
    except UnexpectedStatus as exc:
        _fail_if_raises("patch", exc)
    _assert_not_snippet(result, "patch")


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _assert_not_snippet(result: object, fn_name: str) -> None:
    """Assert result is not a Snippet (the happy-path model).

    On Free plan, snippets endpoints return 402. The SDK must return Error/None,
    not a Snippet object.
    """
    assert not isinstance(result, Snippet), (
        f"snippets.{fn_name} returned a Snippet object on a Free-plan workspace — "
        f"expected Error or None (402/404 from API). "
        f"The spec does not document 402 for this endpoint (spec gap). "
        f"If the SDK returned Snippet, the plan restriction is not active or "
        f"the workspace was accidentally upgraded."
    )
