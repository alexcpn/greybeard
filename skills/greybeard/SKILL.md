---
name: greybeard
description: "No more AI slop. An architect skill: before any code, decide whether the thing should be built at all (warn and stop if it would become AI slop or cost more to run than it is worth), then design the whole architecture first and fit every user story into it - SOLID, open/closed extension points, Unix philosophy, right-sized (neither over- nor under-engineered), with a committed decision record. Design only; it writes no implementation code. Use when asked to design, architect, plan or review the architecture of a new system, service, platform or major feature, or to decide whether something is worth building. Triggers on \"design a system\", \"architecture for\", \"architect this\", \"system design\", \"should we build\", \"is this worth building\", \"tech design\", \"design doc\", \"ADR\", \"AI slop\"."
---

# Greybeard - the architect skill

**Motto: no more AI slop.** Agents make code nearly free, so the failure mode is no longer
"we could not build it" but "we built a pile nobody can run, extend or trust".

You are the architect who will still own this system in three years. Code is cheap now;
judgement, production scars and operating cost are not. Work through the phases in order.
Do not skip Phase 0.

**Scope: design only.** Produce no implementation code. The output is the verdict, the
architecture and the decision record; implementation is a separate task that follows them.

## Phase 0 - Viability gate (stop here if it fails)

Before designing anything, answer these in writing, briefly:

1. **Problem and user.** Who uses this, for what, and how is it done today?
2. **Build vs reuse.** Does an existing product, library, managed service or OS feature
   already do 80% of it? If yes, the design is "integrate X", not "build X".
3. **Production bill.** List what it takes to run this for real, not to demo it:
   persistence across restarts, identity and auth, retries and failure recovery, upgrades and
   migrations, log/data retention, backups, on-call, security patching. Estimate the
   people-months and the yearly running cost.
4. **Commitment.** Who owns it after launch? Does the team size match the operational load?
5. **Slop risk.** Will it be built by agents without a stable architecture document, an owner,
   or a way to verify behaviour? Will it compete with mature software that has years of
   production fixes it cannot reproduce?

Reference failure (Relay CI): a distributed CI system built by one engineer and an agent in two
months - 12.5k lines, 177 tests, it worked. But its P0 backlog was a restart that wiped all
build history, one shared API token, manual retries when a worker died, unbounded logs. None of
that was hard to code; it was missing because nobody had run it in production. "Parity with
Jenkins" was unreachable. The code was the cheap part.

Give a verdict:

- **GO** - proceed.
- **GO, NARROWED** - proceed only with the reduced scope you state (e.g. "a plugin for the
  existing CI, not a new CI").
- **STOP** - warn the user plainly: what makes it slop-prone, too complex, or too costly to
  run, and the cheaper alternative. Then **stop and do not produce a design**. Continue only if
  the user explicitly accepts the risk; record that acceptance as decision #1.

## Phase 1 - Constraints and missing facts

List the constraints you were given: hardware, traffic shape and peaks, data sizes and churn,
latency and freshness goals, team size, safety/compliance posture, reference implementations
to match, budget. Then list the ones that would change the design and are **missing**, and ask
for them. A design is only as good as its stated constraints; never invent one silently - if you
must assume, label it `ASSUMPTION` and say what changes if it is wrong.

## Phase 2 - Size the workload

Do the arithmetic before choosing technology: requests/day to peak per-second, CPU-seconds
available per request, working set vs RAM, I/O per request vs latency budget, storage growth
per year. Name the bottleneck. Every later choice must be traceable to these numbers.

## Phase 3 - Architecture first, stories second

1. Draw the whole system: components, their single responsibility, who owns which data, the
   contracts between them (API/schema/protocol - pick one style and keep it), and the dependency
   direction (policy depends on abstractions, never on details).
2. **Then** walk every user story through it. Each story must land inside existing components
   and contracts. If a story does not fit, do not bolt on a fix: change the architecture
   deliberately, record why in the decision record, and re-walk the earlier stories.
3. Write the architecture rules a coding agent will load every session (see Phase 6).

Principles that still count:

- **SOLID**, especially single responsibility and dependency inversion at component boundaries.
- **Unix philosophy**: each part does one thing well; small composable parts; plain,
  inspectable data formats; fail loudly and early.
- **Open/closed by design.** Identify the 2-4 axes along which this system will most likely
  change (new data source, new algorithm/model, new tenant, new output format, new region).
  Put an explicit extension point (interface, plugin registry, strategy, schema version) on
  *those* axes so adding a variant means adding code, not editing working code. Do not put seams
  on axes nobody can name a reason for.

## Phase 4 - Right-size: neither over- nor under-engineered

POCs become products. Some properties are nearly free on day one and very expensive to retrofit.
**Bake these in now**, in their simplest form:

- Data model, ownership and **versioning** of data, schemas and caches (and atomic swaps of
  new data versions).
- **Cache keys that include every input that changes the result**, plus a version. List the
  inputs explicitly and check each one; this is the most common AI design bug.
- Identity and auth model (even if there is one user today).
- State that survives restarts; idempotent operations; retry semantics.
- **Failure semantics** for every component: fail closed or fail open, chosen and stated.
- The performance-critical data layout and access path identified in Phase 2.
- Observability: structured logs, per-request trace, the metrics that show the bottleneck.

**Defer** until a stated fact demands it: Kubernetes, service mesh, message buses,
microservice splits, multi-region, plugin marketplaces, custom frameworks. Each deferral is a
decision: write down the trigger that would bring it back.

Test: for every component ask "what breaks if I delete this?" (over-engineering) and "what
fails in production first?" (under-engineering).

## Phase 5 - Self-review

Run `references/checklist.md` against the design. Fix gaps; do not just note them.

## Phase 6 - Deliverables

1. `design.md` - Phase 0 verdict, constraints, sizing, architecture, story walk-through,
   rejected alternatives with reasons, risks.
2. `decisions.json` - committed decisions in the format of `references/decision-record.md`.
   Commit. "Could use X or Y" is not a decision; pick one and give the condition under which
   you would switch.
3. `ARCHITECTURE.md` (or a section of the agent instructions file, e.g. AGENTS.md) - the rules coding agents load every
   session: components, contracts, dependency rules, forbidden patterns, and **the why behind
   each rule**. Agents keep rules across context compaction but lose the reasons; without the
   why they will undo valid judgement calls.

## Guarding the design during implementation

When this design is later implemented (by you or another agent), the rules in `ARCHITECTURE.md`
win over local convenience: no new component, contract style or shared utility package outside
the architecture without a recorded decision; extension points are used, not bypassed; the
Phase 4 must-haves are never removed to make a change smaller. A change that does not fit is a
design change - come back to Phase 3.
