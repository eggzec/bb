# Stage 1 — Test Environment Preparation Checklist

**Workspace:** `beaverish`  
**Probe repo:** `bb-probe`  
**Seeding strategy:** `context/test_data_seeding_strategy.md`  
**Re-probe:** `make probe-workspace`

Mark each item `[x]` when done. Fill in discovered IDs — they are needed by test fixtures and `.env`.

---

## 0 — Credentials & `.env`

- [ ] `BB_EMAIL` set in `.env`  
  value: `___`

- [ ] `BB_TOKEN` set in `.env` (API token from id.atlassian.com, not app password)  
  value: `ATATT3x…` *(do not record full token here)*

- [ ] `BB_WORKSPACE` set in `.env`  
  value: `___`

- [ ] `BB_REPO_SLUG` set in `.env`  
  value: `___`

- [ ] `BB_PROJECT_KEY` set in `.env`  
  value: `___`

- [ ] `BB_SEARCH_QUERY` set in `.env` (a string that exists in the probe repo code)  
  value: `___`

---

## 1 — Identity

- [ ] Authenticated user resolves (`users.me`)  
  display_name: `___`  
  account_id: `___`  
  uuid: `___`

- [ ] Workspace accessible (`workspaces.get`)  
  slug: `___`  
  uuid: `___`

---

## 2 — Project

- [ ] At least one project exists  
  key: `___`  
  name: `___`  
  uuid: `___`

---

## 3 — Probe repository (`bb-probe`)

- [ ] Repository `bb-probe` exists  
  full_name: `beaverish/bb-probe`  
  uuid: `___`

- [ ] Repository has issues tracker enabled  
  setting: Public / Private *(circle one)*

- [ ] Repository is assigned to project `PROJ`

---

## 4 — Commits & branches

- [ ] At least one commit on `main`  
  first_commit_hash: `___`

- [ ] `main` branch exists  
  branch_name: `main`

- [ ] At least one additional feature branch exists (needed for PR source)  
  branch_name: `___`

- [ ] At least one git tag exists  
  tag_name: `___`  
  tag_hash: `___`

---

## 5 — Source

- [ ] Source tree root is accessible (`source.root`)

- [ ] At least one file path is known for `source.get` / `source.history`  
  file_path: `___`

---

## 6 — Commit statuses

- [ ] At least one build status on the latest commit  
  key: `___`  
  state: `SUCCESSFUL / FAILED / INPROGRESS` *(circle one)*

---

## 7 — Code Insights reports

- [ ] At least one report on the latest commit  
  report_id: `___`  
  report_type: `TEST / COVERAGE / BUG / SECURITY / VULNERABILITY / OTHER` *(circle one)*

- [ ] At least one annotation on that report  
  annotation_id: `___`

---

## 8 — Pull requests

- [ ] At least one **open** pull request exists  
  pr_id: `___`  
  source_branch: `___`  
  destination_branch: `main`

- [ ] At least one **merged** pull request exists *(can be same PR after merge — update id)*  
  pr_id: `___`

- [ ] At least one comment on the open PR  
  comment_id: `___`

- [ ] At least one task on the open PR  
  task_id: `___`

---

## 9 — Branching model

- [ ] Effective branching model accessible (`branching_model.effective`)  
  development_branch: `___`

- [ ] Branching model settings readable (`branching_model.settings`)

---

## 10 — Branch restrictions

- [ ] At least one branch restriction rule exists  
  restriction_id: `___`  
  kind: `___`  
  pattern: `___`

---

## 11 — Default reviewers

- [ ] At least one default reviewer configured on the repo *(optional — skip if workspace has only one user)*  
  account_id: `___`

---

## 12 — Pipelines

- [ ] Pipelines enabled on `bb-probe`

- [ ] `bitbucket-pipelines.yml` present on `main`

- [ ] At least one pipeline run exists  
  pipeline_uuid: `___`  
  state: `SUCCESSFUL / FAILED / IN_PROGRESS` *(circle one)*

- [ ] Pipeline run has at least one step  
  step_uuid: `___`  
  step_name: `___`

- [ ] At least one pipeline repository variable  
  variable_uuid: `___`  
  key: `___`

- [ ] At least one pipeline schedule (enabled: false is fine)  
  schedule_uuid: `___`  
  cron: `___`

- [ ] At least one pipeline known host  
  known_host_uuid: `___`  
  hostname: `___`

- [ ] Pipeline SSH key pair generated  
  *(UI: Repo settings → Pipelines → SSH keys → Generate)*

- [ ] Pipeline caches present (generated automatically after a run that uses `caches:`)  
  cache_uuid: `___`  
  cache_name: `___`

---

## 13 — Workspace-level pipeline resources

- [ ] At least one workspace pipeline variable  
  variable_uuid: `___`  
  key: `___`

---

## 14 — Deployments

- [ ] At least one deployment environment exists  
  environment_uuid: `___`  
  environment_name: `___` *(e.g. Test)*

- [ ] At least one additional environment *(Staging or Production)*  
  environment_uuid: `___`  
  environment_name: `___`

- [ ] At least one deployment object exists (requires a pipeline `deployment:` step to have run)  
  deployment_uuid: `___`

- [ ] At least one variable on the first environment  
  env_var_uuid: `___`  
  key: `___`

---

## 15 — Deploy keys

- [ ] At least one deploy key on `bb-probe`  
  key_id: `___`  
  label: `___`

---

## 16 — Webhooks

- [ ] At least one **repo** webhook on `bb-probe`  
  webhook_uuid: `___`  
  url: `___`

- [ ] At least one **workspace** webhook  
  webhook_uuid: `___`  
  url: `___`

---

## 17 — Issues

- [ ] Issue tracker enabled and at least one issue exists  
  issue_id: `___`  
  title: `___`

- [ ] At least one comment on that issue  
  comment_id: `___`

- [ ] At least one milestone  
  milestone_id: `___`  
  name: `___`

- [ ] At least one version  
  version_id: `___`  
  name: `___`

- [ ] At least one component  
  component_id: `___`  
  name: `___`

---

## 18 — Downloads

- [ ] At least one file uploaded to `bb-probe` downloads  
  filename: `___`  
  size: `___`

---

## 19 — Snippets

- [ ] At least one snippet exists in workspace `beaverish`  
  encoded_id: `___`  
  title: `___`

- [ ] Snippet has at least one file  
  file_path: `___`

- [ ] Snippet has at least one comment  
  comment_id: `___`

- [ ] Snippet has at least one commit (auto-created on first save)  
  revision: `___`

---

## 20 — Repo permissions

- [ ] Repo has at least one group permission entry *(requires a workspace group to exist)*  
  group_slug: `___`  
  permission: `read / write / admin` *(circle one)*

- [ ] Repo has at least one explicit user permission entry  
  account_id: `___`  
  permission: `read / write / admin` *(circle one)*

---

## 21 — User account resources

- [ ] At least one SSH key on the Bitbucket account  
  key_uuid: `___`  
  label: `___`

- [ ] At least one GPG key on the Bitbucket account  
  fingerprint: `___`

---

## 22 — Workspace members

- [ ] Workspace has at least one member (for `workspaces.members / get_member`)  
  member_account_id: `___`

---

## 23 — Search

- [ ] `BB_SEARCH_QUERY` returns at least one result against `bb-probe`  
  query: `___`  
  tested: yes / no *(circle one)*

---

## Untestable — no action required

These require infrastructure beyond a standard Bitbucket Cloud account.
Document here for reference; do not block Stage 1 completion on them.

- [ ] **Connect add-on** — `addon.*` (10 fn) + `properties.*` (12 fn)  
  reason: requires a deployed Connect app with installed lifecycle  
  status: `not applicable`

- [ ] **Self-hosted runners** — `pipelines.runners` / `pipelines.workspace_runners` (10 fn)  
  reason: requires a running runner agent registered with the workspace  
  status: `not applicable`

- [ ] **Pipeline test reports** — `pipelines.test_reports/test_cases/test_case_reasons` (3 fn)  
  reason: requires a pipeline step that publishes JUnit XML via Bitbucket's test-report feature  
  status: `not applicable`

---

## Completion criteria

**Stage 1 is complete when:**

- All items in sections 0–23 are checked **or** explicitly marked `n/a` with a reason.
- `make probe-workspace` reports ≥ 34/38 resource categories present.
- All discovered IDs are filled in above.
- `.env` contains `BB_REPO_SLUG`, `BB_PROJECT_KEY`, and `BB_SEARCH_QUERY`.

Record the final probe score here:  
**Final score:** `___ / 38`  
**Probe run timestamp:** `___`
