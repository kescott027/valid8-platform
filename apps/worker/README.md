# worker

The worker polls a file-backed queue (`data/queue.jsonl` by default), executes steps, and appends results to
`data/results.jsonl`.

For day-0, only a `shell` step is supported.

Run:
```bash
uv run python -m worker
```
