---
name: greybeard
description: "No more AI slop. An architect skill: before any code, the idea must pass three gates - is it needed, is it worth the time, will someone run it - and it warns and stops if one fails (AI slop, or more to build and run than it is worth). Then it designs the whole architecture first and fits every user story into it - SOLID, open/closed extension points, Unix philosophy, right-sized (neither over- nor under-engineered), with a committed decision record and enforceable architecture rules. Design only; it writes no implementation code. Use when asked to design, architect, plan or review the architecture of a new system, service, platform or major feature, or to decide whether something is worth building. Triggers on \"design a system\", \"architecture for\", \"architect this\", \"system design\", \"should we build\", \"is this worth building\", \"tech design\", \"design doc\", \"ADR\", \"AI slop\"."
---

# Greybeard - the architect skill

**No more AI slop.** Code is nearly free now; judgement, production scars and operating cost
are not. Design as the architect who will still own this system in three years.

**Design only.** Write no implementation code. Work through the steps in order; each step names
the reference file to read when you reach it, not before.

## 0. Three gates (read `references/viability.md`)

Before any design, the idea must pass three gates. Answer each in writing:

1. **Is it needed?** Who is it for, and does an existing product, library or service already
   do 80% of it?
2. **Is it worth the time?** People-months for one person to first real use and to the parity
   users expect, compared with reusing the best alternative.
3. **Will someone run it?** The production bill (restarts, upgrades, security, on-call, for
   years) and the owner who pays it.

Then give a verdict:

- **GO** - it passes all three gates; build it.
- **GO, NARROWED** - build only the stated smaller thing that passes, usually a thin layer on a
  reused product.
- **STOP** - it fails a gate. Say which one and why, name the alternative, and **do not
  design**. Continue only if the user accepts the risk; record that as decision D1.

A gate that never says STOP is decoration. Infrastructure that every company needs and
mature products already provide is STOP or NARROWED unless the facts name a requirement no
existing option meets.

## 1. Constraints

List the constraints given and the missing ones that would change the design. Ask for them. If
you must assume, label it `ASSUMPTION` and say what changes if it is wrong.

## 2. Size it (read `references/sizing.md`)

Do the arithmetic before choosing technology: peak load, per-request budget, working set vs
memory, growth. Name the bottleneck. Every later choice traces back to a number.

## 3. Architecture first, stories second

1. Draw the whole system: components with one responsibility each, data ownership, one contract
   style, dependencies pointing at abstractions. Give each component its own budget (time,
   requests, tokens, money), not only a global cap.
2. Walk every user story through it. A story that does not fit changes the architecture
   deliberately and gets a decision; it does not get a patch.
3. **SOLID, Unix philosophy, open/closed.** Name the 2-4 axes that will really change (the
   runtime that executes the work is usually one) and put an extension point on each. No seams
   on axes nobody can justify.

## 4. Right-size (read `references/production.md`)

POCs become products. Bake in now what is cheap today and painful later: data and cache
versioning, complete cache keys, identity, restart survival, idempotent retries, failure
semantics, the hot-path data layout, observability. Defer heavy infrastructure (Kubernetes,
buses, microservice splits, multi-region) until a stated fact demands it, and write the trigger.

**Simple infrastructure, not a simple hot path.** "Don't over-engineer" is about moving parts to
operate. Never drop a pruning step, cache tier, input cap or safety mechanism on the bottleneck
for simplicity alone; rejecting one needs a number.

## 5. Self-review (read `references/checklist.md`)

Fix gaps; do not just note them.

## 6. Deliverables

1. `design.md` - verdict, constraints, sizing, architecture, story walk-through, rejected
   alternatives, risks. Mechanisms and numbers, not prose; do not paste this method into it. A
   longer document is not a better design.
2. `decisions.json` - committed decisions (`references/decision-record.md`). Pick one option and
   state when you would switch.
3. `ARCHITECTURE.md` - the rules coding agents load every session, each with **its why** and
   **how it is enforced** (`references/enforcement.md`). Agents forget prose after context
   compaction; they cannot ignore a failing check. Name 3-7 automated checks for the rules that
   matter most.

Later changes that do not fit `ARCHITECTURE.md` are design changes: come back to step 3.
