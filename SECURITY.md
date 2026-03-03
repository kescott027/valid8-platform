# Security Policy

## Supported Versions

This repository tracks a single active development line on `main`. Security fixes are applied to `main` and released forward.

## Reporting a Vulnerability

- Do not open public issues for suspected vulnerabilities.
- Report privately to repository maintainers with:
  - affected component and version
  - reproduction steps or proof-of-concept
  - impact and exploitability assumptions

## Response Expectations

- Initial triage target: within 2 business days.
- Severity assignment target: within 5 business days.
- Critical/high remediation target: as soon as practical with tracked blocker stories.

## Security Controls in This Repo

- PR CI: lint, tests, build, dependency and static checks.
- Secret scanning: Gitleaks in CI.
- Dependency review: GitHub dependency review for PRs.
- SAST: CodeQL for Python and JavaScript/TypeScript.
- Local guardrails: pre-commit and pre-push hook chain.
