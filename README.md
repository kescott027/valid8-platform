# hyperdev-scaffold

A seeded Python + Node monorepo scaffold designed to exercise a multi-agent TDD development loop over a realistic product shape:

- **Control plane** (Node/TypeScript): REST API for pipelines/jobs/runs + file-backed queue boundary.
- **Worker** (Python): polls the queue, executes steps via a plugin registry (starts with a safe-ish `shell` step), writes results.
- **Contracts**: OpenAPI + JSON schema placeholders for shared payloads.

## Quick start

Prereqs:
- Node 20+
- Python 3.11+
- `uv` (recommended) or you can adapt to your preferred tool

### Install

```bash
make bootstrap
```

Optional but recommended:
```bash
make precommit-install
```

### Run (two terminals)

```bash
make dev-api
```

```bash
make dev-worker
```

Then:
```bash
curl -s http://localhost:3000/health
```

### Test

```bash
make test
```

### Security

```bash
make security
```

## Project layout

```
apps/
  control-plane/      # Node/TS API
  worker/             # Python worker
packages/
  contracts/          # OpenAPI + schema placeholders
infra/
  docker-compose.yml  # Local optional (API + worker + shared volume)
project_management/   # Backlog, stories, sprint artifacts, governance rules
```

## Notes

- This scaffold is intentionally **file-backed** for queue/results to keep day-0 simple while still preserving a clean boundary you can swap later (Redis/SQS/etc.).
- CI is configured to run lint + tests + build + security checks for both runtimes.
