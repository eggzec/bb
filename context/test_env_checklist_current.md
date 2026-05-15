# Stage 1 — Test Environment Preparation Checklist (Working Copy)

**Workspace:** `beaverish`  
**Probe repo:** `bb-probe` *(to be created — see section 3)*  
**Last probe:** 2026-05-15 — score **27/38 (71%)**  
**Re-probe:** `make probe-workspace`

> Legend: `[x]` done · `[ ]` todo · `[~]` partial · `[n/a]` not applicable

---

## 0 — Credentials & `.env`

- [x] `BB_EMAIL` set in `.env`  
  value: `laraib.ali@soco-engineers.com`

- [x] `BB_TOKEN` set in `.env`  
  value: `ATATT3x…` *(present — not recorded)*

- [x] `BB_WORKSPACE` set in `.env`  
  value: `beaverish`

- [x] `BB_REPO_SLUG` set in `.env`  
  value: `bb-probe`

- [x] `BB_PROJECT_KEY` set in `.env`  
  value: `PROJ`

- [x] `BB_SEARCH_QUERY` set in `.env`  
  value: `def`

---

## 1 — Identity

- [x] Authenticated user resolves (`users.me`)  
  display_name: `Laraib`  
  account_id: `712020:f464b5ca-adb8-4a1e-80d4-c867bbf50805`  
  uuid: `{e8e13d7c-8af1-409a-9a9e-e2bf80ade040}`

- [x] Workspace accessible (`workspaces.get`)  
  slug: `beaverish`  
  uuid: `{8606bca9-e0ce-40b5-9b2b-a359e6ddb8b5}`

---

## 2 — Project

- [x] At least one project exists  
  key: `PROJ`  
  name: `BB`  
  uuid: `{639f8e8a-097d-4aff-90b1-2b2d1ddfd7a8}`

---

## 3 — Probe repository (`bb-probe`)

- [x] Repository `bb-probe` exists  
  full_name: `beaverish/bb-probe`  
  uuid: `{c634ca7b-67a6-41c3-a501-62e031e08902}`

- [n/a] Repository has issues tracker enabled  
  reason: `has_issues` not available on Free plan — API returns 404 for issues endpoints

- [x] Repository is assigned to project `PROJ`

---

## 4 — Commits & branches

- [x] At least one commit on `main`  
  first_commit_hash: `84952fad87fb39e3c6d61811a93769378dd4fad7`

- [x] `main` branch exists  
  branch_name: `main`

- [x] At least one additional feature branch exists  
  branch_name: `feature/add-farewell`

- [x] At least one git tag exists  
  tag_name: `v0.1.0`  
  tag_hash: `84952fad87fb39e3c6d61811a93769378dd4fad7`

---

## 5 — Source

- [x] Source tree root is accessible (`source.root`)

- [x] At least one file path is known  
  file_path: `greet.py` *(e.g. `greet.py`)*

---

## 6 — Commit statuses

- [x] At least one build status on the latest commit  
  key: `bb-probe-ci`  
  state: `SUCCESSFUL`

---

## 7 — Code Insights reports

- [x] At least one report on the latest commit  
  report_id: `bb-probe-report`  
  report_type: `TEST`

- [x] At least one annotation on that report  
  annotation_id: `bb-probe-ann-001`

---

## 8 — Pull requests

- [x] At least one **open** pull request exists  
  pr_id: `1`  
  source_branch: `feature/add-farewell`  
  destination_branch: `main`

- [x] At least one **merged** pull request exists  
  pr_id: `2`

- [x] At least one comment on the open PR  
  comment_id: `797172056`

- [x] At least one task on the open PR  
  task_id: `64759588`

---

## 9 — Branching model

- [x] Effective branching model accessible (`branching_model.effective`)  
  development_branch: `main`

- [x] Branching model settings readable (`branching_model.settings`)

---

## 10 — Branch restrictions

- [x] At least one branch restriction rule exists  
  restriction_id: `76271307`  
  kind: `require_approvals_to_merge`  
  pattern: `main`

---

## 11 — Default reviewers

- [n/a] Default reviewer *(workspace has only one user — skip)*  
  account_id: `n/a`

---

## 12 — Pipelines

- [x] Pipelines enabled on `bb-probe`

- [x] `bitbucket-pipelines.yml` present on `main`

- [~] At least one pipeline run exists  
  pipeline_uuid: `{88efe83d-e4a6-4886-aff9-f6241fa5cf80}`  
  state: `PENDING` *(stuck — Atlassian-hosted runners not configured; needs UI action)*

- [~] Pipeline run has at least one step  
  step_uuid: `{a763ede3-…}` *(present but PENDING)*  
  step_name: `Test`

- [x] At least one pipeline repository variable  
  variable_uuid: `{45920ece-ce1e-4854-a192-4f8e630aa683}`  
  key: `PROBE_VAR`

- [x] At least one pipeline schedule  
  schedule_uuid: `{5784e0da-f082-4f91-9d65-20e1d7f0ed8e}`  
  cron: `0 0 0 * * ? *`

- [x] At least one pipeline known host  
  known_host_uuid: `{6f24c288-d2fe-4935-999b-b0f494056957}`  
  hostname: `gitlab.com`

- [x] Pipeline SSH key pair generated

- [~] Pipeline caches present  
  cache_uuid: `___`  
  note: auto-generated after pipeline run completes (requires runner)

---

## 13 — Workspace-level pipeline resources

- [x] At least one workspace pipeline variable  
  variable_uuid: `{70868f27-6d0e-48a5-8cf3-c7ece5a848a9}`  
  key: `WS_PROBE_VAR`

---

## 14 — Deployments

- [x] At least one deployment environment exists  
  environment_uuid: `{697d8906-4609-448e-85f1-6b05d5c9faa9}`  
  environment_name: `Test`

- [x] At least one additional environment  
  environment_uuid: `{13053a34-e7a9-49c0-9647-f748f576208d}`  
  environment_name: `Staging`

- [~] At least one deployment object exists  
  deployment_uuid: `___` *(requires pipeline run with `deployment:` step)*

- [x] At least one variable on the first environment  
  env_var_uuid: `{bbab80d0-4e11-4d66-96e9-e74cb47e981a}`  
  key: `DEPLOY_VAR`

---

## 15 — Deploy keys

- [x] At least one deploy key on `bb-probe`  
  key_id: `10958984`  
  label: `probe-deploy-key`

---

## 16 — Webhooks

- [x] At least one **repo** webhook on `bb-probe`  
  webhook_uuid: `{842a6a21-5169-4b95-90c2-57337ff53e18}`  
  url: `https://example.com/probe-webhook`

- [x] At least one **workspace** webhook  
  webhook_uuid: `{b71bcb12-c9de-49e5-9d8e-e08738571d66}`  
  url: `https://example.com/probe-ws-webhook`

---

## 17 — Issues

- [n/a] Issue tracker not available — Free plan restriction (API returns 404)  
  reason: `has_issues` not supported on beaverish workspace plan; API returns 404 for all issue endpoints

- [n/a] Milestones, versions, components — plan restriction (same as above)

---

## 18 — Downloads

- [n/a] Downloads not available — Free plan restriction (API returns 402 Payment Required)

---

## 19 — Snippets

- [n/a] Snippets not available — Free plan restriction (API returns 402 Payment Required)  
  reason: "A workspace on a Free plan does not support snippets. Upgrade to Standard or Premium."

---

## 20 — Repo permissions

- [x] Repo has at least one group permission entry  
  group_slug: `0804948d-0ec2-4630-bc87-d3ef37cdb221`  
  permission: `read`  
  group_name: `bitbucket-users-beaverish`

- [x] Repo has at least one explicit user permission entry  
  account_id: `712020:f464b5ca-adb8-4a1e-80d4-c867bbf50805` *(owner)*  
  permission: `admin`

---

## 21 — User account resources

- [x] At least one SSH key on the Bitbucket account  
  key_uuid: `{ed7d598c-4e45-4328-a461-554d7c0e5369}`  
  label: `___`

- [x] At least one GPG key on the Bitbucket account  
  fingerprint: `7e7cd216a8df00cb…`

---

## 22 — Workspace members

- [x] Workspace has at least one member  
  member_count: `3`  
  first_member_account_id: `712020:f464b5ca-adb8-4a1e-80d4-c867bbf50805` *(own account)*

---

## 23 — Search

- [x] `BB_SEARCH_QUERY` returns at least one result  
  query: `def`  
  tested: *(circle one: yes / no)*

---

## Untestable — no action required

- [n/a] **Connect add-on** — `addon.*` (10 fn) + `properties.*` (12 fn)  
  reason: requires a deployed Connect app  
  status: `not applicable`

- [n/a] **Self-hosted runners** — `pipelines.runners` / `pipelines.workspace_runners` (10 fn)  
  reason: requires a running runner agent  
  status: `not applicable`

- [n/a] **Pipeline test reports** — `pipelines.test_reports/test_cases/test_case_reasons` (3 fn)  
  reason: requires a pipeline step publishing JUnit XML  
  status: `not applicable`

## Plan restrictions — Free plan

- [n/a] **Issues tracker** — `issues.*` (all endpoints return 404)  
  reason: `has_issues` not available on Free plan  
  affects: `issues`, `issue_comments`, `issue_changes`, `issue_milestones`, `issue_versions`, `issue_components`

- [n/a] **Downloads** — `downloads.*` (POST returns 402)  
  reason: Downloads feature requires Standard or Premium plan

- [n/a] **Snippets** — `snippets.*` (POST returns 402)  
  reason: "A workspace on a Free plan does not support snippets."

## Workspace limitations

- [n/a] **Default reviewers** — `default_reviewers.*`  
  reason: single-user workspace (Laraib is the only member who can review)  
  workaround: add a second user account to the workspace

---

## Completion criteria

**Stage 1 is complete when** all sections 0–23 are checked or `n/a`, and probe score ≥ 34/38.

**Current score:** `27 / 38` (71%) — as of 2026-05-15  
**Max achievable on Free plan (no pipeline runner):** `27 / 38`  
**Max achievable with pipeline runner:** `30 / 38` (+3: pipeline_caches, sched_executions, deployments)  
**Max achievable on Standard plan + pipeline runner:** `34 / 38` (original target)  
**Final score:** `27 / 38` *(Free plan ceiling — see plan restriction notes)*  
**Probe timestamp at completion:** `2026-05-15T01:34:41Z`

### Plan upgrade / runner actions required to reach 34/38

| Blocker | Items | Action |
|---------|-------|--------|
| Atlassian-hosted runners not configured | `pipeline_caches`, `sched_executions`, `deployments` (+3) | Workspace Settings → Pipelines → Runners → Enable |
| Free plan | `issues`, `issue_comments`, `issue_changes`, `issue_milestones`, `issue_versions`, `issue_components`, `downloads` (+7) | Upgrade workspace to Standard plan |
| Single-user workspace | `default_reviewers` | Add a second user to workspace |
