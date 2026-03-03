from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator


@dataclass
class FileQueueReader:
  queue_path: Path
  state_path: Path

  def _load_offset(self) -> int:
    if not self.state_path.exists():
      return 0
    try:
      raw = json.loads(self.state_path.read_text("utf-8"))
      return int(raw.get("offset", 0))
    except Exception:
      return 0

  def _save_offset(self, offset: int) -> None:
    self.state_path.parent.mkdir(parents=True, exist_ok=True)
    self.state_path.write_text(json.dumps({"offset": offset}), "utf-8")

  def read_new(self) -> Iterator[dict]:
    self.queue_path.parent.mkdir(parents=True, exist_ok=True)
    self.queue_path.touch(exist_ok=True)

    offset = self._load_offset()
    with self.queue_path.open("r", encoding="utf-8") as f:
      f.seek(offset)
      while True:
        line = f.readline()
        if not line:
          break
        offset = f.tell()
        yield json.loads(line)
    self._save_offset(offset)
