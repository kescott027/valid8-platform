# Epics

## EPIC-001
- **Phase:** 0
- **Outcome:** Repository is reproducible and green across local + CI.
- **Dependencies:** None
- **Risks:** Toolchain drift across Node/Python; inconsistent lockfile usage.
- **Exit criteria:** ST-0001 through ST-0004 complete and `make ci` stable.

## EPIC-002
- **Phase:** 0
- **Outcome:** End-to-end run lifecycle is verifiable with contract and integration tests.
- **Dependencies:** EPIC-001
- **Risks:** API/worker contract mismatch; non-deterministic integration behavior.
- **Exit criteria:** ST-0005 through ST-0008 complete with deterministic E2E coverage.

## EPIC-003
- **Phase:** 0
- **Outcome:** Operational and planning artifacts are internally consistent and enforceable.
- **Dependencies:** EPIC-001
- **Risks:** Drift between docs/rules and actual repo layout.
- **Exit criteria:** ST-0009 and ST-0010 complete.

## EPIC-004
- **Phase:** 1
- **Outcome:** Golem-maker core can persist sessions and deterministically generate product artifacts.
- **Dependencies:** EPIC-002
- **Risks:** Non-deterministic generation and inconsistent output structure.
- **Exit criteria:** ST-0011 and ST-0012 complete.

## EPIC-005
- **Phase:** 1
- **Outcome:** Backlog/story generation and validation are production-usable and policy-compliant.
- **Dependencies:** EPIC-004
- **Risks:** Poor story quality causing execution failures downstream.
- **Exit criteria:** ST-0013 and ST-0014 complete.

## EPIC-006
- **Phase:** 1
- **Outcome:** Story execution loop can produce code changes safely with approvals and audits.
- **Dependencies:** EPIC-004, EPIC-005
- **Risks:** Unsafe code changes, missing auditability, weak approval controls.
- **Exit criteria:** ST-0015 through ST-0020 complete.

## EPIC-007
- **Phase:** 2
- **Outcome:** Platform is production-ready with auth, resilience, security, observability, and operations.
- **Dependencies:** EPIC-006
- **Risks:** Security exposure and runtime instability under load.
- **Exit criteria:** ST-0021 through ST-0028 complete.

## EPIC-008
- **Phase:** 3
- **Outcome:** Enterprise-scale capabilities exist for provider routing and governance exports.
- **Dependencies:** EPIC-007
- **Risks:** Provider-specific lock-in and compliance reporting gaps.
- **Exit criteria:** ST-0029 and ST-0030 complete.

## EPIC-009
- **Phase:** 3
- **Outcome:** Supply-chain and runtime security controls reach production-grade depth.
- **Dependencies:** EPIC-007
- **Risks:** Residual runtime and artifact-chain vulnerabilities without image scanning/provenance/DAST.
- **Exit criteria:** ST-0031 through ST-0034 complete.
