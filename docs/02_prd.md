# PRD — AID8 Platform

## Problem
Users have ideas, but translating them into professional software is slow, ambiguous, and costly.

## Target users
1) Solo founders / builders
2) Product teams bootstrapping new internal tools
3) Enterprises creating standardized “product starters”

## Core user journeys
1) Chat to define product intent and constraints
2) Generate seed docs and repo
3) Generate backlog aligned to phased execution
4) Execute stories via code engine with rules
5) Review, test, deploy, observe
6) Maintain: regular reviews, tech debt management, security posture

## MVP scope (Phase 1)
- Web chat UI
- Conversation state + artifact generation
- Seed doc generation and repo creation (GitHub)
- Backlog generation and story execution loop (human-in-the-loop approvals)
- Basic auth and user/workspace concept
- Audit log of actions and changes

## Out of scope (Phase 1)
- Voice chat
- Multi-tenant enterprise SSO
- Fully autonomous deployment without approvals

## Functional requirements
- FR1: Chat interface supports long-running product definition conversations
- FR2: AI can generate/update docs in repo deterministically
- FR3: AI can generate backlog items conforming to backlog rules
- FR4: Code engine executes stories as PRs with tests and evidence
- FR5: System detects blockers and proposes utilities to remove them
- FR6: All actions are auditable (who/what/when/why)

## Non-functional requirements
- NFR1: Security baseline (SAST/DAST/dependency scanning/secrets scanning)
- NFR2: Reliability baseline (health checks, retries, circuit breakers where relevant)
- NFR3: Observability baseline (structured logs, metrics, tracing hooks)
- NFR4: Maintainability (lint, formatting, modular architecture, docs)
- NFR5: Cost awareness (limits, quotas, safe defaults)

## Success metrics
- Time from idea → repo created
- Time from repo → MVP demo
- Story throughput (completed/started)
- % PRs passing CI on first try
- Security findings severity and time-to-fix
- User activation and retention

## Risks
- Hallucinated requirements or unsafe code changes
- Repo drift from standards
- Secret leakage
- Non-deterministic backlog creation
- Over-automation without guardrails
