import json
from pathlib import Path

import pytest
from jsonschema import ValidationError, validate


def root_dir() -> Path:
  return Path(__file__).resolve().parents[3]


def load_schema(name: str) -> dict:
  schema_path = root_dir() / "packages" / "contracts" / "schemas" / name
  return json.loads(schema_path.read_text(encoding="utf-8"))


def test_run_request_contract_validates_expected_payload():
  schema = load_schema("run_request.schema.json")
  payload = {
    "runId": "run-1",
    "jobId": "job-1",
    "pipeline": {"steps": [{"type": "shell", "cmd": ["echo", "ok"]}]},
    "input": {"k": "v"},
  }
  validate(payload, schema)


def test_run_result_contract_validates_running_and_final_payloads():
  schema = load_schema("run_result.schema.json")

  running = {
    "runId": "run-1",
    "status": "running",
    "logs": [],
    "ts": "2026-03-03T21:00:00.000Z",
  }
  succeeded = {
    "runId": "run-1",
    "status": "succeeded",
    "logs": ["ok"],
    "ts": "2026-03-03T21:00:01.000Z",
  }
  failed = {
    "runId": "run-1",
    "status": "failed",
    "logs": ["error"],
    "ts": "2026-03-03T21:00:02.000Z",
  }

  validate(running, schema)
  validate(succeeded, schema)
  validate(failed, schema)


def test_run_result_contract_rejects_missing_timestamp():
  schema = load_schema("run_result.schema.json")
  payload = {"runId": "run-1", "status": "succeeded", "logs": ["ok"]}
  with pytest.raises(ValidationError):
    validate(payload, schema)
