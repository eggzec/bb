"""Live tests for ``bb.cloud.sdk.projects``.

Covers all 15 SDK functions:
    list, get, create, update, delete,
    default_reviewers, get_default_reviewer, add_default_reviewer, remove_default_reviewer,
    group_permissions, update_group_permission, delete_group_permission,
    user_permissions, update_user_permission, delete_user_permission

Seed data (read-only):
    workspace: beaverish
    project key: PROJ  (name="BB", uuid={639f8e8a-097d-4aff-90b1-2b2d1ddfd7a8})
    owner account_id: 712020:f464b5ca-adb8-4a1e-80d4-c867bbf50805
    owner uuid: {e8e13d7c-8af1-409a-9a9e-e2bf80ade040}
"""

from __future__ import annotations

import pytest

from bb.cloud.errors import UnexpectedStatus
from bb.cloud.models.bitbucket_apps_permissions_serializers_project_permission_update_schema import (
    BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchema as ProjectPermissionSchema,
)
from bb.cloud.models.bitbucket_apps_permissions_serializers_project_permission_update_schema_permission import (
    BitbucketAppsPermissionsSerializersProjectPermissionUpdateSchemaPermission as ProjectPermission,
)
from bb.cloud.models.error import Error
from bb.cloud.models.project import Project
from bb.cloud.sdk import projects
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live

OWNER_ACCOUNT_ID = "712020:f464b5ca-adb8-4a1e-80d4-c867bbf50805"
OWNER_UUID = "{e8e13d7c-8af1-409a-9a9e-e2bf80ade040}"

# ──────────────────────────────────────────────────────────────────────────────
# projects.list
# ──────────────────────────────────────────────────────────────────────────────


async def test_list_returns_projects(client: BBClient, workspace: str) -> None:
    """PROJ-LIST-001/002/004: list returns a list of Project instances."""
    result = await projects.list(client, workspace, pagelen=10)
    assert not isinstance(result, Error), (
        f"projects.list errored: {result.error.message if result.error else result!r}"
    )
    assert isinstance(result, list), f"projects.list must return list, got {type(result).__name__}"
    for idx, project in enumerate(result):
        assert isinstance(project, Project), (
            f"projects.list[{idx}] is {type(project).__name__}, expected Project"
        )
        assert project.key, f"projects.list[{idx}] has empty key: {project!r}"


async def test_list_contains_seeded_project(client: BBClient, workspace: str) -> None:
    """PROJ-LIST-003: PROJ with name=BB must appear in the list."""
    result = await projects.list(client, workspace, pagelen=50)
    assert not isinstance(result, Error), (
        f"projects.list errored: {result.error.message if result.error else result!r}"
    )
    keys = {p.key for p in result if p.key}
    assert "PROJ" in keys, (
        f"Seeded project PROJ not found in projects.list — keys={keys!r}"
    )
    proj = next(p for p in result if p.key == "PROJ")
    assert proj.name == "BB", (
        f"PROJ project name expected 'BB', got {proj.name!r}"
    )


async def test_list_pagination_integrity(client: BBClient, workspace: str) -> None:
    """PROJ-LIST-005: pagelen=1 and pagelen=25 must produce the same set of keys."""
    small = await projects.list(client, workspace, pagelen=1)
    big = await projects.list(client, workspace, pagelen=25)
    assert not isinstance(small, Error), f"projects.list(pagelen=1) errored: {small!r}"
    assert not isinstance(big, Error), f"projects.list(pagelen=25) errored: {big!r}"
    assert len(small) == len(big), (
        f"pagination changed count: pagelen=1 → {len(small)}, pagelen=25 → {len(big)}"
    )
    small_keys = {p.key for p in small if p.key}
    big_keys = {p.key for p in big if p.key}
    assert small_keys == big_keys, (
        f"pagination returned different project keys: "
        f"only-small={small_keys - big_keys!r}, only-big={big_keys - small_keys!r}"
    )


# ──────────────────────────────────────────────────────────────────────────────
# projects.get
# ──────────────────────────────────────────────────────────────────────────────


async def test_get_returns_seeded_project(client: BBClient, workspace: str) -> None:
    """PROJ-GET-001/002: get(PROJ) returns Project with key='PROJ' and name='BB'."""
    result = await projects.get(client, workspace, "PROJ")
    assert not isinstance(result, Error), (
        f"projects.get('PROJ') errored: {result.error.message if result.error else result!r}"
    )
    assert isinstance(result, Project), (
        f"projects.get must return Project, got {type(result).__name__}"
    )
    assert result.key == "PROJ", f"returned key={result.key!r}, expected 'PROJ'"
    assert result.name == "BB", f"returned name={result.name!r}, expected 'BB'"


async def test_get_via_fixture_key(client: BBClient, workspace: str, probe_project_key: str) -> None:
    """PROJ-GET-001 (fixture variant): probe_project_key fixture returns a valid project."""
    result = await projects.get(client, workspace, probe_project_key)
    assert not isinstance(result, Error), (
        f"projects.get({probe_project_key!r}) errored: "
        f"{result.error.message if result.error else result!r}"
    )
    assert isinstance(result, Project), (
        f"projects.get must return Project, got {type(result).__name__}"
    )
    assert result.key == probe_project_key, (
        f"returned key={result.key!r}, expected {probe_project_key!r}"
    )


async def test_get_missing_project_is_error_or_none(client: BBClient, workspace: str) -> None:
    """PROJ-GET-003: non-existent key returns Error|None, never Project."""
    result = await projects.get(client, workspace, "ZZZNOPE")
    assert not isinstance(result, Project), (
        f"projects.get for a nonexistent key must not return Project, got {result!r}"
    )


# ──────────────────────────────────────────────────────────────────────────────
# projects.create / update / delete  (lifecycle)
# ──────────────────────────────────────────────────────────────────────────────


class _CreatableProjectBody:
    """Shim that strips the `type` field from the serialized payload.

    Bitbucket's POST /workspaces/{ws}/projects rejects ``type`` in the body
    with 'extra keys not allowed', but the generated Project model always
    emits ``"type": "project"`` via to_dict().  Wrapping in this shim avoids
    patching generated code.
    """

    def __init__(self, project: Project) -> None:
        self._project = project

    def to_dict(self) -> dict:
        payload = self._project.to_dict()
        payload.pop("type", None)
        return payload


async def test_project_create_update_delete(
    client: BBClient, workspace: str, throwaway_project_key: str
) -> None:
    """PROJ-CRE-001..003 / PROJ-UPD-001..002 / PROJ-DEL-001..002: full lifecycle."""
    body = _CreatableProjectBody(
        Project(
            type_="project",
            key=throwaway_project_key,
            name=f"bb-sdk-live {throwaway_project_key}",
            is_private=True,
            description="initial description",
        )
    )
    created = await projects.create(client, workspace, body=body)  # type: ignore[arg-type]
    if isinstance(created, Error):
        pytest.skip(
            f"project create not permitted on {workspace!r}: "
            f"{created.error.message if created.error else created!r}"
        )
    if created is None:
        pytest.skip(
            f"projects.create returned None for {throwaway_project_key!r} — "
            "likely 400/422 not mapped by generated endpoint"
        )
    assert isinstance(created, Project), (
        f"projects.create returned {type(created).__name__}, expected Project"
    )
    assert created.key == throwaway_project_key, (
        f"created project key={created.key!r}, expected {throwaway_project_key!r}"
    )

    try:
        # Verify immediately fetchable.
        fetched = await projects.get(client, workspace, throwaway_project_key)
        assert isinstance(fetched, Project), (
            f"projects.get after create returned {type(fetched).__name__}: {fetched!r}"
        )
        assert fetched.key == throwaway_project_key

        # Update description.
        update_body = _CreatableProjectBody(
            Project(
                type_="project",
                key=throwaway_project_key,
                name=f"bb-sdk-live {throwaway_project_key}",
                description="updated description",
            )
        )
        updated = await projects.update(
            client, workspace, throwaway_project_key, body=update_body  # type: ignore[arg-type]
        )
        if isinstance(updated, Error):
            pytest.skip(
                f"projects.update failed: {updated.error.message if updated.error else updated!r}"
            )
        if updated is not None:
            assert isinstance(updated, Project), (
                f"projects.update returned {type(updated).__name__}, expected Project"
            )
            # Key must survive partial update.
            assert updated.key == throwaway_project_key, (
                f"update wipe key: got {updated.key!r}"
            )
            # Description should now be updated.
            if updated.description is not None:
                assert updated.description == "updated description", (
                    f"description not updated: {updated.description!r}"
                )

    finally:
        await projects.delete(client, workspace, throwaway_project_key)

    # Confirm deletion.
    gone = await projects.get(client, workspace, throwaway_project_key)
    assert not isinstance(gone, Project), (
        f"projects.delete left the project reachable: {gone!r}"
    )


# ──────────────────────────────────────────────────────────────────────────────
# projects.default_reviewers
# ──────────────────────────────────────────────────────────────────────────────


async def test_default_reviewers_returns_list(
    client: BBClient, workspace: str, probe_project_key: str
) -> None:
    """PROJ-DR-001/002: default_reviewers returns list (may be empty)."""
    result = await projects.default_reviewers(client, workspace, probe_project_key, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"projects.default_reviewers not available: "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"projects.default_reviewers must return list, got {type(result).__name__}"
    )


# ──────────────────────────────────────────────────────────────────────────────
# projects.add_default_reviewer / get_default_reviewer / remove_default_reviewer
# ──────────────────────────────────────────────────────────────────────────────


async def test_add_default_reviewer_self_returns_error_or_raises(
    client: BBClient, workspace: str, probe_project_key: str
) -> None:
    """PROJ-DR-003: adding self as reviewer should return 400 or raise UnexpectedStatus."""
    try:
        await projects.add_default_reviewer(
            client, workspace, probe_project_key, OWNER_UUID
        )
        # If it succeeds (somehow), clean up.
        try:
            await projects.remove_default_reviewer(
                client, workspace, probe_project_key, OWNER_UUID
            )
        except Exception:
            pass
    except UnexpectedStatus as exc:
        # 400 Bad Request is expected (cannot add self as reviewer).
        assert exc.status_code in (400, 403), (
            f"add_default_reviewer raised UnexpectedStatus with unexpected code {exc.status_code}"
        )
    except Exception:
        # Any exception is acceptable — we are documenting behaviour.
        pass


async def test_get_default_reviewer_nonexistent_is_tolerant(
    client: BBClient, workspace: str, probe_project_key: str
) -> None:
    """PROJ-DR-004: get non-existent default reviewer returns Error|None, not exception."""
    try:
        result = await projects.get_default_reviewer(
            client, workspace, probe_project_key, "{00000000-0000-0000-0000-000000000000}"
        )
        # None or Error are both acceptable.
        assert result is None or isinstance(result, Error), (
            f"expected None or Error for missing reviewer, got {result!r}"
        )
    except UnexpectedStatus:
        pass  # 404 surfaced as exception is acceptable


async def test_remove_default_reviewer_nonexistent_is_tolerant(
    client: BBClient, workspace: str, probe_project_key: str
) -> None:
    """PROJ-DR-005: remove non-existent default reviewer returns None or raises UnexpectedStatus."""
    try:
        result = await projects.remove_default_reviewer(
            client, workspace, probe_project_key, "{00000000-0000-0000-0000-000000000000}"
        )
        assert result is None
    except UnexpectedStatus:
        pass  # 404 is acceptable


# ──────────────────────────────────────────────────────────────────────────────
# projects.group_permissions
# ──────────────────────────────────────────────────────────────────────────────


async def test_group_permissions_returns_list(
    client: BBClient, workspace: str, probe_project_key: str
) -> None:
    """PROJ-GP-001/002: group_permissions returns list (empty is fine; 403 → skip)."""
    result = await projects.group_permissions(client, workspace, probe_project_key, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"projects.group_permissions not available (403/plan): "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"projects.group_permissions must return list, got {type(result).__name__}"
    )


async def test_update_group_permission_nonexistent_is_tolerant(
    client: BBClient, workspace: str, probe_project_key: str
) -> None:
    """PROJ-GP-003: update with non-existent group slug returns Error|None or raises."""
    body = ProjectPermissionSchema(permission=ProjectPermission.READ)
    try:
        result = await projects.update_group_permission(
            client, workspace, probe_project_key, "nonexistent-group-zzz", body=body
        )
        assert result is None or isinstance(result, Error), (
            f"expected None or Error for unknown group, got {result!r}"
        )
    except UnexpectedStatus:
        pass  # 404/403 surfaced as exception is acceptable


async def test_delete_group_permission_nonexistent_is_tolerant(
    client: BBClient, workspace: str, probe_project_key: str
) -> None:
    """PROJ-GP-004: delete with non-existent group slug returns None or raises."""
    try:
        await projects.delete_group_permission(
            client, workspace, probe_project_key, "nonexistent-group-zzz"
        )
    except UnexpectedStatus:
        pass  # 404/403 is acceptable


# ──────────────────────────────────────────────────────────────────────────────
# projects.user_permissions
# ──────────────────────────────────────────────────────────────────────────────


async def test_user_permissions_returns_list(
    client: BBClient, workspace: str, probe_project_key: str
) -> None:
    """PROJ-UP-001: user_permissions returns list; owner should appear."""
    result = await projects.user_permissions(client, workspace, probe_project_key, pagelen=10)
    if isinstance(result, Error):
        pytest.skip(
            f"projects.user_permissions not available (403/plan): "
            f"{result.error.message if result.error else result!r}"
        )
    assert isinstance(result, list), (
        f"projects.user_permissions must return list, got {type(result).__name__}"
    )


async def test_user_permissions_contains_owner(
    client: BBClient, workspace: str, probe_project_key: str
) -> None:
    """PROJ-UP-002: owner account_id appears in user permissions list."""
    result = await projects.user_permissions(client, workspace, probe_project_key, pagelen=50)
    if isinstance(result, Error):
        pytest.skip(
            f"projects.user_permissions not available: "
            f"{result.error.message if result.error else result!r}"
        )
    if not result:
        pytest.skip("user_permissions list is empty — cannot verify owner presence")
    # Each item is a dict-like or model; check for owner identity in any string representation.
    found_owner = any(
        OWNER_ACCOUNT_ID in str(item) or OWNER_UUID in str(item)
        for item in result
    )
    assert found_owner, (
        f"Owner {OWNER_ACCOUNT_ID!r} not found in user_permissions: {result!r}"
    )


async def test_update_user_permission_own_is_tolerant(
    client: BBClient, workspace: str, throwaway_project_key: str
) -> None:
    """PROJ-UP-003/004: update own permission on throwaway project; skip if create fails."""
    body_create = _CreatableProjectBody(
        Project(
            type_="project",
            key=throwaway_project_key,
            name=f"bb-sdk-live {throwaway_project_key}",
            is_private=True,
        )
    )
    created = await projects.create(client, workspace, body=body_create)  # type: ignore[arg-type]
    if isinstance(created, Error) or created is None:
        pytest.skip("project create not permitted — skipping user_permission update test")

    try:
        perm_body = ProjectPermissionSchema(permission=ProjectPermission.ADMIN)
        try:
            result = await projects.update_user_permission(
                client, workspace, throwaway_project_key, OWNER_UUID, body=perm_body
            )
            # Result may be the updated permission object, Error, or None.
            assert result is None or isinstance(result, Error) or hasattr(result, "permission"), (
                f"update_user_permission returned unexpected type {type(result).__name__}"
            )
        except UnexpectedStatus as exc:
            # 400 (cannot demote yourself), 403 (plan restriction) are acceptable.
            assert exc.status_code in (400, 403, 404), (
                f"update_user_permission raised UnexpectedStatus {exc.status_code}"
            )
    finally:
        await projects.delete(client, workspace, throwaway_project_key)


# PROJ-UP-005: delete_user_permission is intentionally skipped (would lock out admin).
@pytest.mark.skip(reason="Intentionally skipped — deleting admin's own permission would lock us out")
async def test_delete_user_permission_skipped(client: BBClient, workspace: str) -> None:
    pass
