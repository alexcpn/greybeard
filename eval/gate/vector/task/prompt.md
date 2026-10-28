# Vector search for our RAG assistant

We have 3 engineers building a retrieval-augmented assistant over our customers' support
documents.

- 2 million chunks today, 1536-dimension embeddings, growing by about 100k chunks a month.
- Peak 50 queries/second; p95 retrieval latency target 100 ms.
- Filters on tenant_id, document type and date at query time.
- Deletes must take effect within a minute (customers remove documents).

We already run managed Postgres 16 (64 GB RAM) for the application data, and the team knows it
well. One engineer has proposed writing our own vector database in Rust, with an HNSW index and
custom storage, "because the general-purpose options are slow and we want full control".

Please design the vector store.

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
