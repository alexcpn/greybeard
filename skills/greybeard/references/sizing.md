# Sizing

Do the arithmetic before choosing technology, and show it.

- **Load:** requests per day, then peak per second; the CPU-seconds, I/O and memory available
  per request; storage growth per year.
- **Bottleneck:** name it. The design attacks it first.
- **Multipliers:** retries, re-runs, fan-out and polling multiply the stated load. Say whether
  the given numbers include them, and size the worst realistic case.
- **Working set per node, after routing:** how requests are routed (affinity or sharding vs
  spread or hash) decides whether each node's cache sees a slice of the data or all of it. Size
  it per node, against that node's memory.
- **Reuse ratio:** estimate each planned cache's hit rate under the stated churn. A result cache
  invalidated by every daily data update is not a cache; reuse the expensive intermediate
  instead.
- **Unbounded inputs:** find every input with no upper size (profiles, logs, documents, result
  sets) and cap it or say why it is bounded.

Every big technology choice later in the design must point back to one of these numbers.
