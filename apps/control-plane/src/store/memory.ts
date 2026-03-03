export type Step = { type: "shell"; cmd: string[] };
export type Pipeline = { id: string; name: string; steps: Step[] };
export type Job = { id: string; pipelineId: string; input: Record<string, unknown>; runId: string };
export type RunStatus = "queued" | "running" | "succeeded" | "failed";
export type Run = { id: string; jobId: string; status: RunStatus; startedAt: string | null; finishedAt: string | null; logs: string[] };

export class MemoryStore {
  pipelines = new Map<string, Pipeline>();
  jobs = new Map<string, Job>();
  runs = new Map<string, Run>();
}
