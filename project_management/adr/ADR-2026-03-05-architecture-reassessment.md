# ADR-2026-03-05: Architecture Reassessment and Sprint-002 Reprioritization

## Context

After Sprint-001 closure, the repository had:

- completed baseline run-loop hardening stories,
- a large set of stale generated PRs,
- and a failing major dependency upgrade PR (`zod` v4) that exposed contract/runtime drift risk.

## Current-State Assessment

### Control Plane
- API contract tests exist and catch payload regressions.
- Major dependency upgrades can break request handling paths without controlled migration.

### Worker
- Execution and failure-mode tests exist for current runner plugins.
- Cross-service observability and debt reporting workflows are not yet enforced at sprint boundaries.

### Governance/Delivery Process
- Sprint close-out process is now explicit and merge-gated.
- Sprint start gate for technical debt/PR hygiene was previously implicit and is now formalized.

## Gaps Identified

1. No mandatory pre-sprint technical debt gate.
2. No repeatable PR hygiene cleanup process for superseded generated PRs.
3. No controlled workflow for major dependency upgrades with contract-first migration.
4. Architecture reassessment was not codified as a recurring backlog-refresh activity.

## Decision

Reprioritize Sprint-002 to address governance and architecture-debt controls before deeper functional-core expansion.

## Backlog Mapping

- ST-0035: Pre-Sprint Technical Debt Check Gate
- ST-0036: PR Hygiene and Superseded Branch Cleanup Automation
- ST-0037: Controlled Major Dependency Upgrade Workflow (Zod v4 Pilot)
- ST-0038: Architecture Reassessment and Gap-Driven Backlog Refresh

## Consequences

- Sprint starts become more deterministic and auditable.
- PR queue noise is reduced, improving signal for active delivery.
- Major dependency upgrades move from opportunistic to controlled migrations.
- Functional-core stories continue with lower hidden integration risk.
