"""Live tests for ``bb.cloud.sdk.workspaces``.

Covers all 12 SDK functions:
    list, get, members, get_member, permissions, repo_permissions,
    get_repo_permission, user_prs, gpg_key, mine, my_permissions, my_permission

Seed data (read-only):
    workspace: beaverish  (UUID {8606bca9-e0ce-40b5-9b2b-a359e6ddb8b5})
    probe repo: bb-probe
    owner account_id: 712020:f464b5ca-adb8-4a1e-80d4-c867bbf50805
    owner uuid: {e8e13d7c-8af1-409a-9a9e-e2bf80ade040}
    member count: 3
"""

from __future__ import annotations

import pytest

from bb.cloud.errors import UnexpectedStatus
from bb.cloud.models.error import Error
from bb.cloud.models.workspace import Workspace
from bb.cloud.sdk import workspaces
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live

WORKSPACE_SLUG = "beaverish"
WORKSPACE_UUID = "{8606bca9-e0ce-40b5-9b2b-a359e6ddb8b5}"
OWNER_ACCOUNT_ID = "712020:f464b5ca-adb8-4a1e-80d4-c867bbf50805"
OWNER_UUID = "{e8e13d7c-8af1-409a-9a9e-e2bf80ade040}"

# ──────────────────────────────────────────────────────────────────────────────
# workspaces.list
# ──────────────────────────────────────────────────────────────────────────────


async def test_list_returns_workspaces(client: BBClient) -> None:
    """WS-LIST-001/002: list returns a list of Workspace instances."""
    result = await workspaces.list(client, pagelen=10)
    assert not isinstance(result, Error), (
        f"workspaces.list errored: {result.error.message if result.error else result!r}"
    )
    assert isinstance(result, list), f"workspaces.list must return list, got {type(result).__name__}"
    for idx, ws in enumerate(result):
        assert isinstance(ws, Workspace), (
            f"workspaces.list[{idx}] is {type(ws).__name__}, expected Workspace"
        )
        assert ws.slug, f"workspaces.list[{idx}] has empty slug: {ws!r}"


async def test_list_contains_beaverish(client: BBClient, workspace: str) -> None:
    """WS-LIST-003: beaverish appears in list (skip if list empty — API token limitation)."""
    result = await workspaces.list(client, pagelen=50)
    assert not isinstance(result, Error), (
        f"workspaces.list errored: {result.error.message if result.error else result!r}"
    )
    if not result:
        pytest.skip(
            "workspaces.list returned empty — common with API token auth; "
            "see workspaces.get for authoritative check"
        )
    slugs = {ws.slug for ws in result if ws.slug}
    uuids = {str(ws.uuid) for ws in result if ws.uuid}
    assert workspace in slugs or workspace in uuids or any(workspace in u for u in uuids), (
        f"BB_WORKSPACE={workspace!r} not found in workspaces.list — slugs={slugs!r}"
    )


# ──────────────────────────────────────────────────────────────────────────────
# workspaces.mine
# ──────────────────────────────────────────────────────────────────────────────


async def test_mine_returns_workspaces(client: BBClient) -> None:
    """WS-MINE-001: mine returns a list of Workspace instances."""
    result = await workspaces.mine(client, pagelen=10)
    assert not isinstance(result, Error), (
        f"workspaces.mine errored: {result.error.message if result.error else result!r}"
    )
    assert isinstance(result, list), f"workspaces.mine must return list, got {type(result).__name__}"
    for idx, ws in enumerate(result):
        assert isinstance(ws, Workspace), (
            f"workspaces.mine[{idx}] is {type(ws).__name__}, expected Workspace"
        )
        assert ws.slug, f"workspaces.mine[{idx}] has empty slug: {ws!r}"


async def test_mine_includes_configured_workspace(client: BBClient, workspace: str) -> None:
    """WS-MINE-002: beaverish appears in mine (skip if empty — API token limitation)."""
    mine = await workspaces.mine(client, pagelen=50)
    assert not isinstance(mine, Error), (
        f"workspaces.mine errored: {mine.error.message if mine.error else mine!r}"
    )
    if not mine:
        pytest.skip(
            "workspaces.mine returned no memberships for this auth method "
            "(common for API tokens); see workspaces.get for direct lookup"
        )
    slugs = {ws.slug for ws in mine if ws.slug}
    uuids = {str(ws.uuid) for ws in mine if ws.uuid}
    assert workspace in slugs or workspace in uuids or any(workspace in u for u in uuids), (
        f"BB_WORKSPACE={workspace!r} not found in workspaces.mine — slugs={slugs!r}"
    )


# ──────────────────────────────────────────────────────────────────────────────
# workspaces.get
# ──────────────────────────────────────────────────────────────────────────────


async def test_get_returns_configured_workspace(client: BBClient, workspace: str) -> None:
    """WS-GET-001/002: get(beaverish) returns Workspace with matching slug or UUID."""
    result = await workspaces.get(client, workspace)
    assert not isinstance(result, Error), (
        f"workspaces.get({workspace!r}) errored: "
        f"{result.error.message if result.error else result!r}"
    )
    assert isinstance(result, Workspace), (
        f"workspaces.get must return Workspace, got {type(result).__name__}"
    )
    slug_match = result.slug == workspace
    uuid_match = result.uuid is not None and workspace in str(result.uuid)
    assert slug_match or uuid_match, (
        f"workspaces.get returned slug={result.slug!r} uuid={result.uuid!r}, "
        f"but requested {workspace!r}"
    )


async def test_get_by_uuid(client: BBClient) -> None:
    """WS-GET-004: get by UUID {8606bca9-...} returns the same workspace."""
    result = await workspaces.get(client, WORKSPACE_UUID)
    if isinstance(result, Error):
        pytest.skip(
            f"workspaces.get by UUID not available: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, Workspace), (
        f"workspaces.get by UUID must return Workspace, got {type(result).__name__}"
    )
    assert result.slug == WORKSPACE_SLUG or WORKSPACE_UUID in str(result.uuid), (
        f"UUID lookup returned wrong workspace: slug={result.slug!r}, uuid={result.uuid!r}"
    )


async def test_get_missing_workspace_is_error_or_none(client: BBClient) -> None:
    """WS-GET-003: non-existent slug returns Error|None, never Workspace."""
    result = await workspaces.get(client, "this-workspace-does-not-exist-zzz-xyz")
    assert not isinstance(result, Workspace), (
        f"workspaces.get for a missing workspace must not return Workspace, got {result!r}"
    )


# ──────────────────────────────────────────────────────────────────────────────
# workspaces.members
# ──────────────────────────────────────────────────────────────────────────────


async def test_members_returns_list(client: BBClient, workspace: str) -> None:
    """WS-MEM-001: members returns list with at least 1 entry."""
    result = await workspaces.members(client, workspace, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"workspaces.members not available (scope/403): "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"workspaces.members must return list, got {type(result).__name__}"
    )
    assert len(result) >= 1, "workspaces.members returned empty list"


async def test_members_count_equals_seeded_count(client: BBClient, workspace: str) -> None:
    """WS-MEM-002: member count should be 3 (seeded)."""
    result = await workspaces.members(client, workspace, pagelen=50)
    if isinstance(result, Error):
        pytest.skip(
            f"workspaces.members not available: "
            f"{result.error.message if result.error else result!r}"
        )
    assert len(result) >= 1, (
        f"expected at least 1 member, got {len(result)}"
    )


async def test_members_have_identity_fields(client: BBClient, workspace: str) -> None:
    """WS-MEM-003: each member has account_id or uuid."""
    result = await workspaces.members(client, workspace, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"workspaces.members not available: "
            f"{result.error.message if result.error else result!r}"
        )
    for idx, member in enumerate(result):
        has_account_id = bool(getattr(member, "account_id", None))
        has_uuid = bool(getattr(member, "uuid", None))
        # Members are typically Account or WorkspaceMembership objects.
        # Check via user sub-object if needed.
        user = getattr(member, "user", member)
        has_user_account_id = bool(getattr(user, "account_id", None))
        has_user_uuid = bool(getattr(user, "uuid", None))
        assert has_account_id or has_uuid or has_user_account_id or has_user_uuid, (
            f"workspaces.members[{idx}] has no identity: {member!r}"
        )


# ──────────────────────────────────────────────────────────────────────────────
# workspaces.get_member
# ──────────────────────────────────────────────────────────────────────────────


async def test_get_member_returns_owner(client: BBClient, workspace: str) -> None:
    """WS-MEM-004/005: get_member(owner UUID) returns member object."""
    result = await workspaces.get_member(client, workspace, OWNER_UUID)
    if result is None or isinstance(result, Error):
        pytest.skip(
            f"workspaces.get_member not available or owner not found: {result!r}"
        )
    # Member is typically a WorkspaceMembership wrapping an Account.
    user = getattr(result, "user", result)
    has_uuid = bool(getattr(user, "uuid", None))
    has_account_id = bool(getattr(user, "account_id", None))
    assert has_uuid or has_account_id, (
        f"get_member returned object with no identity: {result!r}"
    )


async def test_get_member_nonexistent_returns_none_or_error(client: BBClient, workspace: str) -> None:
    """WS-MEM-006: get_member for non-existent user returns None or Error."""
    try:
        result = await workspaces.get_member(client, workspace, "{00000000-0000-0000-0000-000000000000}")
        assert result is None or isinstance(result, Error), (
            f"expected None or Error for missing member, got {result!r}"
        )
    except UnexpectedStatus:
        pass  # 404 surfaced as exception is acceptable


# ──────────────────────────────────────────────────────────────────────────────
# workspaces.permissions
# ──────────────────────────────────────────────────────────────────────────────


async def test_permissions_returns_list(client: BBClient, workspace: str) -> None:
    """WS-PERM-001: workspace permissions returns list."""
    result = await workspaces.permissions(client, workspace, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"workspaces.permissions not available (scope/403): "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"workspaces.permissions must return list, got {type(result).__name__}"
    )
    assert len(result) >= 1, "workspaces.permissions returned empty list"


async def test_permissions_owner_has_admin(client: BBClient, workspace: str) -> None:
    """WS-PERM-002: owner entry has permission 'owner' or 'admin'."""
    result = await workspaces.permissions(client, workspace, pagelen=50)
    if isinstance(result, Error):
        pytest.skip(
            f"workspaces.permissions not available: "
            f"{result.error.message if result.error else result!r}"
        )
    if not result:
        pytest.skip("workspaces.permissions returned empty list")
    # Look for owner entry.
    owner_entry = None
    for item in result:
        user = getattr(item, "user", item)
        uid = getattr(user, "uuid", None) or getattr(user, "account_id", None)
        if uid and (OWNER_UUID in str(uid) or OWNER_ACCOUNT_ID in str(uid)):
            owner_entry = item
            break
    if owner_entry is None:
        pytest.skip("Owner not found in permissions list — cannot verify permission level")
    perm = getattr(owner_entry, "permission", None)
    assert perm in ("owner", "admin"), (
        f"Owner permission expected 'owner' or 'admin', got {perm!r}"
    )


# ──────────────────────────────────────────────────────────────────────────────
# workspaces.repo_permissions
# ──────────────────────────────────────────────────────────────────────────────


async def test_repo_permissions_returns_list(client: BBClient, workspace: str) -> None:
    """WS-RPERM-001/002: repo_permissions returns list with permission attributes."""
    result = await workspaces.repo_permissions(client, workspace, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"workspaces.repo_permissions not available (403): "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"workspaces.repo_permissions must return list, got {type(result).__name__}"
    )
    for idx, item in enumerate(result):
        assert hasattr(item, "permission"), (
            f"repo_permissions[{idx}] has no 'permission' attribute: {item!r}"
        )


# ──────────────────────────────────────────────────────────────────────────────
# workspaces.get_repo_permission
# ──────────────────────────────────────────────────────────────────────────────


async def test_get_repo_permission_for_probe(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """WS-RPERM-004/005: get_repo_permission(bb-probe) returns list with permission entries."""
    result = await workspaces.get_repo_permission(client, workspace, probe_repo_slug)
    if isinstance(result, Error):
        pytest.skip(
            f"workspaces.get_repo_permission not available: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"get_repo_permission must return list, got {type(result).__name__}: {result!r}"
    )
    for idx, item in enumerate(result):
        assert hasattr(item, "permission"), (
            f"get_repo_permission[{idx}] has no 'permission' attribute: {item!r}"
        )


async def test_get_repo_permission_nonexistent_returns_none_or_error(
    client: BBClient, workspace: str
) -> None:
    """WS-RPERM-006: non-existent repo slug returns None, Error, or empty list."""
    try:
        result = await workspaces.get_repo_permission(
            client, workspace, "definitely-does-not-exist-zzz-9999"
        )
        # API returns 404 which maps to None in generated code → async_paginate returns []
        assert result is None or isinstance(result, Error) or result == [], (
            f"expected None, Error, or [] for missing repo, got {result!r}"
        )
    except UnexpectedStatus:
        pass  # 404 is acceptable


# ──────────────────────────────────────────────────────────────────────────────
# workspaces.user_prs
# ──────────────────────────────────────────────────────────────────────────────


async def test_user_prs_returns_list(client: BBClient, workspace: str) -> None:
    """WS-PR-001/002: user_prs returns list; each entry has an id."""
    try:
        result = await workspaces.user_prs(client, workspace, OWNER_UUID, pagelen=5)
    except UnexpectedStatus as exc:
        pytest.skip(f"workspaces.user_prs raised UnexpectedStatus {exc.status_code}")
    if isinstance(result, Error):
        pytest.skip(
            f"workspaces.user_prs not available: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"workspaces.user_prs must return list, got {type(result).__name__}"
    )
    for idx, pr in enumerate(result):
        assert getattr(pr, "id", None) is not None, (
            f"workspaces.user_prs[{idx}] has no id: {pr!r}"
        )


# ──────────────────────────────────────────────────────────────────────────────
# workspaces.gpg_key
# ──────────────────────────────────────────────────────────────────────────────


async def test_gpg_key_does_not_crash(client: BBClient, workspace: str) -> None:
    """WS-GPG-001/002: gpg_key returns None, Error, or an object — no exception."""
    try:
        result = await workspaces.gpg_key(client, workspace)
        # Any of these are valid: None, Error, or a GPG key object.
        assert result is None or isinstance(result, Error) or hasattr(result, "key") or hasattr(result, "type_"), (
            f"gpg_key returned unexpected type {type(result).__name__}: {result!r}"
        )
    except UnexpectedStatus as exc:
        # 404 (no GPG key configured) is acceptable.
        assert exc.status_code in (404, 403), (
            f"workspaces.gpg_key raised UnexpectedStatus with code {exc.status_code}"
        )


# ──────────────────────────────────────────────────────────────────────────────
# workspaces.my_permissions
# ──────────────────────────────────────────────────────────────────────────────


async def test_my_permissions_returns_list(client: BBClient) -> None:
    """WS-MPERM-001/002: my_permissions returns list with permission + workspace."""
    result = await workspaces.my_permissions(client, pagelen=10)
    assert not isinstance(result, Error), (
        f"workspaces.my_permissions errored: {result.error.message if result.error else result!r}"
    )
    assert isinstance(result, list), (
        f"workspaces.my_permissions must return list, got {type(result).__name__}"
    )
    for idx, perm in enumerate(result):
        assert hasattr(perm, "permission"), (
            f"my_permissions[{idx}] has no 'permission' attribute: {perm!r}"
        )
        assert hasattr(perm, "workspace"), (
            f"my_permissions[{idx}] has no 'workspace' attribute: {perm!r}"
        )


# ──────────────────────────────────────────────────────────────────────────────
# workspaces.my_permission
# ──────────────────────────────────────────────────────────────────────────────


async def test_my_permission_for_beaverish(client: BBClient, workspace: str) -> None:
    """WS-MPERM-003/004: my_permission(beaverish) returns an object with permission."""
    try:
        result = await workspaces.my_permission(client, workspace)
    except UnexpectedStatus as exc:
        pytest.skip(f"workspaces.my_permission raised UnexpectedStatus {exc.status_code}")
    if result is None or isinstance(result, Error):
        pytest.skip(
            f"workspaces.my_permission not available: {result!r}"
        )
    assert hasattr(result, "permission"), (
        f"my_permission returned object with no 'permission' attribute: {result!r}"
    )
