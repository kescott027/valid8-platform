# AI Guardrails

AI outputs are not trusted until validated.

Hard rules:
- Never include secrets or instruct users to paste secrets
- Never modify production infrastructure without explicit approval
- All repo changes occur via PRs with CI and policy checks
- Every story execution must link to acceptance criteria and evidence
- When uncertain, create a spike story rather than guessing

Required behaviors:
- Keep artifacts consistent across docs/backlog/ADRs
- Explain changes in PR descriptions
- Prefer minimal, reversible changes
- Detect blockers and propose utilities or scope reductions

Approval gates:
- Repo creation
- Changing security posture
- Introducing new external integrations
- Any deploy to production
