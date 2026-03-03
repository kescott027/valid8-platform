#
REPO_BACKLOG_AND_SPRINT_MANAGEMENT_SETUP.md

## Objective

Implement a lightweight, durable, professional development management system **inside this repository** using Markdown files and an append-only audit log. This replaces JIRA for fast iteration while maintaining quality and continuity.

You must:

1. create the directory structure
2. create the management files (templates + initial content)
3. define operational rules
4. optionally add CI enforcement (if GitHub Actions is present)
   Do not implement product features. This is repo governance only.

---

## 1) Directory Structure (Required)

Create the following directories:

```
/docs/
  /planning/

/project_management/
  Backlog.md
  Current_Sprint.md
  Project_Sprint_Log.md
  Decision_Matrix.md
  Rules.md
  /completed_sprints/
  /log/
```

Notes:

* `/docs/planning/` is where planning artifacts should live.
* `/project_management/` is the single source of truth for backlog + sprint execution.
* `/project_management/log/` is append-only audit ledger storage.

---

## 2) Core Files to Create (Required)

### 2.1 /project_management/Backlog.md

Create a backlog file containing:

* A header stating it is the authoritative backlog
* A strict story template
* Sections for priorities (P0, P1, P2)
* Stories listed in strict priority order

Include a small “Backlog Index” in the header:

* Last updated date
* Total story count
* Highest story ID present

Story template (must be included in file):

* **ID:**
* **Title:**
* **Description:**
* **Acceptance Criteria:**
* **Dependencies:**
* **Risk:** Low / Medium / High
* **Architectural Impact:** None / Low / Medium / High
* **Notes/Evidence:** (empty until done)

Backlog Completion Rule (must be written in file):
A story is “Done” ONLY when:

* It appears in a completed Sprint_N.md marked Done with closure date
* Evidence is recorded (commit/PR refs + tests + doc updates)
* It is removed from Backlog.md (or moved into an explicit “Archive” section)

---

### 2.2 /project_management/Current_Sprint.md

Create a current sprint file containing:

* Sprint number placeholder
* Sprint goal
* Selected story list (IDs + titles)
* Rationale for selection
* Risks
* Acceptance summary
* Definition of Done checklist

This file contains ONLY current sprint content.

---

### 2.3 /project_management/Project_Sprint_Log.md

Create a running ledger file.

It must append one section per sprint:

* Sprint number
* Date range
* Summary
* Architectural decisions made
* Debt introduced/resolved
* Test delta summary
* Risk flags

This file is never reset.

---

### 2.4 /project_management/Decision_Matrix.md

Create a table-based decision log.

Include table header:

| Date | Topic | Options | Recommended | Decision | Rationale | Impact | Status |
| ---- | ----- | ------- | ----------- | -------- | --------- | ------ | ------ |

Rules:

* Any decision affecting architecture/security/protocol/storage must be logged here before proceeding.
* If not decided, Status = Pending.

---

### 2.5 /project_management/Rules.md

Create a rules document containing:

* Change management requirements
* Sprint lifecycle rules
* Definition of Done (DoD)
* Required quality checks per sprint
* Cadence for deeper reviews (example: every 3 sprints)

Minimum required sections:

* “Non-Negotiable Quality Rules”
* “Sprint Close Checklist”
* “Every 3 Sprints: Architecture Integrity Review”
* “Feature Flag Expectations (if applicable)”
* “No Log Entry, No Change”

---

## 3) Sprint File Templates (Required)

Create a template file:

`/project_management/Sprint_TEMPLATE.md`

Include:

* Sprint number
* Start date
* End date
* Goal
* Included stories
* Files touched
* Notes (architecture/security)
* Test results
* Review summary
* Close-out checklist
* Retro notes
* Closure signature line (who/what closed)

Do not create Sprint_1.md unless instructed by the user.
If you do create Sprint_1.md, it must be placed in `/project_management/` while active and moved to `/project_management/completed_sprints/` on close.

---

## 4) Append-Only Audit Ledger (Required)

Create daily rotating log files stored in:

`/project_management/log/story_management_YYYY-MM-DD.log`

Format must be NDJSON: one JSON object per line.

Each entry MUST include:

* ts (RFC3339 UTC timestamp)
* actor ("human" | "ai" | identifier)
* change_type (add|update|remove|move|reorder|split|close_sprint|reopen_sprint|correct)
* entity_type (story|sprint|decision|file)
* entity_id (story ID or Sprint_N or "BACKLOG")
* files_touched (array)
* summary (short)
* rationale (short)
* links (array; commit hashes or PR refs if available)

Rules:

* Never edit existing log lines.
* Corrections must be appended as change_type="correct" referencing prior entry in summary.
* Every change to project_management markdown files MUST add a log entry.

---

## 5) Required Operational Rules (Must be Enforced)

### 5.1 Source-of-Truth Rules

* Backlog.md is authoritative for planned work.
* Completed work is authoritative in completed sprint files.
* Current_Sprint.md is authoritative for “what’s being worked now.”

### 5.2 “No Log Entry, No Change”

Any edit that touches:

* Backlog.md
* Current_Sprint.md
* Decision_Matrix.md
* Project_Sprint_Log.md
* Sprint files
  MUST include a corresponding audit log entry the same day.

### 5.3 Close Sprint Procedure

When a sprint closes:

1. Sprint file is finalized (tests + notes + close checklist)
2. Project_Sprint_Log.md is appended
3. Current_Sprint.md is cleared/reset
4. Sprint file is moved to /completed_sprints/
5. Audit log entry is appended

---

## 6) Optional: CI Enforcement (Recommended If GitHub Actions Exists)

If repo uses GitHub Actions, add a workflow:

* Any PR that modifies `/project_management/*.md` must also modify:

  * `/project_management/log/story_management_*.log` (today’s or current PR date)

If CI cannot reliably determine “today’s” date:

* Allow any story_management_*.log modification in same PR.

Also recommend:

* Fail if a completed sprint file is modified without a matching audit log entry.

If Actions is not present, document this as “manual enforcement until CI exists.”

---

## 7) Deliverables Checklist (Must be satisfied before completion)

* [ ] /docs/planning exists
* [ ] /project_management exists
* [ ] Backlog.md created with templates + rules
* [ ] Current_Sprint.md created
* [ ] Project_Sprint_Log.md created
* [ ] Decision_Matrix.md created
* [ ] Rules.md created
* [ ] Sprint_TEMPLATE.md created
* [ ] /project_management/log exists and contains at least one example log file
* [ ] If CI added, workflow is present and documented

---

## 8) First Output Required From You

After creating the above, output:

1. A short summary of what was created
2. The file tree
3. Any assumptions made
4. Any repo-specific adjustments recommended (naming, policies, branching)

End.
