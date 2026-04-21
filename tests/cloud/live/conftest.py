"""Fixtures for live Bitbucket Cloud SDK integration tests."""

from __future__ import annotations

import os
import uuid
from pathlib import Path

import pytest

from bb.cloud.sdk._client import BBClient


def _load_dotenv(path: Path) -> None:
    """Load KEY=value lines from ``path`` into os.environ (no overwrite)."""
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip())


_load_dotenv(Path(__file__).resolve().parents[3] / ".env")


def pytest_collection_modifyitems(config, items):
    """Auto-skip live tests unless credentials are present or --run-live set."""
    has_creds = all(os.environ.get(k) for k in ("BB_EMAIL", "BB_TOKEN", "BB_WORKSPACE"))
    run_live = config.getoption("--run-live", default=False)
    if has_creds or run_live:
        return
    skip = pytest.mark.skip(reason="live creds (BB_EMAIL/BB_TOKEN/BB_WORKSPACE) not set")
    for item in items:
        item.add_marker(skip)


def pytest_addoption(parser):
    parser.addoption(
        "--run-live",
        action="store_true",
        default=False,
        help="Force live integration tests even if creds look missing",
    )


@pytest.fixture(scope="session")
def workspace() -> str:
    ws = os.environ.get("BB_WORKSPACE")
    if not ws:
        pytest.skip("BB_WORKSPACE not set")
    return ws


@pytest.fixture
def client() -> BBClient:
    # Function-scoped so the underlying httpx AsyncClient binds to each
    # test's event loop (pytest-asyncio creates a fresh loop per test).
    return BBClient.from_env()


@pytest.fixture
def throwaway_repo_slug() -> str:
    """A unique repo slug safe to use for write tests."""
    return f"bb-sdk-live-{uuid.uuid4().hex[:8]}"
