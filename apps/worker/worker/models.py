from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Literal


@dataclass(frozen=True)
class ShellStep:
  type: Literal["shell"]
  cmd: list[str]


Step = ShellStep


@dataclass(frozen=True)
class Pipeline:
  id: str
  name: str
  steps: list[Step]


@dataclass(frozen=True)
class RunRequest:
  runId: str
  jobId: str
  pipeline: dict[str, Any]
  input: dict[str, Any]
