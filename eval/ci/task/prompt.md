# Design Task: CI for an agent-heavy engineering team

You are the architect. Produce a design for the system below. You have no code to look at;
everything you know is in this document.

## Context

An engineering organisation increasingly writes code with AI coding agents. Agents push
commits, open pull requests, read build failures, fix them and push again, often without a
human in the loop. The current CI is a self-hosted Jenkins (about 9 years old, ~60 plugins,
used for 20 repositories, maintained part-time by one person). It works for humans reading a
web UI; agents have to scrape console text to find out why a build failed.

The team asks you to design the CI system they should use for agent-driven work. Whether that
means extending what exists, adopting something, or building something new is part of your job.

## Facts

| Item | Value |
|---|---|
| Repositories | 15 active (Go, Python, TypeScript); pipelines defined per repository |
| People | ~40 developers; ~20 concurrent coding-agent instances during working hours, some overnight |
| Build volume | ~600 builds/day today; peaks of ~80 builds/hour; agent fix loops resubmit after every fix (median 4 attempts per change, worst seen 30+) |
| Typical pipeline | clone, build, unit tests, 1–3 linters, a dependency/vulnerability scanner, an AI code review step; 8–15 tasks, most independent after clone; 3–12 minutes |
| Heavy caches | Go module cache ~2 GB, npm ~1.5 GB, vulnerability DB ~0.5 GB, per language toolchain images 0.5–2 GB |
| Hosting | 1 control VM (4 vCPU, 8 GB RAM) and 4 worker VMs (16 vCPU, 64 GB RAM, 500 GB NVMe each), Docker available, no managed Kubernetes |
| Source hosting | GitHub (most repos) and GitLab (3 repos); webhooks available; status checks gate merges |
| Team to build and run it | 2 engineers (Go preferred), one of them also maintains Jenkins; target: first production use in 3 months |
| Security | Pipelines need secrets (registry credentials, API keys for the AI review). Agents will submit pipelines from branches whose code no human has read. |

## User stories

1. As a developer, a push or pull request triggers the pipeline defined in the repository, and
   the result is reported back to GitHub/GitLab as a commit/PR status.
2. As a coding agent, I can submit a build for any repo/branch/commit, follow its progress,
   fetch logs, get a structured explanation of why it failed, and re-run only what failed.
3. As a team lead, an AI code review runs as a pipeline step and can block a merge.
4. As a developer, I can watch logs live while a task runs.
5. As a security owner, secrets used by pipelines never appear in logs or in agent-visible output.
6. As the platform owner, I can add a new linter, scanner or integration without changing the
   scheduler.
7. As an engineering manager, I can see build volume, queue time and failure rates, and how much
   build capacity agents consume.

## Deliverables

Write these files in the current directory:

1. `design.md`: your design. Cover at least: workload and constraints analysis, components and
   their responsibilities, contracts between them, data storage, concurrency/execution model,
   failure handling, security, how each user story is served, extensibility, operations,
   trade-offs and rejected alternatives, risks. Commit to decisions; a list of options without
   a choice is not a decision.
2. `decisions.json`: a JSON array of your committed decisions:
   ```json
   [{"id": "D1", "area": "short area name", "decision": "what you will do",
     "rationale": "the fact that forces it", "status": "decided | assumption | deferred"}]
   ```
