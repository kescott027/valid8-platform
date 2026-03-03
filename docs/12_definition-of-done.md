# Definition of Done

A story is “Done” only if:
- Acceptance criteria met
- Tests added/updated and passing in CI
- Lint/format/type checks pass
- Security checks pass or have approved exceptions
- Observability requirements satisfied (logs/metrics where needed)
- Documentation updated (if behavior changes)
- Rollback plan documented when the story affects deploy/runtime

A phase is “Done” only if its phase gate checklist is satisfied (see hyperdev planning rules).
