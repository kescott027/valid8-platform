# Operating Principles (Hard)

1) Git is source of truth. No “hidden state” outside repo for requirements, decisions, backlog.
2) All changes happen via PRs. No direct commits to protected branches.
3) Security and quality are default. If something is skipped, it must be explicitly justified and time-boxed.
4) Small batches. Prefer frequent, reviewable PRs.
5) Evidence-driven. Every claim of completion links to tests, logs, screenshots, or reproducible steps.
6) Human approval gates for sensitive actions (security posture, deployments, new integrations).
