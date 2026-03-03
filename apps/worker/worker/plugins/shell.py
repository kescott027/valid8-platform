from __future__ import annotations

import subprocess
from dataclasses import dataclass

from .base import StepPlugin, StepResult


@dataclass(frozen=True)
class ShellPlugin(StepPlugin):
  kind: str = "shell"

  def run(self, step: dict, *, workdir: str) -> StepResult:
    cmd = step.get("cmd")
    if not isinstance(cmd, list) or not all(isinstance(x, str) for x in cmd) or not cmd:
      return StepResult(ok=False, logs=["invalid shell cmd"])

    # Day-0 safety: no shell=True, no string command parsing.
    try:
      proc = subprocess.run(
        cmd,
        cwd=workdir,
        check=False,
        capture_output=True,
        text=True,
      )
      logs: list[str] = []
      if proc.stdout:
        logs.append(proc.stdout.strip())
      if proc.stderr:
        logs.append(proc.stderr.strip())
      return StepResult(ok=proc.returncode == 0, logs=logs)
    except Exception as e:  # noqa: BLE001
      return StepResult(ok=False, logs=[f"shell_error: {e!r}"])
