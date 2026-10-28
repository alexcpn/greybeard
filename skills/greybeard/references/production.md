# Right-sizing: what to bake in, what to defer

## Bake in now, in the simplest form

- **Versioning** of data, schemas and caches, with atomic swaps of new data versions.
- **Complete cache keys:** list every input that changes the result, plus a version, and check
  each one. This is the most common AI design bug.
- **Identity and auth model,** even if there is one user today.
- **Restart survival:** durable state, and a backup with a stated loss window.
- **Idempotent retries:** for everything that can be retried or re-run (a task, a webhook, a job
  after a worker dies), say why running it twice is safe: publish by content digest, upsert by
  key, dedupe by request id. Detect lost work with a watchdog that does not depend on the lost
  worker.
- **Failure semantics:** each component fails closed or fails open, chosen and stated. A failure
  must never look like a valid result: no sentinel or default value in place of an error, and no
  catch-and-skip that drops an item from an aggregate. Name these silent-success paths and alert
  on them.
- **Verify, then correct once:** check model or untrusted output independently. On failure,
  retry once with the reason fed back, then surface the failure.
- **Trust follows the code that runs:** secrets and privileges depend on who wrote the code being
  executed, not on which config file asked for it. Isolation for untrusted code matches the
  threat; if you choose weaker isolation, name the threat you accept.
- **Hot path:** the data layout and access path from sizing, including cheap work-avoidance
  before the expensive step: conservative bounds or filters that provably skip work, caps on
  unbounded inputs, and reuse of expensive intermediates.
- **Observability:** structured logs, a per-request trace, the metrics that show the
  bottleneck, and a single-process mode that reproduces one request.

## Defer, with a trigger

Kubernetes, service meshes, message buses, microservice splits, multi-region, plugin
marketplaces and custom frameworks. Each deferral is a decision (`status: deferred`) with the
observable condition that brings it back.

## Two tests

- **Over-engineering:** for each component, what breaks if you delete it?
- **Under-engineering:** what fails first in production?
