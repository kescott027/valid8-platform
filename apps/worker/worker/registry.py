from __future__ import annotations

from dataclasses import dataclass

from .plugins.base import StepPlugin
from .plugins.shell import ShellPlugin


@dataclass
class PluginRegistry:
  _plugins: dict[str, StepPlugin]

  @classmethod
  def default(cls) -> "PluginRegistry":
    plugins: dict[str, StepPlugin] = {
      "shell": ShellPlugin(),
    }
    return cls(_plugins=plugins)

  def get(self, kind: str) -> StepPlugin:
    return self._plugins[kind]
