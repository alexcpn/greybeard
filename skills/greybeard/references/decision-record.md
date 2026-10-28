# Decision record format

Write `decisions.json` as a list. One object per decision; keep each field to a sentence or two.

```json
[
  {
    "id": "D1",
    "area": "viability | workload | data | decomposition | concurrency | caching | pipeline | correctness | failure | extensibility | operations",
    "decision": "What we will do, stated as a commitment.",
    "because": "The fact or number that forces it (cite the constraint or Phase 2 figure).",
    "rejected": ["Alternative - one-line reason it lost"],
    "switch_if": "The observable condition under which we would revisit this.",
    "extension_point": "If this is an OCP seam: the interface/registry and what a new variant adds. Else null.",
    "failure_mode": "What happens when this part fails, and whether that fails closed or open. Else null.",
    "enforced_by": "The automated check that fails if this decision is violated (see enforcement.md). Else \"review only\".",
    "status": "decided | assumption | deferred"
  }
]
```

Rules:

- `decision` must be one choice. "X or Y depending on needs" fails review.
- `status: assumption` for anything resting on a constraint the user did not give.
- `status: deferred` for things consciously left out (e.g. Kubernetes); `switch_if` is the trigger.
- For caching decisions, `decision` lists the full key, e.g.
  `"key = (user_id, locale, price_list_id, currency, catalog_version)"`.
- If Phase 0 was STOP and the user overrode it, D1 records that override and the accepted risk.

## Mirror in prose (ADR style, in design.md)

```
### D3 - Process pool, shared state loaded once per worker
Context: <constraint>. Decision: <choice>. Consequences: <good / bad>. Revisit if: <trigger>.
```
