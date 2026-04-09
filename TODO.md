# bb — Task Tracker

> Format: `- [x]` = done, `- [ ]` = pending, `- [~]` = in progress

---

## Setup & Infrastructure

- [x] Initialize project with `uv`
- [x] Obtain Bitbucket Cloud OpenAPI spec (`bb_cloud.openapi.json`)
- [x] Fix OpenAPI spec for parser compatibility (`bb_cloud_fixed.openapi.json`)
- [x] Create `config/generator.yml` for openapi-python-client
- [x] Generate Cloud client with `uvx openapi-python-client` (0-error, 382 models, all API tags)
- [x] Sync generated code into `src/bb/cloud/` (models, api, client.py, types.py, errors.py)
- [x] Restructure for multi-target: `src/bb/cloud/` (Cloud) + `src/bb/datacenter/` (future DC)
- [x] Add `httpx`, `attrs`, `python-dateutil` to `pyproject.toml` and run `uv sync`
- [x] Verify generated client importable: `from bb.cloud.client import AuthenticatedClient`
- [x] Configure `amdb.toml` with exclude list; initialized amdb index
- [x] Write `CLAUDE.md` with conventions, ownership boundary, pitfalls
- [x] Set up `cmd_outputs/` with separate stdout/stderr timestamped convention
- [x] Delete misplaced `bb_out/` (old generated client in wrong location)
- [ ] Fetch typer reference docs → `context/typer/` (use `gh api` or curl)
- [ ] Fetch openapi-python-client template docs → `context/openapi_python_client/` (already partially done)

---

## Templates (openapi-python-client Jinja2 Customization)

- [x] Override `endpoint_module.py.jinja` → add `__all__` using `parsed_responses` variable
- [x] Regenerate after template change and verify `__all__` appears in output
- [ ] Validate generated code quality (ruff, imports, type hints)

---

## Phase 1 — Cloud SDK (current focus)

### Auth & Client Factory
- [x] Implement `src/bb/cloud/sdk/_client.py` — `BBClient` class
  - Reads `BB_TOKEN` from env (clear error if missing)
  - Reads `BB_WORKSPACE` from env (optional default)
  - `BBClient.from_env()` → configured `AuthenticatedClient`
  - `base_url = "https://api.bitbucket.org/2.0"`

### Resource Modules (Phase 1 — initial coverage)
- [x] `src/bb/cloud/sdk/workspaces.py` — list + 11 new functions (get, members, permissions, etc.)
- [x] `src/bb/cloud/sdk/repos.py` — list/get/create/update/delete/fork + 13 new (permissions, overrides)
- [x] `src/bb/cloud/sdk/prs.py` — core CRUD + 17 new (comments, tasks, activity, diffstat, etc.)
- [x] `src/bb/cloud/sdk/pipelines.py` — core ops + 18 new (runners, schedules, known_hosts, caches, etc.)
- [x] `src/bb/cloud/sdk/commits.py` — `list_commits`, `get_commit`
- [x] `src/bb/cloud/sdk/branches.py` — `list_branches`, `create_branch`
  - Note: branch create uses httpx directly — spec has no requestBody for this endpoint
- [x] `src/bb/cloud/sdk/issues.py` — core CRUD + 18 new (comments, changes, attachments, import/export)
- [x] `src/bb/cloud/sdk/snippets.py` — core CRUD + 13 new (nodes, diff, patch, watching)
- [x] `src/bb/cloud/sdk/deployments.py` — existing + 4 new (env_variables CRUD)
- [x] `src/bb/cloud/sdk/projects.py` — existing + `list()` function
- [x] `src/bb/cloud/sdk/search.py` — existing + `account()`, `team()` functions
- [x] `src/bb/cloud/sdk/addon.py` — new module, 10 functions (linkers, linker values)

### Sync Wrappers
- [x] All `src/bb/cloud/sync/` wrappers regenerated to match expanded SDK `__all__` lists
- [x] `src/bb/cloud/sync/addon.py` — new sync wrapper for addon module

### Public Surface
- [x] `src/bb/cloud/__init__.py` — `__all__`, re-exports `BBClient`, resource modules, `paginate`
- [x] `src/bb/cloud/sdk/__init__.py` — `__all__` listing all resource modules (incl. addon)
- [x] `src/bb/cloud/sync/__init__.py` — `__all__` listing all sync modules (incl. addon)

### Pagination
- [x] `src/bb/cloud/sdk/_pagination.py` — `async_paginate()` async generator for page-based endpoints
- [ ] Cursor-based pagination (follow `next_` URL) for endpoints without explicit page param

---

## Phase 2 — CLI (after SDK complete)

- [ ] Fetch typer reference docs → `context/typer/`
- [ ] Implement `src/bb/cli/__init__.py` — root Typer app, global options (`--workspace`, `--json`, `--verbose`, `--target cloud|datacenter`)
- [ ] `bb repo` — list, view, create, clone, delete
- [ ] `bb pr` — list, view, create, merge, approve, checkout, diff
- [ ] `bb pipeline` — list, view, run
- [ ] `bb commit` — list, view
- [ ] `bb branch` — list, create
- [ ] `bb workspace` — list, use
- [ ] Rich table output for list commands
- [ ] Rich panel output for view commands
- [ ] `--json` global flag for machine-readable output
- [ ] `bb --help` shows all resource groups

---

## Phase 3 — Datacenter (future)

- [ ] Obtain Bitbucket Data Center OpenAPI spec
- [ ] Create `config/datacenter.yml`
- [ ] Generate DC client → sync into `src/bb/datacenter/`
- [ ] Mirror SDK wrappers in `src/bb/datacenter/sdk/`
- [ ] Wire datacenter target into CLI (`--target datacenter`)

---

## Quality & Distribution

- [ ] Write tests for Cloud SDK layer
- [ ] Integration smoke tests
- [ ] Configure `pyproject.toml` for distribution
- [ ] CI/CD pipeline
