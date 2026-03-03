import json

from worker.registry import PluginRegistry
from worker.runner import WorkerRunner


def write_queue(tmp_path, payload):
  queue = tmp_path / "queue.jsonl"
  queue.write_text(json.dumps(payload) + "\n", encoding="utf-8")


def read_results(tmp_path):
  results_file = tmp_path / "results.jsonl"
  return [json.loads(line) for line in results_file.read_text("utf-8").splitlines() if line.strip()]


def test_runner_writes_running_and_succeeded_events(tmp_path):
  write_queue(
    tmp_path,
    {
      "runId": "run-1",
      "jobId": "job-1",
      "pipeline": {"steps": [{"type": "shell", "cmd": ["echo", "hi"]}]},
      "input": {},
    },
  )

  runner = WorkerRunner(data=tmp_path, registry=PluginRegistry.default())
  processed = runner.run_once()

  assert processed == 1
  events = read_results(tmp_path)
  assert [event["status"] for event in events] == ["running", "succeeded"]
  assert "ts" in events[0]
  assert "ts" in events[1]
  assert any("hi" in item for item in events[1]["logs"])


def test_runner_marks_unknown_step_failed(tmp_path):
  write_queue(
    tmp_path,
    {
      "runId": "run-2",
      "jobId": "job-2",
      "pipeline": {"steps": [{"type": "unknown"}]},
      "input": {},
    },
  )

  runner = WorkerRunner(data=tmp_path, registry=PluginRegistry.default())
  processed = runner.run_once()

  assert processed == 1
  events = read_results(tmp_path)
  assert [event["status"] for event in events] == ["running", "failed"]
  assert any("unknown_step" in item for item in events[1]["logs"])
