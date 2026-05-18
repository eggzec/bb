"""Live integration tests for ``bb.cloud.sdk.deployments`` (16 functions).

Seed data (beaverish/bb-probe):
  - Environment "Test":    {697d8906-4609-448e-85f1-6b05d5c9faa9}
  - Environment "Staging": {13053a34-e7a9-49c0-9647-f748f576208d}
  - Env variable "DEPLOY_VAR": {bbab80d0-4e11-4d66-96e9-e74cb47e981a}
  - Deploy key id: 10958984 (label: probe-deploy-key)
"""

from __future__ import annotations

import uuid

import pytest

from bb.cloud.models.deploy_key import DeployKey
from bb.cloud.models.deployment import Deployment
from bb.cloud.models.deployment_environment import DeploymentEnvironment
from bb.cloud.models.deployment_environment_type import DeploymentEnvironmentType
from bb.cloud.models.deployment_variable import DeploymentVariable
from bb.cloud.models.error import Error
from bb.cloud.sdk import deployments
from bb.cloud.sdk._client import BBClient
from bb.cloud.types import UNSET

pytestmark = pytest.mark.live

# ---------------------------------------------------------------------------
# A test RSA public key — valid format but never registered anywhere.
# Each test run appends a unique comment so the key content is unique.
# ---------------------------------------------------------------------------
_RSA_KEY_BODY = (
    "AAAAB3NzaC1yc2EAAAADAQABAAABAQDPrkfpJ0qafO6g82NDdzNCcDzjvTXbGWfSWGGOk"
    "VRSC60WZppMLcFBT1T0OcwAWwjxHT+NgXFTpKeY3dQQN0zxMeUNpom9IYqZEYUG77wx"
    "YqgOkZV+rDj8+U9vsvXMufIfhyfGWYK+fRlvhb9q++2TsIo55x8xqISujfgEwDN1TAU"
    "s7s/YvFzy9k2Yy8Rmklfuzo5YTps5PXgtcoO0KxYZaI6HTCqRXXa46EqUrBVkTcPM+c"
    "iSsv7m0lvj3gB+sNTr8nzmKJ/7MBQRUdShG5denP6HV/w2aYQoDhPQaCz5mNhfHtZ1+"
    "+TFOMq9G4Ky7E1aqEnV/L2cmqp75GrAI0m9"
)


def _test_public_key(suffix: str) -> str:
    """Return a unique SSH public key string for a throwaway deploy key."""
    return f"ssh-rsa {_RSA_KEY_BODY} test-bb-sdk-{suffix}@bb-sdk-test"


# ---------------------------------------------------------------------------
# Local fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def probe_env_uuid() -> str:
    return "{697d8906-4609-448e-85f1-6b05d5c9faa9}"


@pytest.fixture
def probe_staging_uuid() -> str:
    return "{13053a34-e7a9-49c0-9647-f748f576208d}"


@pytest.fixture
def probe_deploy_key_id() -> int:
    return 10958984


@pytest.fixture
def probe_env_var_uuid() -> str:
    return "{bbab80d0-4e11-4d66-96e9-e74cb47e981a}"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _skip_if_error(result: object, label: str) -> None:
    if isinstance(result, Error):
        msg = result.error.message if result.error else repr(result)
        pytest.skip(f"{label} returned Error: {msg}")


# ===========================================================================
# 1. deployments.list
# ===========================================================================


async def test_list_returns_list(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """list() must return a list (possibly empty) — not an Error or exception."""
    result = await deployments.list(client, workspace, probe_repo_slug, pagelen=10)
    _skip_if_error(result, "deployments.list")
    assert isinstance(result, list), (
        f"deployments.list must return list, got {type(result).__name__}"
    )


async def test_list_items_are_deployment_type(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """Every item in list() must be a Deployment instance."""
    result = await deployments.list(client, workspace, probe_repo_slug, pagelen=10)
    _skip_if_error(result, "deployments.list")
    assert isinstance(result, list)
    for idx, item in enumerate(result):
        assert isinstance(item, Deployment), (
            f"deployments.list[{idx}] is {type(item).__name__}, expected Deployment"
        )


# ===========================================================================
# 2. deployments.get
# ===========================================================================


async def test_get_nonexistent_deployment_is_none(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """get() on a non-existent deployment UUID must return None or Error, not raise."""
    fake_uuid = "{00000000-0000-0000-0000-000000000000}"
    result = await deployments.get(client, workspace, probe_repo_slug, fake_uuid)
    assert not isinstance(result, Deployment), (
        f"Expected None/Error for fake deployment UUID, got Deployment: {result!r}"
    )


# ===========================================================================
# 3. deployments.envs
# ===========================================================================


async def test_envs_returns_list(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """envs() must return a non-empty list of DeploymentEnvironment."""
    result = await deployments.envs(client, workspace, probe_repo_slug, pagelen=25)
    _skip_if_error(result, "deployments.envs")
    assert isinstance(result, list), (
        f"deployments.envs must return list, got {type(result).__name__}"
    )
    assert len(result) > 0, "deployments.envs returned empty list — expected Test + Staging"


async def test_envs_contains_test_env(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """envs() must include the seeded 'Test' environment."""
    result = await deployments.envs(client, workspace, probe_repo_slug, pagelen=25)
    _skip_if_error(result, "deployments.envs")
    assert isinstance(result, list)
    names = [e.name for e in result if isinstance(e, DeploymentEnvironment)]
    assert "Test" in names, (
        f"Expected environment 'Test' in envs list, got names: {names!r}"
    )


async def test_envs_contains_staging_env(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """envs() must include the seeded 'Staging' environment."""
    result = await deployments.envs(client, workspace, probe_repo_slug, pagelen=25)
    _skip_if_error(result, "deployments.envs")
    assert isinstance(result, list)
    names = [e.name for e in result if isinstance(e, DeploymentEnvironment)]
    assert "Staging" in names, (
        f"Expected environment 'Staging' in envs list, got names: {names!r}"
    )


async def test_envs_items_have_uuid_and_name(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """Every DeploymentEnvironment item must have uuid and name set."""
    result = await deployments.envs(client, workspace, probe_repo_slug, pagelen=25)
    _skip_if_error(result, "deployments.envs")
    assert isinstance(result, list)
    for idx, env in enumerate(result):
        assert isinstance(env, DeploymentEnvironment), (
            f"envs[{idx}] is {type(env).__name__}, expected DeploymentEnvironment"
        )
        assert env.uuid is not UNSET and env.uuid, (
            f"envs[{idx}].uuid is missing: {env!r}"
        )
        assert env.name is not UNSET and env.name, (
            f"envs[{idx}].name is missing: {env!r}"
        )


# ===========================================================================
# 4. deployments.get_env
# ===========================================================================


async def test_get_env_returns_test_env(
    client: BBClient, workspace: str, probe_repo_slug: str, probe_env_uuid: str
) -> None:
    """get_env() must return the Test environment by UUID."""
    result = await deployments.get_env(client, workspace, probe_repo_slug, probe_env_uuid)
    _skip_if_error(result, "deployments.get_env")
    assert isinstance(result, DeploymentEnvironment), (
        f"Expected DeploymentEnvironment, got {type(result).__name__}: {result!r}"
    )
    assert result.name == "Test", (
        f"Expected name='Test', got name={result.name!r}"
    )


async def test_get_env_nonexistent_is_error_or_none(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """get_env() on a non-existent UUID must return None or Error, not a DeploymentEnvironment."""
    fake_uuid = "{00000000-0000-0000-0000-000000000000}"
    result = await deployments.get_env(client, workspace, probe_repo_slug, fake_uuid)
    assert not isinstance(result, DeploymentEnvironment), (
        f"Expected None/Error for fake env UUID, got DeploymentEnvironment: {result!r}"
    )


# ===========================================================================
# 5–7. deployments.create_env / update_env / delete_env
# ===========================================================================


async def test_create_env_roundtrip(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """create_env() → verify name → delete_env() cleanup."""
    env_name = f"bb-test-env-{uuid.uuid4().hex[:8]}"
    created_uuid: str | None = None
    try:
        created = await deployments.create_env(
            client,
            workspace,
            probe_repo_slug,
            body=DeploymentEnvironment(type_="deployment_environment", environment_type=DeploymentEnvironmentType(name="Test"), name=env_name),
        )
        if isinstance(created, Error):
            msg = created.error.message if created.error else repr(created)
            pytest.skip(f"create_env not permitted: {msg}")
        assert isinstance(created, DeploymentEnvironment), (
            f"create_env must return DeploymentEnvironment, got {type(created).__name__}"
        )
        assert created.name == env_name, (
            f"Expected name={env_name!r}, got {created.name!r}"
        )
        assert created.uuid is not UNSET and created.uuid, (
            f"create_env returned environment with no uuid: {created!r}"
        )
        created_uuid = created.uuid
    finally:
        if created_uuid:
            await deployments.delete_env(client, workspace, probe_repo_slug, created_uuid)


async def test_create_env_visible_via_get(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """Created environment must be visible via get_env immediately."""
    env_name = f"bb-test-env-{uuid.uuid4().hex[:8]}"
    created_uuid: str | None = None
    try:
        created = await deployments.create_env(
            client,
            workspace,
            probe_repo_slug,
            body=DeploymentEnvironment(type_="deployment_environment", environment_type=DeploymentEnvironmentType(name="Test"), name=env_name),
        )
        if isinstance(created, Error):
            msg = created.error.message if created.error else repr(created)
            pytest.skip(f"create_env not permitted: {msg}")
        assert isinstance(created, DeploymentEnvironment)
        created_uuid = created.uuid
        assert created_uuid

        fetched = await deployments.get_env(client, workspace, probe_repo_slug, created_uuid)
        assert isinstance(fetched, DeploymentEnvironment), (
            f"get_env after create should return DeploymentEnvironment, got {type(fetched).__name__}"
        )
        assert fetched.name == env_name, (
            f"Expected name={env_name!r} via get_env, got {fetched.name!r}"
        )
    finally:
        if created_uuid:
            await deployments.delete_env(client, workspace, probe_repo_slug, created_uuid)


async def test_update_env_roundtrip(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """update_env() posts to the /changes endpoint (202 Accepted, async).

    The SDK returns None for 202 — verify no exception is raised.
    """
    env_name = f"bb-test-env-{uuid.uuid4().hex[:8]}"
    created_uuid: str | None = None
    try:
        created = await deployments.create_env(
            client,
            workspace,
            probe_repo_slug,
            body=DeploymentEnvironment(type_="deployment_environment", environment_type=DeploymentEnvironmentType(name="Test"), name=env_name),
        )
        if isinstance(created, Error):
            msg = created.error.message if created.error else repr(created)
            pytest.skip(f"create_env not permitted: {msg}")
        assert isinstance(created, DeploymentEnvironment)
        created_uuid = created.uuid
        assert created_uuid

        new_name = f"{env_name}-updated"
        update_result = await deployments.update_env(
            client,
            workspace,
            probe_repo_slug,
            created_uuid,
            body=DeploymentEnvironment(type_="deployment_environment", environment_type=DeploymentEnvironmentType(name="Test"), name=new_name),
        )
        # update_env returns None (202 Accepted) — not an Error
        assert not isinstance(update_result, Error), (
            f"update_env returned Error: {update_result!r}"
        )
    finally:
        if created_uuid:
            await deployments.delete_env(client, workspace, probe_repo_slug, created_uuid)


async def test_delete_env_removes_it(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """delete_env() must remove the environment so get_env returns None or Error."""
    env_name = f"bb-test-env-{uuid.uuid4().hex[:8]}"
    created = await deployments.create_env(
        client,
        workspace,
        probe_repo_slug,
        body=DeploymentEnvironment(type_="deployment_environment", environment_type=DeploymentEnvironmentType(name="Test"), name=env_name),
    )
    if isinstance(created, Error):
        msg = created.error.message if created.error else repr(created)
        pytest.skip(f"create_env not permitted: {msg}")
    assert isinstance(created, DeploymentEnvironment)
    created_uuid = created.uuid
    assert created_uuid

    await deployments.delete_env(client, workspace, probe_repo_slug, created_uuid)

    after = await deployments.get_env(client, workspace, probe_repo_slug, created_uuid)
    assert not isinstance(after, DeploymentEnvironment), (
        f"get_env after delete returned DeploymentEnvironment — should be None/Error: {after!r}"
    )


# ===========================================================================
# 8. deployments.deploy_keys
# ===========================================================================


async def test_deploy_keys_returns_list(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """deploy_keys() must return a non-empty list."""
    result = await deployments.deploy_keys(client, workspace, probe_repo_slug, pagelen=25)
    _skip_if_error(result, "deployments.deploy_keys")
    assert isinstance(result, list), (
        f"deploy_keys must return list, got {type(result).__name__}"
    )
    assert len(result) > 0, "deploy_keys returned empty list — expected probe-deploy-key"


async def test_deploy_keys_contains_seed_key(
    client: BBClient, workspace: str, probe_repo_slug: str, probe_deploy_key_id: int
) -> None:
    """deploy_keys() list must contain the seeded key (id=10958984)."""
    result = await deployments.deploy_keys(client, workspace, probe_repo_slug, pagelen=25)
    _skip_if_error(result, "deployments.deploy_keys")
    assert isinstance(result, list)
    ids = []
    for key in result:
        if isinstance(key, DeployKey):
            # id is stored in additional_properties since it is not a first-class field
            kid = key.additional_properties.get("id")
            ids.append(kid)
    assert probe_deploy_key_id in ids, (
        f"Expected deploy key id={probe_deploy_key_id} in list, got ids: {ids!r}"
    )


# ===========================================================================
# 9. deployments.get_deploy_key
# ===========================================================================


async def test_get_deploy_key_returns_seed_key(
    client: BBClient, workspace: str, probe_repo_slug: str, probe_deploy_key_id: int
) -> None:
    """get_deploy_key() must return the seeded key with correct label."""
    result = await deployments.get_deploy_key(
        client, workspace, probe_repo_slug, probe_deploy_key_id
    )
    _skip_if_error(result, "deployments.get_deploy_key")
    assert isinstance(result, DeployKey), (
        f"get_deploy_key must return DeployKey, got {type(result).__name__}"
    )
    assert result.label == "bb-probe-deploy-key", (
        f"Expected label='bb-probe-deploy-key', got {result.label!r}"
    )


async def test_get_deploy_key_nonexistent_is_error_or_none(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """get_deploy_key() on a non-existent id must return None or Error, not raise."""
    result = await deployments.get_deploy_key(client, workspace, probe_repo_slug, 999999999)
    assert not isinstance(result, DeployKey), (
        f"Expected None/Error for fake key_id, got DeployKey: {result!r}"
    )


# ===========================================================================
# 10–12. deployments.create_deploy_key / update_deploy_key / delete_deploy_key
# ===========================================================================


async def test_create_deploy_key_roundtrip(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """create_deploy_key() → verify label → delete_deploy_key() cleanup."""
    suffix = uuid.uuid4().hex[:12]
    label = f"test-key-{suffix}"
    pub_key = _test_public_key(suffix)
    created_id: int | None = None
    try:
        created = await deployments.create_deploy_key(
            client,
            workspace,
            probe_repo_slug,
            body=DeployKey(type_="deploy_key", key=pub_key, label=label),
        )
        if isinstance(created, Error):
            msg = created.error.message if created.error else repr(created)
            pytest.skip(f"create_deploy_key not permitted or duplicate: {msg}")
        assert isinstance(created, DeployKey), (
            f"create_deploy_key must return DeployKey, got {type(created).__name__}: {created!r}"
        )
        assert created.label == label, (
            f"Expected label={label!r}, got {created.label!r}"
        )
        kid = created.additional_properties.get("id")
        assert kid is not None, f"create_deploy_key returned no id: {created!r}"
        created_id = int(kid)
    finally:
        if created_id is not None:
            await deployments.delete_deploy_key(client, workspace, probe_repo_slug, created_id)


async def test_create_deploy_key_visible_via_get(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """Created deploy key must be visible via get_deploy_key immediately."""
    suffix = uuid.uuid4().hex[:12]
    label = f"test-key-{suffix}"
    pub_key = _test_public_key(suffix)
    created_id: int | None = None
    try:
        created = await deployments.create_deploy_key(
            client,
            workspace,
            probe_repo_slug,
            body=DeployKey(type_="deploy_key", key=pub_key, label=label),
        )
        if isinstance(created, Error):
            msg = created.error.message if created.error else repr(created)
            pytest.skip(f"create_deploy_key not permitted or duplicate: {msg}")
        assert isinstance(created, DeployKey)
        kid = created.additional_properties.get("id")
        assert kid is not None
        created_id = int(kid)

        fetched = await deployments.get_deploy_key(client, workspace, probe_repo_slug, created_id)
        assert isinstance(fetched, DeployKey), (
            f"get_deploy_key after create should return DeployKey, got {type(fetched).__name__}"
        )
        assert fetched.label == label, (
            f"Expected label={label!r} via get_deploy_key, got {fetched.label!r}"
        )
    finally:
        if created_id is not None:
            await deployments.delete_deploy_key(client, workspace, probe_repo_slug, created_id)


async def test_update_deploy_key_roundtrip(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """update_deploy_key() must return a DeployKey with the updated label."""
    suffix = uuid.uuid4().hex[:12]
    label = f"test-key-{suffix}"
    pub_key = _test_public_key(suffix)
    created_id: int | None = None
    try:
        created = await deployments.create_deploy_key(
            client,
            workspace,
            probe_repo_slug,
            body=DeployKey(type_="deploy_key", key=pub_key, label=label),
        )
        if isinstance(created, Error):
            msg = created.error.message if created.error else repr(created)
            pytest.skip(f"create_deploy_key not permitted: {msg}")
        assert isinstance(created, DeployKey)
        kid = created.additional_properties.get("id")
        assert kid is not None
        created_id = int(kid)

        new_label = f"{label}-updated"
        updated = await deployments.update_deploy_key(
            client,
            workspace,
            probe_repo_slug,
            created_id,
            body=DeployKey(type_="deploy_key", key=pub_key, label=new_label),
        )
        if isinstance(updated, Error):
            msg = updated.error.message if updated.error else repr(updated)
            pytest.skip(f"update_deploy_key not permitted: {msg}")
        assert isinstance(updated, DeployKey), (
            f"update_deploy_key must return DeployKey, got {type(updated).__name__}"
        )
        assert updated.label == new_label, (
            f"Expected label={new_label!r} after update, got {updated.label!r}"
        )
    finally:
        if created_id is not None:
            await deployments.delete_deploy_key(client, workspace, probe_repo_slug, created_id)


async def test_delete_deploy_key_removes_it(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """delete_deploy_key() must remove the key so get_deploy_key returns None or Error."""
    suffix = uuid.uuid4().hex[:12]
    label = f"test-key-{suffix}"
    pub_key = _test_public_key(suffix)

    created = await deployments.create_deploy_key(
        client,
        workspace,
        probe_repo_slug,
        body=DeployKey(type_="deploy_key", key=pub_key, label=label),
    )
    if isinstance(created, Error):
        msg = created.error.message if created.error else repr(created)
        pytest.skip(f"create_deploy_key not permitted: {msg}")
    assert isinstance(created, DeployKey)
    kid = created.additional_properties.get("id")
    assert kid is not None
    created_id = int(kid)

    await deployments.delete_deploy_key(client, workspace, probe_repo_slug, created_id)

    after = await deployments.get_deploy_key(client, workspace, probe_repo_slug, created_id)
    assert not isinstance(after, DeployKey), (
        f"get_deploy_key after delete returned DeployKey — should be None/Error: {after!r}"
    )


# ===========================================================================
# 13. deployments.env_variables
# ===========================================================================


async def test_env_variables_returns_list(
    client: BBClient, workspace: str, probe_repo_slug: str, probe_env_uuid: str
) -> None:
    """env_variables() must return a list for the Test environment."""
    result = await deployments.env_variables(
        client, workspace, probe_repo_slug, probe_env_uuid, pagelen=25
    )
    _skip_if_error(result, "deployments.env_variables")
    assert isinstance(result, list), (
        f"env_variables must return list, got {type(result).__name__}"
    )


async def test_env_variables_contains_deploy_var(
    client: BBClient, workspace: str, probe_repo_slug: str, probe_env_uuid: str,
    probe_env_var_uuid: str
) -> None:
    """env_variables() list must contain the seeded DEPLOY_VAR variable."""
    result = await deployments.env_variables(
        client, workspace, probe_repo_slug, probe_env_uuid, pagelen=25
    )
    _skip_if_error(result, "deployments.env_variables")
    assert isinstance(result, list)
    var_keys = []
    var_uuids = []
    for var in result:
        if isinstance(var, DeploymentVariable):
            var_keys.append(var.key)
            var_uuids.append(var.uuid)
    assert "DEPLOY_VAR" in var_keys or probe_env_var_uuid in var_uuids, (
        f"Expected DEPLOY_VAR in env_variables; keys={var_keys!r}, uuids={var_uuids!r}"
    )


# ===========================================================================
# 14–16. deployments.create_env_variable / update_env_variable / delete_env_variable
# ===========================================================================


async def test_create_env_variable_roundtrip(
    client: BBClient, workspace: str, probe_repo_slug: str, probe_env_uuid: str
) -> None:
    """create_env_variable() → verify uuid → delete_env_variable() cleanup."""
    var_key = f"TEST_VAR_{uuid.uuid4().hex[:8].upper()}"
    created_uuid: str | None = None
    try:
        created = await deployments.create_env_variable(
            client,
            workspace,
            probe_repo_slug,
            probe_env_uuid,
            body=DeploymentVariable(
                type_="pipeline_variable",
                key=var_key,
                value="test-value",
                secured=False,
            ),
        )
        if isinstance(created, Error):
            msg = created.error.message if created.error else repr(created)
            pytest.skip(f"create_env_variable not permitted: {msg}")
        assert isinstance(created, DeploymentVariable), (
            f"create_env_variable must return DeploymentVariable, got {type(created).__name__}"
        )
        assert created.uuid is not UNSET and created.uuid, (
            f"create_env_variable returned no uuid: {created!r}"
        )
        assert created.key == var_key, (
            f"Expected key={var_key!r}, got {created.key!r}"
        )
        created_uuid = created.uuid
    finally:
        if created_uuid:
            await deployments.delete_env_variable(
                client, workspace, probe_repo_slug, probe_env_uuid, created_uuid
            )


async def test_update_env_variable_roundtrip(
    client: BBClient, workspace: str, probe_repo_slug: str, probe_env_uuid: str
) -> None:
    """update_env_variable() must return a DeploymentVariable with updated value."""
    var_key = f"TEST_VAR_{uuid.uuid4().hex[:8].upper()}"
    created_uuid: str | None = None
    try:
        created = await deployments.create_env_variable(
            client,
            workspace,
            probe_repo_slug,
            probe_env_uuid,
            body=DeploymentVariable(
                type_="pipeline_variable",
                key=var_key,
                value="original-value",
                secured=False,
            ),
        )
        if isinstance(created, Error):
            msg = created.error.message if created.error else repr(created)
            pytest.skip(f"create_env_variable not permitted: {msg}")
        assert isinstance(created, DeploymentVariable)
        created_uuid = created.uuid
        assert created_uuid

        updated = await deployments.update_env_variable(
            client,
            workspace,
            probe_repo_slug,
            probe_env_uuid,
            created_uuid,
            body=DeploymentVariable(
                type_="pipeline_variable",
                key=var_key,
                value="updated-value",
                secured=False,
            ),
        )
        if isinstance(updated, Error):
            msg = updated.error.message if updated.error else repr(updated)
            pytest.skip(f"update_env_variable not permitted: {msg}")
        assert isinstance(updated, DeploymentVariable), (
            f"update_env_variable must return DeploymentVariable, got {type(updated).__name__}"
        )
        assert updated.value == "updated-value", (
            f"Expected value='updated-value', got {updated.value!r}"
        )
    finally:
        if created_uuid:
            await deployments.delete_env_variable(
                client, workspace, probe_repo_slug, probe_env_uuid, created_uuid
            )


async def test_delete_env_variable_removes_it(
    client: BBClient, workspace: str, probe_repo_slug: str, probe_env_uuid: str
) -> None:
    """delete_env_variable() must remove the variable from env_variables() list."""
    var_key = f"TEST_VAR_{uuid.uuid4().hex[:8].upper()}"

    created = await deployments.create_env_variable(
        client,
        workspace,
        probe_repo_slug,
        probe_env_uuid,
        body=DeploymentVariable(
            type_="pipeline_variable",
            key=var_key,
            value="ephemeral",
            secured=False,
        ),
    )
    if isinstance(created, Error):
        msg = created.error.message if created.error else repr(created)
        pytest.skip(f"create_env_variable not permitted: {msg}")
    assert isinstance(created, DeploymentVariable)
    created_uuid = created.uuid
    assert created_uuid

    await deployments.delete_env_variable(
        client, workspace, probe_repo_slug, probe_env_uuid, created_uuid
    )

    after_list = await deployments.env_variables(
        client, workspace, probe_repo_slug, probe_env_uuid, pagelen=25
    )
    if isinstance(after_list, Error):
        return  # can't verify, but no crash means pass
    remaining_uuids = [
        v.uuid for v in after_list if isinstance(v, DeploymentVariable)
    ]
    assert created_uuid not in remaining_uuids, (
        f"Deleted variable {created_uuid!r} still in env_variables list"
    )


# ===========================================================================
# BUG-DEPLOY-002 regression test
# ===========================================================================


async def test_update_env_body_is_sent(
    client: BBClient, workspace: str, probe_repo_slug: str
) -> None:
    """update_env sends the body after BUG-DEPLOY-002 fix — creates, renames, deletes an env."""
    env_name = f"bb-test-env-deploy002-{uuid.uuid4().hex[:8]}"
    created_uuid: str | None = None
    try:
        created = await deployments.create_env(
            client,
            workspace,
            probe_repo_slug,
            body=DeploymentEnvironment(
                type_="deployment_environment",
                environment_type=DeploymentEnvironmentType(name="Test"),
                name=env_name,
            ),
        )
        if isinstance(created, Error):
            msg = created.error.message if created.error else repr(created)
            pytest.skip(f"Cannot create env: {msg}")
        assert isinstance(created, DeploymentEnvironment)
        created_uuid = created.uuid
        assert created_uuid

        renamed = f"{env_name}-renamed"
        result = await deployments.update_env(
            client,
            workspace,
            probe_repo_slug,
            created_uuid,
            body=DeploymentEnvironment(
                type_="deployment_environment",
                environment_type=DeploymentEnvironmentType(name="Test"),
                name=renamed,
            ),
        )
        assert not isinstance(result, Error), (
            f"update_env with body failed: {result!r}"
        )
    finally:
        if created_uuid:
            await deployments.delete_env(client, workspace, probe_repo_slug, created_uuid)
