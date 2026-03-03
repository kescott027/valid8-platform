import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { mkdtemp, rm } from "node:fs/promises";
import Ajv2020 from "ajv/dist/2020.js";
import { describe, it, expect } from "vitest";
import { buildApp } from "../src/app.js";

function rootDir() {
  return path.resolve(process.cwd(), "..", "..");
}

function readJson(filePath: string): unknown {
  return JSON.parse(fs.readFileSync(filePath, "utf-8"));
}

describe("contracts", () => {
  it("validates queue and run result fixtures", () => {
    const ajv = new Ajv2020({ allErrors: true });

    const runRequestSchema = readJson(path.join(rootDir(), "packages/contracts/schemas/run_request.schema.json"));
    const runResultSchema = readJson(path.join(rootDir(), "packages/contracts/schemas/run_result.schema.json"));

    const validateRunRequest = ajv.compile(runRequestSchema);
    const validateRunResult = ajv.compile(runResultSchema);

    const runRequest = {
      runId: "r1",
      jobId: "j1",
      pipeline: { id: "p1", name: "sample", steps: [{ type: "shell", cmd: ["echo", "ok"] }] },
      input: {}
    };

    const runningResult = { runId: "r1", status: "running", logs: [], ts: "2026-03-03T00:00:00.000Z" };
    const finalResult = { runId: "r1", status: "succeeded", logs: ["ok"], ts: "2026-03-03T00:00:01.000Z" };
    const invalidResult = { runId: "r1", status: "succeeded", logs: [] };

    expect(validateRunRequest(runRequest)).toBe(true);
    expect(validateRunResult(runningResult)).toBe(true);
    expect(validateRunResult(finalResult)).toBe(true);
    expect(validateRunResult(invalidResult)).toBe(false);
  });

  it("writes queue payloads that satisfy run_request schema", async () => {
    const tmp = await mkdtemp(path.join(os.tmpdir(), "valid8-contracts-"));
    const prev = process.env.DATA_DIR;
    process.env.DATA_DIR = tmp;

    const ajv = new Ajv2020({ allErrors: true });
    const runRequestSchema = readJson(path.join(rootDir(), "packages/contracts/schemas/run_request.schema.json"));
    const validateRunRequest = ajv.compile(runRequestSchema);

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
        payload: { pipelineId: pipeline.id, input: { hello: "world" } }
      });
      expect(jobRes.statusCode).toBe(201);

      const lines = fs.readFileSync(path.join(tmp, "queue.jsonl"), "utf-8").trim().split("\n");
      expect(lines.length).toBe(1);

      const payload = JSON.parse(lines[0]) as unknown;
      expect(validateRunRequest(payload)).toBe(true);
    } finally {
      await app.close();
      if (prev === undefined) delete process.env.DATA_DIR;
      else process.env.DATA_DIR = prev;
      await rm(tmp, { recursive: true, force: true });
    }
  });
});
