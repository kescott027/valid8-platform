import Fastify from "fastify";
import { z } from "zod";
import { nanoid } from "nanoid";
import { dataDir } from "./config.js";
import { FileQueue } from "./queue/fileQueue.js";
import { MemoryStore, Step, Pipeline, Job, Run } from "./store/memory.js";
import { FileResults } from "./results/fileResults.js";

const StepSchema = z.object({
  type: z.literal("shell"),
  cmd: z.array(z.string()).min(1)
});

const PipelineCreateSchema = z.object({
  name: z.string().min(1),
  steps: z.array(StepSchema).min(1)
});

const JobCreateSchema = z.object({
  pipelineId: z.string().min(1),
  input: z.record(z.string(), z.unknown())
});

export type AppDeps = {
  store?: MemoryStore;
  queue?: Pick<FileQueue, "enqueue">;
  results?: Pick<FileResults, "readNew">;
};

export function buildApp(deps: AppDeps = {}) {
  const app = Fastify({ logger: false });
  const store = deps.store ?? new MemoryStore();
  const queue = deps.queue ?? new FileQueue(dataDir());
  const results = deps.results ?? new FileResults(dataDir());

  const syncRunResults = () => {
    const updates = results.readNew();
    for (const event of updates) {
      const run = store.runs.get(event.runId);
      if (!run) continue;

      const ts = event.ts ?? new Date().toISOString();
      if (event.status === "running") {
        run.status = "running";
        run.startedAt = run.startedAt ?? ts;
      } else {
        run.status = event.status;
        run.startedAt = run.startedAt ?? ts;
        run.finishedAt = ts;
      }
      if (event.logs.length > 0) run.logs.push(...event.logs);
    }
  };

  app.get("/health", async () => ({ ok: true }));

  app.post("/pipelines", async (req, reply) => {
    const body = PipelineCreateSchema.parse(req.body);
    const id = nanoid();
    const pipeline: Pipeline = { id, name: body.name, steps: body.steps as Step[] };
    store.pipelines.set(id, pipeline);
    return reply.code(201).send(pipeline);
  });

  app.post("/jobs", async (req, reply) => {
    const body = JobCreateSchema.parse(req.body);
    const pipeline = store.pipelines.get(body.pipelineId);
    if (!pipeline) return reply.code(404).send({ error: "pipeline_not_found" });

    const jobId = nanoid();
    const runId = nanoid();

    const job: Job = { id: jobId, pipelineId: pipeline.id, input: body.input, runId };
    store.jobs.set(jobId, job);

    const run: Run = { id: runId, jobId, status: "queued", startedAt: null, finishedAt: null, logs: [] };
    store.runs.set(runId, run);

    queue.enqueue({ runId, jobId, pipeline, input: body.input });
    return reply.code(201).send(job);
  });

  app.get("/runs/:runId", async (req, reply) => {
    syncRunResults();
    const runId = (req.params as { runId: string }).runId;
    const run = store.runs.get(runId);
    if (!run) return reply.code(404).send({ error: "run_not_found" });
    return reply.send(run);
  });

  return { app, store };
}
