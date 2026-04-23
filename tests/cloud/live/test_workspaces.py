"""Live tests for ``bb.cloud.sdk.workspaces``."""

from __future__ import annotations

import pytest

from bb.cloud.models.error import Error
from bb.cloud.models.workspace import Workspace
from bb.cloud.sdk import workspaces
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live


async def test_mine_returns_workspaces(client: BBClient) -> None:
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
    mine = await workspaces.mine(client, pagelen=50)
    assert not isinstance(mine, Error), (
        f"workspaces.mine errored: {mine.error.message if mine.error else mine!r}"
    )
    # API tokens do not surface workspace memberships via /2.0/workspaces
    # even when the caller can read the workspace directly. Skip when the
    # listing is empty so this test doesn't spuriously fail — the
    # authoritative check is ``workspaces.get`` below.
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


async def test_get_returns_configured_workspace(client: BBClient, workspace: str) -> None:
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


async def test_get_missing_workspace_is_error_or_none(client: BBClient) -> None:
    result = await workspaces.get(client, "this-workspace-does-not-exist-zzz-xyz")
    assert not isinstance(result, Workspace), (
        f"workspaces.get for a missing workspace must not return Workspace, got {result!r}"
    )


async def test_my_permissions_returns_list(client: BBClient) -> None:
    result = await workspaces.my_permissions(client, pagelen=10)
    assert not isinstance(result, Error), (
        f"workspaces.my_permissions errored: {result.error.message if result.error else result!r}"
    )
    assert isinstance(result, list), (
        f"workspaces.my_permissions must return list, got {type(result).__name__}"
    )


async def test_members_returns_list(client: BBClient, workspace: str) -> None:
    result = await workspaces.members(client, workspace, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"workspaces.members forbidden for this workspace/auth: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"workspaces.members must return list, got {type(result).__name__}"
    )


async def test_permissions_returns_list(client: BBClient, workspace: str) -> None:
    result = await workspaces.permissions(client, workspace, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"workspaces.permissions forbidden for this workspace/auth: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"workspaces.permissions must return list, got {type(result).__name__}"
    )
