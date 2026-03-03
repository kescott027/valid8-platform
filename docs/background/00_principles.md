# Principles (Definition of Done)

1. Any behavior change must be driven by a failing automated test first (red → green → refactor).
2. No skipped tests in main.
3. Public boundaries (API payloads, queue payloads) must be validated and versioned.
4. CI must be green: lint + tests pass.
5. Every story includes clear acceptance criteria mapped to tests.
6. Prefer small PRs: one story per PR.
