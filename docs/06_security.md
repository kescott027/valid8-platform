# Security Baseline

Non-negotiables:
- No secrets committed to Git (enforce secrets scanning)
- Dependency scanning and patch policy (SLA by severity)
- Least privilege for GitHub tokens and cloud roles
- Auth required for any non-public operation
- Audit logs for repo writes, deployments, and admin actions

Required controls (Phase 0+):
- SAST (static analysis)
- Dependency vulnerability scanning
- Secrets scanning
- License scanning (if applicable)
- Security review cadence (see hyperdev rules)

Implemented guardrails in this repo:
- CI security job (`.github/workflows/security.yml`) runs dependency and static checks.
- Dependency review job (`.github/workflows/dependency-review.yml`) gates high-risk dependency additions.
- `make security` runs:
  - `npm audit --omit=dev --audit-level=high` for Node
  - `pip-audit` on exported Python requirements
  - `bandit` with medium+ severity and medium+ confidence threshold
- Local pre-commit/pre-push chains (`.pre-commit-config.yaml`) enforce lint, test, and security checks before push.
- Weekly Dependabot updates (`.github/dependabot.yml`) for npm, pip, and GitHub Actions.

Required controls (Phase 2):
- Threat model for core flows
- DAST or dynamic security checks (where feasible)
- Rate limiting and abuse protection
- Secure headers + CSP (web)

Open blockers to track:
- Container image vulnerability scanning in CI (Trivy/Grype) for built images.
- Signed releases and provenance attestations.
- SBOM generation and publication for every release artifact.
- Runtime policy enforcement for shell-step command allowlists.
