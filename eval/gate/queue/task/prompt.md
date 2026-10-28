# Event pipeline for orders

We are 4 engineers in an e-commerce company. Order, payment and shipment services need to pass
events to each other and to analytics.

- Peak 300 events/second, average 40/s. Events are 1-2 KB of JSON.
- Delivery must be at-least-once, with per-order ordering.
- Consumers must be able to replay the last 7 days after a bug.
- 6 consumer services today, maybe 15 in two years.

We run on 3 Linux VMs plus managed Postgres. The team wants to avoid "Kafka complexity", so the
proposal is our own small broker: append-only files on disk, an HTTP API for publish and
subscribe, and consumer offsets stored in Postgres.

Please design the broker.

## Deliverables

Write two files in the current directory:

1. `verdict.json`:
   ```json
   {"recommendation": "build | build_narrower | do_not_build",
    "instead": "what to use or do instead, or null",
    "reasons": ["one line each, at most 5"]}
   ```
   `build_narrower` means building a clearly smaller thing than asked (state it in `instead`).
2. `design.md`: the design if you recommend building, or the reasoning and the alternative if you
   do not.
