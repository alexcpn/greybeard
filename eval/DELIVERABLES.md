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
