"""Fixtures for live Bitbucket Cloud SDK integration tests.

See ``index.md`` in this directory for environment-variable documentation and
how to generate each credential.
"""

from __future__ import annotations

import os
import uuid
from pathlib import Path

import pytest

from bb.cloud.models.error import Error
from bb.cloud.sdk import branches as branches_sdk
from bb.cloud.sdk import commits as commits_sdk
from bb.cloud.sdk import projects as projects_sdk
from bb.cloud.sdk import prs as prs_sdk
from bb.cloud.sdk import repos as repos_sdk
from bb.cloud.sdk._client import BBClient


def _load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {chr(34), chr(39)}:
            value = value[1:-1]
        os.environ.setdefault(key.strip(), value)


_load_dotenv(Path(__file__).resolve().parents[3] / ".env")


def pytest_addoption(parser):
    parser.addoption(
        "--run-live",
        action="store_true",
        default=False,
        help="Force live integration tests even if credentials look missing.",
    )


def _has_any_auth() -> bool:
    return bool(
        (os.environ.get("BB_EMAIL") and os.environ.get("BB_TOKEN"))
        or (os.environ.get("BB_OAUTH_CLIENT_ID") and os.environ.get("BB_OAUTH_CLIENT_SECRET"))
        or os.environ.get("BB_OAUTH_TOKEN")
        or (os.environ.get("BB_JWT_CLIENT_KEY") and os.environ.get("BB_JWT_CLIENT_SECRET"))
        or (os.environ.get("BB_USERNAME") and os.environ.get("BB_APP_PASSWORD"))
    )


def pytest_collection_modifyitems(config, items):
    has_creds = _has_any_auth() and bool(os.environ.get("BB_WORKSPACE"))
    run_live = config.getoption("--run-live", default=False)
    if has_creds or run_live:
        return
    skip = pytest.mark.skip(
        reason="live tests require BB_WORKSPACE plus a supported auth method "
        "(BB_EMAIL/BB_TOKEN, BB_OAUTH_*, BB_JWT_*, or BB_USERNAME/BB_APP_PASSWORD) — see tests/cloud/live/index.md",
    )
    for item in items:
        if item.get_closest_marker("live"):
            item.add_marker(skip)


@pytest.fixture(scope="session")
def workspace() -> str:
    ws = os.environ.get("BB_WORKSPACE")
    if not ws:
        pytest.skip("BB_WORKSPACE is not set")
    return ws


@pytest.fixture
def client() -> BBClient:
    return BBClient.from_env()


@pytest.fixture(scope="session")
def _session_client() -> BBClient:
    return BBClient.from_env()


@pytest.fixture(scope="session")
async def probe_repo_slug(_session_client: BBClient, workspace: str) -> str:
    pinned = os.environ.get("BB_REPO_SLUG", "").strip()
    if pinned:
        return pinned
    repo_list = await repos_sdk.list(_session_client, workspace, pagelen=1)
    if isinstance(repo_list, Error):
        msg = repo_list.error.message if getattr(repo_list, "error", None) else repo_list
        pytest.skip(f"repos.list errored: {msg!r}")
    if not repo_list:
        pytest.skip(f"workspace {workspace!r} has no repos — set BB_REPO_SLUG to a known repo")
    full_name = repo_list[0].full_name
    assert full_name, f"first repo has no full_name: {repo_list[0]!r}"
    return full_name.split("/", 1)[-1]


@pytest.fixture(scope="session")
async def probe_branch_name(_session_client: BBClient, workspace: str, probe_repo_slug: str) -> str:
    branch_list = await branches_sdk.list(_session_client, workspace, probe_repo_slug, pagelen=1)
    if isinstance(branch_list, Error):
        msg = branch_list.error.message if getattr(branch_list, "error", None) else branch_list
        pytest.skip(f"branches.list errored on {probe_repo_slug!r}: {msg!r}")
    if not branch_list:
        pytest.skip(f"repo {probe_repo_slug!r} has no branches")
    name = branch_list[0].name
    assert name, f"first branch has no name: {branch_list[0]!r}"
    return name


@pytest.fixture(scope="session")
async def probe_commit_hash(_session_client: BBClient, workspace: str, probe_repo_slug: str) -> str:
    commit_list = await commits_sdk.list(_session_client, workspace, probe_repo_slug, pagelen=1)
    if isinstance(commit_list, Error):
        msg = commit_list.error.message if getattr(commit_list, "error", None) else commit_list
        pytest.skip(f"commits.list errored on {probe_repo_slug!r}: {msg!r}")
    if not commit_list:
        pytest.skip(f"repo {probe_repo_slug!r} has no commits")
    hash_ = commit_list[0].hash_
    assert hash_, f"first commit has no hash: {commit_list[0]!r}"
    return hash_


@pytest.fixture(scope="session")
async def probe_pr_id(_session_client: BBClient, workspace: str, probe_repo_slug: str) -> int:
    from bb.cloud.models.get_repositories_workspace_repo_slug_pullrequests_state import (
        GetRepositoriesWorkspaceRepoSlugPullrequestsState as State,
    )

    for state in (None, State.OPEN, State.MERGED, State.DECLINED, State.SUPERSEDED):
        kwargs: dict = {"pagelen": 1}
        if state is not None:
            kwargs["state"] = state
        pr_list = await prs_sdk.list(_session_client, workspace, probe_repo_slug, **kwargs)
        if isinstance(pr_list, Error) or not pr_list:
            continue
        first = pr_list[0]
        if first.id is not None:
            return first.id
    pytest.skip(f"repo {probe_repo_slug!r} has no pull requests in any state")


@pytest.fixture(scope="session")
async def probe_project_key(_session_client: BBClient, workspace: str) -> str:
    pinned = os.environ.get("BB_PROJECT_KEY", "").strip()
    if pinned:
        return pinned
    project_list = await projects_sdk.list(_session_client, workspace, pagelen=1)
    if isinstance(project_list, Error):
        msg = project_list.error.message if getattr(project_list, "error", None) else project_list
        pytest.skip(f"projects.list errored: {msg!r}")
    if not project_list:
        pytest.skip(f"workspace {workspace!r} has no projects — set BB_PROJECT_KEY")
    key = project_list[0].key
    assert key, f"first project has no key: {project_list[0]!r}"
    return key


@pytest.fixture
def throwaway_repo_slug() -> str:
    return f"bb-sdk-live-{uuid.uuid4().hex[:8]}"


@pytest.fixture
def throwaway_project_key() -> str:
    return f"BB{uuid.uuid4().hex[:4].upper()}"
