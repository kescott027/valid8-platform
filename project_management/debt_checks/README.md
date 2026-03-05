# Debt Preflight Process

1. Copy `project_management/debt_checks/TEMPLATE.md` to `project_management/debt_checks/<Sprint-Number>.md`.
2. Set `Date` to the same date as the sprint update commit date.
3. Record findings with severity, owner, target sprint, status, and link.
4. Set `Gate Result: PASS` only when findings are triaged and owned.
5. Append a same-day `story_management_YYYY-MM-DD.log` entry mentioning debt for that sprint.

Validation is enforced by:

- `python3 project_management/scripts/validate_sprint_governance.py`
- `make ci` (via `governance` target)
