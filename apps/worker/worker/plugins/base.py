from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class StepResult:
  ok: bool
  logs: list[str]


class StepPlugin(Protocol):
  kind: str

  def run(self, step: dict, *, workdir: str) -> StepResult: ...
