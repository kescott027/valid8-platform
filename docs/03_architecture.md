# Architecture (initial)

## High-level components
1) Chat UI (web) — user conversation surface
2) Orchestrator — routes messages, chooses agent workflows, manages approvals
3) Artifact Service — produces and updates seed docs + backlog artifacts
4) Repo Service — creates repos, commits changes, opens PRs, enforces branch protections
5) Code Engine — executes stories as PRs with tests and evidence
6) Policy Engine — validates all outputs against rules (security, backlog format, quality gates)
7) Observability — logs/metrics/traces + audit log
8) Data Store — conversation state, tasks, approvals, audit events

## Critical architectural decisions (to be finalized Phase 0)
- Monolith vs modular services
- Authn/authz strategy
- Tenant/workspace model
- Eventing (queue) for long-running tasks
- Provider abstraction for LLMs

## Trust boundaries
- User input is untrusted
- AI output is untrusted until validated
- Repo changes must be policy-checked + CI-checked before merge
- Secrets must never enter Git

## Operational model
- All changes to customer repos happen via PRs with required checks
- Human approval gates at defined phase transitions and sensitive actions
- Automated rollback plan for deploy and repo changes
