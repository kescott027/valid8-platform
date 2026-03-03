from __future__ import annotations

import json
import time
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

from .config import data_dir
from .filequeue import FileQueueReader
from .registry import PluginRegistry


@dataclass
class WorkerRunner:
  data: Path
  registry: PluginRegistry

  def run_once(self) -> int:
    queue_path = self.data / "queue.jsonl"
    state_path = self.data / "worker_state.json"
    results_path = self.data / "results.jsonl"
    reader = FileQueueReader(queue_path=queue_path, state_path=state_path)

    processed = 0
    for req in reader.read_new():
      processed += 1
      run_id = str(req.get("runId", ""))
      pipeline = req.get("pipeline") or {}
      steps = pipeline.get("steps") or []

      workdir = self.data / "workspaces" / run_id
      workdir.mkdir(parents=True, exist_ok=True)

      logs: list[str] = []
      ok = True
      started_at = datetime.now(UTC).isoformat()

      running_event = {
        "runId": run_id,
        "status": "running",
        "logs": [],
        "ts": started_at,
      }
      results_path.parent.mkdir(parents=True, exist_ok=True)
      with results_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(running_event) + "\n")

      for step in steps:
        kind = step.get("type")
        if kind not in self.registry._plugins:
          ok = False
          logs.append(f"unknown_step: {kind}")
          break
        plugin = self.registry.get(kind)
        res = plugin.run(step, workdir=str(workdir))
        logs.extend(res.logs)
        if not res.ok:
          ok = False
          break

      result = {
        "runId": run_id,
        "status": "succeeded" if ok else "failed",
        "logs": logs,
        "ts": datetime.now(UTC).isoformat(),
      }
      with results_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(result) + "\n")

    return processed

  def loop(self, *, poll_interval_s: float = 0.5) -> None:
    while True:
      self.run_once()
      time.sleep(poll_interval_s)


def main() -> None:
  runner = WorkerRunner(data=data_dir(), registry=PluginRegistry.default())
  runner.loop()
