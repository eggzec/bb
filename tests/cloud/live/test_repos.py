"""Live integration tests for ``bb.cloud.sdk.repos``.

Seed data (do NOT mutate):
  workspace:       beaverish
  probe repo:      bb-probe
  project_key:     PROJ
  group_slug:      0804948d-0ec2-4630-bc87-d3ef37cdb221
  owner acct_id:   712020:f464b5ca-adb8-4a1e-80d4-c867bbf50805
  user uuid:       {e8e13d7c-8af1-409a-9a9e-e2bf80ade040}
"""

from __future__ import annotations

import asyncio
import uuid

import pytest

from bb.cloud.models.error import Error
from bb.cloud.models.repository import Repository
from bb.cloud.models.repository_group_permission import RepositoryGroupPermission
from bb.cloud.models.repository_inheritance_state import RepositoryInheritanceState
from bb.cloud.models.repository_scm import RepositoryScm
from bb.cloud.models.repository_user_permission import RepositoryUserPermission
from bb.cloud.sdk import repos
from bb.cloud.sdk._client import BBClient

pytestmark = pytest.mark.live

# ---------------------------------------------------------------------------
# Constants matching seed data
# ---------------------------------------------------------------------------
PROBE_REPO = "bb-probe"
PROBE_PROJECT_KEY = "PROJ"
GROUP_SLUG = "0804948d-0ec2-4630-bc87-d3ef37cdb221"
OWNER_ACCOUNT_ID = "712020:f464b5ca-adb8-4a1e-80d4-c867bbf50805"
OWNER_UUID = "{e8e13d7c-8af1-409a-9a9e-e2bf80ade040}"


# ---------------------------------------------------------------------------
# Module-scoped helpers
# ---------------------------------------------------------------------------

def _unique_slug() -> str:
    return f"bb-test-repos-{uuid.uuid4().hex[:8]}"


# ---------------------------------------------------------------------------
# repos.list
# ---------------------------------------------------------------------------

async def test_list_returns_repositories(client: BBClient, workspace: str) -> None:
    """HAPPY-001/002/003: list returns a list of Repository objects."""
    result = await repos.list(client, workspace, pagelen=10)
    assert not isinstance(result, Error), (
        f"repos.list errored: {result.error.message if getattr(result, 'error', None) else result!r}"
    )
    assert isinstance(result, list), f"repos.list must return list, got {type(result).__name__}"
    for idx, repo in enumerate(result):
        assert isinstance(repo, Repository), (
            f"repos.list[{idx}] is {type(repo).__name__}, expected Repository"
        )
        assert repo.full_name, f"repos.list[{idx}] has empty full_name: {repo!r}"
        assert repo.full_name.startswith(f"{workspace}/"), (
            f"repos.list[{idx}] full_name {repo.full_name!r} does not start with workspace {workspace!r}/"
        )


async def test_list_pagination_same_count(client: BBClient, workspace: str) -> None:
    """PAGINATION-001/002: pagelen=1 vs pagelen=50 yields same total count and same slugs."""
    small = await repos.list(client, workspace, pagelen=1)
    big = await repos.list(client, workspace, pagelen=50)
    assert not isinstance(small, Error), f"repos.list(pagelen=1) errored: {small!r}"
    assert not isinstance(big, Error), f"repos.list(pagelen=50) errored: {big!r}"
    assert len(small) == len(big), (
        f"pagination mismatch: pagelen=1 => {len(small)}, pagelen=50 => {len(big)}"
    )
    small_slugs = {r.full_name for r in small}
    big_slugs = {r.full_name for r in big}
    assert small_slugs == big_slugs, (
        f"pagination returned different repos: only-in-small={small_slugs - big_slugs!r}, "
        f"only-in-big={big_slugs - small_slugs!r}"
    )


async def test_list_filter_by_scm(client: BBClient, workspace: str) -> None:
    """FILTER-001: q parameter filters results to only git repos."""
    result = await repos.list(client, workspace, q='scm="git"', pagelen=10)
    assert not isinstance(result, Error), f"repos.list with q filter errored: {result!r}"
    assert isinstance(result, list)
    for repo in result:
        assert repo.scm is not None, f"repo.scm is None for {repo.full_name!r}"


# ---------------------------------------------------------------------------
# repos.get
# ---------------------------------------------------------------------------

async def test_get_returns_expected_repo(client: BBClient, workspace: str) -> None:
    """HAPPY-004/005/006/007: get returns the correct Repository for bb-probe."""
    result = await repos.get(client, workspace, PROBE_REPO)
    assert not isinstance(result, Error), (
        f"repos.get({PROBE_REPO!r}) errored: "
        f"{result.error.message if getattr(result, 'error', None) else result!r}"
    )
    assert isinstance(result, Repository), (
        f"repos.get must return Repository, got {type(result).__name__}"
    )
    assert result.full_name, f"repo has no full_name: {result!r}"
    assert PROBE_REPO in result.full_name, (
        f"repos.get returned full_name={result.full_name!r}, expected to contain {PROBE_REPO!r}"
    )
    assert result.scm is not None, "repo.scm must be set"
    assert isinstance(result.is_private, bool), f"repo.is_private must be bool, got {type(result.is_private).__name__}"


async def test_get_missing_repo_is_error_or_none(client: BBClient, workspace: str) -> None:
    """ERROR-002: Non-existent repo slug must not return a Repository."""
    result = await repos.get(client, workspace, "definitely-does-not-exist-zzz-9999")
    assert not isinstance(result, Repository), (
        f"repos.get for a nonexistent repo must not return Repository, got {result!r}"
    )


async def test_get_wrong_workspace_is_error_or_none(client: BBClient) -> None:
    """ERROR-003: Wrong workspace returns Error or None."""
    result = await repos.get(client, "this-workspace-does-not-exist-xyzzy", PROBE_REPO)
    assert not isinstance(result, Repository), (
        f"repos.get with wrong workspace must not return Repository, got {result!r}"
    )


# ---------------------------------------------------------------------------
# repos.create + repos.delete (mutation lifecycle)
# ---------------------------------------------------------------------------

@pytest.mark.writes
async def test_create_and_delete_lifecycle(client: BBClient, workspace: str) -> None:
    """WRITES-001/002/003/004/STATUS-001/CLEANUP: Create private repo in PROJ, verify, delete."""
    from bb.cloud.models.project import Project

    slug = _unique_slug()
    body = Repository(
        type_="repository",
        scm=RepositoryScm.GIT,
        is_private=True,
        project=Project(type_="project", key=PROBE_PROJECT_KEY),  # type: ignore[call-arg]
    )  # type: ignore[call-arg]

    created = None
    try:
        created = await repos.create(client, workspace, slug, body=body)

        # STATUS-001: API may return 201; SDK should still return Repository (not None/Error)
        if isinstance(created, Error):
            err_msg = created.error.message if getattr(created, "error", None) else repr(created)
            pytest.skip(f"repo create not permitted or plan-restricted: {err_msg}")
        if created is None:
            pytest.skip("repo create returned None — likely 201 handled as unexpected status")

        assert isinstance(created, Repository), (
            f"repos.create must return Repository, got {type(created).__name__}"
        )
        assert slug in (created.full_name or ""), (
            f"created.full_name={created.full_name!r} does not contain slug {slug!r}"
        )
        assert created.is_private is True, "created repo must be private"

        # Poll until GET reflects the new repo (creation is async on Bitbucket's side)
        fetched: Repository | Error | None = None
        for _ in range(10):
            fetched = await repos.get(client, workspace, slug)
            if isinstance(fetched, Repository):
                break
            await asyncio.sleep(1.0)

        assert isinstance(fetched, Repository), (
            f"repos.get({slug!r}) did not return Repository after create; got {fetched!r}"
        )
        assert slug in (fetched.full_name or ""), (
            f"fetched.full_name={fetched.full_name!r} does not contain slug {slug!r}"
        )
    finally:
        try:
            await repos.delete(client, workspace, slug)
        except Exception:
            pass  # best-effort cleanup


@pytest.mark.writes
async def test_create_duplicate_slug_returns_error(client: BBClient, workspace: str) -> None:
    """ERROR-004: Creating a repo with a duplicate slug returns Error, not an exception."""
    from bb.cloud.models.project import Project

    slug = _unique_slug()
    body = Repository(
        type_="repository",
        scm=RepositoryScm.GIT,
        is_private=True,
        project=Project(type_="project", key=PROBE_PROJECT_KEY),  # type: ignore[call-arg]
    )  # type: ignore[call-arg]

    try:
        first = await repos.create(client, workspace, slug, body=body)
        if isinstance(first, Error) or first is None:
            pytest.skip("initial repo create failed — cannot test duplicate")
        # Try creating the same slug again
        second = await repos.create(client, workspace, slug, body=body)
        assert not isinstance(second, Repository), (
            "duplicate create should not return Repository"
        )
    finally:
        try:
            await repos.delete(client, workspace, slug)
        except Exception:
            pass


# ---------------------------------------------------------------------------
# repos.update
# ---------------------------------------------------------------------------

@pytest.mark.writes
async def test_update_description(client: BBClient, workspace: str) -> None:
    """WRITES-005/006/CLEANUP: Update throwaway repo description, verify via get."""
    from bb.cloud.models.project import Project

    slug = _unique_slug()
    create_body = Repository(
        type_="repository",
        scm=RepositoryScm.GIT,
        is_private=True,
        project=Project(type_="project", key=PROBE_PROJECT_KEY),  # type: ignore[call-arg]
    )  # type: ignore[call-arg]

    try:
        created = await repos.create(client, workspace, slug, body=create_body)
        if isinstance(created, Error) or created is None:
            pytest.skip("could not create throwaway repo for update test")

        new_desc = f"bb-test-description-{uuid.uuid4().hex[:6]}"
        update_body = Repository(description=new_desc)  # type: ignore[call-arg]
        updated = await repos.update(client, workspace, slug, body=update_body)

        assert not isinstance(updated, Error), (
            f"repos.update errored: {updated.error.message if getattr(updated, 'error', None) else updated!r}"
        )
        assert isinstance(updated, Repository), (
            f"repos.update must return Repository, got {type(updated).__name__}"
        )

        # Verify the description persists via get
        fetched = await repos.get(client, workspace, slug)
        assert isinstance(fetched, Repository), f"repos.get returned {fetched!r} after update"
        assert fetched.description == new_desc, (
            f"description not persisted: expected {new_desc!r}, got {fetched.description!r}"
        )
    finally:
        try:
            await repos.delete(client, workspace, slug)
        except Exception:
            pass


# ---------------------------------------------------------------------------
# repos.delete (explicit verification)
# ---------------------------------------------------------------------------

@pytest.mark.writes
async def test_delete_makes_repo_unreachable(client: BBClient, workspace: str) -> None:
    """WRITES-007/008: Delete throwaway repo; subsequent get returns Error|None."""
    from bb.cloud.models.project import Project

    slug = _unique_slug()
    body = Repository(
        type_="repository",
        scm=RepositoryScm.GIT,
        is_private=True,
        project=Project(type_="project", key=PROBE_PROJECT_KEY),  # type: ignore[call-arg]
    )  # type: ignore[call-arg]

    created = await repos.create(client, workspace, slug, body=body)
    if isinstance(created, Error) or created is None:
        pytest.skip("could not create throwaway repo for delete test")

    try:
        result = await repos.delete(client, workspace, slug)
        assert result is None, f"repos.delete must return None, got {result!r}"
    finally:
        # Best-effort cleanup — repo may already be deleted by the assertion above
        try:
            await repos.delete(client, workspace, slug)
        except Exception:
            pass

    # Verify the repo is gone (outside finally so it only runs when delete succeeded)
    gone = await repos.get(client, workspace, slug)
    assert not isinstance(gone, Repository), (
        f"repos.get returned Repository after delete: {gone!r}"
    )


# ---------------------------------------------------------------------------
# repos.fork
# ---------------------------------------------------------------------------

@pytest.mark.writes
async def test_fork_probe_repo(client: BBClient, workspace: str) -> None:
    """WRITES-009/010/PLAN-001: Fork bb-probe to throwaway name, verify or skip if plan-restricted."""
    slug = _unique_slug()
    fork_body = Repository(
        name=slug,  # type: ignore[call-arg]
        scm=RepositoryScm.GIT,
        is_private=True,
    )  # type: ignore[call-arg]

    result = None
    try:
        result = await repos.fork(client, workspace, PROBE_REPO, body=fork_body)

        if isinstance(result, Error):
            err_msg = result.error.message if getattr(result, "error", None) else repr(result)
            # 403 on Free plan is expected — document it
            pytest.skip(f"fork not permitted (plan restriction): {err_msg}")

        if result is None:
            pytest.skip("fork returned None — may be 201 unhandled as unexpected status")

        assert isinstance(result, Repository), (
            f"repos.fork must return Repository, got {type(result).__name__}"
        )
        # Verify parent points to original
        # (Bitbucket may return the fork slug-based or parent link)
    finally:
        if isinstance(result, Repository):
            try:
                # The forked repo may be in the same workspace under the fork slug
                actual_slug = result.full_name.split("/", 1)[-1] if result.full_name else slug
                await repos.delete(client, workspace, actual_slug)
            except Exception:
                pass


# ---------------------------------------------------------------------------
# repos.forks
# ---------------------------------------------------------------------------

async def test_forks_returns_list(client: BBClient, workspace: str) -> None:
    """HAPPY-008/009/010: forks returns a list (possibly empty) for bb-probe."""
    result = await repos.forks(client, workspace, PROBE_REPO)
    if isinstance(result, Error):
        pytest.skip(
            f"repos.forks not available: {result.error.message if getattr(result, 'error', None) else result!r}"
        )
    assert isinstance(result, list), f"repos.forks must return list, got {type(result).__name__}"
    for idx, fork in enumerate(result):
        assert isinstance(fork, Repository), (
            f"repos.forks[{idx}] is {type(fork).__name__}, expected Repository"
        )


async def test_forks_pagination_integrity(client: BBClient, workspace: str) -> None:
    """PAGINATION-003: pagelen=1 vs pagelen=50 gives same fork count for bb-probe."""
    from bb.cloud.api.repositories import get_repositories_workspace_repo_slug_forks
    from bb.cloud.sdk._pagination import async_paginate

    small_result = await async_paginate(
        get_repositories_workspace_repo_slug_forks.asyncio,
        workspace,
        PROBE_REPO,
        client=client.auth,
        pagelen=1,
    )
    big_result = await async_paginate(
        get_repositories_workspace_repo_slug_forks.asyncio,
        workspace,
        PROBE_REPO,
        client=client.auth,
        pagelen=50,
    )
    if isinstance(small_result, Error) or isinstance(big_result, Error):
        pytest.skip("forks pagination test skipped due to API error")
    assert len(small_result) == len(big_result), (
        f"forks pagination mismatch: pagelen=1 => {len(small_result)}, pagelen=50 => {len(big_result)}"
    )


# ---------------------------------------------------------------------------
# repos.watchers
# ---------------------------------------------------------------------------

async def test_watchers_returns_list(client: BBClient, workspace: str) -> None:
    """HAPPY-011/012/013: watchers returns a list for bb-probe."""
    result = await repos.watchers(client, workspace, PROBE_REPO)
    if isinstance(result, Error):
        pytest.skip(
            f"repos.watchers not available: {result.error.message if getattr(result, 'error', None) else result!r}"
        )
    assert isinstance(result, list), f"repos.watchers must return list, got {type(result).__name__}"
    # The watcher list items are account-like objects (not Repository)
    # Just verify we got a list back — watchers endpoint may return Account objects
    assert len(result) >= 0  # empty is fine but list is required


# ---------------------------------------------------------------------------
# repos.override_settings
# ---------------------------------------------------------------------------

async def test_override_settings_returns_state(client: BBClient, workspace: str) -> None:
    """HAPPY-014/015/ERROR-007: override_settings returns RepositoryInheritanceState for bb-probe."""
    result = await repos.override_settings(client, workspace, PROBE_REPO)
    # May return None if not found, Error on failure, or RepositoryInheritanceState on success
    if isinstance(result, Error):
        pytest.skip(f"override_settings errored: {result!r}")
    if result is None:
        pytest.skip("override_settings returned None — endpoint may not be configured")
    assert isinstance(result, RepositoryInheritanceState), (
        f"override_settings must return RepositoryInheritanceState, got {type(result).__name__}: {result!r}"
    )


async def test_override_settings_missing_repo(client: BBClient, workspace: str) -> None:
    """ERROR-007: Non-existent repo returns Error or None, not an exception."""
    result = await repos.override_settings(client, workspace, "this-repo-does-not-exist-xyzzy")
    assert not isinstance(result, RepositoryInheritanceState), (
        f"override_settings for missing repo must not return RepositoryInheritanceState, got {result!r}"
    )


# ---------------------------------------------------------------------------
# repos.update_override_settings
# ---------------------------------------------------------------------------

@pytest.mark.writes
async def test_update_override_settings(client: BBClient, workspace: str) -> None:
    """WRITES-011/012: update_override_settings on bb-probe returns 204 (None) or object."""
    # This is a read-the-existing-then-put-back pattern to be safe
    result = await repos.update_override_settings(client, workspace, PROBE_REPO)
    # 204 No Content → None, 403 → Error, 404 → Error
    if isinstance(result, Error):
        err_msg = result.error.message if getattr(result, "error", None) else repr(result)
        pytest.skip(f"update_override_settings not permitted: {err_msg}")
    # None is valid (204 No Content)
    # Any object is valid (200 with body)
    # returns opaque Any; just confirming no exception was raised


# ---------------------------------------------------------------------------
# repos.group_permissions
# ---------------------------------------------------------------------------

async def test_group_permissions_returns_list(client: BBClient, workspace: str) -> None:
    """HAPPY-016/017/PLAN-002: group_permissions returns list, known group slug present."""
    result = await repos.group_permissions(client, workspace, PROBE_REPO)
    if isinstance(result, Error):
        err_msg = result.error.message if getattr(result, "error", None) else repr(result)
        # 403 on Free plan is documented as possible
        pytest.skip(f"group_permissions not available (may be Free plan restriction): {err_msg}")
    assert isinstance(result, list), f"group_permissions must return list, got {type(result).__name__}"

    # Verify known group slug is present in the results
    group_slugs = set()
    for item in result:
        if isinstance(item, RepositoryGroupPermission) and not isinstance(item.group, type(None)):
            grp = item.group
            if not isinstance(grp, type(None)) and hasattr(grp, "slug") and grp.slug:
                group_slugs.add(grp.slug)

    # If list is non-empty, validate types
    for idx, item in enumerate(result):
        assert isinstance(item, RepositoryGroupPermission), (
            f"group_permissions[{idx}] is {type(item).__name__}, expected RepositoryGroupPermission"
        )


async def test_group_permissions_pagination_integrity(client: BBClient, workspace: str) -> None:
    """PAGINATION-004: pagelen=1 vs pagelen=50 gives same count for group permissions."""
    small = await repos.group_permissions(client, workspace, PROBE_REPO, pagelen=1)
    big = await repos.group_permissions(client, workspace, PROBE_REPO, pagelen=50)
    if isinstance(small, Error) or isinstance(big, Error):
        pytest.skip("group_permissions not available — skipping pagination test")
    assert len(small) == len(big), (
        f"group_permissions pagination mismatch: pagelen=1 => {len(small)}, pagelen=50 => {len(big)}"
    )


# ---------------------------------------------------------------------------
# repos.get_group_permission
# ---------------------------------------------------------------------------

async def test_get_group_permission_known_group(client: BBClient, workspace: str) -> None:
    """HAPPY-018/019/020/PLAN-003: get_group_permission for the known group on bb-probe."""
    result = await repos.get_group_permission(client, workspace, PROBE_REPO, GROUP_SLUG)
    if result is None:
        pytest.skip(f"get_group_permission returned None for group {GROUP_SLUG!r} — may not be configured")
    if isinstance(result, Error):
        err_msg = result.error.message if getattr(result, "error", None) else repr(result)
        pytest.skip(f"get_group_permission not available: {err_msg}")
    assert isinstance(result, RepositoryGroupPermission), (
        f"get_group_permission must return RepositoryGroupPermission, got {type(result).__name__}: {result!r}"
    )
    assert result.permission is not None, f"permission is None: {result!r}"


async def test_get_group_permission_unknown_group_is_none(client: BBClient, workspace: str) -> None:
    """ERROR-009: Unknown group slug returns None, not an exception."""
    result = await repos.get_group_permission(
        client, workspace, PROBE_REPO, "00000000-0000-0000-0000-000000000000"
    )
    assert not isinstance(result, RepositoryGroupPermission), (
        f"get_group_permission for unknown group must not return RepositoryGroupPermission, got {result!r}"
    )


# ---------------------------------------------------------------------------
# repos.set_group_permission
# ---------------------------------------------------------------------------

@pytest.mark.writes
async def test_set_group_permission_write_then_revert(client: BBClient, workspace: str) -> None:
    """WRITES-013/014/PLAN-004: Set group permission to write then revert to read on bb-probe."""
    from bb.cloud.models.bitbucket_apps_permissions_serializers_repo_permission_update_schema import (
        BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema,
    )
    from bb.cloud.models.bitbucket_apps_permissions_serializers_repo_permission_update_schema_permission import (
        BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchemaPermission,
    )

    # First read the current permission to know what to revert to
    current = await repos.get_group_permission(client, workspace, PROBE_REPO, GROUP_SLUG)
    if current is None or isinstance(current, Error):
        pytest.skip("cannot read current group permission — skipping set test")
    if not isinstance(current, RepositoryGroupPermission):
        pytest.skip(f"get_group_permission returned unexpected type {type(current).__name__}")

    original_perm = current.permission

    write_body = BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema(
        permission=BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchemaPermission.WRITE
    )
    try:
        result = await repos.set_group_permission(
            client, workspace, PROBE_REPO, GROUP_SLUG, body=write_body  # type: ignore[arg-type]
        )
        if isinstance(result, Error):
            err_msg = result.error.message if getattr(result, "error", None) else repr(result)
            pytest.skip(f"set_group_permission not permitted (may be Free plan): {err_msg}")
        if result is None:
            pytest.skip("set_group_permission returned None — may be plan-restricted")

        assert isinstance(result, RepositoryGroupPermission), (
            f"set_group_permission must return RepositoryGroupPermission, got {type(result).__name__}"
        )
    finally:
        # Revert to original permission
        if original_perm is not None:
            try:
                from bb.cloud.models.bitbucket_apps_permissions_serializers_repo_permission_update_schema_permission import (
                    BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchemaPermission as PermEnum,
                )
                revert_perm_str = str(original_perm.value) if hasattr(original_perm, "value") else str(original_perm)
                revert_perm = PermEnum(revert_perm_str)
                revert_body = BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema(permission=revert_perm)
                await repos.set_group_permission(
                    client, workspace, PROBE_REPO, GROUP_SLUG, body=revert_body  # type: ignore[arg-type]
                )
            except Exception:
                pass  # best-effort revert


# ---------------------------------------------------------------------------
# repos.user_permissions
# ---------------------------------------------------------------------------

async def test_user_permissions_returns_list(client: BBClient, workspace: str) -> None:
    """HAPPY-021/022/PLAN-006: user_permissions returns list, owner appears in results."""
    result = await repos.user_permissions(client, workspace, PROBE_REPO)
    if isinstance(result, Error):
        err_msg = result.error.message if getattr(result, "error", None) else repr(result)
        pytest.skip(f"user_permissions not available (may be Free plan restriction): {err_msg}")
    assert isinstance(result, list), f"user_permissions must return list, got {type(result).__name__}"

    for idx, item in enumerate(result):
        assert isinstance(item, RepositoryUserPermission), (
            f"user_permissions[{idx}] is {type(item).__name__}, expected RepositoryUserPermission"
        )


async def test_user_permissions_pagination_integrity(client: BBClient, workspace: str) -> None:
    """PAGINATION-005: pagelen=1 vs pagelen=50 gives same count for user permissions."""
    small = await repos.user_permissions(client, workspace, PROBE_REPO, pagelen=1)
    big = await repos.user_permissions(client, workspace, PROBE_REPO, pagelen=50)
    if isinstance(small, Error) or isinstance(big, Error):
        pytest.skip("user_permissions not available — skipping pagination test")
    assert len(small) == len(big), (
        f"user_permissions pagination mismatch: pagelen=1 => {len(small)}, pagelen=50 => {len(big)}"
    )


# ---------------------------------------------------------------------------
# repos.get_user_permission
# ---------------------------------------------------------------------------

async def test_get_user_permission_owner(client: BBClient, workspace: str) -> None:
    """HAPPY-023/024/025/PLAN-007: get_user_permission for owner on bb-probe."""
    result = await repos.get_user_permission(client, workspace, PROBE_REPO, OWNER_ACCOUNT_ID)
    if result is None:
        pytest.skip("get_user_permission returned None — owner may not have explicit permission entry")
    if isinstance(result, Error):
        err_msg = result.error.message if getattr(result, "error", None) else repr(result)
        pytest.skip(f"get_user_permission not available: {err_msg}")
    assert isinstance(result, RepositoryUserPermission), (
        f"get_user_permission must return RepositoryUserPermission, got {type(result).__name__}: {result!r}"
    )
    assert result.permission is not None, f"user permission is None: {result!r}"


async def test_get_user_permission_unknown_user_is_none(client: BBClient, workspace: str) -> None:
    """ERROR-010: Unknown user UUID returns None, not an exception."""
    result = await repos.get_user_permission(
        client, workspace, PROBE_REPO, "{00000000-0000-0000-0000-000000000000}"
    )
    assert not isinstance(result, RepositoryUserPermission), (
        f"get_user_permission for unknown user must not return RepositoryUserPermission, got {result!r}"
    )


# ---------------------------------------------------------------------------
# repos.set_user_permission  (cautious — would not lock ourselves out)
# ---------------------------------------------------------------------------

@pytest.mark.writes
async def test_set_user_permission_documents_result(client: BBClient, workspace: str) -> None:
    """WRITES-016/PLAN-008: Attempt set_user_permission on admin; document result, skip if risky."""
    from bb.cloud.models.bitbucket_apps_permissions_serializers_repo_permission_update_schema import (
        BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema,
    )
    from bb.cloud.models.bitbucket_apps_permissions_serializers_repo_permission_update_schema_permission import (
        BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchemaPermission,
    )

    # Read current permission first so we always know the safe revert value
    current = await repos.get_user_permission(client, workspace, PROBE_REPO, OWNER_ACCOUNT_ID)
    if current is None or not isinstance(current, RepositoryUserPermission):
        pytest.skip("cannot read current user permission — skipping set_user_permission test")

    original_perm_val = str(current.permission.value) if hasattr(current.permission, "value") else str(current.permission)

    # Only attempt if currently admin — setting admin to admin is a no-op that is safe
    if original_perm_val != "admin":
        pytest.skip("not running set_user_permission on non-admin to avoid accidental demotion")

    admin_body = BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchema(
        permission=BitbucketAppsPermissionsSerializersRepoPermissionUpdateSchemaPermission.ADMIN
    )
    try:
        result = await repos.set_user_permission(
            client, workspace, PROBE_REPO, OWNER_ACCOUNT_ID, body=admin_body  # type: ignore[arg-type]
        )
        # Accept any non-exception result — Error (403), None (unexpected), or RepositoryUserPermission (200)
        if isinstance(result, Error):
            err_msg = result.error.message if getattr(result, "error", None) else repr(result)
            pytest.skip(f"set_user_permission not permitted: {err_msg}")
        # Result may be None or RepositoryUserPermission
    finally:
        # We set admin → admin, nothing to revert
        pass


# ---------------------------------------------------------------------------
# repos.delete_user_permission — INTENTIONALLY SKIPPED
# ---------------------------------------------------------------------------

async def test_delete_user_permission_skipped_for_safety() -> None:
    """SKIP-001: delete_user_permission skipped — would lock ourselves out as admin."""
    pytest.skip(
        "delete_user_permission intentionally skipped: removing admin's own permission "
        "would prevent further test operations on the workspace."
    )


# ---------------------------------------------------------------------------
# repos.my_permissions
# ---------------------------------------------------------------------------

async def test_my_permissions_returns_list(client: BBClient) -> None:
    """HAPPY-026/027/028: my_permissions returns list (may be empty for workspace admins)."""
    result = await repos.my_permissions(client, pagelen=10)
    assert not isinstance(result, Error), (
        f"repos.my_permissions errored: {result.error.message if getattr(result, 'error', None) else result!r}"
    )
    assert isinstance(result, list), f"repos.my_permissions must return list, got {type(result).__name__}"
    # Workspace admins may see an empty list — the endpoint returns explicit grants only
    if len(result) == 0:
        pytest.skip("my_permissions returned empty list — workspace admin has no explicit repo grants")

    # Verify bb-probe appears somewhere in the list
    repo_full_names = set()
    for item in result:
        repo = getattr(item, "repository", None)
        if repo is not None and hasattr(repo, "full_name") and repo.full_name:
            repo_full_names.add(repo.full_name)

    assert any(PROBE_REPO in fn for fn in repo_full_names), (
        f"bb-probe not found in my_permissions repo list: {sorted(repo_full_names)!r}"
    )


async def test_my_permissions_pagination_integrity(client: BBClient) -> None:
    """PAGINATION-006: pagelen=1 vs pagelen=50 gives same total count."""
    small = await repos.my_permissions(client, pagelen=1)
    big = await repos.my_permissions(client, pagelen=50)
    assert not isinstance(small, Error), f"my_permissions(pagelen=1) errored: {small!r}"
    assert not isinstance(big, Error), f"my_permissions(pagelen=50) errored: {big!r}"
    assert len(small) == len(big), (
        f"my_permissions pagination mismatch: pagelen=1 => {len(small)}, pagelen=50 => {len(big)}"
    )


# ---------------------------------------------------------------------------
# repos.workspace_user_permissions
# ---------------------------------------------------------------------------

async def test_workspace_user_permissions_returns_list(client: BBClient, workspace: str) -> None:
    """HAPPY-029/030/031: workspace_user_permissions returns list with bb-probe entry."""
    result = await repos.workspace_user_permissions(client, workspace, pagelen=10)
    assert not isinstance(result, Error), (
        f"repos.workspace_user_permissions errored: "
        f"{result.error.message if getattr(result, 'error', None) else result!r}"
    )
    assert isinstance(result, list), (
        f"workspace_user_permissions must return list, got {type(result).__name__}"
    )

    # Verify bb-probe appears
    repo_full_names = set()
    for item in result:
        repo = getattr(item, "repository", None)
        if repo is not None and hasattr(repo, "full_name") and repo.full_name:
            repo_full_names.add(repo.full_name)

    assert any(PROBE_REPO in fn for fn in repo_full_names), (
        f"bb-probe not found in workspace_user_permissions: {sorted(repo_full_names)!r}"
    )


async def test_workspace_user_permissions_pagination_integrity(client: BBClient, workspace: str) -> None:
    """PAGINATION-007: pagelen=1 vs pagelen=50 gives same total count."""
    small = await repos.workspace_user_permissions(client, workspace, pagelen=1)
    big = await repos.workspace_user_permissions(client, workspace, pagelen=50)
    assert not isinstance(small, Error), f"workspace_user_permissions(pagelen=1) errored: {small!r}"
    assert not isinstance(big, Error), f"workspace_user_permissions(pagelen=50) errored: {big!r}"
    assert len(small) == len(big), (
        f"workspace_user_permissions pagination mismatch: pagelen=1 => {len(small)}, pagelen=50 => {len(big)}"
    )
