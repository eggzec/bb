SHELL := /bin/bash

# Load .env into make variables and re-export them as shell env vars for all targets.
# Required for schema-* targets. Silently ignored when .env is absent.
-include .env
export

.PHONY: help generate-cloud generate-dc generate diff-cloud diff-dc diff \
        schema-test-cloud schema-discover-cloud probe-workspace \
        schema-test-dc schema-discover-dc

help:
	@echo "Available targets:"
	@echo "  generate-cloud          Generate Cloud SDK from OpenAPI spec"
	@echo "  generate-dc             Generate DC SDK from OpenAPI spec (includes fixing spec)"
	@echo "  generate                Generate both Cloud and DC SDKs"
	@echo "  diff-cloud              Compare generated Cloud SDK with current version"
	@echo "  diff-dc                 Compare generated DC SDK with current version"
	@echo "  diff                    Compare both generated SDKs with current versions"
	@echo ""
	@echo "  [Cloud API Testing]"
	@echo "  schema-test-cloud       Run schemathesis conformance tests against BB Cloud API (GET-only)"
	@echo "  schema-discover-cloud   Discover workspace probe data and suggest .env additions"
	@echo "  probe-workspace         Deep-probe workspace: all resources, coverage map, seeding actions"
	@echo ""
	@echo "  [Data Center API Testing]"
	@echo "  schema-test-dc          Run schemathesis conformance tests against BB DC instance (GET-only)"
	@echo "  schema-discover-dc      Discover DC workspace and suggest .env additions"
	@echo ""
	@echo "Cloud schema-* targets require BB_EMAIL, BB_TOKEN, BB_WORKSPACE (set in .env)."
	@echo "DC schema-* targets require BB_DC_BASE_URL and BB_DC_ADMIN_PASSWORD (set in .env)."

# Cloud SDK generation
generate-cloud:
	@echo "Generating Cloud SDK..."
	@mkdir -p cmd_outputs
	@GEN_TMP=$$(mktemp -d); \
	TS=$$(date +%Y%m%d_%H%M%S); \
	BB_PROJECT_ROOT=$$(pwd) uvx openapi-python-client generate \
	  --path bb_cloud_fixed.openapi.json \
	  --output-path "$$GEN_TMP" \
	  --config config/generator.yml \
	  --custom-template-path templates/ \
	  --overwrite \
	  > cmd_outputs/$${TS}_generate_stdout.txt \
	  2> cmd_outputs/$${TS}_generate_stderr.txt; \
	echo "Generation log: cmd_outputs/$${TS}_generate_stdout.txt"; \
	echo "Error count: $$(grep -c 'Endpoint will not be generated\|Cannot parse' cmd_outputs/$${TS}_generate_stderr.txt || echo 0)"; \
	rsync -a --delete "$$GEN_TMP/bb/models/" src/bb/cloud/models/; \
	rsync -a --delete "$$GEN_TMP/bb/api/" src/bb/cloud/api/; \
	cp "$$GEN_TMP/bb/client.py" src/bb/cloud/client.py; \
	cp "$$GEN_TMP/bb/types.py" src/bb/cloud/types.py; \
	cp "$$GEN_TMP/bb/errors.py" src/bb/cloud/errors.py; \
	rm -rf "$$GEN_TMP"; \
	echo "Cloud SDK generated successfully"

# DC SDK generation (includes spec fix if script exists)
generate-dc:
	@echo "Generating DC SDK..."
	@mkdir -p cmd_outputs
	@GEN_TMP=$$(mktemp -d); \
	TS=$$(date +%Y%m%d_%H%M%S); \
	BB_PROJECT_ROOT=$$(pwd) uvx openapi-python-client generate \
	  --path bb_datacenter_fixed.openapi.json \
	  --output-path "$$GEN_TMP" \
	  --config config/generator_dc.yml \
	  --overwrite \
	  > cmd_outputs/$${TS}_dc_generate_stdout.txt \
	  2> cmd_outputs/$${TS}_dc_generate_stderr.txt; \
	echo "Generation log: cmd_outputs/$${TS}_dc_generate_stdout.txt"; \
	echo "Error count: $$(grep -c 'Endpoint will not be generated\|Cannot parse' cmd_outputs/$${TS}_dc_generate_stderr.txt || echo 0)"; \
	rsync -a --delete "$$GEN_TMP/bb/models/" src/bb/datacenter/models/; \
	rsync -a --delete "$$GEN_TMP/bb/api/" src/bb/datacenter/api/; \
	cp "$$GEN_TMP/bb/client.py" src/bb/datacenter/client.py; \
	cp "$$GEN_TMP/bb/types.py" src/bb/datacenter/types.py; \
	cp "$$GEN_TMP/bb/errors.py" src/bb/datacenter/errors.py; \
	rm -rf "$$GEN_TMP"; \
	echo "DC SDK generated successfully"

# Generate both
generate: generate-cloud generate-dc
	@echo "Both SDKs generated successfully"

# Compare Cloud SDK (creates temp files for diff)
diff-cloud:
	@echo "Comparing Cloud SDK with generated version..."
	@GEN_TMP=$$(mktemp -d); \
	BB_PROJECT_ROOT=$$(pwd) uvx openapi-python-client generate \
	  --path bb_cloud_fixed.openapi.json \
	  --output-path "$$GEN_TMP" \
	  --config config/generator.yml \
	  --custom-template-path templates/ \
	  --overwrite \
	  > /dev/null 2>&1; \
	diff -r "$$GEN_TMP/bb/models/" src/bb/cloud/models/ || true; \
	diff -r "$$GEN_TMP/bb/api/" src/bb/cloud/api/ || true; \
	diff "$$GEN_TMP/bb/client.py" src/bb/cloud/client.py || true; \
	diff "$$GEN_TMP/bb/types.py" src/bb/cloud/types.py || true; \
	diff "$$GEN_TMP/bb/errors.py" src/bb/cloud/errors.py || true; \
	rm -rf "$$GEN_TMP"

# Compare DC SDK (creates temp files for diff)
diff-dc:
	@echo "Comparing DC SDK with generated version..."
	@if [ -f scripts/fix_dc_spec.py ]; then \
		python3 scripts/fix_dc_spec.py > /dev/null 2>&1; \
	fi
	@GEN_TMP=$$(mktemp -d); \
	BB_PROJECT_ROOT=$$(pwd) uvx openapi-python-client generate \
	  --path bb_datacenter_fixed.openapi.json \
	  --output-path "$$GEN_TMP" \
	  --config config/generator_dc.yml \
	  --overwrite \
	  > /dev/null 2>&1; \
	diff -r "$$GEN_TMP/bb/models/" src/bb/datacenter/models/ || true; \
	diff -r "$$GEN_TMP/bb/api/" src/bb/datacenter/api/ || true; \
	diff "$$GEN_TMP/bb/client.py" src/bb/datacenter/client.py || true; \
	diff "$$GEN_TMP/bb/types.py" src/bb/datacenter/types.py || true; \
	diff "$$GEN_TMP/bb/errors.py" src/bb/datacenter/errors.py || true; \
	rm -rf "$$GEN_TMP"

# Compare both
diff: diff-cloud diff-dc
	@echo "Comparison complete"

# ---------------------------------------------------------------------------
# API conformance testing
# ---------------------------------------------------------------------------
#
# schema-test-cloud runs schemathesis against the real BB Cloud API using your
# spec file.  It only issues GET requests so it is safe to run at any time.
#
# What it catches even without seed data (random path params → 404s):
#   status_code_conformance     — flags any status code the spec doesn't document
#                                 (the primary bug class: missing 403, 400, 429 …)
#   response_schema_conformance — flags response bodies that don't match the schema
#                                 (required fields the API omits, wrong types, etc.)
#   not_a_server_error          — flags 5xx responses
#   content_type_conformance    — flags undocumented Content-Type headers
#
# What requires seed data (BB_REPO_SLUG pointing to a real repo with commits):
#   200-response schema coverage — without seed data most repo-scoped endpoints
#   return 404, so schema issues in success responses are only caught by the
#   live pytest suite (tests/cloud/live/).
#
# Run schema-discover-cloud first to find a suitable BB_REPO_SLUG.

schema-test-cloud:
	@if [ -z "$(BB_EMAIL)" ] || [ -z "$(BB_TOKEN)" ] || [ -z "$(BB_WORKSPACE)" ]; then \
		echo "ERROR: BB_EMAIL, BB_TOKEN, and BB_WORKSPACE must be set."; \
		echo "       Add them to .env (see .env.example) or export them before running make."; \
		exit 1; \
	fi
	@mkdir -p cmd_outputs
	@TS=$$(date +%Y%m%d_%H%M%S); \
	XMLOUT="cmd_outputs/$${TS}_schemathesis_cloud.xml"; \
	JSONOUT="cmd_outputs/$${TS}_schemathesis_cloud.ndjson"; \
	TXTOUT="cmd_outputs/$${TS}_schemathesis_cloud_stdout.txt"; \
	echo "schemathesis conformance run — reports: cmd_outputs/$${TS}_schemathesis_cloud.*"; \
	uvx schemathesis run bb_cloud_fixed.openapi.json \
		--url https://api.bitbucket.org/2.0 \
		--auth "$(BB_EMAIL):$(BB_TOKEN)" \
		--checks status_code_conformance,response_schema_conformance,not_a_server_error,content_type_conformance \
		--include-method GET \
		--mode positive \
		--phases coverage \
		-n 1 \
		--seed 42 \
		--no-color \
		--report junit \
		--report-junit-path "$$XMLOUT" \
		--report ndjson \
		--report-ndjson-path "$$JSONOUT" \
		2>&1 | tee "$$TXTOUT"; \
	EXIT=$${PIPESTATUS[0]}; \
	echo ""; \
	echo "stdout saved : $$TXTOUT"; \
	echo "JUnit report : $$XMLOUT"; \
	echo "NDJSON events: $$JSONOUT"; \
	exit $$EXIT

# Probe the workspace via the BB Cloud API and print suggested .env additions.
# Run this once before schema-test-cloud to populate BB_REPO_SLUG.
schema-discover-cloud:
	@if [ -z "$(BB_EMAIL)" ] || [ -z "$(BB_TOKEN)" ] || [ -z "$(BB_WORKSPACE)" ]; then \
		echo "ERROR: BB_EMAIL, BB_TOKEN, BB_WORKSPACE must be set."; \
		echo "       Add them to .env (see .env.example) or export them before running make."; \
		exit 1; \
	fi
	uv run python3 scripts/discover_cloud_probe.py

# Deep workspace probe: checks all live-test resource categories concurrently,
# writes JSON + Markdown reports to cmd_outputs/, and prints a seeding action plan.
probe-workspace:
	@if [ -z "$(BB_EMAIL)" ] || [ -z "$(BB_TOKEN)" ] || [ -z "$(BB_WORKSPACE)" ]; then \
		echo "ERROR: BB_EMAIL, BB_TOKEN, BB_WORKSPACE must be set."; \
		echo "       Add them to .env (see .env.example) or export them before running make."; \
		exit 1; \
	fi
	uv run python3 scripts/probe_workspace.py

# ---------------------------------------------------------------------------
# Data Center API conformance testing
# ---------------------------------------------------------------------------
#
# schema-test-dc runs schemathesis against a running Bitbucket DC instance.
# It only issues GET requests so it is safe to run at any time.
# The instance must be running and BB_DC_BASE_URL must point to its /rest endpoint.
#
# What it catches even without seed data (random path params → 404s):
#   status_code_conformance     — flags any status code the spec doesn't document
#   response_schema_conformance — flags response bodies that don't match the schema
#   not_a_server_error          — flags 5xx responses
#   content_type_conformance    — flags undocumented Content-Type headers
#
# Uses Basic auth (admin:BB_DC_ADMIN_PASSWORD) to access the instance.
# Run scripts/seed_dc.py first to create seed data for better 200-response coverage.

schema-test-dc:
	@if [ -z "$(BB_DC_BASE_URL)" ] || [ -z "$(BB_DC_ADMIN_PASSWORD)" ]; then \
		echo "ERROR: BB_DC_BASE_URL and BB_DC_ADMIN_PASSWORD must be set."; \
		echo "       Add them to .env (see .env.example) or export them before running make."; \
		exit 1; \
	fi
	@mkdir -p cmd_outputs
	@TS=$$(date +%Y%m%d_%H%M%S); \
	XMLOUT="cmd_outputs/$${TS}_schemathesis_dc.xml"; \
	JSONOUT="cmd_outputs/$${TS}_schemathesis_dc.ndjson"; \
	TXTOUT="cmd_outputs/$${TS}_schemathesis_dc_stdout.txt"; \
	echo "schemathesis conformance run — reports: cmd_outputs/$${TS}_schemathesis_dc.*"; \
	uvx schemathesis run bb_datacenter_fixed.openapi.json \
		--url "$(BB_DC_BASE_URL)" \
		--auth "admin:$(BB_DC_ADMIN_PASSWORD)" \
		--checks status_code_conformance,response_schema_conformance,not_a_server_error,content_type_conformance \
		--include-method GET \
		--mode positive \
		--phases coverage \
		-n 1 \
		--seed 42 \
		--no-color \
		--report junit \
		--report-junit-path "$$XMLOUT" \
		--report ndjson \
		--report-ndjson-path "$$JSONOUT" \
		2>&1 | tee "$$TXTOUT"; \
	EXIT=$${PIPESTATUS[0]}; \
	echo ""; \
	echo "stdout saved : $$TXTOUT"; \
	echo "JUnit report : $$XMLOUT"; \
	echo "NDJSON events: $$JSONOUT"; \
	exit $$EXIT

# Probe the DC instance via the REST API and print suggested .env additions.
# Run this after scripts/seed_dc.py to populate BB_DC_PROJECT_KEY and BB_DC_REPO_SLUG.
schema-discover-dc:
	@if [ -z "$(BB_DC_BASE_URL)" ] || [ -z "$(BB_DC_TOKEN)" ]; then \
		echo "ERROR: BB_DC_BASE_URL and BB_DC_TOKEN must be set."; \
		echo "       Add them to .env (see .env.example) or export them before running make."; \
		exit 1; \
	fi
	uv run python3 scripts/discover_dc_probe.py
