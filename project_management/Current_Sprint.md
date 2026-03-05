# Current Sprint

## Sprint Number
Sprint-002

## Sprint Goal
Establish sprint-start debt governance, complete architecture-driven reprioritization controls, and advance the next highest-value platform stories with clean PR hygiene.

## Selected Stories
- ST-0001 Reproducible Bootstrap Across Runtimes (Prerequisite carry-forward)
- ST-0002 Stable CI Pipeline for Lint, Tests, and Build (Prerequisite carry-forward)
- ST-0003 Control Plane Build/Test Separation (Prerequisite carry-forward)
- ST-0004 Worker Test Runtime Reliability (Prerequisite carry-forward)
- ST-0005 Contract Validation Tests for API and Queue Payloads (Prerequisite carry-forward)
- ST-0006 Run Status Synchronization Between Worker and API (Prerequisite carry-forward)
- ST-0007 End-to-End Happy Path Integration Test (Prerequisite carry-forward)
- ST-0010 Backlog/Rules Path Consistency Cleanup
- ST-0035 Pre-Sprint Technical Debt Check Gate
- ST-0036 PR Hygiene and Superseded Branch Cleanup Automation
- ST-0038 Architecture Reassessment and Gap-Driven Backlog Refresh
- ST-0037 Controlled Major Dependency Upgrade Workflow (Zod v4 Pilot)
- ST-0009 Observability Baseline for Core Flows
- ST-0011 Conversation Session Service
- ST-0015 Repo Service for Branch/Commit/PR Operations

## Rationale for Selection
These stories apply governance hardening discovered during Sprint-001, resolve active dependency-upgrade failure patterns, and preserve dependency-safe progress into core functionality. Prerequisite carry-forward stories are included to satisfy strict dependency closure rules in sprint validation.

## Risks
- Major dependency migration may surface hidden contract/API assumptions.
- Debt and hygiene automation can over-close PRs if guardrails are weak.
- Session + repo service stories still require careful contract boundaries and auth handling.

## Acceptance Summary
- Debt gate is required and evidenced before sprint transitions.
- PR hygiene is automated/repeatable and stale PR noise is reduced.
- Sprint work is batched into a single implementation PR for Sprint-002.
- Observability/path/session/repo stories progress with updated architecture-backed priorities.

## Definition of Done Checklist
- [ ] Acceptance criteria met for all selected stories.
- [ ] Tests added/updated and passing in CI.
- [ ] Docs and contracts updated.
- [ ] Evidence captured in sprint notes.
- [ ] Backlog updated to reflect completion state.
