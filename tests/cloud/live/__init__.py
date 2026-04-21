"""Live Bitbucket Cloud API integration tests.

These tests exercise the SDK against the real Bitbucket Cloud API. They are
opt-in: a test is skipped unless all of BB_EMAIL, BB_TOKEN, and BB_WORKSPACE
are present in the environment (loaded automatically from ``.env`` if
present).

Run with::

    uv run pytest tests/cloud/live -m live
    uv run pytest tests/cloud/live --run-live

Tests are read-only unless marked ``@pytest.mark.writes``. Write tests
create and tear down a uniquely-named throwaway repository.
"""
