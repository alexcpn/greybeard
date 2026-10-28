# Reference design (hidden from the agent): small-model terminal agent

The real system is a single-process Python agent (~3.6k lines, deps: requests, duckdb, later
pydantic) built by one developer. Its commit history records the failures it hit.

## What the real system did

- **Explicit state machine** per task: PENDING → EXECUTING → TOOL_CALLING → WAITING_RESULT →
  EVALUATING → COMPLETED / back to EXECUTING; any → FAILED. Transitions validated and logged.
  Loop detection: the same tool call repeated ≥3 times forces FAILED. Max turns per subtask.
- **Plan first, then map/reduce.** A planner (later with constrained-decoding structured
  output, Pydantic schema) produces 2–4 steps with intent and a self-critique; the plan is
  validated structurally with one re-plan; route on plan length (single state machine vs
  map/reduce). Each subtask runs in an isolated, minimal context (system + task + its tool
  results) and passes results via files (`previous_results.txt`), not transcripts. Reduce
  ranks subtask results (TF-IDF) and synthesises. If more than half of subtasks fail, abort and
  mark the parent FAILED instead of reducing over partial results. Input file path is passed
  explicitly so the planner cannot invent names.
- **Command pattern tools.** Each tool is a command class with execute, timing, exit code,
  undo where meaningful (write_file), built from the LLM tool call by a registry. Read-only
  tools cached by SHA256 of canonical args; write tools always execute.
- **Context management.** Tiered retention: latest tool result in full, 1–2 turns ago truncated
  (head/tail), older replaced by one-line summaries; full results kept in the DB and
  re-queryable. Sliding window over history; compact system prompt; binary-format guidance
  moved to a separate file loaded on demand.
- **Persistence.** DuckDB at a user path: sessions, tasks (with parent_id), task transitions,
  tool calls (args hash, output, success, elapsed), task chains. No conversation table:
  conversation is ephemeral.
- **Learning from history.** Playbook retrieval: TF-IDF over completed task chains; the top
  hit's tool sequence is injected as a hint at task start (threshold-gated).
- **Verification.** Intent validator: extract success criteria from the request (one LLM call,
  JSON), check the output against them (files created during this task only), plus a semantic
  LLM-judge criterion; one retry with the failure reason injected.
- **Tool guards.** Blocks writing binary formats as text; detects large inline string literals
  in Python and redirects to reading from files; redirects `python` to `python3`.
- **Backends.** Ollama and OpenAI behind one chat interface; auto-detect local models.

## Known weaknesses (basis for level 4)

1. The read cache was keyed only on tool name + args: a file modified after caching returned
   stale content (fixed later by checking mtime). A content hash or invalidation on any write
   is the complete key.
2. The sliding window evicted an assistant message with tool_calls but kept its tool result,
   producing orphaned tool messages that strict providers reject (400). Fixed by evicting
   whole call/result groups.
3. Tool-call arguments in history had to be re-serialised per provider; message validity was
   provider-specific and fixed reactively.
4. If the DuckDB file is locked, it silently falls back to an in-memory DB: history and
   playbooks for that session are lost.
5. Before the abort rule, reduce ran over mostly failed subtasks and reported COMPLETED.
6. Subtask max_turns initially too tight (2), causing cascade failures.

## Calibration

- A vector database, embeddings server or multi-agent framework for a single-process laptop
  tool needs a forcing reason; TF-IDF or plain keyword retrieval is enough here.
- "Trust the model's own success claim" is level 1 on verification.
- A cache key that omits file state (mtime/size/content hash) is the cache-correctness miss.
