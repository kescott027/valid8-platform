# AI Workflows (Hard)

Workflow A: Chat → Seed Docs
- Produce/Update docs under /docs and /hyperdev as needed
- Validate doc consistency (vision/PRD/architecture)

Workflow B: Seed Docs → Backlog
- Create epics and stories conforming to strict schema
- Assign phase and dependencies
- Ensure each story has acceptance criteria and test plan

Workflow C: Backlog → Execution
- Implement one story per PR
- Include tests and evidence
- Update docs if behavior changes
- Never bypass policy/CI gates

Workflow D: Review Cycles
- Generate review checklists
- Convert findings to backlog stories
- Prioritize to manage technical debt
