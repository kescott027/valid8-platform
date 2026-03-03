# Backlog (Authoritative)

This file is the authoritative backlog for all planned work. Stories are listed in strict priority order.

## Backlog Index

- Last updated: 2026-03-03
- Total story count: 34
- Highest story ID present: ST-0034

## Story Template (Must Be Used)

- **ID:**
- **Title:**
- **Description:**
- **Context:**
- **User Value:**
- **Non-functional Requirements:**
- **Implementation Notes:**
- **Test Plan:**
- **Observability:**
- **Rollback Plan:**
- **Acceptance Criteria:**
- **Dependencies:**
- **Risk:** Low / Medium / High
- **Architectural Impact:** None / Low / Medium / High
- **Notes/Evidence:**

## P0 — Foundation and Green Baseline

### Story 1
- **ID:** ST-0001
- **Title:** Reproducible Bootstrap Across Runtimes
- **Description:** Ensure a clean checkout can install all Node and Python dependencies without manual fixes.
- **Context:** Ensure a clean checkout can install all Node and Python dependencies without manual fixes.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - `make bootstrap` succeeds from a clean clone.
  - Node uses a committed lock file and Python uses a committed `uv.lock`.
  - README install instructions match the actual commands.
- **Dependencies:** None
- **Risk:** Low
- **Architectural Impact:** Low
- **Notes/Evidence:** Pending

### Story 2
- **ID:** ST-0002
- **Title:** Stable CI Pipeline for Lint, Tests, and Build
- **Description:** Add CI automation that enforces repository quality gates on every PR.
- **Context:** Add CI automation that enforces repository quality gates on every PR.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - CI runs `make bootstrap` and `make ci` on pull requests.
  - Failing lint/tests/build blocks merge.
  - CI status is visible in PR checks.
- **Dependencies:** ST-0001
- **Risk:** Low
- **Architectural Impact:** Low
- **Notes/Evidence:** Pending

### Story 3
- **ID:** ST-0003
- **Title:** Control Plane Build/Test Separation
- **Description:** Ensure TypeScript build outputs production artifacts without test-file path conflicts.
- **Context:** Ensure TypeScript build outputs production artifacts without test-file path conflicts.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - `npm run build` in `apps/control-plane` succeeds.
  - Tests still run with `npm test`.
  - Docker image build works using production artifacts.
- **Dependencies:** ST-0001
- **Risk:** Low
- **Architectural Impact:** Low
- **Notes/Evidence:** Pending

### Story 4
- **ID:** ST-0004
- **Title:** Worker Test Runtime Reliability
- **Description:** Fix worker test execution so imports and test discovery are stable in local and CI runs.
- **Context:** Fix worker test execution so imports and test discovery are stable in local and CI runs.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - `uv run python -m pytest -q` succeeds in `apps/worker`.
  - No environment-specific import hacks are required by developers.
  - Test command in `Makefile` passes in CI.
- **Dependencies:** ST-0001
- **Risk:** Low
- **Architectural Impact:** Low
- **Notes/Evidence:** Pending

### Story 5
- **ID:** ST-0005
- **Title:** Contract Validation Tests for API and Queue Payloads
- **Description:** Add tests that validate control-plane and worker payloads against OpenAPI and JSON Schema contracts.
- **Context:** Add tests that validate control-plane and worker payloads against OpenAPI and JSON Schema contracts.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - Request/response fixtures are validated against `packages/contracts/openapi.yaml`.
  - Queue request/result JSONL examples validate against schema files.
  - Contract test failures fail CI.
- **Dependencies:** ST-0002, ST-0003, ST-0004
- **Risk:** Medium
- **Architectural Impact:** Medium
- **Notes/Evidence:** Implemented baseline contract tests in `apps/control-plane/test/contracts.test.ts` and `apps/worker/tests/test_contracts.py`; schema updated in `packages/contracts/schemas/run_result.schema.json`; verified with `make ci` on 2026-03-03.

### Story 6
- **ID:** ST-0006
- **Title:** Run Status Synchronization Between Worker and API
- **Description:** Implement the state handoff so worker result lines update run status and logs in control-plane read models.
- **Context:** Implement the state handoff so worker result lines update run status and logs in control-plane read models.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - A queued run transitions to `running` then `succeeded`/`failed`.
  - `GET /runs/:runId` returns worker logs after completion.
  - Unknown or malformed result lines are handled without crashing services.
- **Dependencies:** ST-0005
- **Risk:** Medium
- **Architectural Impact:** High
- **Notes/Evidence:** Implemented result ingestion and run state sync in `apps/control-plane/src/results/fileResults.ts` and `apps/control-plane/src/app.ts`; worker emits running/final events with timestamps in `apps/worker/worker/runner.py`; verified with `apps/control-plane/test/runs-sync.test.ts` and `make ci` on 2026-03-03.

### Story 7
- **ID:** ST-0007
- **Title:** End-to-End Happy Path Integration Test
- **Description:** Add integration coverage that executes pipeline creation, job submission, worker processing, and run retrieval.
- **Context:** Add integration coverage that executes pipeline creation, job submission, worker processing, and run retrieval.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - A single test validates the full loop from API input to completed run output.
  - Test runs in CI and is deterministic.
  - Test artifacts include example queue and result payloads.
- **Dependencies:** ST-0006
- **Risk:** Medium
- **Architectural Impact:** Medium
- **Notes/Evidence:** Happy-path flow is covered through queue emission + run terminal state assertions in `apps/control-plane/test/runs-sync.test.ts`; contract flow validated in `apps/control-plane/test/contracts.test.ts`; verified with `make ci` on 2026-03-03.

### Story 8
- **ID:** ST-0008
- **Title:** Failure Mode Coverage for Runner and Plugins
- **Description:** Add integration tests for invalid command payloads, non-zero process exits, and unknown step types.
- **Context:** Add integration tests for invalid command payloads, non-zero process exits, and unknown step types.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - Failed shell step produces failed run status and logs.
  - Unknown step type is surfaced as explicit failure reason.
  - Regression suite includes both success and failure cases.
- **Dependencies:** ST-0006, ST-0007
- **Risk:** Medium
- **Architectural Impact:** Medium
- **Notes/Evidence:** Failure behavior is covered in `apps/control-plane/test/runs-sync.test.ts` (malformed and failed result events) and `apps/worker/tests/test_runner.py` (unknown step -> failed); verified with `make ci` on 2026-03-03.

### Story 9
- **ID:** ST-0009
- **Title:** Observability Baseline for Core Flows
- **Description:** Add structured logs, run correlation IDs, and key counters for queue depth and run outcomes.
- **Context:** Add structured logs, run correlation IDs, and key counters for queue depth and run outcomes.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - API and worker emit structured logs with `runId` correlation.
  - Metrics for queued/running/succeeded/failed runs are emitted.
  - Runbook documents where to inspect logs and metrics locally.
- **Dependencies:** ST-0006
- **Risk:** Medium
- **Architectural Impact:** Medium
- **Notes/Evidence:** Pending

### Story 10
- **ID:** ST-0010
- **Title:** Backlog/Rules Path Consistency Cleanup
- **Description:** Standardize all docs and rules to use `project_management/` paths and remove conflicting references.
- **Context:** Standardize all docs and rules to use `project_management/` paths and remove conflicting references.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - No docs reference deprecated `/backlog/` paths.
  - Decision log and backlog rules reference real repository locations.
  - Doc lint/check task verifies path consistency.
- **Dependencies:** ST-0002
- **Risk:** Low
- **Architectural Impact:** None
- **Notes/Evidence:** Pending

## P1 — Golem-Maker Functional Core

### Story 11
- **ID:** ST-0011
- **Title:** Conversation Session Service
- **Description:** Implement service APIs to create, read, and append conversation state for product-definition sessions.
- **Context:** Implement service APIs to create, read, and append conversation state for product-definition sessions.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - Session CRUD endpoints exist with persistence.
  - Messages are ordered, timestamped, and linked to actor metadata.
  - Session tests include concurrency and pagination cases.
- **Dependencies:** ST-0007
- **Risk:** Medium
- **Architectural Impact:** High
- **Notes/Evidence:** Pending

### Story 12
- **ID:** ST-0012
- **Title:** Deterministic Artifact Generator for Seed Docs
- **Description:** Build artifact generation for context, vision, PRD, architecture, and roadmap with deterministic rendering.
- **Context:** Build artifact generation for context, vision, PRD, architecture, and roadmap with deterministic rendering.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - Given identical inputs, generated docs are byte-stable.
  - Generated docs map directly to template files in `docs/`.
  - Golden tests cover formatting and section completeness.
- **Dependencies:** ST-0011
- **Risk:** Medium
- **Architectural Impact:** High
- **Notes/Evidence:** Pending

### Story 13
- **ID:** ST-0013
- **Title:** Backlog Generation Engine
- **Description:** Generate prioritized epics and stories from PRD/architecture artifacts using strict backlog rules.
- **Context:** Generate prioritized epics and stories from PRD/architecture artifacts using strict backlog rules.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - Output includes ordered epics and story list with dependencies.
  - Story entries follow required schema and sizing constraints.
  - Rule validation rejects malformed outputs with clear errors.
- **Dependencies:** ST-0012
- **Risk:** High
- **Architectural Impact:** High
- **Notes/Evidence:** Pending

### Story 14
- **ID:** ST-0014
- **Title:** Story Quality Linter and Auto-Fix Suggestions
- **Description:** Add a linter that checks acceptance criteria quality, missing NFRs, and dependency graph issues.
- **Context:** Add a linter that checks acceptance criteria quality, missing NFRs, and dependency graph issues.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - Linter reports missing required sections and invalid dependencies.
  - Auto-fix mode proposes deterministic edits without destructive rewrites.
  - CI fails on high-severity lint findings.
- **Dependencies:** ST-0013
- **Risk:** Medium
- **Architectural Impact:** Medium
- **Notes/Evidence:** Pending

### Story 15
- **ID:** ST-0015
- **Title:** Repo Service for Branch/Commit/PR Operations
- **Description:** Implement provider abstraction and initial GitHub adapter for branch creation, commits, and pull requests.
- **Context:** Implement provider abstraction and initial GitHub adapter for branch creation, commits, and pull requests.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - Repo service can create feature branches and open PRs.
  - Commit metadata includes story ID and evidence links.
  - Integration tests mock provider APIs and validate failure behavior.
- **Dependencies:** ST-0011
- **Risk:** High
- **Architectural Impact:** High
- **Notes/Evidence:** Pending

### Story 16
- **ID:** ST-0016
- **Title:** Policy Engine Baseline
- **Description:** Validate AI outputs and code changes against security, quality, and process rules before execution.
- **Context:** Validate AI outputs and code changes against security, quality, and process rules before execution.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - Policy checks exist for secrets, forbidden files, and missing tests.
  - Violations are surfaced with actionable remediation text.
  - Policy gate is mandatory before PR creation.
- **Dependencies:** ST-0014, ST-0015
- **Risk:** High
- **Architectural Impact:** High
- **Notes/Evidence:** Pending

### Story 17
- **ID:** ST-0017
- **Title:** Story Execution Orchestrator
- **Description:** Execute one story at a time through plan, code, test, evidence, and PR phases.
- **Context:** Execute one story at a time through plan, code, test, evidence, and PR phases.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - Orchestrator tracks state transitions for each phase.
  - Failed phases can be retried safely without duplicate side effects.
  - Execution summary includes changed files and test outcomes.
- **Dependencies:** ST-0015, ST-0016
- **Risk:** High
- **Architectural Impact:** High
- **Notes/Evidence:** Pending

### Story 18
- **ID:** ST-0018
- **Title:** Human Approval Workflow
- **Description:** Add approval gates for high-risk actions (security posture changes, external integrations, deploy).
- **Context:** Add approval gates for high-risk actions (security posture changes, external integrations, deploy).
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - Approvals can be requested, granted, and denied with rationale.
  - Blocked actions remain paused until explicit approval.
  - Audit records include approver identity and timestamp.
- **Dependencies:** ST-0017
- **Risk:** Medium
- **Architectural Impact:** Medium
- **Notes/Evidence:** Pending

### Story 19
- **ID:** ST-0019
- **Title:** Blocker Detection and Utility Suggestions
- **Description:** Detect recurring blockers during execution and suggest reusable utilities or scope changes.
- **Context:** Detect recurring blockers during execution and suggest reusable utilities or scope changes.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - Blockers are classified by type (dependency, test, contract, environment).
  - System suggests utility actions tied to blocker type.
  - Suggestions are logged and linked to story context.
- **Dependencies:** ST-0017
- **Risk:** Medium
- **Architectural Impact:** Medium
- **Notes/Evidence:** Pending

### Story 20
- **ID:** ST-0020
- **Title:** Full Audit Trail for Agent Actions
- **Description:** Record who/what/when/why for artifact changes, code changes, approvals, and policy decisions.
- **Context:** Record who/what/when/why for artifact changes, code changes, approvals, and policy decisions.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - Every orchestrator phase emits auditable events.
  - Audit entries are queryable by story/session/user.
  - Tamper-evidence approach is documented and tested.
- **Dependencies:** ST-0018
- **Risk:** Medium
- **Architectural Impact:** High
- **Notes/Evidence:** Pending

## P2 — Production Readiness and Hardening

### Story 21
- **ID:** ST-0021
- **Title:** Workspace and RBAC Model
- **Description:** Add user/workspace boundaries with role-based permissions across core APIs.
- **Context:** Add user/workspace boundaries with role-based permissions across core APIs.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - Workspace scoping prevents cross-tenant reads/writes.
  - Roles cover viewer, editor, approver, admin permissions.
  - Authorization tests cover allow/deny matrix.
- **Dependencies:** ST-0011, ST-0020
- **Risk:** High
- **Architectural Impact:** High
- **Notes/Evidence:** Pending

### Story 22
- **ID:** ST-0022
- **Title:** Secret Handling and Redaction Pipeline
- **Description:** Prevent secrets from entering prompts, logs, generated files, and commits.
- **Context:** Prevent secrets from entering prompts, logs, generated files, and commits.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - Secret scanning runs pre-commit and in CI.
  - Redaction middleware masks sensitive tokens in logs.
  - Test fixtures prove known secret patterns are blocked.
- **Dependencies:** ST-0016, ST-0020
- **Risk:** High
- **Architectural Impact:** Medium
- **Notes/Evidence:** Pending

### Story 23
- **ID:** ST-0023
- **Title:** Tracing and Metrics Export
- **Description:** Instrument key workflows with OpenTelemetry-compatible traces and operational metrics.
- **Context:** Instrument key workflows with OpenTelemetry-compatible traces and operational metrics.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - Trace spans cover session, generation, validation, and execution phases.
  - Metrics expose throughput, error rate, and latency by phase.
  - Local and CI smoke tests validate telemetry output paths.
- **Dependencies:** ST-0009, ST-0017
- **Risk:** Medium
- **Architectural Impact:** Medium
- **Notes/Evidence:** Pending

### Story 24
- **ID:** ST-0024
- **Title:** Idempotency, Retry, and Circuit-Breaker Controls
- **Description:** Harden long-running operations and provider calls against transient failures and duplicate execution.
- **Context:** Harden long-running operations and provider calls against transient failures and duplicate execution.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - Idempotency keys prevent duplicate PR/story execution.
  - Retries use bounded exponential backoff with jitter.
  - Circuit breaker opens on repeated provider failures and recovers safely.
- **Dependencies:** ST-0017, ST-0019
- **Risk:** High
- **Architectural Impact:** High
- **Notes/Evidence:** Pending

### Story 25
- **ID:** ST-0025
- **Title:** Environment Promotion Pipeline
- **Description:** Define dev/stage/prod pipeline with gated promotion, immutable artifacts, and rollback metadata.
- **Context:** Define dev/stage/prod pipeline with gated promotion, immutable artifacts, and rollback metadata.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - Pipeline produces reproducible artifacts per commit SHA.
  - Promotion requires passing tests and policy checks.
  - Rollback command and evidence are documented.
- **Dependencies:** ST-0002, ST-0024
- **Risk:** High
- **Architectural Impact:** High
- **Notes/Evidence:** Pending

### Story 26
- **ID:** ST-0026
- **Title:** Operational Runbook Completion
- **Description:** Complete deployment, rollback, incident response, and on-call procedures with scenario drills.
- **Context:** Complete deployment, rollback, incident response, and on-call procedures with scenario drills.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - Runbook includes deploy, rollback, secret rotation, and incident severity matrix.
  - At least one tabletop drill is documented.
  - RTO/RPO objectives are published and testable.
- **Dependencies:** ST-0025
- **Risk:** Medium
- **Architectural Impact:** Low
- **Notes/Evidence:** Pending

### Story 27
- **ID:** ST-0027
- **Title:** Security Gates in CI/CD
- **Description:** Add dependency scanning, SAST, and secret scanning gates in CI with triage policy.
- **Context:** Add dependency scanning, SAST, and secret scanning gates in CI with triage policy.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - Security scans run on PR and main branch.
  - Critical findings fail the pipeline by default.
  - Triage workflow supports temporary exceptions with expiry.
- **Dependencies:** ST-0022, ST-0025
- **Risk:** High
- **Architectural Impact:** Medium
- **Notes/Evidence:** Pending

### Story 28
- **ID:** ST-0028
- **Title:** Performance and Load Test Suite
- **Description:** Create load tests for session creation, artifact generation, story execution, and run retrieval.
- **Context:** Create load tests for session creation, artifact generation, story execution, and run retrieval.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - Baseline throughput and latency targets are defined.
  - Tests run in scheduled CI and produce trend reports.
  - Performance regressions create actionable alerts.
- **Dependencies:** ST-0023, ST-0024
- **Risk:** Medium
- **Architectural Impact:** Medium
- **Notes/Evidence:** Pending

## P3 — Scale and Enterprise Completeness

### Story 29
- **ID:** ST-0029
- **Title:** Multi-Provider LLM Routing and Fallback
- **Description:** Introduce provider abstraction with policy-driven model routing, fallback, and cost controls.
- **Context:** Introduce provider abstraction with policy-driven model routing, fallback, and cost controls.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - System supports at least two providers behind one interface.
  - Fallback activates on timeout/error with deterministic policy.
  - Cost and token usage are recorded per run.
- **Dependencies:** ST-0012, ST-0024
- **Risk:** High
- **Architectural Impact:** High
- **Notes/Evidence:** Pending

### Story 30
- **ID:** ST-0030
- **Title:** Enterprise Governance and Audit Export
- **Description:** Add exportable audit/reporting capabilities for compliance reviews and enterprise operations.
- **Context:** Add exportable audit/reporting capabilities for compliance reviews and enterprise operations.
- **User Value:** Advances golem-maker reliability and delivery confidence for this phase.
- **Non-functional Requirements:** Security, reliability, and performance baselines apply.
- **Implementation Notes:** Keep implementation contract-first, deterministic, and minimally invasive.
- **Test Plan:** Add or update unit, integration, and contract tests for changed behavior.
- **Observability:** Emit run-correlated logs and metrics for touched paths.
- **Rollback Plan:** Revert via PR rollback and restore previous behavior/contracts if needed.
- **Acceptance Criteria:**
  - Audit exports support CSV/JSON with filters by workspace/date/story.
  - Retention policy and deletion policy are configurable.
  - Governance report includes approvals, policy violations, and remediation status.
- **Dependencies:** ST-0020, ST-0021, ST-0027
- **Risk:** Medium
- **Architectural Impact:** Medium
- **Notes/Evidence:** Pending

### Story 31
- **ID:** ST-0031
- **Title:** Container Image Vulnerability Scanning in CI
- **Description:** Add image-level security scanning for control-plane and worker Docker images.
- **Context:** Current security checks cover source dependencies and static analysis, but not packaged runtime image layers.
- **User Value:** Prevents invalid production assumptions by surfacing vulnerable base image layers before release.
- **Non-functional Requirements:** Security-first gate for high/critical image CVEs.
- **Implementation Notes:** Build both Docker images in CI and scan with Trivy or Grype; fail on high/critical unless explicitly waived.
- **Test Plan:** Add workflow tests and sample vulnerable image checks to validate gate behavior.
- **Observability:** Publish scan summary artifacts per CI run and annotate PRs.
- **Rollback Plan:** Temporarily downgrade image scan gate to warning-only via documented exception process.
- **Acceptance Criteria:**
  - CI builds and scans both service images on PRs and main.
  - High/critical image vulnerabilities fail the check.
  - Exceptions require time-bound waiver documentation.
- **Dependencies:** ST-0002, ST-0027
- **Risk:** High
- **Architectural Impact:** Medium
- **Notes/Evidence:** Added as blocker backlog item on 2026-03-03.

### Story 32
- **ID:** ST-0032
- **Title:** SBOM Generation and Release Provenance
- **Description:** Generate signed SBOMs and provenance attestations for release artifacts.
- **Context:** Dependency scans are present, but release traceability and provenance are not yet enforced.
- **User Value:** Improves supply-chain trust and auditability for enterprise/security review.
- **Non-functional Requirements:** Security and compliance baseline for artifact integrity.
- **Implementation Notes:** Generate SPDX/CycloneDX SBOMs in CI and attach provenance/signature metadata to release outputs.
- **Test Plan:** Validate SBOM completeness and verify attestation checks in CI.
- **Observability:** Persist SBOM and provenance artifacts for every build.
- **Rollback Plan:** Keep provenance in report-only mode until signing infrastructure is stable.
- **Acceptance Criteria:**
  - Every release artifact has an SBOM and attestation.
  - CI verifies signature/provenance before release promotion.
  - Security docs include verification procedure.
- **Dependencies:** ST-0025, ST-0027
- **Risk:** Medium
- **Architectural Impact:** Medium
- **Notes/Evidence:** Added as blocker backlog item on 2026-03-03.

### Story 33
- **ID:** ST-0033
- **Title:** Worker Shell Step Sandboxing and Allowlists
- **Description:** Restrict shell plugin execution with command allowlists, timeouts, and workspace isolation guardrails.
- **Context:** Shell execution is intentionally permissive for bootstrap realism and remains a material runtime risk.
- **User Value:** Reduces false-positive security failures and real exploit risk during automated story execution.
- **Non-functional Requirements:** Strong runtime security boundaries with deterministic failure behavior.
- **Implementation Notes:** Enforce allowed command policy, max execution time, and deny risky command patterns.
- **Test Plan:** Add allowlist/denylist and timeout integration tests.
- **Observability:** Emit blocked-command and timeout security events with run correlation.
- **Rollback Plan:** Keep existing permissive mode behind a controlled feature flag for emergency fallback.
- **Acceptance Criteria:**
  - Disallowed commands fail fast with explicit error codes.
  - Long-running commands are terminated at configured timeout.
  - Policy is versioned and documented.
- **Dependencies:** ST-0016, ST-0022
- **Risk:** High
- **Architectural Impact:** High
- **Notes/Evidence:** Added as blocker backlog item on 2026-03-03.

### Story 34
- **ID:** ST-0034
- **Title:** DAST and Abuse-Protection Validation
- **Description:** Add dynamic security testing and abuse-protection checks for exposed API endpoints.
- **Context:** Static and dependency scans are enabled, but runtime/API abuse checks are not automated.
- **User Value:** Catches invalid assumptions around endpoint hardening before production incidents.
- **Non-functional Requirements:** Security and reliability hardening for runtime behavior.
- **Implementation Notes:** Add DAST scan stage and baseline rate-limit/auth abuse tests in CI against ephemeral env.
- **Test Plan:** Integrate DAST job and endpoint abuse test cases with pass/fail thresholds.
- **Observability:** Publish DAST findings and trend metrics per sprint.
- **Rollback Plan:** Start in non-blocking mode, then enforce gate after baseline cleanup.
- **Acceptance Criteria:**
  - DAST runs automatically on scheduled and pre-release pipelines.
  - Critical findings fail release pipeline.
  - Abuse-protection tests exist for auth and request-throttling boundaries.
- **Dependencies:** ST-0021, ST-0025, ST-0027
- **Risk:** High
- **Architectural Impact:** Medium
- **Notes/Evidence:** Added as blocker backlog item on 2026-03-03.

## Backlog Completion Rule

A story is "Done" ONLY when:

- It appears in a completed `Sprint_N.md` marked Done with closure date.
- Evidence is recorded (commit/PR refs + tests + doc updates).
- It is removed from `Backlog.md` (or moved into an explicit Archive section).

---
