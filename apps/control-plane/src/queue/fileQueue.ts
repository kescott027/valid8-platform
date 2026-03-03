import fs from "node:fs";
import path from "node:path";

export type RunRequest = {
  runId: string;
  jobId: string;
  pipeline: unknown;
  input: Record<string, unknown>;
};

export class FileQueue {
  private readonly filePath: string;

  constructor(dataDir: string) {
    this.filePath = path.join(dataDir, "queue.jsonl");
    fs.mkdirSync(dataDir, { recursive: true });
    if (!fs.existsSync(this.filePath)) fs.writeFileSync(this.filePath, "", "utf-8");
  }

  enqueue(req: RunRequest): void {
    const line = JSON.stringify(req);
    fs.appendFileSync(this.filePath, line + "\n", "utf-8");
  }
}
