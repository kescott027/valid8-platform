# Backlog Format (Strict)

## Epic format (in /project_management/epics.md)
Each epic MUST include:
- Epic ID: EPIC-### (sequential)
- Phase: 0|1|2|3
- Outcome: measurable statement
- Dependencies: list of epic/story IDs
- Risks: key risks
- Exit criteria: bullet list

## Story file format (in /project_management/stories/STORY-###.md)
Every story MUST include these sections, in order:

1) Title
2) Phase
3) Context
4) User value
5) Acceptance criteria (testable bullets)
6) Non-functional requirements (security/reliability/perf where relevant)
7) Implementation notes (high-level approach, not a code dump)
8) Test plan (what tests, where)
9) Observability (logs/metrics/traces impact)
10) Rollback plan (required if runtime behavior changes)
11) Risks / edge cases
12) Definition of Done checklist (story-specific)

Sizing rule:
- Must be completable in <= 2 days. If not, split.

Uncertainty rule:
- If requirements are unclear, create a SPIKE story with explicit learning goals and a time box.
