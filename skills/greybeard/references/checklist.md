# Architect self-review checklist

Derived from the weighted dimensions and automatic checks of an architecture eval run across
three rounds and eight models. The items marked **(common miss)** were where models most often
lost points. Answer each with a pointer into `design.md`; a "no" means fix the design.

## Viability
- [ ] All three gates answered (needed, worth the time, someone runs it); verdict stated, with the production bill and owner named.
- [ ] Build-vs-reuse considered; reasons for building are specific.
- [ ] The cost table in `viability.md` is filled in for build and for the best reuse option.
- [ ] For infrastructure mature products already provide, the verdict names the requirement no existing option meets, or it is STOP / GO, NARROWED.

## Workload and bottleneck
- [ ] Peak load, per-request budget (CPU-seconds, I/O, memory) computed from stated numbers.
- [ ] The bottleneck is named, and the design attacks it first.
- [ ] Every big technology choice traces back to a number.
- [ ] Retry, re-run and fan-out multipliers are in the demand estimate.
- [ ] Working set sized per node under the chosen routing (affinity vs spread).

## Data architecture
- [ ] Hot data has an access path that fits the latency budget (layout, indexing, O(1) addressing where it matters).
- [ ] Working set vs RAM checked; what lives where, and why.
- [ ] Data ownership: one component owns each dataset; others go through its contract.

## Decomposition and locality
- [ ] Each component has one responsibility and a reason to be separate (state, scaling, failure isolation, lifecycle).
- [ ] Large shared state is loaded once per worker/process, not shipped per request.
- [ ] One contract style across services.
- [ ] Each component has its own budget (time, requests, tokens, money), not only a global cap.

## Concurrency
- [ ] Concurrency model matches the runtime's real constraints (GIL, non-thread-safe libraries, global state).
- [ ] Backpressure and queue limits defined.

## Caching (common miss)
- [ ] For each cache: list every input that changes the result. Each one is in the key.
- [ ] Each key includes a data/model/code version.
- [ ] Invalidation on data change is defined; no full keyspace scans in the hot path.
- [ ] Hit rate estimated under the stated churn; if the result cache rarely hits, the expensive intermediates are cached instead. (common miss)

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
- [ ] No sentinel/default value stands in for an error; silent-success paths are named and alerted on. (common miss)
- [ ] Every retried or re-run operation has idempotent side effects, stated per operation. (common miss)
- [ ] Lost work is detected by something other than the lost worker; durable state has a stated backup loss window.
- [ ] Model or untrusted output is verified independently, with one corrective retry carrying the failure reason.
- [ ] Secrets and privileges follow who wrote the code that runs; isolation strength matches the threat, or the accepted threat is named.

## Extensibility (OCP)
- [ ] The 2-4 most likely axes of change are named, each with an extension point.
- [ ] No speculative seams on axes nobody can justify.
- [ ] Every user story walked through the architecture; misfits caused an explicit, recorded architecture change.

## Right-sizing
- [ ] Phase 4 must-haves present: versioning, complete cache keys, identity, restart survival, idempotency, failure semantics, observability.
- [ ] Deferred items listed with the trigger that brings each back.
- [ ] Nothing proposed that the stated team and hardware cannot operate.
- [ ] No work-avoidance step (pruning bound, input cap, cache tier) on the bottleneck was rejected for simplicity alone. (common miss)
- [ ] `design.md` is mechanisms and numbers, not a restatement of this method.

## Decision record
- [ ] Decisions committed, not hedged; each has rationale and a "switch if" condition.
- [ ] No two decisions contradict each other.
- [ ] `ARCHITECTURE.md` rules carry their why.
- [ ] The 3-7 most important rules each name an automated check (`enforcement.md`); the rest say "review only".
