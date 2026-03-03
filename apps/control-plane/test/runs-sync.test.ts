import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { mkdtemp, rm } from "node:fs/promises";
import { describe, it, expect } from "vitest";
import { buildApp } from "../src/app.js";

describe("run synchronization", () => {
  it("transitions queued runs to running and then terminal from worker events", async () => {
    const tmp = await mkdtemp(path.join(os.tmpdir(), "valid8-runs-"));
    const prev = process.env.DATA_DIR;
    process.env.DATA_DIR = tmp;

    const { app } = buildApp();
    try {
      const pipelineRes = await app.inject({
        method: "POST",
        url: "/pipelines",
        payload: { name: "demo", steps: [{ type: "shell", cmd: ["echo", "hello"] }] }
      });
      const pipeline = pipelineRes.json() as { id: string };

      const jobRes = await app.inject({
        method: "POST",
        url: "/jobs",
        payload: { pipelineId: pipeline.id, input: {} }
      });
      const job = jobRes.json() as { runId: string };

      const queuedRes = await app.inject({ method: "GET", url: `/runs/${job.runId}` });
      expect(queuedRes.statusCode).toBe(200);
      expect(queuedRes.json().status).toBe("queued");

      const runningTs = "2026-03-03T21:30:00.000Z";
      const finalTs = "2026-03-03T21:30:01.000Z";
      const lines = [
        JSON.stringify({ runId: job.runId, status: "running", logs: [], ts: runningTs }),
        JSON.stringify({ runId: job.runId, status: "succeeded", logs: ["hello"], ts: finalTs })
      ];
      fs.writeFileSync(path.join(tmp, "results.jsonl"), lines.join("\n") + "\n", "utf-8");

      const finalRes = await app.inject({ method: "GET", url: `/runs/${job.runId}` });
      expect(finalRes.statusCode).toBe(200);
      expect(finalRes.json()).toMatchObject({
        id: job.runId,
        status: "succeeded",
        startedAt: runningTs,
        finishedAt: finalTs
      });
      expect(finalRes.json().logs).toContain("hello");
    } finally {
      await app.close();
      if (prev === undefined) delete process.env.DATA_DIR;
      else process.env.DATA_DIR = prev;
      await rm(tmp, { recursive: true, force: true });
    }
  });

  it("ignores malformed result lines and continues processing valid lines", async () => {
    const tmp = await mkdtemp(path.join(os.tmpdir(), "valid8-runs-malformed-"));
    const prev = process.env.DATA_DIR;
    process.env.DATA_DIR = tmp;

    const { app } = buildApp();
    try {
      const pipelineRes = await app.inject({
        method: "POST",
        url: "/pipelines",
        payload: { name: "demo", steps: [{ type: "shell", cmd: ["echo", "hello"] }] }
      });
      const pipeline = pipelineRes.json() as { id: string };

      const jobRes = await app.inject({
        method: "POST",
        url: "/jobs",
        payload: { pipelineId: pipeline.id, input: {} }
      });
      const job = jobRes.json() as { runId: string };

      const lines = [
        "{not-json",
        JSON.stringify({ runId: job.runId, status: "failed", logs: ["invalid shell cmd"], ts: "2026-03-03T21:35:00.000Z" })
      ];
      fs.writeFileSync(path.join(tmp, "results.jsonl"), lines.join("\n") + "\n", "utf-8");

      const runRes = await app.inject({ method: "GET", url: `/runs/${job.runId}` });
      expect(runRes.statusCode).toBe(200);
      expect(runRes.json().status).toBe("failed");
      expect(runRes.json().logs).toContain("invalid shell cmd");
    } finally {
      await app.close();
      if (prev === undefined) delete process.env.DATA_DIR;
      else process.env.DATA_DIR = prev;
      await rm(tmp, { recursive: true, force: true });
    }
  });
});
