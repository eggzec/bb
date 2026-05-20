"""Fixtures and setup for Bitbucket Data Center live API tests.

Loads credentials from .env (BB_DC_BASE_URL, BB_DC_TOKEN, etc.) and provides
session-scoped fixtures for DC API testing.

All tests in this directory are marked with @pytest.mark.live and will be
skipped if BB_DC_TOKEN (or BB_DC_USERNAME+BB_DC_PASSWORD) is not set in .env.
"""
from __future__ import annotations

import os

import pytest
from dotenv import load_dotenv

from bb.datacenter.sdk import BBDCClient

# Load .env at module import time
load_dotenv()


def _has_dc_auth() -> bool:
    """Check if DC authentication credentials are available."""
    has_token = bool(os.environ.get("BB_DC_TOKEN"))
    has_basic = bool(os.environ.get("BB_DC_USERNAME") and os.environ.get("BB_DC_PASSWORD"))
    return has_token or has_basic


def pytest_collection_modifyitems(items: list) -> None:
    """Auto-skip live tests if DC credentials are not set."""
    if not _has_dc_auth():
        skip = pytest.mark.skip(
            reason="BB_DC_TOKEN (or BB_DC_USERNAME+BB_DC_PASSWORD) not set in .env"
        )
        for item in items:
            if "datacenter/live" in str(item.fspath):
                item.add_marker(skip)


@pytest.fixture(scope="session")
def dc_client() -> BBDCClient:
    """Return an authenticated BBDCClient using credentials from .env."""
    return BBDCClient.from_env()


@pytest.fixture(scope="session")
def dc_project_key() -> str:
    """Return the DC project key, skip test if not set in .env."""
    val = os.environ.get("BB_DC_PROJECT_KEY", "").strip()
    if not val:
        pytest.skip("BB_DC_PROJECT_KEY not set — run `make schema-discover-dc` first")
    return val


@pytest.fixture(scope="session")
def dc_repo_slug() -> str:
    """Return the DC repository slug, skip test if not set in .env."""
    val = os.environ.get("BB_DC_REPO_SLUG", "").strip()
    if not val:
        pytest.skip("BB_DC_REPO_SLUG not set — run `make schema-discover-dc` first")
    return val


@pytest.fixture(scope="session")
def dc_branch_name(dc_client: BBDCClient, dc_project_key: str, dc_repo_slug: str) -> str:
    """Return a branch name from the probe repo, skip if none exist."""
    branches = dc_client.branches.list(dc_project_key, dc_repo_slug)
    if not branches:
        pytest.skip(f"No branches found in {dc_project_key}/{dc_repo_slug}")
    return branches[0].display_id


@pytest.fixture(scope="session")
def dc_commit_hash(dc_client: BBDCClient, dc_project_key: str, dc_repo_slug: str) -> str:
    """Return a commit hash from the probe repo, skip if none exist."""
    commits = dc_client.commits.list(dc_project_key, dc_repo_slug, limit=1)
    if not commits:
        pytest.skip(f"No commits found in {dc_project_key}/{dc_repo_slug}")
    return commits[0].id


@pytest.fixture(scope="session")
def dc_pr_id(dc_client: BBDCClient, dc_project_key: str, dc_repo_slug: str) -> int:
    """Return a PR ID from the probe repo, skip if none exist."""
    prs = dc_client.prs.list(dc_project_key, dc_repo_slug)
    if not prs:
        pytest.skip(f"No pull requests found in {dc_project_key}/{dc_repo_slug}")
    return prs[0].id
