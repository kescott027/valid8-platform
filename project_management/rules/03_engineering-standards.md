# Engineering Standards (Hard)

- CI must run on every PR
- Pre-commit and pre-push hooks must be installed and passing locally
- Lint + format enforced
- Tests required for logic changes
- Security scans required (dependency + SAST + secrets)
- No TODOs without linked backlog item and owner
- Dependencies must be pinned/locked
- Error handling: no silent failures; log with correlation IDs
- API contracts documented and versioned (where applicable)
