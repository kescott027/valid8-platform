# Quality Baseline

Required (Phase 0):
- Automated tests in CI
- Lint + formatting enforced
- Type checks (if language supports)
- Pre-commit or equivalent checks
- Build reproducibility

Required (Phase 1):
- Contract tests for key flows (chat → docs → repo → PR)
- Golden tests for backlog/story format validation

Required (Phase 2):
- Load/perf testing for critical endpoints
- Chaos/resilience testing where appropriate
