import fs from "node:fs";
import path from "node:path";

export type RunResultEvent = {
  runId: string;
  status: "running" | "succeeded" | "failed";
  logs: string[];
  ts?: string;
};

function isRunResultEvent(value: unknown): value is RunResultEvent {
  if (!value || typeof value !== "object") return false;
  const item = value as Record<string, unknown>;
  if (typeof item.runId !== "string" || item.runId.length === 0) return false;
  if (item.status !== "running" && item.status !== "succeeded" && item.status !== "failed") return false;
  if (!Array.isArray(item.logs) || !item.logs.every((x) => typeof x === "string")) return false;
  if (item.ts !== undefined && typeof item.ts !== "string") return false;
  return true;
}

export class FileResults {
  private readonly filePath: string;
  private readonly statePath: string;

  constructor(dataDir: string) {
    this.filePath = path.join(dataDir, "results.jsonl");
    this.statePath = path.join(dataDir, "control_plane_state.json");
    fs.mkdirSync(dataDir, { recursive: true });
    if (!fs.existsSync(this.filePath)) fs.writeFileSync(this.filePath, "", "utf-8");
  }

  private loadOffset(): number {
    if (!fs.existsSync(this.statePath)) return 0;
    try {
      const raw = JSON.parse(fs.readFileSync(this.statePath, "utf-8")) as { offset?: unknown };
      const offset = Number(raw.offset ?? 0);
      return Number.isFinite(offset) && offset >= 0 ? offset : 0;
    } catch {
      return 0;
    }
  }

  private saveOffset(offset: number): void {
    fs.writeFileSync(this.statePath, JSON.stringify({ offset }), "utf-8");
  }

  readNew(): RunResultEvent[] {
    const events: RunResultEvent[] = [];
    let offset = this.loadOffset();
    const fd = fs.openSync(this.filePath, "r");
    try {
      const stat = fs.fstatSync(fd);
      if (offset > stat.size) offset = 0;
      const size = stat.size - offset;
      if (size <= 0) {
        this.saveOffset(stat.size);
        return events;
      }

      const chunk = Buffer.alloc(size);
      fs.readSync(fd, chunk, 0, size, offset);
      const text = chunk.toString("utf-8");
      let cursor = 0;

      while (cursor < text.length) {
        const nextNewline = text.indexOf("\n", cursor);
        const end = nextNewline === -1 ? text.length : nextNewline;
        const line = text.slice(cursor, end).trim();
        cursor = nextNewline === -1 ? text.length : nextNewline + 1;
        if (!line) continue;
        try {
          const parsed = JSON.parse(line) as unknown;
          if (isRunResultEvent(parsed)) events.push(parsed);
        } catch {
          // Ignore malformed lines and continue consuming.
        }
      }

      this.saveOffset(stat.size);
      return events;
    } finally {
      fs.closeSync(fd);
    }
  }
}
