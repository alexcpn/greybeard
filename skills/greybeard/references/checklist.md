# Architect self-review checklist

Derived from the weighted dimensions and automatic checks of an architecture eval run across
three rounds and eight models. The items marked **(common miss)** were where models most often
lost points. Answer each with a pointer into `design.md`; a "no" means fix the design.

## Viability
- [ ] Phase 0 verdict stated, with the production bill and owner named.
- [ ] Build-vs-reuse considered; reasons for building are specific.

## Workload and bottleneck
- [ ] Peak load, per-request budget (CPU-seconds, I/O, memory) computed from stated numbers.
- [ ] The bottleneck is named, and the design attacks it first.
- [ ] Every big technology choice traces back to a number.

## Data architecture
- [ ] Hot data has an access path that fits the latency budget (layout, indexing, O(1) addressing where it matters).
- [ ] Working set vs RAM checked; what lives where, and why.
- [ ] Data ownership: one component owns each dataset; others go through its contract.

## Decomposition and locality
- [ ] Each component has one responsibility and a reason to be separate (state, scaling, failure isolation, lifecycle).
- [ ] Large shared state is loaded once per worker/process, not shipped per request.
- [ ] One contract style across services.

## Concurrency
- [ ] Concurrency model matches the runtime's real constraints (GIL, non-thread-safe libraries, global state).
- [ ] Backpressure and queue limits defined.

## Caching (common miss)
- [ ] For each cache: list every input that changes the result. Each one is in the key.
- [ ] Each key includes a data/model/code version.
- [ ] Invalidation on data change is defined; no full keyspace scans in the hot path.

## Data pipeline and evolution (common miss)
- [ ] Incoming data is validated, normalised and enriched once, at ingest, not per request.
- [ ] Updates are incremental where data churn is small; new versions swap in atomically.
- [ ] Results are reproducible: a past answer can be recomputed against the data version it used.

## Correctness and debuggability
- [ ] If a reference implementation exists, there is a per-request trace that maps to its outputs.
- [ ] Verification plan: golden cases, differential tests, property tests on the risky logic.

## Safety and failure semantics
- [ ] Every component states fail-closed or fail-open; safety-relevant paths fail closed.
- [ ] Partial failure (one worker, one dependency, one bad record) has a defined outcome.
- [ ] Bad input records are counted and surfaced, never silently skipped.

## Extensibility (OCP)
- [ ] The 2-4 most likely axes of change are named, each with an extension point.
- [ ] No speculative seams on axes nobody can justify.
- [ ] Every user story walked through the architecture; misfits caused an explicit, recorded architecture change.

## Right-sizing
- [ ] Phase 4 must-haves present: versioning, complete cache keys, identity, restart survival, idempotency, failure semantics, observability.
- [ ] Deferred items listed with the trigger that brings each back.
- [ ] Nothing proposed that the stated team and hardware cannot operate.

## Decision record
- [ ] Decisions committed, not hedged; each has rationale and a "switch if" condition.
- [ ] No two decisions contradict each other.
- [ ] `ARCHITECTURE.md` rules carry their why.
