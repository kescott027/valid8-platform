# Project Management Rules

## Scope

These rules govern all planning, sprint execution, and backlog changes under `project_management/`.

## Source-of-Truth Rules

- `project_management/Backlog.md` is authoritative for planned work.
- `project_management/Current_Sprint.md` is authoritative for active sprint scope.
- Completed sprint files are authoritative for completed work evidence.
- `project_management/Decision_Matrix.md` is authoritative for architectural/security/storage decisions.

## Non-Negotiable Quality Rules

- No story may enter sprint without acceptance criteria and dependencies.
- No story may be marked done without evidence (tests, docs, code refs).
- Security-impacting changes require explicit threat/risk note in sprint file.
- Architecture-impacting changes require a `Decision_Matrix.md` entry before implementation.
- Production/pre-prod readiness claims must include benchmark or test evidence.

## Sprint Lifecycle Rules

1. Plan sprint from highest priority stories only.
2. Freeze sprint scope after kickoff unless formally changed and logged.
3. Record daily progress and blockers in sprint notes.
4. Close sprint only when close checklist is complete.
5. Move closed sprint file to `project_management/completed_sprints/`.

## Definition of Done (DoD)

A story is done only if all are true:

- Acceptance criteria are met.
- Tests are added/updated and passing.
- Documentation is updated where behavior/ops changed.
- Evidence is recorded in sprint file.
- Backlog state is updated.
- Audit log entry is appended the same day.

## Required Quality Checks per Sprint

- Unit/integration/regression test pass summary.
- Security checks (auth, secrets, dependency risk, endpoint protection).
- Performance checks for touched critical paths.
- Operational checks (health, logging, rollback, observability impact).

## Sprint Close Checklist

- [ ] Included stories marked Done/Not Done with rationale.
- [ ] Evidence links captured (commit hashes, PRs, reports, docs).
- [ ] Risks/debt updated.
- [ ] `Project_Sprint_Log.md` appended.
- [ ] `Current_Sprint.md` reset for next sprint.
- [ ] Sprint file moved to `completed_sprints/`.
- [ ] Audit log entry appended.

## Every 3 Sprints: Architecture Integrity Review

Every third sprint must include:

- Dependency and interface contract review.
- Data model and storage consistency review.
- AuthN/AuthZ boundary review.
- Performance trend review against agreed SLOs.
- Technical debt reprioritization with explicit owners.

## Feature Flag Expectations (if applicable)

- New risky behavior should be feature-flagged when practical.
- Flags must have owner, default state, rollback behavior, and removal date.
- Pre-prod and production flag states must be explicitly documented.

## No Log Entry, No Change

Any change to the following requires same-day audit log entry in `project_management/log/story_management_YYYY-MM-DD.log`:

- `Backlog.md`
- `Current_Sprint.md`
- `Decision_Matrix.md`
- `Project_Sprint_Log.md`
- Sprint files
- `Rules.md`

If a change is unlogged, it is considered invalid and must be corrected with an appended `change_type="correct"` entry.

## Manual Enforcement Until CI (if unavailable)

If CI checks are unavailable, reviewers must verify that any PR modifying `project_management/*.md` also modifies a matching `story_management_*.log` file before merge.
